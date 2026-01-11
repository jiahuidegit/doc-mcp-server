#!/bin/bash
#
# Document Analyzer MCP - GitHub上传脚本
# 作者: Yang Jiahui
#

set -e  # 遇到错误立即退出

echo "================================="
echo "Document Analyzer MCP - GitHub上传"
echo "================================="
echo ""

# 进入项目目录
cd /Users/yangjiahui/work/demo/chengtay-ai/document-analyzer-mcp

# 检查是否已经是git仓库
if [ -d ".git" ]; then
    echo "⚠️  检测到已存在的Git仓库"
    read -p "是否要重新初始化？(y/n): " reset_git
    if [ "$reset_git" = "y" ]; then
        rm -rf .git
        echo "✅ 已删除旧的Git仓库"
    fi
fi

# 初始化Git仓库
if [ ! -d ".git" ]; then
    echo ""
    echo "【步骤1】初始化Git仓库..."
    git init
    git branch -M main
    echo "✅ Git仓库初始化完成"
fi

# 添加所有文件
echo ""
echo "【步骤2】添加文件..."
git add .

# 显示状态
echo ""
echo "【步骤3】文件状态检查..."
git status --short | head -20
echo ""
file_count=$(git status --short | wc -l | tr -d ' ')
echo "总计: $file_count 个文件"

# 创建提交
echo ""
echo "【步骤4】创建提交..."
git commit -m "feat: initial release - Document Analyzer MCP v0.1.0

🎉 初始版本发布

核心功能:
- Excel文档智能分析（支持4249+合并单元格）
- 8个MCP工具完整实现
- 270个字段精确映射
- Token消耗降低87%
- 成功率提升至90%+

技术特性:
- Python 3.10+ 支持
- MCP协议标准化接口
- 完整的中英文文档
- 测试覆盖核心功能

详见 CHANGELOG.md"

echo "✅ 提交创建完成"

# 显示提交信息
echo ""
echo "【步骤5】提交信息预览..."
git log -1 --pretty=format:"%h - %s%n%n%b" --stat | head -30
echo ""

# 询问GitHub用户名
echo ""
echo "【步骤6】配置GitHub远程仓库..."
read -p "请输入你的GitHub用户名: " github_username

if [ -z "$github_username" ]; then
    echo "❌ 用户名不能为空"
    exit 1
fi

# 检查remote是否已存在
if git remote | grep -q "^origin$"; then
    echo "⚠️  检测到已存在的remote: origin"
    read -p "是否要更新remote URL？(y/n): " update_remote
    if [ "$update_remote" = "y" ]; then
        git remote remove origin
    else
        echo "跳过remote配置"
    fi
fi

# 添加远程仓库
if ! git remote | grep -q "^origin$"; then
    git remote add origin "https://github.com/$github_username/doc-mcp-server.git"
    echo "✅ 远程仓库配置完成: https://github.com/$github_username/doc-mcp-server.git"
fi

# 提示手动创建GitHub仓库
echo ""
echo "================================="
echo "🌐 下一步: 创建GitHub仓库"
echo "================================="
echo ""
echo "请在浏览器中完成以下步骤:"
echo ""
echo "1. 访问: https://github.com/new"
echo ""
echo "2. 填写仓库信息:"
echo "   Repository name: doc-mcp-server"
echo "   Description: 让AI读懂任何复杂文档 - 通用MCP服务器"
echo "   ✅ Public (公开)"
echo "   ❌ 不要勾选 Add README"
echo "   ❌ 不要勾选 Add .gitignore"
echo "   ❌ 不要选择 License (我们已有)"
echo ""
echo "3. 点击 'Create repository'"
echo ""
read -p "已创建GitHub仓库？按回车继续推送..."

# 推送到GitHub
echo ""
echo "【步骤7】推送到GitHub..."
echo ""
echo "正在推送..."
if git push -u origin main; then
    echo ""
    echo "================================="
    echo "🎉 成功！代码已上传到GitHub"
    echo "================================="
    echo ""
    echo "仓库地址: https://github.com/$github_username/doc-mcp-server"
    echo ""
    echo "下一步:"
    echo "1. 访问仓库并检查文件"
    echo "2. 设置Topics: mcp, python, excel, ai, llm, document-analysis"
    echo "3. 创建Release: v0.1.0"
    echo "4. 发布到PyPI (参考 PUBLISH_GUIDE.md)"
    echo ""
else
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "可能的原因:"
    echo "1. GitHub仓库未创建"
    echo "2. 没有推送权限"
    echo "3. 网络连接问题"
    echo ""
    echo "手动推送命令:"
    echo "git push -u origin main"
    echo ""
fi
