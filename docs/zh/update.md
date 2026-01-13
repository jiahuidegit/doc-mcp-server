# 🔄 更新教程

本教程将指导你如何将 Document Analyzer MCP Server 更新到最新版本。

---

## 📦 检查当前版本

### 使用 pip/pipx 检查

```bash
# 如果使用 pipx 安装
pipx list | grep doc-mcp-server

# 如果使用 pip 安装
pip show doc-mcp-server
```

输出示例：
```
Name: doc-mcp-server
Version: 0.1.0
```

### 在 Python 中检查

```bash
python -c "import document_analyzer; print(document_analyzer.__version__)"
```

---

## 🚀 更新到最新版本

### macOS / Linux

#### 如果使用 pipx 安装 (推荐)

```bash
# 更新到最新版本
pipx upgrade doc-mcp-server

# 查看更新后的版本
pipx list | grep doc-mcp-server
```

#### 如果使用 pip 安装

```bash
# macOS (可能需要添加 --break-system-packages)
pip3 install --upgrade doc-mcp-server --break-system-packages

# Linux
pip3 install --upgrade doc-mcp-server --user
```

#### 如果使用虚拟环境

```bash
# 激活虚拟环境
source ~/doc-mcp-venv/bin/activate

# 更新
pip install --upgrade doc-mcp-server

# 退出虚拟环境
deactivate
```

---

### Windows

#### 如果使用 pip 安装

```bash
# 打开 CMD 或 PowerShell
pip install --upgrade doc-mcp-server
```

#### 如果使用 pipx 安装

```bash
pipx upgrade doc-mcp-server
```

#### 如果使用虚拟环境

```bash
# 激活虚拟环境
doc-mcp-venv\Scripts\activate

# 更新
pip install --upgrade doc-mcp-server

# 退出虚拟环境
deactivate
```

---

## 🔍 验证更新

### 检查新版本

```bash
# 使用 pipx
pipx list | grep doc-mcp-server

# 使用 pip
pip show doc-mcp-server

# 或在 Python 中
python -c "import document_analyzer; print(document_analyzer.__version__)"
```

### 测试功能

```bash
# 测试服务器是否正常运行
python -m document_analyzer.server
```

看到 `MCP server running...` 说明更新成功。按 `Ctrl+C` 停止。

---

## ⚙️ 更新后配置

### Claude Desktop 配置

通常情况下，更新后**无需修改配置文件**。

但如果遇到问题，可以重启 Claude Desktop：

1. **完全关闭** Claude Desktop
2. **重新打开** Claude Desktop

### 清除缓存 (如果需要)

```bash
# macOS
rm -rf ~/Library/Caches/Claude/mcp*

# Windows
del /s /q %LOCALAPPDATA%\Claude\Cache\mcp*

# Linux
rm -rf ~/.cache/Claude/mcp*
```

---

## 📋 版本更新记录

### v0.1.1 (最新)
- ✅ 优化 Excel 表格识别
- ✅ 支持复杂多层表头
- ✅ 子章节拆分功能

### v0.1.0
- 🎉 首次发布
- ✅ Excel 基础支持
- ✅ 8 个核心工具

查看完整更新日志: [CHANGELOG.md](../../CHANGELOG.md)

---

## 🔄 升级到特定版本

如果需要安装特定版本（例如回退到旧版本）：

```bash
# 使用 pipx
pipx install doc-mcp-server==0.1.0

# 使用 pip
pip install doc-mcp-server==0.1.0
```

查看所有可用版本：
```bash
pip index versions doc-mcp-server
```

---

## 🛠️ 强制重新安装

如果更新出现问题，可以尝试强制重新安装：

### 使用 pipx

```bash
# 卸载旧版本
pipx uninstall doc-mcp-server

# 安装新版本
pipx install doc-mcp-server
```

### 使用 pip

```bash
# 强制重新安装
pip install --force-reinstall doc-mcp-server
```

---

## ❓ 常见问题

### Q: 更新后 Claude 无法识别工具

**A:** 可能是缓存问题。

**解决方案**:
1. 完全关闭 Claude Desktop
2. 清除缓存（见上文）
3. 重新打开 Claude Desktop

---

### Q: 更新时提示 "Permission denied"

**A:** 权限不足。

**解决方案**:
```bash
# macOS/Linux (不推荐使用 sudo)
pip3 install --upgrade doc-mcp-server --user

# 或使用 pipx（推荐）
pipx upgrade doc-mcp-server
```

---

### Q: 更新后出现新的错误

**A:** 可能是依赖冲突或破坏性更新。

**解决方案**:
1. 查看 [CHANGELOG.md](../../CHANGELOG.md) 了解破坏性变更
2. 回退到上一个稳定版本（见上文）
3. 提交 [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)

---

### Q: 如何检查是否有新版本可用？

**A:** 使用 pip 检查：

```bash
# 查看当前版本和最新版本
pip list --outdated | grep doc-mcp-server

# 或使用 pipx
pipx upgrade-all --dry-run
```

---

## 🔔 订阅更新通知

推荐方式：

1. **GitHub Watch** - 在 [GitHub 仓库](https://github.com/jiahuidegit/doc-mcp-server) 点击 "Watch" → "Releases only"
2. **PyPI RSS** - 订阅 PyPI RSS: `https://pypi.org/rss/project/doc-mcp-server/releases.xml`

---

## 📝 更新最佳实践

### 更新前

1. ✅ 查看 [CHANGELOG.md](../../CHANGELOG.md) 了解新功能和破坏性变更
2. ✅ 备份重要配置文件（如果有自定义配置）
3. ✅ 记录当前版本号（以便回退）

### 更新后

1. ✅ 验证版本号
2. ✅ 测试核心功能
3. ✅ 重启 Claude Desktop

---

## 🚀 下一步

更新成功后，请查看：
- **[快速开始指南](quickstart.md)** - 学习新功能
- **[使用指南](usage.md)** - 查看完整 API 文档
- **[故障排查](troubleshooting.md)** - 解决常见问题

---

## 📮 需要帮助？

如果遇到问题，欢迎：
- 查看 [故障排查文档](troubleshooting.md)
- 提交 [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)
