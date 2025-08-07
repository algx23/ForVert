from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from f1sc.util import create_label, create_slider


class TransmissionTab(QWidget):
    def __init__(self):
        super().__init__(None)

    def init_tab(self) -> QWidget:
        """initialize the tab with all components - sliders, labels etc

        Returns:
            QWidget: the tab widget populated with all its components
        """
        transmission_page = QWidget()
        transmission_page_layout = QVBoxLayout()
        transmission_page.setLayout(transmission_page_layout)

        # on throttle
        on_throttle_layout = QHBoxLayout()
        diff_adjust_on_label = create_label(
            "Differential Adjustment On Throttle (%)", "data_category"
        )
        diff_adjust_on_slider = create_slider(50, 100, False)

        selected_diff_on_value = create_label(str(diff_adjust_on_slider.getValue()))
        diff_adjust_on_slider.valueChanged.connect(
            lambda: selected_diff_on_value.setText(
                str(diff_adjust_on_slider.getValue())
            )
        )

        on_throttle_widgets = [
            diff_adjust_on_label,
            diff_adjust_on_slider,
            selected_diff_on_value,
        ]

        # off throttle
        off_throttle_layout = QHBoxLayout()
        diff_adjust_off_label = create_label(
            "Differential Adjustment Off throttle (%)", "data_category"
        )
        diff_adjust_off_slider = create_slider(50, 100, False)
        selected_diff_off_value = create_label(str(diff_adjust_off_slider.getValue()))
        diff_adjust_off_slider.valueChanged.connect(
            lambda: selected_diff_off_value.setText(
                str(diff_adjust_off_slider.getValue())
            )
        )

        off_throttle_widgets = [
            diff_adjust_off_label,
            diff_adjust_off_slider,
            selected_diff_off_value,
        ]
        for widget in on_throttle_widgets:
            on_throttle_layout.addWidget(widget)
        for widget in off_throttle_widgets:
            off_throttle_layout.addWidget(widget)

        transmission_page_layout.addLayout(on_throttle_layout)
        transmission_page_layout.addLayout(off_throttle_layout)

        return transmission_page
