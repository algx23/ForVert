from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from f1sc.util import create_slider, create_label


class SuspensionTab(QWidget):
    def __init__(self):
        super().__init__(None)

    def init_tab(self):

        # general layouts
        suspension_page = QWidget()
        suspension_page_layout = QVBoxLayout()
        suspension_page.setLayout(suspension_page_layout)

        # all the sliders share the same min and max so just define them here
        SLIDER_MIN = 1
        SLIDER_MAX = 11
        sliders = []
        # suspension layout
        front_suspension_layout = QHBoxLayout()
        rear_suspension_layout = QHBoxLayout()

        # arb layout
        front_arb_layout = QHBoxLayout()
        rear_arb_layout = QHBoxLayout()

        # rh layout
        front_rh_layout = QHBoxLayout()
        rear_rh_layout = QHBoxLayout()
        layouts = [
            front_suspension_layout,
            rear_suspension_layout,
            front_arb_layout,
            rear_arb_layout,
            front_rh_layout,
            rear_rh_layout,
        ]

        for layout in layouts:
            suspension_page_layout.addLayout(layout)

        # Suspension
        front_suspension_label = create_label(
            "Front Suspension (soft - firm)", "data_category"
        )
        front_suspension_slider = create_slider(SLIDER_MIN, SLIDER_MAX, False)
        selected_front_suspension_value_label = create_label(
            str(front_suspension_slider.getValue())
        )
        front_suspension_slider.valueChanged.connect(
            lambda: selected_front_suspension_value_label.setText(
                str(front_suspension_slider.getValue())
            )
        )
        front_suspension_widgets = [
            front_suspension_label,
            front_suspension_slider,
            selected_front_suspension_value_label,
        ]
        for widget in front_suspension_widgets:
            front_suspension_layout.addWidget(widget)

        # rear suspension

        rear_suspension_label = create_label(
            "Rear Suspension (soft - firm)", "data_category"
        )
        rear_suspension_slider = create_slider(SLIDER_MIN, SLIDER_MAX, False)
        selected_rear_suspension_value_label = create_label(
            str(rear_suspension_slider.getValue())
        )
        rear_suspension_slider.valueChanged.connect(
            lambda: selected_rear_suspension_value_label.setText(
                str(rear_suspension_slider.getValue())
            )
        )

        rear_suspension_widgets = [
            rear_suspension_label,
            rear_suspension_slider,
            selected_rear_suspension_value_label,
        ]

        for widget in rear_suspension_widgets:
            rear_suspension_layout.addWidget(widget)

        # front anti roll bar
        front_arb_label = create_label("Front Anti Roll Bar", "data_category")
        front_arb_slider = create_slider(SLIDER_MIN, SLIDER_MAX, False)
        selected_front_arb_value_label = create_label(str(front_arb_slider.getValue()))
        front_arb_slider.valueChanged.connect(
            lambda: selected_front_arb_value_label.setText(
                str(front_arb_slider.getValue())
            )
        )
        front_arb_widgets = [
            front_arb_label,
            front_arb_slider,
            selected_front_arb_value_label,
        ]
        for widget in front_arb_widgets:
            front_arb_layout.addWidget(widget)

        # rear anti roll bar
        rear_arb_label = create_label("Rear Anti Roll Bar")
        rear_arb_label.setObjectName("data_category")
        rear_arb_slider = create_slider(SLIDER_MIN, SLIDER_MAX, False)
        selected_rear_arb_value_label = create_label(str(rear_arb_slider.getValue()))
        rear_arb_slider.valueChanged.connect(
            lambda: selected_rear_arb_value_label.setText(
                str(rear_arb_slider.getValue())
            )
        )
        rear_arb_widgets = [
            rear_arb_label,
            rear_arb_slider,
            selected_rear_arb_value_label,
        ]
        for widget in rear_arb_widgets:
            rear_arb_layout.addWidget(widget)

        # front ride height
        front_rh_label = create_label("Front Ride Height", "data_category")
        front_rh_slider = create_slider(SLIDER_MIN, SLIDER_MAX, False)
        selected_front_rh_value_label = create_label(str(front_rh_slider.getValue()))
        front_rh_slider.valueChanged.connect(
            lambda: selected_front_rh_value_label.setText(
                str(front_rh_slider.getValue())
            )
        )
        front_rh_widgets = [
            front_rh_label,
            front_rh_slider,
            selected_front_rh_value_label,
        ]

        for widget in front_rh_widgets:
            front_rh_layout.addWidget(widget)

        # rear ride height
        rear_rh_label = create_label("Rear Ride Height", "data_category")
        rear_rh_slider = create_slider(SLIDER_MIN, SLIDER_MAX, False)
        selected_rear_rh_value_label = create_label(str(rear_rh_slider.getValue()))
        rear_rh_slider.valueChanged.connect(
            lambda: selected_rear_rh_value_label.setText(str(rear_rh_slider.getValue()))
        )
        rear_rh_widgets = [rear_rh_label, rear_rh_slider, selected_rear_rh_value_label]
        for widget in rear_rh_widgets:
            rear_rh_layout.addWidget(widget)

        return suspension_page
