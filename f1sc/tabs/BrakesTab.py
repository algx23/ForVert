from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from f1sc.util import create_label, create_slider


class BrakesTab(QWidget):
    def __init__(self):
        super().__init__(None)

    def init_tab(self):

        # create the brakes page
        brakes_page = QWidget()
        # layout
        brakes_page_layout = QVBoxLayout()
        brakes_page.setLayout(brakes_page_layout)
        brake_bias_layout = QHBoxLayout()
        brake_pressure_layout = QHBoxLayout()

        layouts = [brake_pressure_layout, brake_bias_layout]
        for layout in layouts:
            brakes_page_layout.addLayout(layout)

        brake_pressure_label = create_label("Brake Pressure %", "data_category")
        brake_pressure_slider = create_slider(50, 100, False)
        selected_brake_pressure_value_label = create_label(
            str(brake_pressure_slider.getValue())
        )
        brake_pressure_slider.valueChanged.connect(
            lambda: selected_brake_pressure_value_label.setText(
                str(brake_pressure_slider.getValue())
            )
        )
        brake_pressure_widgets = [
            brake_pressure_label,
            brake_pressure_slider,
            selected_brake_pressure_value_label,
        ]

        for widget in brake_pressure_widgets:
            brake_pressure_layout.addWidget(widget)

        brakes_page_layout.addLayout(brake_pressure_layout)
        brakes_page_layout.addLayout(brake_bias_layout)

        brake_bias_label = create_label(
            "Brake Bias (Front ---  Rear) %", "data_category"
        )
        brake_bias_slider = create_slider(50, 70, False)
        selected_brake_bias_value_label = create_label(
            str(brake_bias_slider.getValue())
        )
        brake_bias_slider.valueChanged.connect(
            lambda: selected_brake_bias_value_label.setText(
                str(brake_bias_slider.getValue())
            )
        )

        brake_bias_widgets = [
            brake_bias_label,
            brake_bias_slider,
            selected_brake_bias_value_label,
        ]

        for widget in brake_bias_widgets:
            brake_bias_layout.addWidget(widget)

        return brakes_page
