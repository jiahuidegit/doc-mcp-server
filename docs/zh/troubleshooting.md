# 🔧 故障排查指南

本文档帮助你解决使用 Document Analyzer MCP Server 时遇到的常见问题。

---

## 📋 快速诊断

### 问题分类

| 症状 | 可能原因 | 跳转 |
|------|---------|------|
| Claude 无法识别工具 | 配置问题 | [配置问题](#配置问题) |
| 工具调用失败 | Python 环境问题 | [环境问题](#环境问题) |
| 文件找不到 | 路径问题 | [文件路径问题](#文件路径问题) |
| 分析结果不正确 | 文档格式问题 | [文档格式问题](#文档格式问题) |
| 性能慢 | 性能优化 | [性能问题](#性能问题) |

---

## 配置问题

### 问题 1: Claude 提示"没有相关工具"

**症状**: 在 Claude Code 中询问工具列表,显示没有 document-analyzer 相关工具。

**原因**:
- 配置文件路径错误
- 配置文件 JSON 格式错误
- 配置文件未保存

**解决方案**:

#### 步骤 1: 检查配置文件位置

```bash
# 全局配置
ls -la ~/.claude.json

# 项目配置
ls -la .claude.json
```

如果文件不存在,创建它：
```bash
# 全局配置
touch ~/.claude.json

# 项目配置
touch .claude.json
```

#### 步骤 2: 验证 JSON 格式

使用在线 JSON 验证器（如 jsonlint.com）检查配置文件。

常见错误：
```json
// ❌ 错误：末尾有多余逗号
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server",
    }
  }
}

// ✅ 正确
{
  "mcpServers": {
    "document-analyzer": {
      "command": "doc-mcp-server"
    }
  }
}
```

#### 步骤 3: 重启会话

如果配置文件已修改，可能需要：
1. 退出当前 Claude Code 会话
2. 重新启动 Claude Code
3. 或重启终端

---

### 问题 2: 配置文件不生效

**症状**: 修改了配置文件,但 Claude 没有加载。

**解决方案**:

1. **确认配置文件位置**
   - 全局配置：`~/.claude.json`
   - 项目配置：项目根目录 `.claude.json`
   - 项目配置优先级高于全局配置

2. **重启 Claude Code 会话**
   - 退出当前会话
   - 重新启动 Claude Code

3. **检查配置文件权限**
```bash
# macOS/Linux
chmod 644 ~/.claude.json
```

---

## 环境问题

### 问题 3: 提示 "ModuleNotFoundError: No module named 'document_analyzer'"

**症状**: Claude 日志显示找不到 Python 模块。

**原因**:
- doc-mcp-server 未安装
- Python 路径配置错误
- 使用了错误的 Python 环境

**解决方案**:

#### 步骤 1: 验证安装

```bash
# 如果使用 pipx
pipx list | grep doc-mcp-server

# 如果使用 pip
pip show doc-mcp-server

# 或直接测试导入
python -c "import document_analyzer; print('成功')"
```

#### 步骤 2: 重新安装

```bash
# 使用 pipx（推荐）
pipx uninstall doc-mcp-server
pipx install doc-mcp-server

# 使用 pip
pip uninstall doc-mcp-server
pip install doc-mcp-server
```

#### 步骤 3: 检查 Python 路径

```bash
# 查看 Python 路径
which python  # macOS/Linux
where python  # Windows

# 确保配置文件使用正确的 Python 路径
```

如果使用虚拟环境,更新配置文件：
```json
{
  "mcpServers": {
    "document-analyzer": {
      "command": "/完整路径/到/虚拟环境/bin/python",
      "args": ["-m", "document_analyzer.server"]
    }
  }
}
```

---

### 问题 4: macOS 提示 "externally-managed-environment"

**症状**: 使用 pip 安装时提示环境被外部管理。

**原因**: macOS 的 Python 环境被 Homebrew 保护。

**解决方案**:

**方式 1: 使用 pipx（推荐）**
```bash
brew install pipx
pipx install doc-mcp-server
```

**方式 2: 使用虚拟环境**
```bash
python3 -m venv ~/doc-mcp-venv
source ~/doc-mcp-venv/bin/activate
pip install doc-mcp-server
```

**方式 3: 强制安装（不推荐）**
```bash
pip3 install doc-mcp-server --break-system-packages
```

---

### 问题 5: Windows 提示 "command not found"

**症状**: 配置中使用 `python`,但找不到命令。

**解决方案**:

使用完整路径：
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

查找 Python 路径：
```bash
where python
```

---

## 文件路径问题

### 问题 6: 提示"文件不存在"

**症状**: Claude 调用工具时提示找不到文件。

**原因**:
- 路径不正确
- 使用了相对路径,但工作目录不对
- 文件名包含特殊字符

**解决方案**:

#### 使用绝对路径

✅ **正确**:
```python
# macOS/Linux
/Users/username/Documents/report.xlsx

# Windows
C:\Users\username\Documents\report.xlsx
```

❌ **错误**:
```python
~/Documents/report.xlsx  # ~ 可能不被识别
.\report.xlsx           # 相对路径可能不对
```

#### 检查文件是否存在

```bash
# macOS/Linux
ls -l /path/to/file.xlsx

# Windows
dir C:\path\to\file.xlsx
```

#### 处理特殊字符

如果文件名包含空格或特殊字符：
```python
# 在 Claude 中使用引号
"分析这个文件: '/path/with spaces/file.xlsx'"
```

---

### 问题 7: Windows 路径反斜杠问题

**症状**: Windows 路径中的反斜杠导致错误。

**解决方案**:

```python
# 方式 1: 使用双反斜杠
C:\\Users\\username\\Documents\\report.xlsx

# 方式 2: 使用正斜杠（推荐）
C:/Users/username/Documents/report.xlsx

# 方式 3: 使用原始字符串（Python 中）
r"C:\Users\username\Documents\report.xlsx"
```

---

## 文档格式问题

### 问题 8: Excel 分析结果不准确

**症状**: 章节识别错误或字段缺失。

**原因**:
- 文档结构复杂（多层表头、不规则合并单元格）
- 空行干扰章节识别
- 字段名不规范

**解决方案**:

#### 开启深度分析

```python
# 在 Claude 中明确要求深度分析
"使用深度分析模式分析这个文件"
```

#### 检查文档结构

1. 手动打开 Excel 文件
2. 检查是否有：
   - ✅ 明确的章节标题
   - ✅ 规范的表格结构
   - ❌ 过多空行
   - ❌ 不规则合并单元格

#### 预处理文档

如果文档结构太复杂：
1. 清理多余空行
2. 规范章节标题格式
3. 简化合并单元格

---

### 问题 9: PDF/Word 支持问题

**症状**: 提示不支持 PDF 或 Word 文件。

**原因**: PDF 和 Word 支持还在开发中。

**当前状态**:
- ✅ Excel (.xlsx, .xls) - 完整支持
- 🚧 PDF - 开发中
- 🚧 Word - 开发中

**临时方案**:
将 PDF/Word 转换为 Excel：
1. 使用 Adobe Acrobat 或在线工具转换
2. 检查转换后的格式
3. 使用 Excel 版本

---

## 性能问题

### 问题 10: 分析大文件很慢

**症状**: 分析超过 500 行的 Excel 文件时耗时很长。

**解决方案**:

#### 使用缓存

```python
# 第一次分析（慢）
analyze_document("/path/to/large.xlsx")

# 后续操作使用 get_structure（快）
get_structure("/path/to/large.xlsx")
read_section(...)
```

#### 只读取必要的章节

```python
# ❌ 不要读取所有章节
read_section("章节1")
read_section("章节2")
read_section("章节3")

# ✅ 只读取需要的
read_section("我需要的章节")
```

#### 关闭深度分析

```python
# 对于简单文档,可以关闭深度分析
"快速分析这个文件"
```

---

### 问题 11: Token 消耗过大

**症状**: 处理大文档导致 API 费用高。

**优化方案**:

| 操作 | Token 消耗 | 优化后 |
|------|----------|-------|
| 直接读整个 Excel | 15000+ | 2000 |
| 重复分析 | 5000 | 100 |
| 读取不需要的数据 | 3000 | 500 |

**优化技巧**:
1. 使用 `analyze_document` 只分析一次
2. 使用 `get_structure` 读取缓存
3. 只读取必要的章节和字段
4. 导出结构为文件,复用分析结果

---

## 工具调用问题

### 问题 12: Claude 不调用工具,直接回答

**症状**: Claude 不使用 MCP 工具,而是尝试直接回答。

**原因**: 提问不够明确,Claude 觉得不需要工具。

**解决方案**:

明确指示使用工具：
```python
# ❌ 模糊提问
"这个文件有什么内容？"

# ✅ 明确指示
"请使用 analyze_document 工具分析这个文件"
"使用 document-analyzer 读取这个文件的结构"
```

---

### 问题 13: 工具调用超时

**症状**: 调用工具时长时间无响应。

**原因**:
- 文件过大
- 网络问题
- 服务器繁忙

**解决方案**:

1. **检查文件大小**
```bash
ls -lh /path/to/file.xlsx
```

2. **优化文件**
   - 删除不需要的工作表
   - 移除图片和图表
   - 简化复杂公式

3. **重试操作**
```python
"再试一次分析这个文件"
```

---

## 写入操作问题

### 问题 14: 写入失败 "Permission denied"

**症状**: 使用 `write_field` 时提示权限不足。

**原因**:
- 文件被其他程序打开（如 Excel）
- 文件只读
- 没有写入权限

**解决方案**:

1. **关闭文件**
   - 确保 Excel 或其他程序没有打开该文件

2. **检查文件权限**
```bash
# macOS/Linux
ls -l /path/to/file.xlsx
chmod 644 /path/to/file.xlsx

# Windows
# 右键文件 → 属性 → 去掉"只读"
```

3. **备份后重试**
```bash
cp file.xlsx file_backup.xlsx
# 然后重试写入
```

---

## 调试技巧

### 手动测试服务器

```bash
# 直接运行 MCP 服务器
python -m document_analyzer.server

# 应该看到
# MCP server running...

# 如果报错,查看错误信息
```

---

### 测试工具功能

创建测试脚本 `test.py`：
```python
from document_analyzer.analyzers.excel_analyzer import ExcelAnalyzer

# 测试分析功能
analyzer = ExcelAnalyzer("/path/to/test.xlsx")
result = analyzer.analyze()
print(result)
```

运行：
```bash
python test.py
```

---

### 启用调试模式

在配置文件中添加环境变量：

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

## 💡 预防措施

### 安装阶段

- ✅ 使用 pipx 而不是 pip（避免环境冲突）
- ✅ 验证 Python 版本 >= 3.10
- ✅ 记录安装路径和版本

### 配置阶段

- ✅ 使用 JSON 验证器检查配置文件
- ✅ 备份配置文件
- ✅ 记录自定义配置

### 使用阶段

- ✅ 使用绝对路径
- ✅ 先用小文件测试
- ✅ 写入前备份文件

---

## 📮 获取帮助

如果以上方法都无法解决问题：

1. **收集信息**:
   - 操作系统和版本
   - Python 版本
   - doc-mcp-server 版本
   - 完整错误信息
   - Claude 日志相关部分

2. **提交 Issue**:
   - 访问 [GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues)
   - 使用 Bug Report 模板
   - 提供详细信息

3. **查看已知问题**:
   - [CHANGELOG.md](../../CHANGELOG.md) - 版本更新日志
   - [GitHub Issues](https://github.com/jiahuidegit/doc-mcp-server/issues) - 已知问题列表

---

## 🔄 常见解决方案速查

| 问题 | 快速解决 |
|------|---------|
| Claude 无法识别工具 | 重启 Claude Desktop |
| 找不到模块 | `pipx reinstall doc-mcp-server` |
| 配置不生效 | 清除缓存 + 重启 |
| 文件找不到 | 使用绝对路径 |
| 分析太慢 | 使用缓存 get_structure |
| Token 太多 | 只读必要章节 |
| 写入失败 | 关闭文件 + 检查权限 |
