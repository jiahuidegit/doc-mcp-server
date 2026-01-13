# 📦 Installation Guide

This tutorial will guide you through installing Document Analyzer MCP Server on different operating systems.

---

## 📋 Prerequisites

- **Python 3.10 or higher**
- **pip or pipx** (package management tools)
- **Claude Code CLI** (if you want to use it with Claude)

Check your Python version:
```bash
python --version
# or
python3 --version
```

---

## 🍎 macOS Installation

### Method 1: Using pipx (Recommended)

pipx creates isolated virtual environments for each tool, avoiding dependency conflicts.

#### Step 1: Install pipx

```bash
# Install pipx using Homebrew
brew install pipx

# Ensure pipx path is configured correctly
pipx ensurepath
```

#### Step 2: Install doc-mcp-server

```bash
pipx install doc-mcp-server
```

#### Step 3: Verify Installation

```bash
# Check if installation was successful
pipx list

# You should see output similar to:
# venvs are in /Users/your-username/.local/pipx/venvs
# apps are exposed on your $PATH at /Users/your-username/.local/bin
# package doc-mcp-server 0.1.1, installed using Python 3.10.0
```

---

### Method 2: Using pip (Not Recommended)

If you insist on using pip:

```bash
# macOS system protection requires --break-system-packages
pip3 install doc-mcp-server --break-system-packages
```

⚠️ **Warning**: This approach may cause system Python environment issues.

---

### Method 3: Using Virtual Environment

```bash
# Create virtual environment
python3 -m venv ~/doc-mcp-venv

# Activate virtual environment
source ~/doc-mcp-venv/bin/activate

# Install
pip install doc-mcp-server

# Remember the virtual environment Python path (needed for Claude configuration)
which python
# Output: /Users/your-username/doc-mcp-venv/bin/python
```

---

## 🪟 Windows Installation

### Method 1: Using pip (Recommended)

#### Step 1: Open Command Prompt (CMD) or PowerShell

Press `Win + R`, type `cmd` or `powershell`

#### Step 2: Install doc-mcp-server

```bash
pip install doc-mcp-server
```

#### Step 3: Verify Installation

```bash
pip show doc-mcp-server

# You should see output similar to:
# Name: doc-mcp-server
# Version: 0.1.1
# Location: C:\Users\your-username\AppData\Local\Programs\Python\Python310\Lib\site-packages
```

---

### Method 2: Using pipx

#### Step 1: Install pipx

```bash
pip install pipx
pipx ensurepath
```

#### Step 2: Restart Command Prompt

Close and reopen CMD or PowerShell

#### Step 3: Install doc-mcp-server

```bash
pipx install doc-mcp-server
```

---

## 🐧 Linux Installation

### Ubuntu / Debian

#### Method 1: Using pipx (Recommended)

```bash
# Install pipx
sudo apt update
sudo apt install pipx

# Configure path
pipx ensurepath

# Reload shell configuration
source ~/.bashrc  # or source ~/.zshrc

# Install doc-mcp-server
pipx install doc-mcp-server
```

#### Method 2: Using pip

```bash
pip3 install doc-mcp-server --user
```

---

### Fedora / CentOS / RHEL

```bash
# Install pipx
sudo dnf install pipx

# Configure path
pipx ensurepath

# Install doc-mcp-server
pipx install doc-mcp-server
```

---

### Arch Linux

```bash
# Install pipx
sudo pacman -S python-pipx

# Configure path
pipx ensurepath

# Install doc-mcp-server
pipx install doc-mcp-server
```

---

## 🔍 Verify Installation

### Check if Command is Available

```bash
# If installed with pipx
doc-mcp-server --version

# If installed with pip, try importing the module
python -c "import document_analyzer; print('Installation successful')"
```

### Test MCP Server

```bash
# Run server directly (for testing)
python -m document_analyzer.server
```

If you see output like `MCP server running...`, the installation was successful.

Press `Ctrl+C` to stop the server.

---

## ⚙️ Configure Claude Code

After installation, you need to configure Claude Code to use it.

### Configuration File Location

Claude Code supports two configuration methods:

**1. Global Configuration (Recommended)**
```bash
~/.claude.json
```
Available to all projects

**2. Project Configuration**
```bash
.claude.json in project root
```
Only effective in current project

### Edit Configuration File

Open or create the configuration file:

**macOS / Linux:**
```bash
# Edit global configuration
nano ~/.claude.json
# or
code ~/.claude.json

# Edit project configuration
nano .claude.json
code .claude.json
```

**Windows:**
```bash
# Edit global configuration
notepad %USERPROFILE%\.claude.json

# Edit project configuration
notepad .claude.json
```

### Add MCP Server Configuration

#### If installed with pipx (Recommended)

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

---

## ✅ Test if Working

In Claude Code, type:

```
What document-analyzer tools do you have?
```

Claude should list the following tools:
1. `analyze_document` - Analyze document structure
2. `get_structure` - Get analyzed document structure
3. `read_field` - Read specified field
4. `read_section` - Read entire section
5. `write_field` - Write field value
6. `list_sections` - List all sections
7. `list_fields` - List all fields
8. `export_structure` - Export document structure

---

## ❓ Common Issues

### Q: "command not found: doc-mcp-server"

**A:** PATH environment variable may not be configured correctly.

**Solution**:
```bash
# macOS/Linux
pipx ensurepath
source ~/.bashrc  # or source ~/.zshrc

# Then reopen terminal
```

---

### Q: "ModuleNotFoundError: No module named 'document_analyzer'"

**A:** Python cannot find the module.

**Solution**:
1. Check if installation was successful: `pip show doc-mcp-server`
2. If using virtual environment, ensure it's activated
3. Reinstall: `pipx reinstall doc-mcp-server`

---

### Q: Claude Code cannot recognize tools

**A:** Configuration file format error or incorrect path.

**Solution**:
1. Check if JSON format is correct (use JSON validator)
2. Check if Python path is correct
3. Confirm configuration file location (global `~/.claude.json` or project `.claude.json`)
4. Restart terminal or Claude Code session

---

### Q: macOS shows "externally-managed-environment"

**A:** macOS Python environment is protected by Homebrew.

**Solution**: Use pipx installation (Method 1) or use virtual environment (Method 3)

---

## 🚀 Next Steps

After successful installation, check out:
- **[Quick Start Guide](quickstart.md)** - Learn basic usage
- **[Usage Guide](usage.md)** - View complete API documentation
- **[Troubleshooting](troubleshooting.md)** - Solve common problems

---

## 📮 Need Help?

If you encounter issues, feel free to:
- Check [Troubleshooting Documentation](troubleshooting.md)
- Submit [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)
