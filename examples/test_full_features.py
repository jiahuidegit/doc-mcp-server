#!/usr/bin/env python3
"""
完整功能测试 - 验证所有核心功能
无需MCP SDK，直接测试分析器
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from document_analyzer.analyzers.excel_analyzer import ExcelAnalyzer


def test_all_features():
    """测试所有核心功能"""
    print("="*80)
    print("Document Analyzer MCP - 完整功能测试")
    print("="*80)

    template_path = "../../src/main/resources/templates/credit_report_template.xlsx"

    if not os.path.exists(template_path):
        print(f"\n❌ 文件不存在: {template_path}")
        return False

    print(f"\n📄 测试文件: {template_path}\n")

    try:
        # ==================== 测试1: 文档分析 ====================
        print("【测试1】文档分析 (analyze_document)")
        print("-" * 80)

        analyzer = ExcelAnalyzer(template_path)
        structure = analyzer.analyze()

        assert structure['meta'].format.value == 'excel', "格式检测失败"
        assert len(structure['sections']) > 0, "章节检测失败"
        assert len(structure['fields']) > 0, "字段提取失败"

        print(f"✅ 通过")
        print(f"   - 检测到 {len(structure['sections'])} 个章节")
        print(f"   - 提取到 {len(structure['fields'])} 个字段")
        print(f"   - 合并单元格: {structure['merged_cells_count']}")

        # ==================== 测试2: 获取结构 ====================
        print("\n【测试2】获取结构 (get_structure)")
        print("-" * 80)

        cached_structure = analyzer.get_structure()
        assert cached_structure == structure, "缓存机制失败"

        print(f"✅ 通过 - 缓存机制正常")

        # ==================== 测试3: 列出章节 ====================
        print("\n【测试3】列出章节 (list_sections)")
        print("-" * 80)

        sections = analyzer.list_sections()
        assert len(sections) > 0, "列出章节失败"

        print(f"✅ 通过 - 共 {len(sections)} 个章节:")
        for i, section in enumerate(sections[:5], 1):
            print(f"   {i}. {section}")
        if len(sections) > 5:
            print(f"   ... 还有 {len(sections) - 5} 个")

        # ==================== 测试4: 列出字段 ====================
        print("\n【测试4】列出字段 (list_fields)")
        print("-" * 80)

        # 列出所有字段
        all_fields = analyzer.list_fields()
        assert len(all_fields) > 0, "列出所有字段失败"

        # 列出特定章节的字段
        if sections:
            section_fields = analyzer.list_fields(sections[0])
            assert len(section_fields) > 0, "列出章节字段失败"

            print(f"✅ 通过")
            print(f"   - 所有字段: {len(all_fields)} 个")
            print(f"   - '{sections[0]}' 字段: {len(section_fields)} 个")

        # ==================== 测试5: 读取字段 ====================
        print("\n【测试5】读取字段 (read_field)")
        print("-" * 80)

        if all_fields:
            # 读取前3个字段
            test_fields = all_fields[:3]
            success_count = 0

            for field_key in test_fields:
                try:
                    value = analyzer.get_field_value(field_key)
                    print(f"   ✓ {field_key[:50]}...")
                    print(f"     值: {value}")
                    success_count += 1
                except Exception as e:
                    print(f"   ✗ {field_key}: {e}")

            assert success_count > 0, "读取字段全部失败"
            print(f"\n✅ 通过 - {success_count}/{len(test_fields)} 个字段读取成功")

        # ==================== 测试6: 读取章节 ====================
        print("\n【测试6】读取章节 (read_section)")
        print("-" * 80)

        if sections:
            section_name = sections[0]
            section_data = analyzer.get_section_data(section_name)

            assert isinstance(section_data, dict), "返回类型错误"
            print(f"✅ 通过 - '{section_name}'")
            print(f"   - 字段数: {len(section_data)}")
            print(f"   - 前3个字段:")
            for i, (key, value) in enumerate(list(section_data.items())[:3], 1):
                print(f"     {i}. {key}: {value}")

        # ==================== 测试7: 写入字段 ====================
        print("\n【测试7】写入字段 (write_field)")
        print("-" * 80)

        if all_fields:
            test_field = all_fields[0]
            test_value = "测试数据_123"

            # 写入
            analyzer.set_field_value(test_field, test_value)

            # 读取验证
            read_value = analyzer.get_field_value(test_field)
            assert read_value == test_value, f"写入失败: 期望 {test_value}, 实际 {read_value}"

            print(f"✅ 通过")
            print(f"   - 写入字段: {test_field[:50]}...")
            print(f"   - 写入值: {test_value}")
            print(f"   - 验证读取: {read_value}")

        # ==================== 测试8: 导出结构 ====================
        print("\n【测试8】导出结构 (export_structure)")
        print("-" * 80)

        json_output = "test_full_structure.json"
        md_output = "test_full_structure.md"

        analyzer.export_structure(json_output, format='json')
        analyzer.export_structure(md_output, format='markdown')

        assert os.path.exists(json_output), "JSON导出失败"
        assert os.path.exists(md_output), "Markdown导出失败"

        json_size = os.path.getsize(json_output)
        md_size = os.path.getsize(md_output)

        print(f"✅ 通过")
        print(f"   - JSON文件: {json_output} ({json_size} 字节)")
        print(f"   - Markdown文件: {md_output} ({md_size} 字节)")

        # ==================== 汇总 ====================
        print("\n" + "="*80)
        print("🎉 所有测试通过！")
        print("="*80)

        print("\n📊 测试摘要:")
        print(f"   ✅ 文档分析: 通过")
        print(f"   ✅ 获取结构: 通过")
        print(f"   ✅ 列出章节: 通过 ({len(sections)} 个)")
        print(f"   ✅ 列出字段: 通过 ({len(all_fields)} 个)")
        print(f"   ✅ 读取字段: 通过")
        print(f"   ✅ 读取章节: 通过")
        print(f"   ✅ 写入字段: 通过")
        print(f"   ✅ 导出结构: 通过")

        print("\n🚀 核心功能完全正常！")
        print("   MCP服务器可以正常使用这些分析器功能\n")

        return True

    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
        return False
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_all_features()
    sys.exit(0 if success else 1)
