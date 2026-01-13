# 📄 Document Analyzer MCP Server

[English](README.md) | [简体中文](README.zh.md)

[![PyPI version](https://badge.fury.io/py/doc-mcp-server.svg)](https://pypi.org/project/doc-mcp-server/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)

> **让 AI 读懂任何复杂文档** - 解决 AI 上下文限制问题的 MCP 服务器

---

## 🎯 核心功能

- ✅ **智能文档分析** - 自动识别章节结构、处理合并单元格
- ✅ **多格式支持** - Excel (.xlsx, .xls) | PDF/Word 开发中
- ✅ **精确字段定位** - 字段映射表 + 章节级别读取
- ✅ **高效性能** - 结构化缓存 + 按需加载

## 🚀 快速开始

### 安装

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

### 配置 Claude Code

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

## 📚 完整文档

- **[安装教程](docs/zh/installation.md)** - 分平台详细安装步骤
- **[更新教程](docs/zh/update.md)** - 如何升级到最新版本
- **[快速开始](docs/zh/quickstart.md)** - 配置和基础使用
- **[使用指南](docs/zh/usage.md)** - 完整的 API 和示例
- **[故障排查](docs/zh/troubleshooting.md)** - 常见问题解决

## 💡 使用示例

```python
# 1. 分析文档结构
analyze_document(file_path="/path/to/document.xlsx")

# 2. 读取特定章节
read_section(file_path="/path/to/document.xlsx", section_name="第一部分")

# 3. 读取单个字段
read_field(file_path="/path/to/document.xlsx", field_key="第一部分_企业名称")
```

## 🛠️ 可用工具

| 工具 | 说明 |
|------|------|
| `analyze_document` | 分析文档结构，生成元数据 |
| `get_structure` | 获取已缓存的文档结构 |
| `read_field` | 读取指定字段值 |
| `read_section` | 读取整个章节数据 |
| `write_field` | 写入字段值（仅 Excel） |
| `list_sections` | 列出所有章节 |
| `list_fields` | 列出所有字段 |
| `export_structure` | 导出文档结构 |

## 🎯 为什么使用？

**问题**：大型 Excel 文件被 AI 直接读取时消耗大量 token

- ❌ 传统方式：直接读取 323 行 Excel → 15000+ token → 经常失败
- ✅ 使用 MCP：结构化读取 → 2000 token → 90%+ 成功率

**性能提升**：
- 🚀 Token 消耗减少 87%（15000 → 2000）
- ✅ 成功率从 30% 提升到 90%+
- ⚡ 可处理 323 行 × 24 列，包含 4249 个合并单元格

## 🤝 贡献与反馈

- **问题反馈**: [GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues)
- **贡献代码**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

**Made with ❤️ by Yang Jiahui**
