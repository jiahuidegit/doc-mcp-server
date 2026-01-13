# 📖 Usage Guide

Complete Document Analyzer MCP Server API documentation and usage guide.

---

## 📚 Table of Contents

- [Tool Overview](#tool-overview)
- [Detailed API Documentation](#detailed-api-documentation)
- [Real-World Cases](#real-world-cases)
- [Best Practices](#best-practices)

---

## Tool Overview

Document Analyzer MCP Server provides **8 core tools**:

| Tool Name | Function | Supported Formats |
|-----------|----------|-------------------|
| `analyze_document` | Analyze document structure, generate metadata | Excel, PDF(dev), Word(dev) |
| `get_structure` | Get analyzed document structure | All |
| `read_field` | Read specified field value | All |
| `read_section` | Read entire section data | All |
| `write_field` | Write field value | Excel |
| `list_sections` | List all sections | All |
| `list_fields` | List all fields | All |
| `export_structure` | Export document structure | All |

---

## Detailed API Documentation

### 1. analyze_document

Analyze document structure, generate metadata and field mapping table.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `file_path` | string | ✅ | - | Absolute or relative path to document |
| `output_format` | string | ❌ | `"json"` | Output format: `"json"` or `"markdown"` |
| `deep_analysis` | boolean | ❌ | `true` | Whether to perform deep analysis |

#### Returns

```json
{
  "meta": {
    "format": "excel",
    "file_size": 45678,
    "page_count": 1,
    "total_fields": 68
  },
  "sections": [...],
  "field_mapping": {...},
  "summary": "..."
}
```

---

### 2. read_field

Read specified field value.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_path` | string | ✅ | Document path |
| `field_key` | string | ✅ | Field key, format: `"section_name_field_name"` |

#### Field Key Format

Field key consists of **section name** and **field name**, connected by underscore:

```
section_name_field_name
```

Examples:
- ✅ `"Basic Information_Company Name"`
- ✅ `"Section 1_Registration Date"`
- ❌ `"Company Name"` (missing section name)

---

### 3. read_section

Read entire section data.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_path` | string | ✅ | Document path |
| `section_name` | string | ✅ | Section name |

---

### 4. write_field

Write field value (Excel only).

⚠️ **Note**: Write operations directly modify the original file. Backup is recommended.

---

### 5-8. Other Tools

- `get_structure`: Get cached structure without re-analysis
- `list_sections`: List all sections
- `list_fields`: List all fields or fields in specific section
- `export_structure`: Export structure as JSON or Markdown

---

## Real-World Cases

### Case 1: Process Corporate Credit Report

**Scenario**: Analyze a 323-row corporate credit report, extract key information.

**Performance Comparison**:
- ❌ Traditional: Read entire Excel → Token consumption 15000+ → Often fails
- ✅ Using MCP: Structured reading → Token consumption 2000 → 90%+ success rate

---

### Case 2: Batch Data Extraction

Extract same fields from multiple reports systematically.

---

### Case 3: Data Validation and Correction

Check and correct erroneous data in Excel.

---

## Best Practices

### 1. File Path Standards

✅ **Recommended**:
```python
# Use absolute paths
/Users/username/Documents/report.xlsx
C:\Users\username\Documents\report.xlsx
```

❌ **Not Recommended**:
```python
# Ambiguous paths
report.xlsx
~/Documents/report.xlsx  # ~ not supported on some systems
```

---

### 2. Step-by-Step Operations

For complex tasks, execute step by step:

✅ **Recommended**:
```python
1. analyze_document  # First analyze structure
2. list_sections     # View sections
3. read_section      # Read specific data
4. Process and summarize
```

---

### 3. Cache Utilization

For already analyzed documents, use `get_structure` instead of repeating `analyze_document`:

```python
# First time
analyze_document("/path/to/report.xlsx")

# Subsequent operations
get_structure("/path/to/report.xlsx")  # Faster, no re-analysis
read_section(...)
```

---

### 4. Write Operation Precautions

⚠️ Before using `write_field`:
1. Confirm file is writable (not open by other programs)
2. Backup original file is recommended
3. Confirm field key is correct

---

## 🎯 Performance Optimization Tips

### Token Optimization

| Operation | Token Consumption | Optimization |
|-----------|-------------------|--------------|
| Direct read large Excel | 15000+ | Use `analyze_document` + `read_section` |
| Repeated analysis | 5000+ | Use `get_structure` to read cache |
| Read unnecessary data | 3000+ | Only read necessary sections/fields |

---

## 📚 More Resources

- **[Troubleshooting](troubleshooting.md)** - Solve common problems
- **[Example Code](../../examples/)** - More real-world cases
- **[GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues)** - Report issues

---

## 📮 Feedback & Suggestions

Any questions or suggestions during usage, feel free to:
- Submit [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)
- Join community discussion
