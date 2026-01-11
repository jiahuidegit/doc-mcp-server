"""
Document Analyzer MCP Server
基于MCP协议的文档分析服务器
"""

import asyncio
import os
from typing import Any, Dict, Optional
import json

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from .analyzers.base import BaseAnalyzer
from .analyzers.excel_analyzer import ExcelAnalyzer


# 全局分析器缓存
_analyzer_cache: Dict[str, BaseAnalyzer] = {}


def get_analyzer(file_path: str) -> BaseAnalyzer:
    """获取文档分析器(带缓存)"""
    if file_path in _analyzer_cache:
        return _analyzer_cache[file_path]

    # 检测文件格式
    format = BaseAnalyzer.detect_format(file_path)

    # 创建分析器
    if format.name == 'EXCEL':
        analyzer = ExcelAnalyzer(file_path)
    else:
        raise ValueError(f"暂不支持的文档格式: {format.name}")

    # 缓存
    _analyzer_cache[file_path] = analyzer
    return analyzer


# 创建MCP服务器实例
app = Server("doc-mcp-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """列出所有可用工具"""
    return [
        Tool(
            name="analyze_document",
            description="分析文档结构,生成元数据和字段映射表。支持Excel/PDF/Word等格式",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "文档文件路径(绝对路径)"
                    },
                    "output_format": {
                        "type": "string",
                        "enum": ["json", "markdown", "both"],
                        "description": "输出格式",
                        "default": "json"
                    },
                    "deep_analysis": {
                        "type": "boolean",
                        "description": "是否深度分析",
                        "default": True
                    }
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="get_structure",
            description="获取已分析文档的结构信息",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "文档文件路径"
                    },
                    "section": {
                        "type": "string",
                        "description": "指定章节名(可选)"
                    }
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="read_field",
            description="读取指定字段的值。字段键格式: '章节名_字段名'",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "文档文件路径"
                    },
                    "field_key": {
                        "type": "string",
                        "description": "字段键名,格式: '章节名_字段名'"
                    }
                },
                "required": ["file_path", "field_key"]
            }
        ),
        Tool(
            name="read_section",
            description="读取整个章节的所有字段数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "文档文件路径"
                    },
                    "section_name": {
                        "type": "string",
                        "description": "章节名称"
                    }
                },
                "required": ["file_path", "section_name"]
            }
        ),
        Tool(
            name="write_field",
            description="写入字段值(仅Excel支持)",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "文档文件路径"
                    },
                    "field_key": {
                        "type": "string",
                        "description": "字段键名"
                    },
                    "value": {
                        "description": "要写入的值"
                    }
                },
                "required": ["file_path", "field_key", "value"]
            }
        ),
        Tool(
            name="list_sections",
            description="列出文档的所有章节",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "文档文件路径"
                    }
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="list_fields",
            description="列出所有字段或指定章节的字段",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "文档文件路径"
                    },
                    "section_name": {
                        "type": "string",
                        "description": "章节名称(可选)"
                    }
                },
                "required": ["file_path"]
            }
        ),
        Tool(
            name="export_structure",
            description="导出文档结构为JSON或Markdown文件",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "文档文件路径"
                    },
                    "output_path": {
                        "type": "string",
                        "description": "输出文件路径"
                    },
                    "format": {
                        "type": "string",
                        "enum": ["json", "markdown"],
                        "description": "导出格式",
                        "default": "json"
                    }
                },
                "required": ["file_path", "output_path"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """处理工具调用"""
    try:
        if name == "analyze_document":
            return await handle_analyze_document(arguments)
        elif name == "get_structure":
            return await handle_get_structure(arguments)
        elif name == "read_field":
            return await handle_read_field(arguments)
        elif name == "read_section":
            return await handle_read_section(arguments)
        elif name == "write_field":
            return await handle_write_field(arguments)
        elif name == "list_sections":
            return await handle_list_sections(arguments)
        elif name == "list_fields":
            return await handle_list_fields(arguments)
        elif name == "export_structure":
            return await handle_export_structure(arguments)
        else:
            raise ValueError(f"未知工具: {name}")

    except Exception as e:
        return [TextContent(type="text", text=f"错误: {str(e)}")]


async def handle_analyze_document(args: Dict[str, Any]) -> list[TextContent]:
    """处理文档分析请求"""
    file_path = args["file_path"]
    output_format = args.get("output_format", "json")

    # 获取分析器
    analyzer = get_analyzer(file_path)

    # 分析文档
    structure = analyzer.analyze()

    # 根据输出格式返回
    if output_format == "markdown":
        result = structure['summary']
    else:
        # JSON格式(需要序列化dataclass)
        result = json.dumps({
            'meta': {
                'format': structure['meta'].format.value,
                'file_path': structure['meta'].file_path,
                'file_size': structure['meta'].file_size,
                'page_count': structure['meta'].page_count,
                'total_fields': structure['meta'].total_fields
            },
            'sections': [
                {
                    'title': s.title,
                    'start_row': s.start_row,
                    'end_row': s.end_row
                } for s in structure['sections']
            ],
            'fields_count': len(structure['fields']),
            'summary': structure['summary']
        }, ensure_ascii=False, indent=2)

    return [TextContent(type="text", text=result)]


async def handle_get_structure(args: Dict[str, Any]) -> list[TextContent]:
    """获取文档结构"""
    file_path = args["file_path"]
    section = args.get("section")

    analyzer = get_analyzer(file_path)
    structure = analyzer.get_structure()

    if section:
        # 只返回指定章节
        sections = [s for s in structure['sections'] if s.title == section]
        if not sections:
            return [TextContent(type="text", text=f"章节不存在: {section}")]

        result = json.dumps({
            'section': {
                'title': sections[0].title,
                'start_row': sections[0].start_row,
                'end_row': sections[0].end_row
            }
        }, ensure_ascii=False, indent=2)
    else:
        # 返回所有章节列表
        result = json.dumps({
            'sections': [
                {
                    'title': s.title,
                    'row_range': f"{s.start_row}-{s.end_row}"
                } for s in structure['sections']
            ]
        }, ensure_ascii=False, indent=2)

    return [TextContent(type="text", text=result)]


async def handle_read_field(args: Dict[str, Any]) -> list[TextContent]:
    """读取字段值"""
    file_path = args["file_path"]
    field_key = args["field_key"]

    analyzer = get_analyzer(file_path)
    value = analyzer.get_field_value(field_key)

    result = json.dumps({
        'field_key': field_key,
        'value': value
    }, ensure_ascii=False, indent=2)

    return [TextContent(type="text", text=result)]


async def handle_read_section(args: Dict[str, Any]) -> list[TextContent]:
    """读取章节数据"""
    file_path = args["file_path"]
    section_name = args["section_name"]

    analyzer = get_analyzer(file_path)
    data = analyzer.get_section_data(section_name)

    result = json.dumps({
        'section_name': section_name,
        'data': data
    }, ensure_ascii=False, indent=2)

    return [TextContent(type="text", text=result)]


async def handle_write_field(args: Dict[str, Any]) -> list[TextContent]:
    """写入字段值"""
    file_path = args["file_path"]
    field_key = args["field_key"]
    value = args["value"]

    analyzer = get_analyzer(file_path)

    # 仅Excel支持写入
    if not isinstance(analyzer, ExcelAnalyzer):
        return [TextContent(type="text", text="错误: 该文档格式不支持写入操作")]

    analyzer.set_field_value(field_key, value)
    analyzer.save()

    return [TextContent(type="text", text=f"成功写入字段: {field_key} = {value}")]


async def handle_list_sections(args: Dict[str, Any]) -> list[TextContent]:
    """列出章节"""
    file_path = args["file_path"]

    analyzer = get_analyzer(file_path)
    sections = analyzer.list_sections()

    result = json.dumps({
        'sections': sections
    }, ensure_ascii=False, indent=2)

    return [TextContent(type="text", text=result)]


async def handle_list_fields(args: Dict[str, Any]) -> list[TextContent]:
    """列出字段"""
    file_path = args["file_path"]
    section_name = args.get("section_name")

    analyzer = get_analyzer(file_path)
    fields = analyzer.list_fields(section_name)

    result = json.dumps({
        'section': section_name,
        'fields': fields,
        'count': len(fields)
    }, ensure_ascii=False, indent=2)

    return [TextContent(type="text", text=result)]


async def handle_export_structure(args: Dict[str, Any]) -> list[TextContent]:
    """导出结构"""
    file_path = args["file_path"]
    output_path = args["output_path"]
    format = args.get("format", "json")

    analyzer = get_analyzer(file_path)

    # Excel特有方法
    if isinstance(analyzer, ExcelAnalyzer):
        analyzer.export_structure(output_path, format)
        return [TextContent(type="text", text=f"成功导出到: {output_path}")]
    else:
        return [TextContent(type="text", text="错误: 该文档格式暂不支持导出")]


async def main():
    """启动MCP服务器"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
