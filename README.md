# 📄 Document Analyzer MCP Server

[English](README.md) | [简体中文](README.zh.md)

[![PyPI version](https://badge.fury.io/py/doc-mcp-server.svg)](https://pypi.org/project/doc-mcp-server/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)

> **Make AI understand complex documents** - MCP server solving AI context limitations

---

## 🎯 Key Features

- ✅ **Smart Document Analysis** - Auto-detect sections, handle merged cells
- ✅ **Multi-format Support** - Excel (.xlsx, .xls) | PDF/Word in development
- ✅ **Precise Field Mapping** - Field mapping table + section-level reading
- ✅ **High Performance** - Structured caching + lazy loading

## 🚀 Quick Start

### Installation

**macOS / Linux (Recommended with pipx)**
```bash
# Install pipx
brew install pipx  # macOS
# or sudo apt install pipx  # Ubuntu/Debian

# Install doc-mcp-server
pipx install doc-mcp-server
```

**Windows**
```bash
pip install doc-mcp-server
```

For more installation options, see **[Full Installation Guide](docs/en/installation.md)**

### Configure Claude Code

Add to `~/.claude.json` or your project's config file:

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server"
    }
  }
}
```

For detailed configuration, see **[Quick Start Guide](docs/en/quickstart.md)**

## 📚 Full Documentation

- **[Installation Guide](docs/en/installation.md)** - Platform-specific installation steps
- **[Update Guide](docs/en/update.md)** - How to upgrade to the latest version
- **[Quick Start](docs/en/quickstart.md)** - Configuration and basic usage
- **[Usage Guide](docs/en/usage.md)** - Complete API and examples
- **[Troubleshooting](docs/en/troubleshooting.md)** - Common issues and solutions

## 💡 Usage Example

```python
# 1. Analyze document structure
analyze_document(file_path="/path/to/document.xlsx")

# 2. Read specific section
read_section(file_path="/path/to/document.xlsx", section_name="Section 1")

# 3. Read single field
read_field(file_path="/path/to/document.xlsx", field_key="Section1_CompanyName")
```

## 🛠️ Available Tools

| Tool | Description |
|------|-------------|
| `analyze_document` | Analyze document structure and generate metadata |
| `get_structure` | Get cached document structure |
| `read_field` | Read specific field value |
| `read_section` | Read entire section data |
| `write_field` | Write field value (Excel only) |
| `list_sections` | List all sections |
| `list_fields` | List all fields |
| `export_structure` | Export document structure |

## 🎯 Why Use This?

**Problem**: Large Excel files consume massive tokens when directly read by AI

- ❌ Traditional: Read entire 323-row Excel → 15000+ tokens → Often fails
- ✅ Using MCP: Structured reading → 2000 tokens → 90%+ success rate

**Performance Improvements**:
- 🚀 Token consumption reduced by 87% (15000 → 2000)
- ✅ Success rate improved from 30% to 90%+
- ⚡ Handles 323 rows × 24 columns with 4249 merged cells

## 🤝 Contributing & Feedback

- **Report Issues**: [GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues)
- **Contribute Code**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

**Made with ❤️ by Yang Jiahui**
