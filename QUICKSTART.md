# 快速开始指南

## 📦 安装

### 1. 克隆项目
```bash
cd /Users/yangjiahui/work/demo/chengtay-ai
cd doc-mcp-server
```

### 2. 安装依赖
```bash
pip install -e .
```

## 🧪 测试功能

### 方式1: 直接测试(不需要Claude Desktop)

```bash
cd examples
python test_example.py
```

这个测试会：
- 分析征信报告模板结构
- 列出所有章节和字段
- 导出JSON和Markdown文档

### 方式2: 通过MCP测试(需要配置Claude Desktop)

#### 步骤1: 配置Claude Desktop

编辑 `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "python",
      "args": [
        "-m",
        "document_analyzer.server"
      ],
      "cwd": "/Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server/src"
    }
  }
}
```

#### 步骤2: 重启Claude Desktop

#### 步骤3: 在Claude中测试

```
提示词: 请使用 analyze_document 工具分析这个文件:
/Users/yangjiahui/work/demo/chengtay-ai/src/main/resources/templates/credit_report_template.xlsx
```

Claude会自动调用MCP工具并返回结果。

## 📖 使用示例

### 示例1: 分析文档结构

```
用户: 分析征信报告的结构

AI调用:
{
  "tool": "analyze_document",
  "arguments": {
    "file_path": "/path/to/credit_report.xlsx",
    "output_format": "json"
  }
}

AI返回:
{
  "meta": {
    "total_fields": 68,
    "sections": 4
  },
  "summary": "..."
}
```

### 示例2: 读取特定章节

```
用户: 读取"第一部分：信息概要"的数据

AI调用:
{
  "tool": "read_section",
  "arguments": {
    "file_path": "/path/to/credit_report.xlsx",
    "section_name": "第一部分：信息概要"
  }
}

AI返回:
{
  "section_name": "第一部分：信息概要",
  "data": {
    "首次有信贷交易的年份": "",
    "发生信贷交易的机构数": "",
    ...
  }
}
```

### 示例3: 列出所有章节

```
用户: 这个文档有哪些章节？

AI调用:
{
  "tool": "list_sections",
  "arguments": {
    "file_path": "/path/to/credit_report.xlsx"
  }
}

AI返回:
{
  "sections": [
    "第一部分：信息概要",
    "未结清信贷及授信信息概要",
    "第二部分：信贷记录明细",
    "第三部分：账户附件文件"
  ]
}
```

## 🔧 开发和调试

### 查看MCP日志

Claude Desktop的日志位置：
```bash
tail -f ~/Library/Logs/Claude/mcp*.log
```

### 测试MCP服务器

```bash
# 直接运行服务器
python -m document_analyzer.server
```

## 🚀 下一步

1. **扩展到其他格式**: 添加PDF、Word支持
2. **优化性能**: 添加缓存机制
3. **添加更多工具**: 智能分块、语义搜索
4. **完善文档**: API文档、最佳实践

## ❓ 常见问题

### Q: 为什么AI无法调用工具？
A: 检查 claude_desktop_config.json 配置是否正确，重启Claude Desktop

### Q: 如何查看MCP工具列表？
A: 在Claude中询问："你有哪些document-analyzer相关的工具？"

### Q: 支持哪些Excel格式？
A: 目前支持 .xlsx 和 .xls，包括复杂的合并单元格

### Q: 如何添加新的文档格式？
A: 参考 excel_analyzer.py，继承 BaseAnalyzer 实现新的分析器
