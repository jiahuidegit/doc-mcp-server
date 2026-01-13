# 🚀 Quick Start Guide

This guide will help you start using Document Analyzer MCP Server in 5 minutes.

---

## 📋 Prerequisites

Ensure you have completed these steps:

- ✅ [Install doc-mcp-server](installation.md)
- ✅ Install Claude Code CLI

---

## ⚙️ Configure Claude Code

### Step 1: Choose Configuration Method

Claude Code supports two configurations:

**Global Configuration (Recommended)**
- Config file: `~/.claude.json`
- Available to all projects

**Project Configuration**
- Config file: `.claude.json` in project root
- Only effective in current project

### Step 2: Edit Configuration File

Open or create the configuration file with any text editor:

**macOS / Linux:**
```bash
# Global configuration
nano ~/.claude.json
# or
code ~/.claude.json

# Project configuration
nano .claude.json
# or
code .claude.json
```

**Windows:**
```bash
# Global configuration
notepad %USERPROFILE%\.claude.json

# Project configuration
notepad .claude.json
```

### Step 3: Add MCP Server Configuration

#### 🎯 If installed with pipx (Recommended)

This is the simplest configuration:

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server"
    }
  }
}
```

#### If installed with pip

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "python",
      "args": ["-m", "document_analyzer.server"]
    }
  }
}
```

**Windows users may need to specify full path:**
```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "C:\\Users\\your-username\\AppData\\Local\\Programs\\Python\\Python310\\python.exe",
      "args": ["-m", "document_analyzer.server"]
    }
  }
}
```

#### If installed with virtual environment

**macOS / Linux:**
```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "/full/path/doc-mcp-venv/bin/python",
      "args": ["-m", "document_analyzer.server"]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "C:\\Users\\your-username\\doc-mcp-venv\\Scripts\\python.exe",
      "args": ["-m", "document_analyzer.server"]
    }
  }
}
```

### Step 4: Save Configuration File

After saving the configuration file, it takes effect immediately. No restart needed.

---

## ✅ Verify Configuration

### Check if Tools are Loaded

In Claude Code, type:

```
What document-analyzer tools do you have?
```

Claude should list **8 tools**:

1. **analyze_document** - Analyze document structure, generate metadata
2. **get_structure** - Get analyzed document structure
3. **read_field** - Read specified field value
4. **read_section** - Read entire section data
5. **write_field** - Write field value (Excel only)
6. **list_sections** - List all sections
7. **list_fields** - List all fields or fields in specified section
8. **export_structure** - Export document structure as JSON or Markdown

If you see these tools, configuration successful! 🎉

---

## 📖 Basic Usage Examples

### Example 1: Analyze Document Structure

Prepare an Excel file, e.g., `/path/to/report.xlsx`

In Claude, type:

```
Please analyze this file structure:
/path/to/report.xlsx
```

Claude will call `analyze_document` tool and return something like:

```json
{
  "meta": {
    "format": "excel",
    "file_size": 45678,
    "page_count": 1,
    "total_fields": 50
  },
  "sections": [
    {
      "title": "Basic Information",
      "row_range": "2-10",
      "fields_count": 15
    },
    {
      "title": "Detailed Data",
      "row_range": "11-30",
      "fields_count": 35
    }
  ]
}
```

### Example 2: List All Sections

```
What sections does this document have?
/path/to/report.xlsx
```

Returns:
```json
{
  "sections": [
    "Basic Information",
    "Detailed Data",
    "Statistics Summary"
  ]
}
```

### Example 3: Read Specific Section

```
Read all data from "Basic Information" section
```

Returns:
```json
{
  "section_name": "Basic Information",
  "data": {
    "Company Name": "Example Company",
    "Registration Date": "2020-01-01",
    "Registered Capital": "10 million"
  }
}
```

### Example 4: Read Single Field

```
Read the "Basic Information_Company Name" field
```

Returns:
```json
{
  "field_key": "Basic Information_Company Name",
  "value": "Example Company"
}
```

### Example 5: Export Document Structure

```
Export this document's structure as JSON file
Save to /path/to/output.json
```

Will generate a JSON file containing the complete document structure.

---

## 🎯 Real-World Application Scenarios

### Scenario 1: Process Complex Credit Reports

```
User question: "Analyze this corporate credit report, tell me about the company's borrowing situation"

AI workflow:
1. Call analyze_document to analyze report structure
2. Call list_sections to see available sections
3. Call read_section to read "Borrowing Information" section
4. Summarize and answer user
```

### Scenario 2: Batch Data Extraction

```
User question: "Extract all financial metrics from this report"

AI workflow:
1. Call analyze_document to identify financial sections
2. Call read_section to read "Financial Data" section
3. Organize into table for user display
```

### Scenario 3: Document Comparison

```
User question: "Compare the differences between these two reports"

AI workflow:
1. Call analyze_document separately for both documents
2. Use read_section to read same sections
3. Compare data and highlight differences
```

---

## 📝 Usage Tips

### Tip 1: Use Relative Paths

If working in a specific directory, you can use relative paths:

```
# File in current directory
Analyze ./report.xlsx

# Parent directory
Analyze ../data/report.xlsx
```

### Tip 2: Batch Operations

You can have Claude handle multiple tasks at once:

```
Please help me:
1. Analyze report.xlsx structure
2. List all sections
3. Read data from first 3 sections
4. Export structure as JSON
```

### Tip 3: Fuzzy Search

Not sure of exact field name? Ask like this:

```
Does this document have any "Company Name" related fields?
```

Claude will call `list_fields` and help you find similar fields.

---

## ❓ Common Issues

### Q: Claude doesn't call tools, just answers directly

**A:** Claude may not think tools are needed. Explicitly tell it to use tools:

```
Please use the analyze_document tool to analyze this file
```

---

### Q: File not found error

**A:** Check if file path is correct:

```bash
# Check if file exists in terminal
ls -l /path/to/your/file.xlsx
```

Use **absolute paths** for reliability:
- macOS/Linux: `/Users/username/Documents/file.xlsx`
- Windows: `C:\Users\username\Documents\file.xlsx`

---

### Q: Tool call failed

**A:** May be a configuration issue. In Claude Code, errors should be displayed in the response.

---

## 🚀 Next Steps

Congratulations! You've mastered the basics. Next:

- **[Usage Guide](usage.md)** - View complete API documentation and advanced usage
- **[Troubleshooting](troubleshooting.md)** - Solve common problems
- **[Example Projects](../../examples/)** - See more real-world cases

---

## 📮 Need Help?

If you encounter issues, feel free to:
- Check [Troubleshooting Documentation](troubleshooting.md)
- Submit [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)
