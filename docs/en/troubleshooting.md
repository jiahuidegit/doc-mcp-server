# 🔧 Troubleshooting Guide

This document helps you solve common issues when using Document Analyzer MCP Server.

---

## 📋 Quick Diagnosis

### Issue Categories

| Symptom | Possible Cause | Jump To |
|---------|----------------|---------|
| Claude cannot recognize tools | Configuration issues | [Configuration Issues](#configuration-issues) |
| Tool call fails | Python environment issues | [Environment Issues](#environment-issues) |
| File not found | Path issues | [File Path Issues](#file-path-issues) |
| Analysis results incorrect | Document format issues | [Document Format Issues](#document-format-issues) |
| Slow performance | Performance optimization | [Performance Issues](#performance-issues) |

---

## Configuration Issues

### Issue 1: Claude shows "no related tools"

**Symptoms**: When asking for tool list in Claude Code, shows no document-analyzer tools.

**Causes**:
- Configuration file path error
- Configuration file JSON format error
- Configuration file not saved

**Solutions**:

#### Step 1: Check configuration file location

```bash
# Global configuration
ls -la ~/.claude.json

# Project configuration
ls -la .claude.json
```

If file doesn't exist, create it:
```bash
# Global configuration
touch ~/.claude.json

# Project configuration
touch .claude.json
```

#### Step 2: Verify JSON format

Use online JSON validator (like jsonlint.com) to check configuration file.

Common errors:
```json
// ❌ Wrong: trailing comma
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server",
    }
  }
}

// ✅ Correct
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server"
    }
  }
}
```

#### Step 3: Restart session

If configuration file is modified, may need to:
1. Exit current Claude Code session
2. Restart Claude Code
3. Or restart terminal

---

## Environment Issues

### Issue 2: "ModuleNotFoundError: No module named 'document_analyzer'"

**Symptoms**: Python cannot find the module.

**Solutions**:

#### Step 1: Verify installation

```bash
# If using pipx
pipx list | grep doc-mcp-server

# If using pip
pip show doc-mcp-server

# Or test import directly
python -c "import document_analyzer; print('Success')"
```

#### Step 2: Reinstall

```bash
# Using pipx (recommended)
pipx uninstall doc-mcp-server
pipx install doc-mcp-server

# Using pip
pip uninstall doc-mcp-server
pip install doc-mcp-server
```

---

### Issue 3: macOS shows "externally-managed-environment"

**Symptoms**: When using pip to install, shows environment is externally managed.

**Cause**: macOS Python environment is protected by Homebrew.

**Solutions**:

**Method 1: Use pipx (recommended)**
```bash
brew install pipx
pipx install doc-mcp-server
```

**Method 2: Use virtual environment**
```bash
python3 -m venv ~/doc-mcp-venv
source ~/doc-mcp-venv/bin/activate
pip install doc-mcp-server
```

---

## File Path Issues

### Issue 4: "File not found" error

**Symptoms**: When Claude calls tool, shows file not found.

**Causes**:
- Path incorrect
- Using relative path, but working directory wrong
- Filename contains special characters

**Solutions**:

#### Use absolute paths

✅ **Correct**:
```python
# macOS/Linux
/Users/username/Documents/report.xlsx

# Windows
C:\Users\username\Documents\report.xlsx
```

❌ **Wrong**:
```python
~/Documents/report.xlsx  # ~ may not be recognized
.\report.xlsx           # relative path may be wrong
```

#### Check if file exists

```bash
# macOS/Linux
ls -l /path/to/file.xlsx

# Windows
dir C:\path\to\file.xlsx
```

---

### Issue 5: Windows path backslash issues

**Symptoms**: Backslashes in Windows paths cause errors.

**Solutions**:

```python
# Method 1: Use double backslashes
C:\\Users\\username\\Documents\\report.xlsx

# Method 2: Use forward slashes (recommended)
C:/Users/username/Documents/report.xlsx

# Method 3: Use raw string (in Python)
r"C:\Users\username\Documents\report.xlsx"
```

---

## Document Format Issues

### Issue 6: Excel analysis results inaccurate

**Symptoms**: Section recognition errors or missing fields.

**Causes**:
- Complex document structure (multi-level headers, irregular merged cells)
- Empty rows interfering with section recognition
- Non-standard field names

**Solutions**:

#### Enable deep analysis

```python
# In Claude, explicitly request deep analysis
"Use deep analysis mode to analyze this file"
```

#### Check document structure

1. Manually open Excel file
2. Check for:
   - ✅ Clear section titles
   - ✅ Standard table structure
   - ❌ Too many empty rows
   - ❌ Irregular merged cells

---

## Performance Issues

### Issue 7: Slow analysis of large files

**Symptoms**: Takes a long time to analyze Excel files over 500 rows.

**Solutions**:

#### Use caching

```python
# First analysis (slow)
analyze_document("/path/to/large.xlsx")

# Subsequent operations use get_structure (fast)
get_structure("/path/to/large.xlsx")
read_section(...)
```

#### Only read necessary sections

```python
# ❌ Don't read all sections
read_section("Section 1")
read_section("Section 2")
read_section("Section 3")

# ✅ Only read what you need
read_section("The section I need")
```

---

## Debugging Tips

### Manual server testing

```bash
# Run MCP server directly
python -m document_analyzer.server

# Should see
# MCP server running...

# If error, check error message
```

---

### Test tool functionality

Create test script `test.py`:
```python
from document_analyzer.analyzers.excel_analyzer import ExcelAnalyzer

# Test analysis function
analyzer = ExcelAnalyzer("/path/to/test.xlsx")
result = analyzer.analyze()
print(result)
```

Run:
```bash
python test.py
```

---

### Enable debug mode

Add environment variables to configuration file:

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server",
      "env": {
        "DEBUG": "1"
      }
    }
  }
}
```

---

## 💡 Prevention Measures

### Installation Phase

- ✅ Use pipx instead of pip (avoid environment conflicts)
- ✅ Verify Python version >= 3.10
- ✅ Record installation path and version

### Configuration Phase

- ✅ Use JSON validator to check configuration file
- ✅ Backup configuration file
- ✅ Record custom configurations

### Usage Phase

- ✅ Use absolute paths
- ✅ Test with small files first
- ✅ Backup files before writing

---

## 📮 Get Help

If above methods don't solve the problem:

1. **Collect information**:
   - Operating system and version
   - Python version
   - doc-mcp-server version
   - Complete error message
   - Relevant log parts

2. **Submit Issue**:
   - Visit [GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues)
   - Use Bug Report template
   - Provide detailed information

3. **Check known issues**:
   - [CHANGELOG.md](../../CHANGELOG.md) - Version changelog
   - [GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues) - Known issues list

---

## 🔄 Quick Solution Reference

| Issue | Quick Solution |
|-------|----------------|
| Claude cannot recognize tools | Restart Claude Code session |
| Module not found | `pipx reinstall doc-mcp-server` |
| Configuration not effective | Restart terminal |
| File not found | Use absolute path |
| Analysis too slow | Use cache get_structure |
| Too many tokens | Only read necessary sections |
| Write failed | Close file + check permissions |
