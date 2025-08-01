"""
this file contains certain utility functions which make code a little bit cleaner
"""

from PyQt6.QtWidgets import QLabel
from pyqt_advanced_slider import Slider


def create_label(text: str, data_category: str = None) -> QLabel:
    label = QLabel()
    label.setText(text)
    if data_category:
        label.setObjectName(data_category)
    return label


def create_slider(min: int | float, max: int | float, is_float: bool) -> Slider:
    slider = Slider()
    if is_float:
        slider.setFloat(True)
    slider.setMinimum(min)
    slider.setMaximum(max)
    return slider
