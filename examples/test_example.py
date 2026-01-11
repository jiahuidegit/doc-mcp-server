"""
Document Analyzer MCP - 测试示例
演示如何直接使用分析器(不通过MCP)
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from document_analyzer.analyzers.excel_analyzer import ExcelAnalyzer


def test_credit_report():
    """测试征信报告分析"""
    print("="*80)
    print("Document Analyzer MCP - 测试示例")
    print("="*80)

    # 征信报告路径(请修改为实际路径)
    template_path = "../../src/main/resources/templates/credit_report_template.xlsx"

    if not os.path.exists(template_path):
        print(f"\n❌ 文件不存在: {template_path}")
        print("请修改 template_path 为你的实际文件路径\n")
        return

    print(f"\n正在分析: {template_path}\n")

    # 1. 创建分析器
    analyzer = ExcelAnalyzer(template_path)

    # 2. 分析文档结构
    print("【步骤1】分析文档结构...")
    structure = analyzer.analyze()

    print(f"\n文档元数据:")
    print(f"  - 格式: {structure['meta'].format.value}")
    print(f"  - 文件大小: {structure['meta'].file_size / 1024:.2f} KB")
    print(f"  - 工作表数: {structure['meta'].page_count}")
    print(f"  - 总字段数: {structure['meta'].total_fields}")
    print(f"  - 合并单元格: {structure['merged_cells_count']}")

    # 3. 列出章节
    print(f"\n【步骤2】列出所有章节:")
    sections = analyzer.list_sections()
    for i, section in enumerate(sections, 1):
        print(f"  {i}. {section}")

    # 4. 读取字段(如果存在)
    print(f"\n【步骤3】读取字段示例:")
    fields = analyzer.list_fields(sections[0] if sections else None)

    if fields:
        # 读取前3个字段
        for field_key in fields[:3]:
            try:
                value = analyzer.get_field_value(field_key)
                print(f"  {field_key}: {value}")
            except Exception as e:
                print(f"  {field_key}: [读取失败: {e}]")
    else:
        print("  (没有检测到字段)")

    # 5. 读取章节数据
    if sections:
        print(f"\n【步骤4】读取章节数据示例:")
        section_name = sections[0]
        data = analyzer.get_section_data(section_name)
        print(f"  章节: {section_name}")
        print(f"  字段数: {len(data)}")

        # 显示前5个字段
        for i, (key, value) in enumerate(list(data.items())[:5], 1):
            print(f"    {i}. {key}: {value}")

    # 6. 导出结构
    print(f"\n【步骤5】导出结构文档:")
    json_path = "test_output_structure.json"
    md_path = "test_output_structure.md"

    analyzer.export_structure(json_path, format='json')
    analyzer.export_structure(md_path, format='markdown')

    print(f"  ✅ 已导出JSON: {json_path}")
    print(f"  ✅ 已导出Markdown: {md_path}")

    print("\n" + "="*80)
    print("✅ 测试完成！")
    print("="*80)

    print("\n下一步:")
    print("  1. 查看 test_output_structure.md 了解文档结构")
    print("  2. 查看 test_output_structure.json 查看字段映射表")
    print("  3. 配置Claude Desktop使用MCP服务器\n")


if __name__ == "__main__":
    test_credit_report()
