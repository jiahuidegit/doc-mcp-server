"""
Document Analyzer MCP - 基础分析器抽象类
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class DocumentFormat(Enum):
    """文档格式枚举"""
    EXCEL = "excel"
    PDF = "pdf"
    WORD = "word"
    CSV = "csv"
    MARKDOWN = "markdown"
    UNKNOWN = "unknown"


@dataclass
class DocumentMeta:
    """文档元数据"""
    format: DocumentFormat
    file_path: str
    file_size: int  # 字节
    page_count: Optional[int] = None  # PDF页数或Excel sheet数
    total_fields: Optional[int] = None
    encoding: Optional[str] = None


@dataclass
class SectionInfo:
    """章节信息"""
    title: str
    start_row: int
    end_row: int
    start_col: Optional[int] = None
    end_col: Optional[int] = None
    level: int = 1  # 章节层级
    parent: Optional[str] = None  # 父章节标题


@dataclass
class FieldInfo:
    """字段信息"""
    key: str  # 字段唯一键(章节名_完整字段路径)
    name: str  # 字段显示名(最底层字段名)
    coord: str  # 坐标(如A1)
    row: int  # 表头所在行
    col: int  # 列号
    section: str  # 所属章节
    full_path: Optional[str] = None  # 完整字段路径(多层表头合并, 如: 借贷交易_余额_被追偿余额)
    data_row: Optional[int] = None  # 数据所在行(实际值的位置)
    value_type: Optional[str] = None  # 数据类型


class BaseAnalyzer(ABC):
    """文档分析器基类"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self._structure_cache = None

    @abstractmethod
    def analyze(self) -> Dict[str, Any]:
        """
        分析文档结构

        Returns:
            {
                'meta': DocumentMeta,
                'sections': List[SectionInfo],
                'fields': List[FieldInfo],
                'summary': str
            }
        """
        pass

    @abstractmethod
    def get_field_value(self, field_key: str) -> Any:
        """获取字段值"""
        pass

    @abstractmethod
    def set_field_value(self, field_key: str, value: Any):
        """设置字段值"""
        pass

    @abstractmethod
    def get_section_data(self, section_name: str) -> Dict[str, Any]:
        """获取章节数据"""
        pass

    def get_structure(self) -> Dict[str, Any]:
        """获取文档结构(带缓存)"""
        if self._structure_cache is None:
            self._structure_cache = self.analyze()
        return self._structure_cache

    def clear_cache(self):
        """清除缓存"""
        self._structure_cache = None

    @staticmethod
    def detect_format(file_path: str) -> DocumentFormat:
        """检测文档格式"""
        file_path_lower = file_path.lower()

        if file_path_lower.endswith(('.xlsx', '.xls')):
            return DocumentFormat.EXCEL
        elif file_path_lower.endswith('.pdf'):
            return DocumentFormat.PDF
        elif file_path_lower.endswith('.docx'):
            return DocumentFormat.WORD
        elif file_path_lower.endswith('.csv'):
            return DocumentFormat.CSV
        elif file_path_lower.endswith('.md'):
            return DocumentFormat.MARKDOWN
        else:
            return DocumentFormat.UNKNOWN
