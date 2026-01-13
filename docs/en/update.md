# 🔄 Update Guide

This tutorial will guide you on how to update Document Analyzer MCP Server to the latest version.

---

## 📦 Check Current Version

### Using pip/pipx

```bash
# If installed with pipx
pipx list | grep doc-mcp-server

# If installed with pip
pip show doc-mcp-server
```

Example output:
```
Name: doc-mcp-server
Version: 0.1.0
```

### Check in Python

```bash
python -c "import document_analyzer; print(document_analyzer.__version__)"
```

---

## 🚀 Update to Latest Version

### macOS / Linux

#### If installed with pipx (Recommended)

```bash
# Update to latest version
pipx upgrade doc-mcp-server

# Check updated version
pipx list | grep doc-mcp-server
```

#### If installed with pip

```bash
# macOS (may need --break-system-packages)
pip3 install --upgrade doc-mcp-server --break-system-packages

# Linux
pip3 install --upgrade doc-mcp-server --user
```

#### If installed with virtual environment

```bash
# Activate virtual environment
source ~/doc-mcp-venv/bin/activate

# Update
pip install --upgrade doc-mcp-server

# Deactivate virtual environment
deactivate
```

---

### Windows

#### If installed with pip

```bash
# Open CMD or PowerShell
pip install --upgrade doc-mcp-server
```

#### If installed with pipx

```bash
pipx upgrade doc-mcp-server
```

#### If installed with virtual environment

```bash
# Activate virtual environment
doc-mcp-venv\Scripts\activate

# Update
pip install --upgrade doc-mcp-server

# Deactivate virtual environment
deactivate
```

---

## 🔍 Verify Update

### Check New Version

```bash
# Using pipx
pipx list | grep doc-mcp-server

# Using pip
pip show doc-mcp-server

# Or in Python
python -c "import document_analyzer; print(document_analyzer.__version__)"
```

### Test Functionality

```bash
# Test if server runs normally
python -m document_analyzer.server
```

Seeing `MCP server running...` means update was successful. Press `Ctrl+C` to stop.

---

## ⚙️ Post-Update Configuration

### Claude Code Configuration

Usually, **no configuration changes are needed** after updating.

But if issues occur, you can restart Claude Code session:

1. **Exit** current Claude Code session
2. **Restart** Claude Code

### Clear Cache (if needed)

Generally not needed for Claude Code, but if you encounter issues:

```bash
# Try restarting terminal or shell session
```

---

## 📋 Version Changelog

### v0.1.1 (Latest)
- ✅ Optimized Excel table recognition
- ✅ Support for complex multi-level headers
- ✅ Sub-section splitting functionality

### v0.1.0
- 🎉 First release
- ✅ Basic Excel support
- ✅ 8 core tools

View complete changelog: [CHANGELOG.md](../../CHANGELOG.md)

---

## 🔄 Install Specific Version

If you need to install a specific version (e.g., rollback to old version):

```bash
# Using pipx
pipx install doc-mcp-server==0.1.0

# Using pip
pip install doc-mcp-server==0.1.0
```

View all available versions:
```bash
pip index versions doc-mcp-server
```

---

## 🛠️ Force Reinstall

If update encounters issues, try force reinstalling:

### Using pipx

```bash
# Uninstall old version
pipx uninstall doc-mcp-server

# Install new version
pipx install doc-mcp-server
```

### Using pip

```bash
# Force reinstall
pip install --force-reinstall doc-mcp-server
```

---

## ❓ Common Issues

### Q: Claude cannot recognize tools after update

**A:** May be a cache issue.

**Solution**:
1. Exit Claude Code completely
2. Restart terminal
3. Restart Claude Code

---

### Q: "Permission denied" when updating

**A:** Insufficient permissions.

**Solution**:
```bash
# macOS/Linux (not recommended to use sudo)
pip3 install --upgrade doc-mcp-server --user

# Or use pipx (recommended)
pipx upgrade doc-mcp-server
```

---

### Q: New errors after update

**A:** May be dependency conflicts or breaking changes.

**Solution**:
1. Check [CHANGELOG.md](../../CHANGELOG.md) for breaking changes
2. Rollback to previous stable version (see above)
3. Submit [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)

---

### Q: How to check if new version is available?

**A:** Use pip to check:

```bash
# View current version and latest version
pip list --outdated | grep doc-mcp-server

# Or using pipx
pipx upgrade-all --dry-run
```

---

## 🔔 Subscribe to Update Notifications

Recommended methods:

1. **GitHub Watch** - Click "Watch" → "Releases only" on [GitHub Repository](https://github.com/jiahuidegit/doc-mcp-server)
2. **PyPI RSS** - Subscribe to PyPI RSS: `https://pypi.org/rss/project/doc-mcp-server/releases.xml`

---

## 📝 Update Best Practices

### Before Updating

1. ✅ Check [CHANGELOG.md](../../CHANGELOG.md) for new features and breaking changes
2. ✅ Backup important configuration files (if any custom configs)
3. ✅ Record current version number (for potential rollback)

### After Updating

1. ✅ Verify version number
2. ✅ Test core functionality
3. ✅ Restart Claude Code if needed

---

## 🚀 Next Steps

After successful update, check out:
- **[Quick Start Guide](quickstart.md)** - Learn new features
- **[Usage Guide](usage.md)** - View complete API documentation
- **[Troubleshooting](troubleshooting.md)** - Solve common problems

---

## 📮 Need Help?

If you encounter issues, feel free to:
- Check [Troubleshooting Documentation](troubleshooting.md)
- Submit [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)
