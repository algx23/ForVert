from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from f1sc.util import create_label, create_slider


class AeroTab(QWidget):
    def __init__(self):
        super().__init__(None)

    def init_tab(self):

        # aerodynamics

        aero_page = QWidget()
        aero_page_layout = QVBoxLayout()
        aero_page.setLayout(aero_page_layout)

        # in the front wing and rear wing sections the widgets appear next to each other
        front_wing_section_layout = QHBoxLayout()
        rear_wing_section_layout = QHBoxLayout()

        front_wing_label = create_label("Front Wing Aero", "data_category")
        front_wing_slider = create_slider(min=1, max=11, is_float=False)

        # show the value of the slider next to it, and update it when a you drag across it
        selected_front_wing_value_label = create_label(
            str(front_wing_slider.getValue())
        )
        front_wing_slider.valueChanged.connect(
            lambda: selected_front_wing_value_label.setText(
                str(front_wing_slider.getValue())
            )
        )

        rear_wing_label = create_label("Rear Wing Aero", "data_category")
        rear_wing_slider = create_slider(1, 11, False)
        selected_rear_wing_value_label = create_label(str(rear_wing_slider.getValue()))
        rear_wing_slider.valueChanged.connect(
            lambda: selected_rear_wing_value_label.setText(
                str(rear_wing_slider.getValue())
            )
        )

        front_aero_widgets = [
            front_wing_label,
            front_wing_slider,
            selected_front_wing_value_label,
        ]
        rear_aero_widgets = [
            rear_wing_label,
            rear_wing_slider,
            selected_rear_wing_value_label,
        ]

        # in each section: section title, slider, slider value
        for widget in front_aero_widgets:
            front_wing_section_layout.addWidget(widget)
        for widget in rear_aero_widgets:
            rear_wing_section_layout.addWidget(widget)

        aero_page_layout.addLayout(front_wing_section_layout)
        aero_page_layout.addLayout(rear_wing_section_layout)

        return aero_page
