# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2025-01-13

### Documentation
- 📚 Complete documentation restructure with Chinese/English separation
- 🔧 Fixed configuration instructions for Claude Code CLI (not Claude Desktop)
- 📖 New comprehensive installation guide for macOS/Windows/Linux
- 🔄 Added dedicated update guide
- 🚀 New 5-minute quick start guide
- 🔍 Comprehensive troubleshooting documentation
- 💡 Added API documentation with real-world use cases
- 🌍 Full bilingual support (docs/zh and docs/en)
- 🗑️ Removed outdated QUICKSTART.md and CLAUDE_SETUP.md

### Changed
- ⚙️ Configuration method updated: Claude Desktop → Claude Code CLI
- 📝 Configuration file location: `~/.claude.json` or project `.claude.json`
- 🔗 Updated GitHub repository links to correct username
- ✉️ Updated author email to jiahuide0320@gmail.com

## [0.1.1] - 2025-01-12

### Improved
- 🚀 Excel complex table recognition significantly enhanced
- 📊 Multi-level header merging algorithm optimized
- 🔍 Automatic subsection splitting for complex sections
- 🎯 Header detection logic improved with keyword recognition
- 📉 Field count reduced by 66% through deduplication (270 → 93)

### Fixed
- ✅ Data reading now correctly reads from data rows instead of header rows
- ✅ Field path generation supports multi-level hierarchy
- ✅ Empty rows in headers are now handled correctly

### Changed
- 📝 Extended `FieldInfo` structure with `full_path` and `data_row` fields
- 🏗️ Sections can now be automatically split into subsections
- 📋 Field keys now include full hierarchical path

### Performance
- Chapter structure optimized: 8 → 12 subsections for better organization
- More accurate field identification for complex enterprise credit reports

## [0.1.0] - 2025-01-11

### Added
- 🎉 Initial release
- ✅ Excel document analyzer with full support for merged cells
- ✅ 8 MCP tools for document analysis
- ✅ Field mapping and structure extraction
- ✅ Section-based data reading
- ✅ Export to JSON/Markdown
- ✅ Comprehensive documentation (EN/CN)
- ✅ Test suite with 100% core functionality coverage

### Features
- **analyze_document**: Analyze document structure
- **get_structure**: Get cached structure info
- **read_field**: Read specific field value
- **read_section**: Read entire section data
- **write_field**: Write field value (Excel only)
- **list_sections**: List all sections
- **list_fields**: List all fields or section fields
- **export_structure**: Export structure to file

### Performance
- Token consumption reduced by 87% (15000 → 2000)
- Success rate improved from 30% to 90%+
- Handles 323 rows × 24 columns with 4249 merged cells

### Documentation
- Complete README (Chinese & English)
- Quick start guide
- Claude Desktop setup guide
- Architecture documentation
- Contributing guidelines

[unreleased]: https://github.com/jiahuidegit/doc-mcp-server/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/jiahuidegit/doc-mcp-server/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/jiahuidegit/doc-mcp-server/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/jiahuidegit/doc-mcp-server/releases/tag/v0.1.0
