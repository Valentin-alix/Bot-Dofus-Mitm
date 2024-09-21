from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Callable, cast

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QHeaderView, QWidget
from qfluentwidgets import LineEdit, SingleDirectionScrollArea, SmoothMode, TableWidget


class SearchType(Enum):
    CONTAINS = auto()
    EXACT = auto()


@dataclass
class ColumnInfo:
    name: str
    search_type: SearchType | None = field(default=SearchType.CONTAINS)
    get_texts_func: Callable[[QWidget], list[str]] | None = field(default=None)


class BaseTableWidget(SingleDirectionScrollArea):
    def __init__(self, is_searchable: bool = True, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_searchable = is_searchable
        self.table = TableWidget(parent=self)

        self.setWidget(self.table)
        self.setStyleSheet("QScrollArea{background: transparent; border: none}")
        self.table.setStyleSheet("QWidget{background: transparent}")

        self.table.setWordWrap(True)
        self.table.scrollDelagate.verticalSmoothScroll.setSmoothMode(
            SmoothMode.NO_SMOOTH
        )
        if self.is_searchable:
            self.table.setRowCount(1)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().hide()

        self.setWidget(self.table)
        self.setWidgetResizable(True)

        self.col_header_edit: list[LineEdit | None] = []
        self.columns_infos: list[ColumnInfo] = []
        self.table.cellChanged.connect(self.on_cell_changed)

    def set_columns(self, columns_infos: list[ColumnInfo]):
        self.columns_infos = columns_infos
        self.table.setColumnCount(len(columns_infos))

        if self.is_searchable:
            for index, col_info in enumerate(columns_infos):
                if not col_info.search_type:
                    self.col_header_edit.append(None)
                    continue

                col_search_edit = LineEdit()
                col_search_edit.textChanged.connect(self.on_header_text_changed)
                col_search_edit.textEdited.connect(self.on_header_text_changed)
                self.col_header_edit.append(col_search_edit)
                self.table.setCellWidget(0, index, col_search_edit)

        self.table.setHorizontalHeaderLabels([_col.name for _col in columns_infos])

    def get_header_filters(self, columns_infos: list[ColumnInfo]) -> list[str]:
        cols_filters: list[str] = []

        for index, col_info in enumerate(columns_infos):
            if not col_info.search_type:
                cols_filters.append("")
                continue
            col_edit = self.col_header_edit[index]
            assert col_edit is not None
            cols_filters.append(col_edit.text())

        return cols_filters

    def filter_row(self, row_index: int, cols_filters: list[str]):
        if row_index == 0:
            return
        for col_index, col_info in enumerate(self.columns_infos):
            if not col_info.search_type or cols_filters[col_index] == "":
                continue

            if col_info.get_texts_func is not None:
                col_widget = self.table.cellWidget(row_index, col_index)
                col_widget = cast(QWidget, col_widget)
                cell_texts = col_info.get_texts_func(col_widget)
            else:
                wid_item = self.table.item(row_index, col_index)
                if not wid_item:
                    continue
                cell_texts = [wid_item.text()]

            if col_info.search_type == SearchType.CONTAINS:
                if all(
                    not cell_text.lower().startswith(cols_filters[col_index].lower())
                    for cell_text in cell_texts
                ):
                    self.table.setRowHidden(row_index, True)
                    break
            elif col_info.search_type == SearchType.EXACT:
                if all(
                    not cell_text == cols_filters[col_index] for cell_text in cell_texts
                ):
                    self.table.setRowHidden(row_index, True)
                    break
        else:
            self.table.setRowHidden(row_index, False)

    def filter_rows(self) -> None:
        cols_filters = self.get_header_filters(self.columns_infos)
        for row_index in range(1, self.table.rowCount()):
            self.filter_row(row_index, cols_filters)

    @pyqtSlot(int, int)
    def on_cell_changed(self, row_index: int, _: int):
        cols_filters = self.get_header_filters(self.columns_infos)
        self.filter_row(row_index, cols_filters)

    def on_header_text_changed(self):
        self.filter_rows()
