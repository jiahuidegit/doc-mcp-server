# 📦 安装教程

本教程将指导你在不同操作系统上安装 Document Analyzer MCP Server。

---

## 📋 前提条件

- **Python 3.10 或更高版本**
- **pip 或 pipx** (包管理工具)
- **Claude Desktop** (如果要通过 Claude 使用)

检查 Python 版本：
```bash
python --version
# 或
python3 --version
```

---

## 🍎 macOS 安装

### 方式 1: 使用 pipx (推荐)

pipx 会为每个工具创建独立的虚拟环境，避免依赖冲突。

#### 步骤 1: 安装 pipx

```bash
# 使用 Homebrew 安装 pipx
brew install pipx

# 确保 pipx 路径配置正确
pipx ensurepath
```

#### 步骤 2: 安装 doc-mcp-server

```bash
pipx install doc-mcp-server
```

#### 步骤 3: 验证安装

```bash
# 检查是否安装成功
pipx list

# 应该看到类似输出：
# venvs are in /Users/你的用户名/.local/pipx/venvs
# apps are exposed on your $PATH at /Users/你的用户名/.local/bin
# package doc-mcp-server 0.1.1, installed using Python 3.10.0
```

---

### 方式 2: 使用 pip (不推荐)

如果你坚持使用 pip：

```bash
# macOS 系统保护模式下需要添加 --break-system-packages
pip3 install doc-mcp-server --break-system-packages
```

⚠️ **警告**: 这种方式可能会导致系统 Python 环境混乱。

---

### 方式 3: 使用虚拟环境

```bash
# 创建虚拟环境
python3 -m venv ~/doc-mcp-venv

# 激活虚拟环境
source ~/doc-mcp-venv/bin/activate

# 安装
pip install doc-mcp-server

# 记住虚拟环境的 Python 路径（配置 Claude 时需要）
which python
# 输出类似: /Users/你的用户名/doc-mcp-venv/bin/python
```

---

## 🪟 Windows 安装

### 方式 1: 使用 pip (推荐)

#### 步骤 1: 打开命令提示符 (CMD) 或 PowerShell

按 `Win + R`，输入 `cmd` 或 `powershell`

#### 步骤 2: 安装 doc-mcp-server

```bash
pip install doc-mcp-server
```

#### 步骤 3: 验证安装

```bash
pip show doc-mcp-server

# 应该看到类似输出：
# Name: doc-mcp-server
# Version: 0.1.1
# Location: C:\Users\你的用户名\AppData\Local\Programs\Python\Python310\Lib\site-packages
```

---

### 方式 2: 使用 pipx

#### 步骤 1: 安装 pipx

```bash
pip install pipx
pipx ensurepath
```

#### 步骤 2: 重启命令提示符

关闭并重新打开 CMD 或 PowerShell

#### 步骤 3: 安装 doc-mcp-server

```bash
pipx install doc-mcp-server
```

---

## 🐧 Linux 安装

### Ubuntu / Debian

#### 方式 1: 使用 pipx (推荐)

```bash
# 安装 pipx
sudo apt update
sudo apt install pipx

# 配置路径
pipx ensurepath

# 重新加载 shell 配置
source ~/.bashrc  # 或 source ~/.zshrc

# 安装 doc-mcp-server
pipx install doc-mcp-server
```

#### 方式 2: 使用 pip

```bash
pip3 install doc-mcp-server --user
```

---

### Fedora / CentOS / RHEL

```bash
# 安装 pipx
sudo dnf install pipx

# 配置路径
pipx ensurepath

# 安装 doc-mcp-server
pipx install doc-mcp-server
```

---

### Arch Linux

```bash
# 安装 pipx
sudo pacman -S python-pipx

# 配置路径
pipx ensurepath

# 安装 doc-mcp-server
pipx install doc-mcp-server
```

---

## 🔍 验证安装

### 检查命令是否可用

```bash
# 如果使用 pipx 安装
doc-mcp-server --version

# 如果使用 pip 安装，尝试导入模块
python -c "import document_analyzer; print('安装成功')"
```

### 测试 MCP 服务器

```bash
# 直接运行服务器（测试用）
python -m document_analyzer.server
```

如果看到类似 `MCP server running...` 的输出，说明安装成功。

按 `Ctrl+C` 停止服务器。

---

## ⚙️ 配置 Claude Code

安装完成后，需要配置 Claude Code 才能使用。

### 配置文件位置

Claude Code 支持两种配置方式：

**1. 全局配置（推荐）**
```bash
~/.claude.json
```
所有项目都可以使用

**2. 项目配置**
```bash
项目根目录/.claude.json
```
只在当前项目生效

### 编辑配置文件

打开或创建配置文件：

**macOS / Linux:**
```bash
# 编辑全局配置
nano ~/.claude.json
# 或
code ~/.claude.json

# 编辑项目配置
nano .claude.json
code .claude.json
```

**Windows:**
```bash
# 编辑全局配置
notepad %USERPROFILE%\.claude.json

# 编辑项目配置
notepad .claude.json
```

### 添加 MCP 服务器配置

#### 如果使用 pipx 安装 (推荐)

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server"
    }
  }
}
```

#### 如果使用 pip 安装

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

#### 如果使用虚拟环境安装

**macOS / Linux:**
```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "/完整路径/doc-mcp-venv/bin/python",
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
      "command": "C:\\Users\\你的用户名\\doc-mcp-venv\\Scripts\\python.exe",
      "args": ["-m", "document_analyzer.server"]
    }
  }
}
```

---

## ✅ 测试是否正常工作

在 Claude Code 中输入：

```
你有哪些 document-analyzer 相关的工具？
```

Claude 应该会列出以下工具：
1. `analyze_document` - 分析文档结构
2. `get_structure` - 获取已分析的文档结构
3. `read_field` - 读取指定字段
4. `read_section` - 读取整个章节
5. `write_field` - 写入字段值
6. `list_sections` - 列出所有章节
7. `list_fields` - 列出所有字段
8. `export_structure` - 导出文档结构

---

## ❓ 常见问题

### Q: 提示 "command not found: doc-mcp-server"

**A:** 可能是 PATH 环境变量没有配置好。

**解决方案**:
```bash
# macOS/Linux
pipx ensurepath
source ~/.bashrc  # 或 source ~/.zshrc

# 然后重新打开终端
```

---

### Q: 提示 "ModuleNotFoundError: No module named 'document_analyzer'"

**A:** Python 找不到模块。

**解决方案**:
1. 检查是否安装成功: `pip show doc-mcp-server`
2. 如果使用虚拟环境，确保激活了环境
3. 重新安装: `pipx reinstall doc-mcp-server`

---

### Q: Claude Code 无法识别工具

**A:** 配置文件格式错误或路径不对。

**解决方案**:
1. 检查 JSON 格式是否正确（使用 JSON 验证器）
2. 检查 Python 路径是否正确
3. 确认配置文件位置（全局 `~/.claude.json` 或项目 `.claude.json`）
4. 重启终端或 Claude Code 会话

---

### Q: macOS 提示 "externally-managed-environment"

**A:** macOS 的 Python 环境被 Homebrew 保护。

**解决方案**: 使用 pipx 安装（方式 1）或使用虚拟环境（方式 3）

---

## 🚀 下一步

安装成功后，请查看：
- **[快速开始指南](quickstart.md)** - 学习基础使用
- **[使用指南](usage.md)** - 查看完整 API 文档
- **[故障排查](troubleshooting.md)** - 解决常见问题

---

## 📮 需要帮助？

如果遇到问题，欢迎：
- 查看 [故障排查文档](troubleshooting.md)
- 提交 [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)
