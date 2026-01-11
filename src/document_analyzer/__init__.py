"""
Document Analyzer MCP - 文档分析MCP服务器
"""

__version__ = "0.1.0"
__author__ = "Yang Jiahui"

from .analyzers.base import BaseAnalyzer, DocumentFormat
from .analyzers.excel_analyzer import ExcelAnalyzer

__all__ = [
    "BaseAnalyzer",
    "DocumentFormat",
    "ExcelAnalyzer",
]
