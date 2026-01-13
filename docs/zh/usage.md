# 📖 使用指南

完整的 Document Analyzer MCP Server API 文档和使用指南。

---

## 📚 目录

- [工具总览](#工具总览)
- [详细 API 文档](#详细-api-文档)
- [实战案例](#实战案例)
- [最佳实践](#最佳实践)

---

## 工具总览

Document Analyzer MCP Server 提供 **8 个核心工具**：

| 工具名 | 功能 | 支持格式 |
|-------|------|---------|
| `analyze_document` | 分析文档结构,生成元数据 | Excel, PDF(开发中), Word(开发中) |
| `get_structure` | 获取已分析的文档结构 | 所有 |
| `read_field` | 读取指定字段的值 | 所有 |
| `read_section` | 读取整个章节数据 | 所有 |
| `write_field` | 写入字段值 | Excel |
| `list_sections` | 列出所有章节 | 所有 |
| `list_fields` | 列出所有字段 | 所有 |
| `export_structure` | 导出文档结构 | 所有 |

---

## 详细 API 文档

### 1. analyze_document

分析文档结构,生成元数据和字段映射表。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|-------|-----|------|-------|------|
| `file_path` | string | ✅ | - | 文档的绝对或相对路径 |
| `output_format` | string | ❌ | `"json"` | 输出格式: `"json"` 或 `"markdown"` |
| `deep_analysis` | boolean | ❌ | `true` | 是否进行深度分析 |

#### 返回值

```json
{
  "meta": {
    "format": "excel",
    "file_size": 45678,
    "page_count": 1,
    "total_fields": 68,
    "analyzed_at": "2025-01-13T10:30:00Z"
  },
  "sections": [
    {
      "title": "第一部分：信息概要",
      "row_range": "4-16",
      "fields_count": 15,
      "fields": ["企业名称", "注册时间", ...]
    }
  ],
  "field_mapping": {
    "第一部分：信息概要_企业名称": {"row": 5, "col": 2},
    "第一部分：信息概要_注册时间": {"row": 6, "col": 2}
  },
  "summary": "文档包含 4 个主要章节..."
}
```

#### 使用示例

```python
# 在 Claude 中使用
"请分析这个文件: /path/to/report.xlsx"

# 指定输出格式
"分析这个文件,输出 markdown 格式"

# 快速分析(不进行深度分析)
"快速分析这个文件的大致结构"
```

---

### 2. get_structure

获取已分析文档的结构信息(不重新分析)。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|-------|-----|------|-------|------|
| `file_path` | string | ✅ | - | 文档路径 |
| `section` | string | ❌ | `null` | 指定章节名(可选) |

#### 返回值

```json
{
  "file_path": "/path/to/report.xlsx",
  "sections": [
    {
      "title": "第一部分",
      "fields_count": 15
    }
  ]
}
```

#### 使用示例

```python
# 获取整体结构
"获取这个文档的结构信息"

# 获取特定章节
"获取"第一部分"的结构"
```

---

### 3. read_field

读取指定字段的值。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|-------|-----|------|------|
| `file_path` | string | ✅ | 文档路径 |
| `field_key` | string | ✅ | 字段键,格式: `"章节名_字段名"` |

#### 返回值

```json
{
  "field_key": "第一部分_企业名称",
  "value": "示例科技有限公司",
  "location": {"row": 5, "col": 2}
}
```

#### 使用示例

```python
# 读取单个字段
'读取"第一部分_企业名称"字段'

# 读取多个字段
"""
读取以下字段:
1. 第一部分_企业名称
2. 第一部分_注册时间
3. 第一部分_注册资本
"""
```

#### 字段键格式说明

字段键由 **章节名** 和 **字段名** 组成,用下划线连接：

```
章节名_字段名
```

示例：
- ✅ `"基本信息_企业名称"`
- ✅ `"第一部分：信息概要_首次有信贷交易的年份"`
- ❌ `"企业名称"` (缺少章节名)

---

### 4. read_section

读取整个章节的所有数据。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|-------|-----|------|------|
| `file_path` | string | ✅ | 文档路径 |
| `section_name` | string | ✅ | 章节名称 |

#### 返回值

```json
{
  "section_name": "第一部分：信息概要",
  "fields_count": 15,
  "data": {
    "企业名称": "示例科技有限公司",
    "注册时间": "2020-01-01",
    "注册资本": "1000万元",
    "首次有信贷交易的年份": "2020"
  }
}
```

#### 使用示例

```python
# 读取单个章节
'读取"第一部分：信息概要"章节'

# 读取并分析
'读取"财务数据"章节,并总结关键指标'

# 批量读取
"""
读取以下章节:
1. 基本信息
2. 财务数据
3. 风险评估
"""
```

---

### 5. write_field

写入字段值(仅支持 Excel)。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|-------|-----|------|------|
| `file_path` | string | ✅ | Excel 文件路径 |
| `field_key` | string | ✅ | 字段键 |
| `value` | any | ✅ | 要写入的值 |

#### 返回值

```json
{
  "success": true,
  "field_key": "第一部分_企业名称",
  "old_value": "旧公司名",
  "new_value": "新公司名"
}
```

#### 使用示例

```python
# 写入单个字段
'将"第一部分_企业名称"改为"新科技公司"'

# 批量写入
"""
修改以下字段:
1. 第一部分_企业名称 = "新公司"
2. 第一部分_注册资本 = "2000万"
"""
```

⚠️ **注意**: 写入操作会直接修改原文件,建议先备份。

---

### 6. list_sections

列出文档的所有章节。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|-------|-----|------|------|
| `file_path` | string | ✅ | 文档路径 |

#### 返回值

```json
{
  "total_sections": 4,
  "sections": [
    {
      "title": "第一部分：信息概要",
      "fields_count": 15
    },
    {
      "title": "第二部分：信贷记录",
      "fields_count": 30
    }
  ]
}
```

#### 使用示例

```python
# 列出所有章节
"这个文档有哪些章节？"

# 获取章节统计
"统计各章节的字段数量"
```

---

### 7. list_fields

列出所有字段或指定章节的字段。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|-------|-----|------|------|
| `file_path` | string | ✅ | 文档路径 |
| `section_name` | string | ❌ | 章节名(可选) |

#### 返回值

```json
{
  "total_fields": 68,
  "fields": [
    {
      "field_key": "第一部分_企业名称",
      "section": "第一部分：信息概要",
      "field_name": "企业名称"
    },
    {
      "field_key": "第一部分_注册时间",
      "section": "第一部分：信息概要",
      "field_name": "注册时间"
    }
  ]
}
```

#### 使用示例

```python
# 列出所有字段
"这个文档有哪些字段？"

# 列出特定章节的字段
'列出"第一部分"的所有字段'

# 搜索字段
"有没有包含'企业名称'的字段？"
```

---

### 8. export_structure

导出文档结构为 JSON 或 Markdown 文件。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|-------|-----|------|-------|------|
| `file_path` | string | ✅ | - | 文档路径 |
| `output_path` | string | ✅ | - | 输出文件路径 |
| `format` | string | ❌ | `"json"` | 输出格式: `"json"` 或 `"markdown"` |

#### 返回值

```json
{
  "success": true,
  "output_path": "/path/to/output.json",
  "format": "json",
  "file_size": 12345
}
```

#### 使用示例

```python
# 导出为 JSON
"导出这个文档的结构为 JSON,保存到 /path/to/output.json"

# 导出为 Markdown
"导出为 markdown 格式,保存到 structure.md"
```

---

## 实战案例

### 案例 1: 处理企业征信报告

**场景**: 分析一份 323 行的企业征信报告,提取关键信息。

**步骤**:

1. **分析结构**
```python
用户: "分析这份征信报告: /data/credit_report.xlsx"

AI 调用: analyze_document(file_path="/data/credit_report.xlsx")

返回:
{
  "sections": [
    "第一部分：信息概要",
    "未结清信贷及授信信息概要",
    "第二部分：信贷记录明细",
    "第三部分：账户附件文件"
  ],
  "total_fields": 68
}
```

2. **提取关键信息**
```python
用户: "读取企业的基本信息和借贷情况"

AI 调用:
- read_section("第一部分：信息概要")
- read_section("未结清信贷及授信信息概要")

AI 总结: "该企业成立于 2020 年,首次信贷交易..."
```

3. **导出报告**
```python
用户: "把分析结果导出为 markdown"

AI 调用: export_structure(output_path="report.md", format="markdown")
```

**性能对比**:
- ❌ 传统方式: 多次读取整个 Excel → Token 消耗 15000+ → 经常失败
- ✅ 使用 MCP: 结构化读取 → Token 消耗 2000 → 成功率 90%+

---

### 案例 2: 批量数据提取

**场景**: 从多份报告中提取相同字段。

```python
用户: """
从以下 3 份报告提取"企业名称"和"注册资本":
- /data/report1.xlsx
- /data/report2.xlsx
- /data/report3.xlsx
"""

AI 工作流:
for report in [report1, report2, report3]:
    analyze_document(report)
    name = read_field(report, "第一部分_企业名称")
    capital = read_field(report, "第一部分_注册资本")

AI 返回表格:
| 报告 | 企业名称 | 注册资本 |
|------|---------|---------|
| report1 | 公司A | 1000万 |
| report2 | 公司B | 2000万 |
| report3 | 公司C | 500万 |
```

---

### 案例 3: 数据验证和修正

**场景**: 检查并修正 Excel 中的错误数据。

```python
用户: "检查这份报告中的注册资本是否合理,如果小于 100 万,标记为异常"

AI 工作流:
1. read_section("第一部分：信息概要")
2. 检查"注册资本"字段
3. 如果 < 100 万:
   - 标记异常
   - 可选: write_field("备注", "注册资本偏低")
```

---

## 最佳实践

### 1. 文件路径规范

✅ **推荐**:
```python
# 使用绝对路径
/Users/username/Documents/report.xlsx
C:\Users\username\Documents\report.xlsx

# 或明确的相对路径
./data/report.xlsx
../reports/report.xlsx
```

❌ **不推荐**:
```python
# 模糊路径
report.xlsx
~/Documents/report.xlsx  # 某些系统不支持 ~
```

---

### 2. 分步操作

对于复杂任务,建议分步执行:

✅ **推荐**:
```python
1. analyze_document  # 先分析结构
2. list_sections     # 查看章节
3. read_section      # 读取具体数据
4. 处理和总结
```

❌ **不推荐**:
```python
# 一次性读取所有数据
read_section("章节1")
read_section("章节2")
read_section("章节3")
# Token 消耗过大
```

---

### 3. 错误处理

文件不存在或格式错误时的处理:

```python
用户: "分析这个文件"

AI 应该:
1. 先检查文件是否存在
2. 如果失败,提供清晰的错误信息
3. 建议用户检查路径或格式
```

---

### 4. 缓存利用

已经分析过的文档,使用 `get_structure` 而不是重复 `analyze_document`:

```python
# 第一次
analyze_document("/path/to/report.xlsx")

# 后续操作
get_structure("/path/to/report.xlsx")  # 更快,不重新分析
read_section(...)
```

---

### 5. 写入操作注意事项

⚠️ 使用 `write_field` 前:
1. 确认文件可写(没有被其他程序打开)
2. 建议先备份原文件
3. 确认字段键正确

```python
# 推荐流程
1. 复制文件作为备份
2. write_field 修改
3. 验证修改是否正确
4. 如果出错,恢复备份
```

---

## 🎯 性能优化建议

### Token 优化

| 操作 | Token 消耗 | 优化方案 |
|------|----------|---------|
| 直接读取大 Excel | 15000+ | 使用 `analyze_document` + `read_section` |
| 重复分析 | 5000+ | 使用 `get_structure` 读取缓存 |
| 读取不需要的数据 | 3000+ | 只读取必要的章节/字段 |

### 速度优化

1. **批量操作**: 一次调用多个字段
2. **并行处理**: 多个文件可以并行分析
3. **缓存复用**: 利用 `get_structure`

---

## 📚 更多资源

- **[故障排查](troubleshooting.md)** - 解决常见问题
- **[示例代码](../../examples/)** - 更多实际案例
- **[GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues)** - 报告问题

---

## 📮 反馈与建议

使用中有任何问题或建议,欢迎：
- 提交 [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)
- 加入社区讨论
