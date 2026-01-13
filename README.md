# 📄 Document Analyzer MCP Server

[![PyPI version](https://badge.fury.io/py/doc-mcp-server.svg)](https://pypi.org/project/doc-mcp-server/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)

> **让 AI 读懂任何复杂文档** - 解决 AI 上下文限制问题的 MCP 服务器
> **Make AI understand complex documents** - MCP server solving AI context limitations

---

## 🌍 语言 / Language

- [中文文档](#中文文档)
- [English Documentation](#english-documentation)

---

## 中文文档

### 🎯 核心功能

- ✅ **智能文档分析** - 自动识别章节结构、处理合并单元格
- ✅ **多格式支持** - Excel (.xlsx, .xls) | PDF/Word 开发中
- ✅ **精确字段定位** - 字段映射表 + 章节级别读取
- ✅ **高效性能** - 结构化缓存 + 按需加载

### 🚀 快速开始

#### 安装

**macOS / Linux (推荐使用 pipx)**
```bash
# 安装 pipx
brew install pipx  # macOS
# 或 sudo apt install pipx  # Ubuntu/Debian

# 安装 doc-mcp-server
pipx install doc-mcp-server
```

**Windows**
```bash
pip install doc-mcp-server
```

更多安装方式请查看 **[完整安装教程](docs/zh/installation.md)**

#### 配置 Claude Code

在 `~/.claude.json` 或项目根目录的配置文件中添加：

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server"
    }
  }
}
```

详细配置请查看 **[快速开始指南](docs/zh/quickstart.md)**

### 📚 完整文档

- **[安装教程](docs/zh/installation.md)** - 分平台详细安装步骤
- **[更新教程](docs/zh/update.md)** - 如何升级到最新版本
- **[快速开始](docs/zh/quickstart.md)** - 配置和基础使用
- **[使用指南](docs/zh/usage.md)** - 完整的 API 和示例
- **[故障排查](docs/zh/troubleshooting.md)** - 常见问题解决

### 💡 使用示例

```python
# 1. 分析文档结构
analyze_document(file_path="/path/to/document.xlsx")

# 2. 读取特定章节
read_section(file_path="/path/to/document.xlsx", section_name="第一部分")

# 3. 读取单个字段
read_field(file_path="/path/to/document.xlsx", field_key="第一部分_企业名称")
```

### 🤝 贡献与反馈

- **问题反馈**: [GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues)
- **贡献代码**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## English Documentation

### 🎯 Key Features

- ✅ **Smart Document Analysis** - Auto-detect sections, handle merged cells
- ✅ **Multi-format Support** - Excel (.xlsx, .xls) | PDF/Word in development
- ✅ **Precise Field Mapping** - Field mapping table + section-level reading
- ✅ **High Performance** - Structured caching + lazy loading

### 🚀 Quick Start

#### Installation

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

#### Configure Claude Code

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

### 📚 Full Documentation

- **[Installation Guide](docs/en/installation.md)** - Platform-specific installation steps
- **[Update Guide](docs/en/update.md)** - How to upgrade to the latest version
- **[Quick Start](docs/en/quickstart.md)** - Configuration and basic usage
- **[Usage Guide](docs/en/usage.md)** - Complete API and examples
- **[Troubleshooting](docs/en/troubleshooting.md)** - Common issues and solutions

### 💡 Usage Example

```python
# 1. Analyze document structure
analyze_document(file_path="/path/to/document.xlsx")

# 2. Read specific section
read_section(file_path="/path/to/document.xlsx", section_name="Section 1")

# 3. Read single field
read_field(file_path="/path/to/document.xlsx", field_key="Section1_CompanyName")
```

### 🤝 Contributing & Feedback

- **Report Issues**: [GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues)
- **Contribute Code**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

**Made with ❤️ by Yang Jiahui**
