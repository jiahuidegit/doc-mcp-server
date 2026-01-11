# 🔧 Claude Desktop 配置指南

## 前提条件

✅ **已完成测试** - 所有8个核心功能测试通过
- 文档分析: ✅
- 获取结构: ✅
- 列出章节/字段: ✅
- 读取字段/章节: ✅
- 写入字段: ✅
- 导出结构: ✅

## 📦 安装MCP SDK

### 方式1: 使用pip (推荐)
```bash
# 如果遇到环境保护，使用--break-system-packages
pip3 install mcp --break-system-packages
```

### 方式2: 使用虚拟环境
```bash
# 创建虚拟环境
python3 -m venv ~/mcp-venv

# 激活虚拟环境
source ~/mcp-venv/bin/activate

# 安装MCP SDK
pip install mcp

# 修改配置文件中的command为虚拟环境的python路径
# /Users/yangjiahui/mcp-venv/bin/python
```

## ⚙️ 配置Claude Desktop

### 步骤1: 找到配置文件

配置文件位置：
```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

### 步骤2: 编辑配置

```bash
# 方式1: 使用nano编辑器
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json

# 方式2: 使用VSCode
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### 步骤3: 添加MCP服务器配置

在配置文件中添加以下内容：

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "python3",
      "args": [
        "-m",
        "document_analyzer.server"
      ],
      "cwd": "/Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server/src",
      "env": {}
    }
  }
}
```

**注意事项**：
1. 如果已有其他MCP服务器，保留它们，只添加document-analyzer部分
2. `cwd`路径必须是**绝对路径**
3. 确保Python能找到`document_analyzer`模块

### 完整配置示例（包含其他MCP）

如果你已经有其他MCP服务器：

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "document-analyzer": {
      "command": "python3",
      "args": ["-m", "document_analyzer.server"],
      "cwd": "/Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server/src"
    }
  }
}
```

### 步骤4: 重启Claude Desktop

**完全关闭并重新打开Claude Desktop应用**

## ✅ 验证配置

### 方法1: 查看MCP工具

在Claude中询问：
```
你有哪些document-analyzer相关的工具？
```

Claude应该列出8个工具：
1. analyze_document
2. get_structure
3. read_field
4. read_section
5. write_field
6. list_sections
7. list_fields
8. export_structure

### 方法2: 测试功能

在Claude中测试：

```
请使用 analyze_document 工具分析这个文件:
/Users/yangjiahui/work/demo/chengtay-ai/src/main/resources/templates/credit_report_template.xlsx
```

预期返回：
```json
{
  "meta": {
    "format": "excel",
    "file_size": 44216,
    "page_count": 1,
    "total_fields": 270
  },
  "sections": [
    {"title": "第一部分：信息概要", "row_range": "4-16"},
    ...
  ],
  "summary": "..."
}
```

## 🐛 故障排查

### 问题1: Claude无法识别工具

**症状**: Claude说"没有相关工具"

**解决方案**:
1. 检查配置文件路径是否正确
2. 检查JSON格式是否有语法错误（使用JSON验证器）
3. 确保完全重启了Claude Desktop
4. 查看Claude日志:
   ```bash
   tail -f ~/Library/Logs/Claude/mcp*.log
   ```

### 问题2: MCP服务器启动失败

**症状**: 日志显示Python模块找不到

**解决方案**:
1. 检查`cwd`路径是否正确
2. 尝试手动运行服务器:
   ```bash
   cd /Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server/src
   python3 -m document_analyzer.server
   ```
3. 确保MCP SDK已安装:
   ```bash
   python3 -c "import mcp; print('MCP已安装')"
   ```

### 问题3: MCP SDK未安装

**症状**: ModuleNotFoundError: No module named 'mcp'

**解决方案**:
```bash
# 方式1
pip3 install mcp --break-system-packages

# 方式2: 使用虚拟环境(见上文)
```

## 📝 查看日志

### Claude Desktop日志位置
```bash
# 查看最新日志
tail -f ~/Library/Logs/Claude/mcp*.log

# 查看所有日志
ls -lh ~/Library/Logs/Claude/
```

### 常见日志信息

**正常启动**:
```
[MCP] Starting server: document-analyzer
[MCP] Server document-analyzer started successfully
```

**工具调用成功**:
```
[MCP] Tool called: analyze_document
[MCP] Tool result: {...}
```

**错误信息**:
```
[MCP] Error: ModuleNotFoundError: No module named 'document_analyzer'
[MCP] Server document-analyzer failed to start
```

## 🎯 使用示例

配置成功后，你可以这样使用：

### 示例1: 分析文档
```
提示词: 分析这个征信报告的结构
/Users/yangjiahui/work/demo/chengtay-ai/src/main/resources/templates/credit_report_template.xlsx
```

### 示例2: 读取数据
```
提示词: 读取"第一部分：信息概要"的所有字段
```

### 示例3: 批量操作
```
提示词:
1. 列出这个Excel的所有章节
2. 读取前3个章节的数据
3. 导出结构为JSON文件
```

## 💡 高级配置

### 启用调试模式

在配置中添加环境变量：

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "python3",
      "args": ["-m", "document_analyzer.server"],
      "cwd": "/Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server/src",
      "env": {
        "DEBUG": "1",
        "LOG_LEVEL": "DEBUG"
      }
    }
  }
}
```

### 使用虚拟环境Python

```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "/Users/yangjiahui/mcp-venv/bin/python",
      "args": ["-m", "document_analyzer.server"],
      "cwd": "/Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server/src"
    }
  }
}
```

## ✨ 下一步

配置成功后，你可以：

1. **开发新功能** - 添加PDF/Word支持
2. **优化性能** - 添加缓存机制
3. **扩展应用** - 集成到你的项目中
4. **分享开源** - 上传GitHub并推广

---

需要帮助？查看 [QUICKSTART.md](QUICKSTART.md) 或提交 [GitHub Issue](https://github.com/yourusername/doc-mcp-server/issues)
