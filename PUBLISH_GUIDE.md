# 📦 GitHub + PyPI 发布指南

完整的开源发布流程，从代码到用户只需3步！

---

## 第一步：上传到GitHub

### 1.1 初始化Git仓库

```bash
cd /Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server

# 初始化Git
git init

# 添加所有文件
git add .

# 首次提交
git commit -m "feat: initial commit - Document Analyzer MCP v0.1.0

- 🎉 初始版本发布
- ✅ 完整的Excel文档分析功能
- ✅ 8个MCP工具
- ✅ 270个字段映射
- ✅ 支持4249个合并单元格
- 📚 完整文档（中英文）

Token消耗降低87%，成功率提升至90%+
"
```

### 1.2 创建GitHub仓库

**选项A：使用GitHub网页**

1. 访问 https://github.com/new
2. 填写信息：
   - Repository name: `doc-mcp-server`
   - Description: `让AI读懂任何复杂文档 - 解决AI上下文限制问题的通用MCP服务器`
   - Public（公开）
   - ✅ Add README (取消勾选，我们已有)
   - ✅ Add .gitignore (取消勾选，我们已有)
   - ✅ Choose a license: MIT (取消勾选，我们已有)
3. 点击 "Create repository"

**选项B：使用GitHub CLI**

```bash
# 安装GitHub CLI（如果没有）
brew install gh

# 登录GitHub
gh auth login

# 创建仓库
gh repo create doc-mcp-server --public --description "让AI读懂任何复杂文档 - 通用MCP服务器" --source=.

# 推送代码
git push -u origin main
```

### 1.3 推送代码（网页创建后）

如果使用网页创建，执行：

```bash
# 添加远程仓库（替换YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/doc-mcp-server.git

# 推送代码
git branch -M main
git push -u origin main
```

### 1.4 设置GitHub Topics

在GitHub仓库页面，点击 "About" 旁边的齿轮图标，添加以下topics：

```
mcp
claude
document-analysis
excel
pdf
python
ai
llm
context-window
rag
```

### 1.5 创建Release

1. 访问 `https://github.com/YOUR_USERNAME/doc-mcp-server/releases/new`
2. 填写信息：
   - Tag version: `v0.1.0`
   - Release title: `v0.1.0 - 初始发布 🎉`
   - Description: 复制以下内容

```markdown
## 🎉 Document Analyzer MCP v0.1.0

让AI读懂任何复杂文档的通用MCP服务器首次发布！

### ✨ 核心功能

- **智能文档分析**: 自动识别章节结构、处理合并单元格
- **精确字段定位**: 270个字段映射，支持坐标精确定位
- **8个MCP工具**: 完整的文档操作API
- **高效性能**: Token消耗降低87%，成功率90%+

### 📊 支持格式

- ✅ Excel (.xlsx, .xls) - 完整支持
- 🚧 PDF - 开发中
- 🚧 Word - 开发中

### 🚀 快速开始

```bash
# 安装
pip install doc-mcp-server

# 配置Claude Desktop
# 查看 QUICKSTART.md
```

### 📈 性能数据

- 处理323行×24列Excel
- 支持4249个合并单元格
- 提取270个字段
- Token消耗: 15000 → 2000 (节省87%)
- 成功率: 30% → 90%+

### 📚 文档

- [README](README.md)
- [快速开始](QUICKSTART.md)
- [Claude Desktop配置](CLAUDE_SETUP.md)
- [架构设计](ARCHITECTURE.md)

### 🙏 致谢

感谢所有早期测试者的反馈！

---

**完整Changelog**: [CHANGELOG.md](CHANGELOG.md)
```

3. 点击 "Publish release"

---

## 第二步：发布到PyPI

### 2.1 注册PyPI账号

1. 访问 https://pypi.org/account/register/
2. 填写信息并验证邮箱
3. 启用两步验证（推荐）

### 2.2 生成API Token

1. 访问 https://pypi.org/manage/account/token/
2. 点击 "Add API token"
3. Token name: `doc-mcp-server`
4. Scope: "Entire account"（第一次发布）或 "Project: doc-mcp-server"（后续）
5. 复制生成的token（以`pypi-`开头）

### 2.3 配置GitHub Secrets

1. 访问 `https://github.com/YOUR_USERNAME/doc-mcp-server/settings/secrets/actions`
2. 点击 "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: 粘贴刚才复制的token
5. 点击 "Add secret"

### 2.4 本地测试打包

```bash
cd /Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server

# 安装打包工具
pip install build twine

# 清理旧的构建文件
rm -rf dist/ build/ *.egg-info

# 构建包
python -m build

# 检查包
twine check dist/*
```

你应该看到：
```
Checking dist/document_analyzer_mcp-0.1.0-py3-none-any.whl: PASSED
Checking dist/document_analyzer_mcp-0.1.0.tar.gz: PASSED
```

### 2.5 测试发布到TestPyPI（可选）

```bash
# 注册TestPyPI账号: https://test.pypi.org/account/register/

# 上传到TestPyPI
twine upload --repository testpypi dist/*

# 测试安装
pip install --index-url https://test.pypi.org/simple/ doc-mcp-server
```

