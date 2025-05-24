from PyQt6.QtWidgets import (
    QApplication,
    QTabWidget,
    QMainWindow,
    QLabel,
    QSlider,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt


def create_aero_tab():
    # aerodynamics

    aero_page = QWidget()
    aero_page_layout = QVBoxLayout()
    aero_page.setLayout(aero_page_layout)

    # in the front wing and rear wing sections the widgets appear next to each other
    front_wing_section_layout = QHBoxLayout()
    rear_wing_section_layout = QHBoxLayout()

    front_wing_label = QLabel()
    front_wing_label.setText("Front Wing Aero")
    front_wing_slider = QSlider(Qt.Orientation.Horizontal)
    front_wing_slider.setMinimum(1)
    front_wing_slider.setMaximum(11)

    # show the value of the slider next to it, and update it when a you drag across it
    selected_front_wing_value_label = QLabel(str(front_wing_slider.value()))
    front_wing_slider.valueChanged.connect(
        lambda: selected_front_wing_value_label.setText(str(front_wing_slider.value()))
    )

    rear_wing_label = QLabel()
    rear_wing_label.setText("Rear Wing Aero")
    rear_wing_slider = QSlider(Qt.Orientation.Horizontal)
    rear_wing_slider.setMinimum(1)
    rear_wing_slider.setMaximum(11)
    selected_rear_wing_value_label = QLabel(str(rear_wing_slider.value()))
    rear_wing_slider.valueChanged.connect(
        lambda: selected_rear_wing_value_label.setText(str(rear_wing_slider.value()))
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


def create_transmission_tab():
    transmission_page = QWidget()
    transmission_page_layout = QVBoxLayout()
    transmission_page.setLayout(transmission_page_layout)

    # on throttle
    on_throttle_layout = QHBoxLayout()
    diff_adjust_on_label = QLabel("Differential Adjustment On Throttle (%)")
    diff_adjust_on_slider = QSlider(Qt.Orientation.Horizontal)
    diff_adjust_on_slider.setMaximum(100)
    diff_adjust_on_slider.setMinimum(50)

    selected_diff_on_value = QLabel(str(diff_adjust_on_slider.value()))
    diff_adjust_on_slider.valueChanged.connect(
        lambda: selected_diff_on_value.setText(str(diff_adjust_on_slider.value()))
    )

    on_throttle_widgets = [
        diff_adjust_on_label,
        diff_adjust_on_slider,
        selected_diff_on_value,
    ]

    # off throttle
    off_throttle_layout = QHBoxLayout()
    diff_adjust_off_label = QLabel("Differential Adjustment Off throttle (%)")
    diff_adjust_off_slider = QSlider(Qt.Orientation.Horizontal)
    diff_adjust_off_slider.setMinimum(50)
    diff_adjust_off_slider.setMaximum(100)
    selected_diff_off_value = QLabel(str(diff_adjust_off_slider.value()))
    diff_adjust_off_slider.valueChanged.connect(
        lambda: selected_diff_off_value.setText(str(diff_adjust_off_slider.value()))
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


def create_suspension_geo_tab():
    suspension_geo_page = QWidget()
    suspension_geo_page_layout = QVBoxLayout()
    suspension_geo_page.setLayout(suspension_geo_page_layout)

    # layouts

    front_camber_layout = QHBoxLayout()
    rear_camber_layout = QHBoxLayout()
    front_toe_layout = QHBoxLayout()
    rear_toe_layout = QHBoxLayout()
    layouts = []
    layouts.append(front_camber_layout)
    layouts.append(rear_camber_layout)
    layouts.append(front_toe_layout)
    layouts.append(rear_toe_layout)

    for layout in layouts:
        suspension_geo_page_layout.addLayout(layout)

    # inputs:

    # camber

    front_camber_label = QLabel("Front Camber")
    front_camber_slider = QSlider(Qt.Orientation.Horizontal)
    front_camber_slider.setMinimum(-350)
    front_camber_slider.setMaximum(-250)
    selected_front_camber_value = QLabel(str(front_camber_slider.value() / 100))
    front_camber_slider.valueChanged.connect(
        lambda: selected_front_camber_value.setText(
            str(front_camber_slider.value() / 100)
        )
    )

    front_camber_widgets = [
        front_camber_label,
        front_camber_slider,
        selected_front_camber_value,
    ]

    rear_camber_label = QLabel("Rear Camber")
    rear_camber_slider = QSlider(Qt.Orientation.Horizontal)
    rear_camber_slider.setMinimum(-350)
    rear_camber_slider.setMaximum(-250)
    selected_rear_camber_value = QLabel(str(rear_camber_slider.value() / 100))
    rear_camber_slider.valueChanged.connect(
        lambda: selected_rear_camber_value.setText(
            str(rear_camber_slider.value() / 100)
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
    front_toe_label = QLabel("Front Toe")
    front_toe_slider = QSlider(Qt.Orientation.Horizontal)
    # maps to 0.05 to 0.15 but pyqt only supports int and +1 increment
    front_toe_slider.setMinimum(5)
    front_toe_slider.setMaximum(15)
    selected_front_toe_value_label = QLabel(str(front_toe_slider.value() / 100))
    front_toe_slider.valueChanged.connect(
        lambda: selected_front_toe_value_label.setText(
            str(front_toe_slider.value() / 100)
        )
    )
    front_toe_widgets = [
        front_toe_label,
        front_toe_slider,
        selected_front_toe_value_label,
    ]

    rear_toe_label = QLabel("Rear Toe")
    rear_toe_slider = QSlider(Qt.Orientation.Horizontal)
    rear_toe_slider.setMinimum(20)
    rear_toe_slider.setMaximum(50)
    # maps to 0.2 to 0.5 but pyqt only supports ints and +1 increments
    selected_rear_toe_value_label = QLabel(str(rear_toe_slider.value() / 100))
    rear_toe_slider.valueChanged.connect(
        lambda: selected_rear_toe_value_label.setText(
            str(rear_toe_slider.value() / 100)
        )
    )
    rear_toe_widgets = [rear_toe_label, rear_toe_slider, selected_rear_toe_value_label]

    for widget in front_toe_widgets:
        front_toe_layout.addWidget(widget)
    for widget in rear_toe_widgets:
        rear_toe_layout.addWidget(widget)

    return suspension_geo_page


def create_suspension_tab():

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
    front_suspension_label = QLabel("Front Suspension (soft - firm)")
    front_suspension_slider = QSlider(Qt.Orientation.Horizontal)
    selected_front_suspension_value_label = QLabel(str(front_suspension_slider.value()))
    front_suspension_slider.valueChanged.connect(
        lambda: selected_front_suspension_value_label.setText(
            str(front_suspension_slider.value())
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

    rear_suspension_label = QLabel("Rear Suspension (soft - firm)")
    rear_suspension_slider = QSlider(Qt.Orientation.Horizontal)
    selected_rear_suspension_value_label = QLabel(str(rear_suspension_slider.value()))
    rear_suspension_slider.valueChanged.connect(
        lambda: selected_rear_suspension_value_label.setText(
            str(rear_suspension_slider.value())
        )
    )

    rear_suspension_widgets = [
        rear_suspension_label,
        rear_suspension_slider,
        selected_rear_suspension_value_label,
    ]
    sliders.append(front_suspension_slider)
    sliders.append(rear_suspension_slider)

    for widget in rear_suspension_widgets:
        rear_suspension_layout.addWidget(widget)

    # front anti roll bar
    front_arb_label = QLabel("Front Anti Roll Bar")
    front_arb_slider = QSlider(Qt.Orientation.Horizontal)
    sliders.append(front_arb_slider)
    selected_front_arb_value_label = QLabel(str(front_arb_slider.value()))
    front_arb_slider.valueChanged.connect(
        lambda: selected_front_arb_value_label.setText(str(front_arb_slider.value()))
    )
    front_arb_widgets = [
        front_arb_label,
        front_arb_slider,
        selected_front_arb_value_label,
    ]
    for widget in front_arb_widgets:
        front_arb_layout.addWidget(widget)

    # rear anti roll bar
    rear_arb_label = QLabel("Rear Anti Roll Bar")
    rear_arb_slider = QSlider(Qt.Orientation.Horizontal)
    sliders.append(rear_arb_slider)
    selected_rear_arb_value_label = QLabel(str(rear_arb_slider.value()))
    rear_arb_slider.valueChanged.connect(
        lambda: selected_rear_arb_value_label.setText(str(rear_arb_slider.value()))
    )
    rear_arb_widgets = [rear_arb_label, rear_arb_slider, selected_rear_arb_value_label]
    for widget in rear_arb_widgets:
        rear_arb_layout.addWidget(widget)

    # front ride height
    front_rh_label = QLabel("Front Ride Height")
    front_rh_slider = QSlider(Qt.Orientation.Horizontal)
    sliders.append(front_rh_slider)
    selected_front_rh_value_label = QLabel(str(front_rh_slider.value()))
    front_rh_slider.valueChanged.connect(
        lambda: selected_front_rh_value_label.setText(str(front_rh_slider.value()))
    )
    front_rh_widgets = [front_rh_label, front_rh_slider, selected_front_rh_value_label]

    for widget in front_rh_widgets:
        front_rh_layout.addWidget(widget)

    # rear ride height
    rear_rh_label = QLabel("Rear Ride Height")
    rear_rh_slider = QSlider(Qt.Orientation.Horizontal)
    sliders.append(rear_rh_slider)
    selected_rear_rh_value_label = QLabel(str(rear_rh_slider.value()))
    rear_rh_slider.valueChanged.connect(
        lambda: selected_rear_rh_value_label.setText(str(rear_rh_slider.value()))
    )
    rear_rh_widgets = [rear_rh_label, rear_rh_slider, selected_rear_rh_value_label]
    for widget in rear_rh_widgets:
        rear_rh_layout.addWidget(widget)

    for slider in sliders:
        slider.setMinimum(SLIDER_MIN)
        slider.setMaximum(SLIDER_MAX)

    return suspension_page


def create_brakes_tab():
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

    brake_pressure_label = QLabel("Brake Pressure %")
    brake_pressure_slider = QSlider(Qt.Orientation.Horizontal)
    brake_pressure_slider.setMinimum(50)
    brake_pressure_slider.setMaximum(100)
    selected_brake_pressure_value_label = QLabel(str(brake_pressure_slider.value()))
    brake_pressure_slider.valueChanged.connect(
        lambda: selected_brake_pressure_value_label.setText(
            str(brake_pressure_slider.value())
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

    brake_bias_label = QLabel("Brake Bias (Front ---  Rear) %")
    brake_bias_slider = QSlider(Qt.Orientation.Horizontal)
    brake_bias_slider.setMinimum(50)
    brake_bias_slider.setMaximum(70)
    brake_bias_slider.setInvertedAppearance(True)
    selected_brake_bias_value_label = QLabel(str(brake_bias_slider.value()))
    brake_bias_slider.valueChanged.connect(
        lambda: selected_brake_bias_value_label.setText(str(brake_bias_slider.value()))
    )

    brake_bias_widgets = [
        brake_bias_label,
        brake_bias_slider,
        selected_brake_bias_value_label,
    ]

    for widget in brake_bias_widgets:
        brake_bias_layout.addWidget(widget)

    return brakes_page


def set_up_window(root):
    """
    This function sets up the window by adding the labels and widgets to enter
    the dry setup details
    """

    setup_tabs = QTabWidget()
    root.setCentralWidget(setup_tabs)
    aero_tab = create_aero_tab()
    suspension_tab = create_suspension_tab()
    transmission_tab = create_transmission_tab()
    suspension_geometry_tab = create_suspension_geo_tab()
    brakes_tab = create_brakes_tab()
    setup_tabs.addTab(aero_tab, "Aerodynamics")
    setup_tabs.addTab(transmission_tab, "Transmission")
    setup_tabs.addTab(suspension_geometry_tab, "Suspension Geometry")
    setup_tabs.addTab(suspension_tab, "Suspension")
    setup_tabs.addTab(brakes_tab, "Brakes")

    # TODO: convert these tabs to PyQt From TKinter
    # tabs for the different areas of setup
    # tires_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)

    # # Tires
    # front_tp_label = Label(master=tires_tab, text="Front Tire Pressure")
    # front_tp_input = tk.Scale(
    #     master=tires_tab, from_=21, to=25, resolution=0.1, orient="horizontal"
    # )
    # front_tp_label.pack()
    # front_tp_input.pack()

    # rear_tp_label = Label(master=tires_tab, text="Rear Tire Pressure")
    # rear_tp_input = tk.Scale(
    #     master=tires_tab, from_=19.5, to=23.5, resolution=0.1, orient="horizontal"
    # )
    # rear_tp_label.pack()
    # rear_tp_input.pack()

    # b = tk.Button(
    #     master=root,
    #     command=lambda: convert_and_display_setup(notebook, root),
    #     text="Convert Setup",
    # )
    # b.pack()

    return root


# TODO: Convert conversion logic to PyQT from Tkinter
def getEntryWidgetsFromTabs(notebook):
    tabs = notebook.winfo_children()
    entries_by_setup_area = dict()

    # {aeordynamics/transmission/... : [scale_widgets]}
    for i in range(len(tabs)):
        tab_title = notebook.tab(i, "text")
        widgets_in_tab = tabs[i].winfo_children()
        entries_by_setup_area[tab_title] = []

        for widget in widgets_in_tab:
            if isinstance(widget, tk.Scale):
                entries_by_setup_area[tab_title].append(widget.get())

    return entries_by_setup_area


def update_aerodynamics(init_aero_vals):
    front_wing = init_aero_vals[0]
    rear_wing = init_aero_vals[1]

    if front_wing + 2 < 11:
        front_wing += 2
    if rear_wing + 2 < 11:
        rear_wing += 2
    return (front_wing, rear_wing)


def update_transmission(init_transmission_vals):
    diff_on_throttle = init_transmission_vals[0]
    diff_off_throttle = init_transmission_vals[1]

    diff_on_throttle = 50
    if diff_off_throttle >= 70:
        diff_off_throttle = 65
    return (diff_on_throttle, diff_off_throttle)


def update_suspension_geometry(init_sg_vals):
    front_camber = init_sg_vals[0]
    rear_camber = init_sg_vals[1]
    front_toe = init_sg_vals[2]
    rear_toe = init_sg_vals[3]

    if rear_camber > -3.5:
        rear_camber -= 0.1
    return (front_camber, rear_camber, front_toe, rear_toe)


def update_suspension(init_suspension_val):
    front_suspension = init_suspension_val[0]
    rear_suspension = init_suspension_val[1]
    front_arb = init_suspension_val[2]
    rear_arb = init_suspension_val[3]
    front_rh = init_suspension_val[4]
    rear_rh = init_suspension_val[5]

    if front_suspension > 5:
        front_suspension -= 2
    else:
        front_suspension -= 1

    if rear_suspension > 5:
        rear_suspension -= 2
    else:
        rear_suspension -= 1

    if rear_arb > 8:
        rear_arb -= 1

    front_rh += 5
    rear_rh += 5

    # check the vals are within the ranges in the game
    front_suspension = 1 if front_suspension < 1 else front_suspension
    rear_suspension = 1 if rear_suspension < 1 else rear_suspension
    front_arb = 1 if front_arb < 1 else front_arb
    rear_arb = 1 if rear_arb < 1 else rear_arb
    front_rh = 11 if front_rh > 11 else front_rh
    rear_rh = 11 if rear_rh > 11 else rear_rh

    return (front_suspension, rear_suspension, front_arb, rear_arb, front_rh, rear_rh)


def update_brakes(init_brake_vals):
    brake_pressure = init_brake_vals[0]
    brake_bias = init_brake_vals[1]

    brake_pressure = 89
    brake_bias = 52 if brake_bias >= 53 else brake_bias
    return (brake_pressure, brake_bias)


def update_tires(init_tire_pressures):
    front_tire_pressure = init_tire_pressures[0]
    rear_tire_pressure = init_tire_pressures[1]

    front_tire_pressure -= 0.1
    rear_tire_pressure -= 0.1

    front_tire_pressure = 21 if front_tire_pressure < 21 else front_tire_pressure
    rear_tire_pressure = 19.5 if rear_tire_pressure < 19.5 else rear_tire_pressure
    return (front_tire_pressure, rear_tire_pressure)


def convertSetup(notebook):
    """
    This function will take the values entered, and on a button press, convert the values,
    which should be for a dry setup, into generally suitable values for a wet track
    """
    widgets = getEntryWidgetsFromTabs(notebook)

    #################################
    # Update key index => tab title
    # 0 => Aero
    # 1 => Transmission
    # 2 => Suspension Geometry
    # 3 => Suspension
    # 4 => Brakes
    # 5 => Tires
    #################################

    result_dict = dict()

    new_aero_values = update_aerodynamics(widgets["Aerodynamics"])
    new_transmission_values = update_transmission(widgets["Transmission"])
    new_suspension_geometry_values = update_suspension_geometry(
        widgets["Suspension Geometry"]
    )
    new_suspension_values = update_suspension(widgets["Suspension"])
    new_brake_values = update_brakes(widgets["Brakes"])
    new_tire_pressure_values = update_tires(widgets["Tires"])

    # build the dict
    result_dict["Aerodynamics"] = {
        "front wing": new_aero_values[0],
        "rear_wing": new_aero_values[1],
    }
    result_dict["Transmission"] = {
        "Diff on throttle": new_transmission_values[0],
        "diff off throttle": new_transmission_values[1],
    }
    result_dict["Suspension Geometry"] = {
        "Front Camber": new_suspension_geometry_values[0],
        "Rear Camber": new_suspension_geometry_values[1],
        "Front Toe": new_suspension_geometry_values[2],
        "Rear Toe": new_suspension_geometry_values[3],
    }
    result_dict["Suspension"] = {
        "Front Suspension": new_suspension_values[0],
        "Rear Suspension": new_suspension_values[1],
        "Front Anti Roll Bar": new_suspension_values[2],
        "Rear Anti Roll Bar": new_suspension_values[3],
        "Front Ride Height": new_suspension_values[4],
        "Rear Ride Height": new_suspension_values[5],
    }
    result_dict["Brakes"] = {
        "Brake Pressure": new_brake_values[0],
        "Brake Bias": new_brake_values[1],
    }
    result_dict["Tires"] = {
        "Front Tire Pressure": new_tire_pressure_values[0],
        "Rear Tire Pressure": new_tire_pressure_values[1],
    }

    return result_dict


def convert_and_display_setup(page_w_existing_setup, window_to_display_on):
    new_setup = convertSetup(page_w_existing_setup)
    new_setup_window = tk.Toplevel(window_to_display_on)
    new_setup_window.title("Converted Setup")

    # {setup_area : setup_item}
    # in setup_item => {setup_item_name : setup_item_value, ..}
    # eg: {"Aerodynamics" : {Front wing: 1, Rear wing: 2, ..}}
    for setup_area, setup_item in new_setup.items():
        area_frame = Frame(master=new_setup_window, width=500, height=500)
        area_frame.pack(pady=20)
        setup_area_label = Label(master=area_frame, text=setup_area)
        setup_area_label.pack()
        for setup_item_name, setup_item_value in setup_item.items():
            item_frame = Frame(master=area_frame, width=1000, height=1000)
            item_frame.pack(side="left", padx=10, pady=10)
            setup_item_name_label = Label(
                master=item_frame, text=str(setup_item_name) + ": "
            )
            setup_item_value_label = Label(
                master=item_frame, text=str(setup_item_value)
            )
            setup_item_name_label.pack(side="left")
            setup_item_value_label.pack(side="left")

    label = Label(master=new_setup_window)
    label.pack()
    return


def main():

    app = QApplication([])
    root = QMainWindow()
    set_up_window(root)
    root.show()
    app.exec()
    # root.mainloop()


if __name__ == "__main__":
    main()
