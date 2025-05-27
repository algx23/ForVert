from PyQt6.QtWidgets import (
    QApplication,
    QTabWidget,
    QMainWindow,
    QLabel,
    QSlider,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
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
    front_wing_label.setObjectName("data_category")
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
    rear_wing_label.setObjectName("data_category")
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
    diff_adjust_on_label.setObjectName("data_category")
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
    diff_adjust_off_label.setObjectName("data_category")
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
    front_camber_label.setObjectName("data_category")
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
    rear_camber_label.setObjectName("data_category")
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
    front_toe_label.setObjectName("data_category")
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
    rear_toe_label.setObjectName("data_category")
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
    front_suspension_label.setObjectName("data_category")
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
    rear_suspension_label.setObjectName("data_category")
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
    front_arb_label.setObjectName("data_category")
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
    rear_arb_label.setObjectName("data_category")
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
    front_rh_label.setObjectName("data_category")
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
    rear_rh_label.setObjectName("data_category")
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
    brake_pressure_label.setObjectName("data_category")
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
    brake_bias_label.setObjectName("data_category")
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


def create_tires_tab():
    tires_page = QWidget()
    # layouts
    tires_page_layout = QVBoxLayout()
    tires_page.setLayout(tires_page_layout)

    front_tire_pressure_layout = QHBoxLayout()
    rear_tire_pressure_layout = QHBoxLayout()

    tires_page_layout.addLayout(front_tire_pressure_layout)
    tires_page_layout.addLayout(rear_tire_pressure_layout)

    # front tire pressure section
    front_tp_label = QLabel("Front Tire Pressure")
    front_tp_label.setObjectName("data_category")

    front_tp_slider = QSlider(Qt.Orientation.Horizontal)
    # PyQT only supports integer increments, so x10 for the min and max values
    # in game the range is 21 -> 25, in the app the internal values are 210 -> 250
    # so to map, when displaying the selected tire pressures, divide the answer by 10
    # so an increment of 1 in the slider is "actually" an increment of 0.1, which
    # reflects the behavior in F1 2019.
    front_tp_slider.setMinimum(210)
    front_tp_slider.setMaximum(250)
    selected_front_tp_value_label = QLabel(str(front_tp_slider.value() / 10))
    front_tp_slider.valueChanged.connect(
        lambda: selected_front_tp_value_label.setText(str(front_tp_slider.value() / 10))
    )
    front_tp_widgets = [front_tp_label, front_tp_slider, selected_front_tp_value_label]

    for widget in front_tp_widgets:
        front_tire_pressure_layout.addWidget(widget)

    # rear tires
    rear_tp_label = QLabel("Rear Tire Pressure")
    rear_tp_label.setObjectName("data_category")
    rear_tp_slider = QSlider(Qt.Orientation.Horizontal)
    rear_tp_slider.setMinimum(195)
    rear_tp_slider.setMaximum(235)
    selected_rear_tp_value_label = QLabel(str(rear_tp_slider.value() / 10))
    rear_tp_slider.valueChanged.connect(
        lambda: selected_rear_tp_value_label.setText(str(rear_tp_slider.value() / 10))
    )

    rear_tp_widgets = [rear_tp_label, rear_tp_slider, selected_rear_tp_value_label]
    for widget in rear_tp_widgets:
        rear_tire_pressure_layout.addWidget(widget)

    return tires_page


def set_up_window(root_layout):
    """
    This function sets up the window by adding the labels and widgets to enter
    the dry setup details
    """

    setup_tabs = QTabWidget()
    root_layout.addWidget(setup_tabs)
    aero_tab = create_aero_tab()
    suspension_tab = create_suspension_tab()
    transmission_tab = create_transmission_tab()
    suspension_geometry_tab = create_suspension_geo_tab()
    brakes_tab = create_brakes_tab()
    tires_tab = create_tires_tab()

    setup_tabs.addTab(aero_tab, "Aerodynamics")
    setup_tabs.addTab(transmission_tab, "Transmission")
    setup_tabs.addTab(suspension_geometry_tab, "Suspension Geometry")
    setup_tabs.addTab(suspension_tab, "Suspension")
    setup_tabs.addTab(brakes_tab, "Brakes")
    setup_tabs.addTab(tires_tab, "Tires")

    convert_setup_button = QPushButton(text="Convert Setup")
    convert_setup_button.setObjectName("convert button")
    parent_containing_tabs = root_layout.parent()
    root_layout.addWidget(convert_setup_button)

    convert_setup_button.clicked.connect(
        lambda: get_layouts_of_tabs(parent_containing_tabs)
    )

    return


def get_layouts_of_tabs(widget_containing_tw):
    """This function takes in the layout of the window, and creates a dictionary tracking the name
    of each tab, and the layouts within it. This result of this function is going to be used in a
    get_data_from_tabs() function which will extract the data from the layouts, to use in conversion

    Args:
        widget_containing_tw (QWidget): this is the widget of the root window, contianing a vbox layout,
                                            which contains the TabWidget, and the convert setup button

    Returns:
        dict: Returns a dictionairy containing the title of the tab, and the layouts within that tab. Each
              layout will hold the labels and sliders of that "section".
    """
    tabs_and_layouts = {}
    widgets_in_parent = (
        widget_containing_tw.children()
    )  # this is the QWidget of the parent window -> so the tabbar, the vbox layout of the tabs, and the button

    for i in range(len(widgets_in_parent)):
        if isinstance(
            widgets_in_parent[i], QTabWidget
        ):  # find the tab widget in the list of widgets
            tab_widget = widgets_in_parent[i]

    tabs = []
    for index in range(
        tab_widget.count()
    ):  # in each tab there is a QWidget which holds all the layouts which hold the sliders labels etc
        tabs.append(
            tab_widget.widget(index)
        )  # add the widget of the tab to the list of tabs

    for index in range(len(tabs)):
        all_widgets_in_tab = []
        tab = tabs[index]
        tab_title = tab_widget.tabText(index)
        for j in range(tab.layout().count()):
            item_inside_tab = tab.layout().itemAt(j)  # things inside the layout
            if item_inside_tab.layout():
                all_widgets_in_tab.append(item_inside_tab.layout())
        tabs_and_layouts[tab_title] = all_widgets_in_tab

    get_data_from_tab_layouts(tabs_and_layouts)
    return


def get_data_from_tab_layouts(tabs_and_layouts):

    setup_values = {}
    for title in tabs_and_layouts.keys():  # loop through each major setup "section"
        setup_values[title] = (
            {}
        )  # empty dict for the values of the setup areas in a section
        layouts = tabs_and_layouts[title]  # the layouts in each tab
        # print(layouts)
        for index in range(len(layouts)):
            child_layout = layouts[index]

            # Each layout holds a category name, e.g. "Front Wing Aero", as a label, and a value for that
            # category, in a slider. For each layout (so set up value that can be changed), iterate
            # through the widgets. If the widget is a QLabel and has the name "data_category", it is
            # the name of a category of the setup that can be changed, e.g. "Front Wing Aero".
            # If the widget is a QSlider, it holds the value that you selected for that set up item.
            # If the data category, and value are found (i.e not "" and not 0 respectively) then you can
            # add the category name, and the value associated with that,
            # to the dict, for the overall SETUP category -> E.g. "Aerodynamics", "Transmission" etc.
            # This means we can hold the category name, and value, for each overall setup area, e.g.
            # "Aerodynamics": front wing aero: 1, rear wing aero: 2
            data_category = ""
            value_of_category = 0
            for other_index in range(child_layout.count()):
                widget_in_layout = child_layout.itemAt(other_index).widget()
                if (
                    isinstance(widget_in_layout, QLabel)
                    and widget_in_layout.objectName() == "data_category"
                ):
                    # print(widget_in_layout.text())
                    data_category = widget_in_layout.text()
                elif isinstance(widget_in_layout, QSlider):
                    # print(f"slider value : {widget_in_layout.value()}")
                    value_of_category = widget_in_layout.value()
            if data_category != "" and value_of_category != 0:
                setup_values[title][data_category] = value_of_category

    suspension_geo_to_map = list(setup_values["Suspension Geometry"].values())
    mapped_sus_values = map_slider_values(
        suspension_geo_to_map, factor=0.01
    )  # the values for suspension geometry needs to be divided by 100

    tp_to_map = list(setup_values["Tires"].values())
    # tire pressure values need to be divided by 10
    mapped_tp_values = map_slider_values(tp_to_map, factor=0.1)

    print(f"mapped suspension values: {mapped_sus_values}")
    print(f"mapped tire pressure values: {mapped_tp_values}")

    return setup_values


def map_slider_values(setup_values: list[int], factor: int):
    for i in range(len(setup_values)):
        setup_values[i] *= factor

    return setup_values


# TODO: Implement conversion logic with the new UI when ready
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
    root_widget = QWidget()
    root_layout = QVBoxLayout()
    root_widget.setLayout(root_layout)
    set_up_window(root_layout)
    root.setCentralWidget(root_widget)
    root.show()
    app.exec()


if __name__ == "__main__":
    main()
