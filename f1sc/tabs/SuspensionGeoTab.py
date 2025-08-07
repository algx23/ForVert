from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from f1sc.util import create_label, create_slider


class SuspensionGeometryTab(QWidget):
    def __init__(self):
        super().__init__(None)
        self.init_tab()

    def init_tab(self) -> QWidget:
        suspension_geo_page = QWidget()
        suspension_geo_page_layout = QVBoxLayout()
        suspension_geo_page.setLayout(suspension_geo_page_layout)

        # layouts

        front_camber_layout = QHBoxLayout()
        rear_camber_layout = QHBoxLayout()
        front_toe_layout = QHBoxLayout()
        rear_toe_layout = QHBoxLayout()
        layouts = []
        layouts.extend(
            [front_camber_layout, rear_camber_layout, front_toe_layout, rear_toe_layout]
        )

        for layout in layouts:
            suspension_geo_page_layout.addLayout(layout)

        # inputs:

        # camber

        front_camber_label = create_label("Front Camber", "data_category")
        front_camber_slider = create_slider(-3.50, -2.50, True)
        front_camber_slider.setSingleStep(0.01)
        selected_front_camber_value = create_label(str(front_camber_slider.getValue()))
        front_camber_slider.valueChanged.connect(
            lambda: selected_front_camber_value.setText(
                str(front_camber_slider.getValue())
            )
        )

        front_camber_widgets = [
            front_camber_label,
            front_camber_slider,
            selected_front_camber_value,
        ]

        rear_camber_label = create_label("Rear Camber", "data_category")
        rear_camber_slider = create_slider(-3.50, -2.50, True)
        rear_camber_slider.setSingleStep(0.01)
        selected_rear_camber_value = create_label(str(rear_camber_slider.getValue()))
        rear_camber_slider.valueChanged.connect(
            lambda: selected_rear_camber_value.setText(
                str(rear_camber_slider.getValue())
            )
        )
        rear_camber_widgets = [
            rear_camber_label,
            rear_camber_slider,
            selected_rear_camber_value,
        ]

        for widget in front_camber_widgets:
            front_camber_layout.addWidget(widget)
        for widget in rear_camber_widgets:
            rear_camber_layout.addWidget(widget)

        #  toe
        front_toe_label = create_label("Front Toe", "data_category")
        front_toe_slider = create_slider(0.05, 0.15, True)
        front_toe_slider.setDecimals(2)  # two decimal places or the slider doesnt work
        front_toe_slider.setSingleStep(0.01)
        selected_front_toe_value_label = create_label(str(front_toe_slider.getValue()))
        front_toe_slider.valueChanged.connect(
            lambda: selected_front_toe_value_label.setText(
                str(front_toe_slider.getValue())
            )
        )
        front_toe_widgets = [
            front_toe_label,
            front_toe_slider,
            selected_front_toe_value_label,
        ]

        rear_toe_label = create_label("Rear Toe", "data_category")
        rear_toe_slider = create_slider(0.2, 0.5, True)
        rear_toe_slider.setDecimals(2)
        rear_toe_slider.setSingleStep(0.01)

        selected_rear_toe_value_label = create_label(str(rear_toe_slider.getValue()))
        rear_toe_slider.valueChanged.connect(
            lambda: selected_rear_toe_value_label.setText(
                str(rear_toe_slider.getValue())
            )
        )
        rear_toe_widgets = [
            rear_toe_label,
            rear_toe_slider,
            selected_rear_toe_value_label,
        ]

        for widget in front_toe_widgets:
            front_toe_layout.addWidget(widget)
        for widget in rear_toe_widgets:
            rear_toe_layout.addWidget(widget)

        return suspension_geo_page
