# 🚀 快速开始指南

本指南将帮助你在 5 分钟内开始使用 Document Analyzer MCP Server。

---

## 📋 前提条件

确保已完成以下步骤：

- ✅ [安装 doc-mcp-server](installation.md)
- ✅ 安装 Claude Code CLI

---

## ⚙️ 配置 Claude Code

### 步骤 1: 选择配置方式

Claude Code 支持两种配置：

**全局配置（推荐）**
- 配置文件：`~/.claude.json`
- 所有项目都可以使用

**项目配置**
- 配置文件：项目根目录 `.claude.json`
- 只在当前项目生效

### 步骤 2: 编辑配置文件

使用任何文本编辑器打开或创建配置文件：

**macOS / Linux:**
```bash
# 全局配置
nano ~/.claude.json
# 或
code ~/.claude.json

# 项目配置
nano .claude.json
# 或
code .claude.json
```

**Windows:**
```bash
# 全局配置
notepad %USERPROFILE%\.claude.json

# 项目配置
notepad .claude.json
```

### 步骤 3: 添加 MCP 服务器配置

#### 🎯 如果使用 pipx 安装 (推荐)

这是最简单的配置方式：

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

**Windows 用户可能需要指定完整路径:**
```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "C:\\Users\\你的用户名\\AppData\\Local\\Programs\\Python\\Python310\\python.exe",
      "args": ["-m", "document_analyzer.server"]
    }
  }
}
```

#### 如果使用虚拟环境

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

### 步骤 4: 保存配置文件

保存配置文件后，配置即生效。无需重启。

---

## ✅ 验证配置

### 检查工具是否加载

在 Claude Code 中输入：

```
你有哪些 document-analyzer 相关的工具？
```

Claude 应该会列出 **8 个工具**：

1. **analyze_document** - 分析文档结构,生成元数据
2. **get_structure** - 获取已分析的文档结构
3. **read_field** - 读取指定字段的值
4. **read_section** - 读取整个章节数据
5. **write_field** - 写入字段值 (仅 Excel)
6. **list_sections** - 列出所有章节
7. **list_fields** - 列出所有字段或指定章节的字段
8. **export_structure** - 导出文档结构为 JSON 或 Markdown

如果看到这些工具,说明配置成功! 🎉

---

## 📖 基础使用示例

### 示例 1: 分析文档结构

准备一个 Excel 文件,例如 `/path/to/report.xlsx`

在 Claude 中输入：

```
请分析这个文件的结构:
/path/to/report.xlsx
```

Claude 会调用 `analyze_document` 工具,返回类似：

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
      "title": "基本信息",
      "row_range": "2-10",
      "fields_count": 15
    },
    {
      "title": "详细数据",
      "row_range": "11-30",
      "fields_count": 35
    }
  ]
}
```

### 示例 2: 列出所有章节

```
这个文档有哪些章节？
/path/to/report.xlsx
```

返回：
```json
{
  "sections": [
    "基本信息",
    "详细数据",
    "统计汇总"
  ]
}
```

### 示例 3: 读取特定章节

```
读取"基本信息"章节的所有数据
```

返回：
```json
{
  "section_name": "基本信息",
  "data": {
    "企业名称": "示例公司",
    "注册时间": "2020-01-01",
    "注册资本": "1000万"
  }
}
```

### 示例 4: 读取单个字段

```
读取"基本信息_企业名称"这个字段
```

返回：
```json
{
  "field_key": "基本信息_企业名称",
  "value": "示例公司"
}
```

### 示例 5: 导出文档结构

```
把这个文档的结构导出为 JSON 文件
保存到 /path/to/output.json
```

会生成一个包含完整文档结构的 JSON 文件。

---

## 🎯 实际应用场景

### 场景 1: 处理复杂征信报告

```
用户提问: "分析这份企业征信报告,告诉我这家公司的借贷情况"

AI 工作流程:
1. 调用 analyze_document 分析报告结构
2. 调用 list_sections 查看有哪些章节
3. 调用 read_section 读取"借贷信息"章节
4. 总结并回答用户
```

### 场景 2: 批量提取数据

```
用户提问: "从这份报告提取所有财务指标"

AI 工作流程:
1. 调用 analyze_document 识别财务章节
2. 调用 read_section 读取"财务数据"章节
3. 整理成表格展示给用户
```

### 场景 3: 文档对比

```
用户提问: "对比这两份报告的差异"

AI 工作流程:
1. 分别调用 analyze_document 分析两份文档
2. 使用 read_section 读取相同章节
3. 对比数据并高亮差异
```

---

## 📝 使用技巧

### 技巧 1: 使用相对路径

如果你在特定目录工作,可以使用相对路径：

```
# 当前目录下的文件
分析 ./report.xlsx

# 上级目录
分析 ../data/report.xlsx
```

### 技巧 2: 批量操作

可以让 Claude 一次处理多个任务：

```
请帮我:
1. 分析 report.xlsx 的结构
2. 列出所有章节
3. 读取前 3 个章节的数据
4. 导出结构为 JSON
```

### 技巧 3: 模糊搜索

不确定准确的字段名？可以这样问：

```
这个文档里有没有"企业名称"相关的字段？
```

Claude 会调用 `list_fields` 并帮你找到相似的字段。

---

## ❓ 常见问题

### Q: Claude 没有调用工具,而是直接回答

**A:** Claude 可能觉得不需要工具。明确告诉它使用工具：

```
请使用 analyze_document 工具分析这个文件
```

---

### Q: 提示找不到文件

**A:** 检查文件路径是否正确：

```bash
# 在终端检查文件是否存在
ls -l /path/to/your/file.xlsx
```

使用**绝对路径**更保险：
- macOS/Linux: `/Users/用户名/Documents/file.xlsx`
- Windows: `C:\Users\用户名\Documents\file.xlsx`

---

### Q: 工具调用失败

**A:** 可能是配置问题。查看 Claude 日志：

**macOS:**
```bash
tail -f ~/Library/Logs/Claude/mcp*.log
```

**Windows:**
```bash
type %APPDATA%\Claude\logs\mcp*.log
```

---

## 🚀 下一步

恭喜!你已经掌握了基础使用。接下来：

- **[使用指南](usage.md)** - 查看完整 API 文档和高级用法
- **[故障排查](troubleshooting.md)** - 解决常见问题
- **[示例项目](../../examples/)** - 查看更多实际案例

---

## 📮 需要帮助？

如果遇到问题,欢迎：
- 查看 [故障排查文档](troubleshooting.md)
- 提交 [GitHub Issue](https://github.com/jiahuidegit/doc-mcp-server/issues)
