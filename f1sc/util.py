"""
this file contains certain utility functions which make code a little bit cleaner
"""

from PyQt6.QtWidgets import QLabel


def create_label(text: str, data_category: str = None) -> QLabel:
    label = QLabel()
    label.setText(text)
    if data_category:
        label.setObjectName(data_category)
    return label