### 2.6 正式发布到PyPI

#### 方式1：手动发布（首次推荐）

```bash
# 上传到PyPI
twine upload dist/*

# 输入用户名：__token__
# 输入密码：<你的PyPI API Token>
```

#### 方式2：通过GitHub Actions自动发布

当你在GitHub创建新Release时，会自动触发发布：

1. 代码推送到GitHub
2. 创建新Release（如v0.1.0）
3. GitHub Actions自动构建并发布到PyPI

### 2.7 验证发布

1. 访问 https://pypi.org/project/doc-mcp-server/
2. 检查版本号和描述
3. 测试安装：

```bash
# 创建新的虚拟环境测试
python3 -m venv test-env
source test-env/bin/activate

# 从PyPI安装
pip install doc-mcp-server

# 验证导入
python -c "from document_analyzer import ExcelAnalyzer; print('成功!')"

# 退出虚拟环境
deactivate
rm -rf test-env
```

---

## 第三步：推广和维护

### 3.1 社区推广

#### 技术社区

1. **Hacker News**
   - 标题: "Show HN: Document Analyzer MCP – Let AI Read Complex Documents"
   - 链接: GitHub仓库
   - 简介: 2-3句话说明核心价值

2. **Reddit**
   - r/MachineLearning
   - r/Python
   - r/Claude (如有)
   - 标题: "[P] Document Analyzer MCP - Solving AI Context Limits"

3. **Twitter/X**
   ```
   🚀 刚开源了 Document Analyzer MCP！

   让AI轻松处理复杂Excel/PDF文档
   ✅ Token消耗降低87%
   ✅ 成功率提升至90%+
   ✅ 支持4249个合并单元格

   GitHub: https://github.com/YOUR_USERNAME/doc-mcp-server
   PyPI: pip install doc-mcp-server

   #MCP #Claude #Python #OpenSource
   ```

#### 中文社区

1. **知乎**
   - 话题：#人工智能 #开源项目 #Python
   - 文章标题：《我开源了一个MCP服务器，让AI能读懂复杂Excel》

2. **掘金**
   - 标签：Python、AI、开源
   - 文章标题：《Document Analyzer MCP：解决AI上下文限制的开源方案》

3. **V2EX**
   - 节点：Python、分享创造
   - 标题：《[开源] Document Analyzer MCP - 让AI处理复杂文档》

4. **CSDN/博客园**
   - 技术教程：《使用MCP让Claude处理复杂Excel文档》

### 3.2 添加Badges

在README.md顶部添加：

```markdown
[![PyPI version](https://badge.fury.io/py/doc-mcp-server.svg)](https://badge.fury.io/py/doc-mcp-server)
[![Python Version](https://img.shields.io/pypi/pyversions/doc-mcp-server.svg)](https://pypi.org/project/doc-mcp-server/)
[![Downloads](https://pepy.tech/badge/doc-mcp-server)](https://pepy.tech/project/doc-mcp-server)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/YOUR_USERNAME/doc-mcp-server/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/doc-mcp-server/actions/workflows/ci.yml)
```

### 3.3 持续维护

#### 每周检查
- [ ] 回复Issues
- [ ] 审查Pull Requests
- [ ] 更新依赖版本

#### 每月更新
- [ ] 发布小版本（bug修复）
- [ ] 更新文档
- [ ] 社区互动统计

#### 季度规划
- [ ] 新功能开发
- [ ] 性能优化
- [ ] 大版本发布

---

## 📊 成功指标追踪

### GitHub指标
- ⭐ Stars: 目标1000+ (6个月内)
- 🍴 Forks: 目标100+
- 👀 Watchers: 目标50+
- 🐛 Issues: 及时回复(<24小时)

### PyPI指标
- 📥 下载量: 目标10k/月
- 📈 周下载增长: >10%

### 社区指标
- 💬 Discord成员: 目标500+
- 📝 博客文章引用: 目标20+
- 🎥 视频教程: 目标5+

---

## 🎯 快速执行清单

### 今天立即执行：
```bash
# 1. Git初始化
cd /Users/yangjiahui/work/demo/chengtay-ai/doc-mcp-server
git init
git add .
git commit -m "feat: initial commit - v0.1.0"

# 2. 创建GitHub仓库（网页或CLI）
gh repo create doc-mcp-server --public --source=.

# 3. 推送代码
git push -u origin main

# 4. 打包测试
python -m build
twine check dist/*

# 5. 发布到PyPI
twine upload dist/*
```

### 本周完成：
- [ ] 创建GitHub Release
- [ ] 发布到PyPI
- [ ] 撰写技术博客
- [ ] 社区推广（至少3个平台）

### 本月完成：
- [ ] 获得100+ Stars
- [ ] 收到第一个PR
- [ ] PyPI下载量>1000

---

需要我帮你执行哪一步？我可以：
1. 生成完整的git命令
2. 撰写推广文案
3. 创建技术博客草稿
4. 优化README的PyPI展示

告诉我下一步做什么！🚀
