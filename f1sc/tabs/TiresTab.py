from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from f1sc.util import create_label, create_slider


class TiresTab(QWidget):
    def __init__(self):
        super().__init__(None)

    def init_tab(self):
        tires_page = QWidget()

        # layouts
        tires_page_layout = QVBoxLayout()
        tires_page.setLayout(tires_page_layout)

        front_tire_pressure_layout = QHBoxLayout()
        rear_tire_pressure_layout = QHBoxLayout()

        tires_page_layout.addLayout(front_tire_pressure_layout)
        tires_page_layout.addLayout(rear_tire_pressure_layout)

        # front tire pressure section
        front_tp_label = create_label("Front Tire Pressure", "data_category")

        front_tp_slider = create_slider(21, 25, True)
        front_tp_slider.setSingleStep(0.4)
        selected_front_tp_value_label = create_label(str(front_tp_slider.getValue()))
        front_tp_slider.valueChanged.connect(
            lambda: selected_front_tp_value_label.setText(
                str(front_tp_slider.getValue())
            )
        )
        front_tp_widgets = [
            front_tp_label,
            front_tp_slider,
            selected_front_tp_value_label,
        ]

        for widget in front_tp_widgets:
            front_tire_pressure_layout.addWidget(widget)

        # rear tires
        rear_tp_label = create_label("Rear Tire Pressure", "data_category")
        rear_tp_slider = create_slider(19.5, 23.5, True)
        rear_tp_slider.setSingleStep(0.4)
        selected_rear_tp_value_label = create_label(str(rear_tp_slider.getValue()))
        rear_tp_slider.valueChanged.connect(
            lambda: selected_rear_tp_value_label.setText(str(rear_tp_slider.getValue()))
        )

        rear_tp_widgets = [rear_tp_label, rear_tp_slider, selected_rear_tp_value_label]
        for widget in rear_tp_widgets:
            rear_tire_pressure_layout.addWidget(widget)

        return tires_page
