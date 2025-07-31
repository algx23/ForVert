from PyQt6.QtWidgets import (
    QApplication,
    QTabWidget,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFrame,
    QStackedWidget,
)
from pyqt_advanced_slider import Slider
from f1sc.util import create_label


def build_menu_page(menu_page_layout: QVBoxLayout):
    setup_button = QPushButton()
    setup_button.setObjectName("setup menu option button")
    setup_button.setText("Setup Converter")

    # Overlay layout : TODO => overlay coming in a future commit
    overlay_button = QPushButton()
    overlay_button.setObjectName("overlay button")
    overlay_button.setText("Overlay")

    menu_page_layout.addWidget(setup_button)
    menu_page_layout.addWidget(overlay_button)

    return


def create_aero_tab():
    # aerodynamics

    aero_page = QWidget()
    aero_page_layout = QVBoxLayout()
    aero_page.setLayout(aero_page_layout)

    # in the front wing and rear wing sections the widgets appear next to each other
    front_wing_section_layout = QHBoxLayout()
    rear_wing_section_layout = QHBoxLayout()

    front_wing_label = create_label("Front Wing Aero", "data_category")
    # front_wing_label.setText("Front Wing Aero")
    # front_wing_label.setObjectName("data_category")
    front_wing_slider = Slider()
    front_wing_slider.setMinimum(1)
    front_wing_slider.setMaximum(11)

    # show the value of the slider next to it, and update it when a you drag across it
    selected_front_wing_value_label = create_label(str(front_wing_slider.getValue()))
    front_wing_slider.valueChanged.connect(
        lambda: selected_front_wing_value_label.setText(
            str(front_wing_slider.getValue())
        )
    )

    rear_wing_label = create_label("Rear Wing Aero", "data_category")
    rear_wing_slider = Slider()
    rear_wing_slider.setMinimum(1)
    rear_wing_slider.setMaximum(11)
    selected_rear_wing_value_label = create_label(str(rear_wing_slider.getValue()))
    rear_wing_slider.valueChanged.connect(
        lambda: selected_rear_wing_value_label.setText(str(rear_wing_slider.getValue()))
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
    diff_adjust_on_label = create_label(
        "Differential Adjustment On Throttle (%)", "data_category"
    )
    diff_adjust_on_slider = Slider()
    diff_adjust_on_slider.setMaximum(100)
    diff_adjust_on_slider.setMinimum(50)

    selected_diff_on_value = create_label(str(diff_adjust_on_slider.getValue()))
    diff_adjust_on_slider.valueChanged.connect(
        lambda: selected_diff_on_value.setText(str(diff_adjust_on_slider.getValue()))
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
    diff_adjust_off_slider = Slider()
    diff_adjust_off_slider.setMinimum(50)
    diff_adjust_off_slider.setMaximum(100)
    selected_diff_off_value = create_label(str(diff_adjust_off_slider.getValue()))
    diff_adjust_off_slider.valueChanged.connect(
        lambda: selected_diff_off_value.setText(str(diff_adjust_off_slider.getValue()))
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

    front_camber_label = create_label("Front Camber", "data_category")
    front_camber_slider = Slider()
    front_camber_slider.setFloat(True)
    front_camber_slider.setMinimum(-3.50)
    front_camber_slider.setMaximum(-2.50)
    front_camber_slider.setSingleStep(0.01)
    selected_front_camber_value = create_label(str(front_camber_slider.getValue()))
    front_camber_slider.valueChanged.connect(
        lambda: selected_front_camber_value.setText(str(front_camber_slider.getValue()))
    )

    front_camber_widgets = [
        front_camber_label,
        front_camber_slider,
        selected_front_camber_value,
    ]

    rear_camber_label = create_label("Rear Camber", "data_category")
    rear_camber_slider = Slider()
    rear_camber_slider.setFloat(True)
    rear_camber_slider.setMinimum(-3.50)
    rear_camber_slider.setMaximum(-2.50)
    rear_camber_slider.setSingleStep(0.01)
    selected_rear_camber_value = create_label(str(rear_camber_slider.getValue()))
    rear_camber_slider.valueChanged.connect(
        lambda: selected_rear_camber_value.setText(str(rear_camber_slider.getValue()))
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
    front_toe_slider = Slider()
    front_toe_slider.setFloat(True)
    front_toe_slider.setDecimals(2)  # two decimal places or the slider doesnt work
    front_toe_slider.setMinimum(0.05)
    front_toe_slider.setMaximum(0.15)
    front_toe_slider.setSingleStep(0.01)
    selected_front_toe_value_label = create_label(str(front_toe_slider.getValue()))
    front_toe_slider.valueChanged.connect(
        lambda: selected_front_toe_value_label.setText(str(front_toe_slider.getValue()))
    )
    front_toe_widgets = [
        front_toe_label,
        front_toe_slider,
        selected_front_toe_value_label,
    ]

    rear_toe_label = create_label("Rear Toe", "data_category")
    rear_toe_slider = Slider()
    rear_toe_slider.setFloat(True)
    rear_toe_slider.setDecimals(2)
    rear_toe_slider.setMinimum(0.2)
    rear_toe_slider.setMaximum(0.5)
    rear_toe_slider.setSingleStep(0.01)

    selected_rear_toe_value_label = create_label(str(rear_toe_slider.getValue()))
    rear_toe_slider.valueChanged.connect(
        lambda: selected_rear_toe_value_label.setText(str(rear_toe_slider.getValue()))
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
    front_suspension_label = create_label(
        "Front Suspension (soft - firm)", "data_category"
    )
    front_suspension_slider = Slider()
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
    rear_suspension_label.setObjectName("data_category")
    rear_suspension_slider = Slider()
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
    sliders.append(front_suspension_slider)
    sliders.append(rear_suspension_slider)

    for widget in rear_suspension_widgets:
        rear_suspension_layout.addWidget(widget)

    # front anti roll bar
    front_arb_label = create_label("Front Anti Roll Bar", "data_category")
    front_arb_slider = Slider()
    sliders.append(front_arb_slider)
    selected_front_arb_value_label = create_label(str(front_arb_slider.getValue()))
    front_arb_slider.valueChanged.connect(
        lambda: selected_front_arb_value_label.setText(str(front_arb_slider.getValue()))
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
    rear_arb_slider = Slider()
    sliders.append(rear_arb_slider)
    selected_rear_arb_value_label = create_label(str(rear_arb_slider.getValue()))
    rear_arb_slider.valueChanged.connect(
        lambda: selected_rear_arb_value_label.setText(str(rear_arb_slider.getValue()))
    )
    rear_arb_widgets = [rear_arb_label, rear_arb_slider, selected_rear_arb_value_label]
    for widget in rear_arb_widgets:
        rear_arb_layout.addWidget(widget)

    # front ride height
    front_rh_label = create_label("Front Ride Height", "data_category")
    front_rh_slider = Slider()
    sliders.append(front_rh_slider)
    selected_front_rh_value_label = create_label(str(front_rh_slider.getValue()))
    front_rh_slider.valueChanged.connect(
        lambda: selected_front_rh_value_label.setText(str(front_rh_slider.getValue()))
    )
    front_rh_widgets = [front_rh_label, front_rh_slider, selected_front_rh_value_label]

    for widget in front_rh_widgets:
        front_rh_layout.addWidget(widget)

    # rear ride height
    rear_rh_label = create_label("Rear Ride Height", "data_category")
    rear_rh_label.setObjectName("data_category")
    rear_rh_slider = Slider()
    sliders.append(rear_rh_slider)
    selected_rear_rh_value_label = create_label(str(rear_rh_slider.getValue()))
    rear_rh_slider.valueChanged.connect(
        lambda: selected_rear_rh_value_label.setText(str(rear_rh_slider.getValue()))
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

    brake_pressure_label = create_label("Brake Pressure %", "data_category")
    brake_pressure_slider = Slider()
    brake_pressure_slider.setMinimum(50)
    brake_pressure_slider.setMaximum(100)
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

    brake_bias_label = create_label("Brake Bias (Front ---  Rear) %", "data_category")
    brake_bias_slider = Slider()
    brake_bias_slider.setMinimum(50)
    brake_bias_slider.setMaximum(70)
    selected_brake_bias_value_label = create_label(str(brake_bias_slider.getValue()))
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
    front_tp_label = create_label("Front Tire Pressure", "data_category")

    front_tp_slider = Slider()
    # PyQT only supports integer increments, so x10 for the min and max values
    # in game the range is 21 -> 25, in the app the internal values are 210 -> 250
    # so to map, when displaying the selected tire pressures, divide the answer by 10
    # so an increment of 1 in the slider is "actually" an increment of 0.1, which
    # reflects the behavior in F1 2019.
    front_tp_slider.setMinimum(21)
    front_tp_slider.setMaximum(25)
    front_tp_slider.setFloat(True)
    front_tp_slider.setSingleStep(0.4)
    selected_front_tp_value_label = create_label(str(front_tp_slider.getValue()))
    front_tp_slider.valueChanged.connect(
        lambda: selected_front_tp_value_label.setText(str(front_tp_slider.getValue()))
    )
    front_tp_widgets = [front_tp_label, front_tp_slider, selected_front_tp_value_label]

    for widget in front_tp_widgets:
        front_tire_pressure_layout.addWidget(widget)

    # rear tires
    rear_tp_label = create_label("Rear Tire Pressure", "data_category")
    rear_tp_slider = Slider()
    rear_tp_slider.setFloat(0.4)
    rear_tp_slider.setMinimum(19.5)
    rear_tp_slider.setMaximum(23.5)
    rear_tp_slider.setSingleStep(0.4)
    selected_rear_tp_value_label = create_label(str(rear_tp_slider.getValue()))
    rear_tp_slider.valueChanged.connect(
        lambda: selected_rear_tp_value_label.setText(str(rear_tp_slider.getValue()))
    )

    rear_tp_widgets = [rear_tp_label, rear_tp_slider, selected_rear_tp_value_label]
    for widget in rear_tp_widgets:
        rear_tire_pressure_layout.addWidget(widget)

    return tires_page


def build_setup_input_window(
    setup_input_window_layout: QVBoxLayout, widget_stack: QStackedWidget
):
    """
    This function sets up the window by adding the labels and widgets to enter
    the dry setup details
    """

    # back to menu button
    back_to_menu_button = QPushButton()
    back_to_menu_button.setText("Back to Menu")
    setup_input_window_layout.addWidget(back_to_menu_button)
    back_to_menu_button.setObjectName("back to menu button")
    # the menu page is always the one at pos 0 as it is added first so just set by index
    back_to_menu_button.clicked.connect(lambda: widget_stack.setCurrentIndex(0))

    setup_tabs = QTabWidget()
    setup_input_window_layout.addWidget(setup_tabs)
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
    setup_input_window_layout.addWidget(convert_setup_button)

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

    return tabs_and_layouts


def get_data_from_tab_layouts(tabs_and_layouts):

    setup_values = {}
    for title in tabs_and_layouts.keys():  # loop through each major setup "section"
        setup_values[title] = (
            {}
        )  # empty dict for the values of the setup areas in a section
        layouts = tabs_and_layouts[title]  # the layouts in each tab
        for index in range(len(layouts)):
            child_layout = layouts[index]

            # Each layout holds a category name, e.g. "Front Wing Aero", as a label, and a value for that
            # category, in a slider. For each layout (so set up value that can be changed), iterate
            # through the widgets. If the widget is a QLabel and has the name "data_category", it is
            # the name of a category of the setup that can be changed, e.g. "Front Wing Aero".
            # If the widget is a Slider, it holds the value that you selected for that set up item.
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
                elif isinstance(widget_in_layout, Slider):
                    # print(f"slider value : {widget_in_layout.value()}")
                    value_of_category = widget_in_layout.getValue()
            if data_category != "" and value_of_category != 0:
                setup_values[title][data_category] = value_of_category

    # the values for suspension geometry needs to be divided by 100
    # map_slider_values(setup_values["Suspension Geometry"], factor=0.01)

    # tire pressure values need to be divided by 10
    # map_slider_values(setup_values["Tires"], factor=0.1)

    return setup_values


def update_aerodynamics(init_aero_vals):
    front_wing = init_aero_vals["Front Wing Aero"]
    rear_wing = init_aero_vals["Rear Wing Aero"]

    if front_wing + 2 < 11:
        front_wing += 2
    if rear_wing + 2 < 11:
        rear_wing += 2
    return (front_wing, rear_wing)


def update_transmission(init_transmission_vals):
    diff_on_throttle = init_transmission_vals["Differential Adjustment On Throttle (%)"]
    diff_off_throttle = init_transmission_vals[
        "Differential Adjustment Off throttle (%)"
    ]

    diff_on_throttle = 50
    if diff_off_throttle >= 70:
        diff_off_throttle = 65
    return (diff_on_throttle, diff_off_throttle)


def update_suspension_geometry(init_sg_vals):
    front_camber = init_sg_vals["Front Camber"]
    rear_camber = init_sg_vals["Rear Camber"]
    front_toe = init_sg_vals["Front Toe"]
    rear_toe = init_sg_vals["Rear Toe"]

    if rear_camber > -3.5:
        rear_camber -= 0.10
    return (front_camber, rear_camber, front_toe, rear_toe)


def update_suspension(init_suspension_val):
    front_suspension = init_suspension_val["Front Suspension (soft - firm)"]
    rear_suspension = init_suspension_val["Rear Suspension (soft - firm)"]
    front_arb = init_suspension_val["Front Anti Roll Bar"]
    rear_arb = init_suspension_val["Rear Anti Roll Bar"]
    front_rh = init_suspension_val["Front Ride Height"]
    rear_rh = init_suspension_val["Rear Ride Height"]

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
    brake_pressure = init_brake_vals["Brake Pressure %"]
    brake_bias = init_brake_vals["Brake Bias (Front ---  Rear) %"]

    brake_pressure = 89
    brake_bias = 52 if brake_bias >= 53 else brake_bias
    return (brake_pressure, brake_bias)


def update_tires(init_tire_pressures):
    front_tire_pressure = init_tire_pressures["Front Tire Pressure"]
    rear_tire_pressure = init_tire_pressures["Rear Tire Pressure"]

    front_tire_pressure -= 0.4
    rear_tire_pressure -= 0.8

    front_tire_pressure = (
        21 if front_tire_pressure < 21 else round(front_tire_pressure, 1)
    )
    rear_tire_pressure = (
        19.5 if rear_tire_pressure < 19.5 else round(rear_tire_pressure, 1)
    )
    return (front_tire_pressure, rear_tire_pressure)


def convert_setup(widget_containing_tw):
    """
    This function will take the values entered, and on a button press, convert the values,
    which should be for a dry setup, into generally suitable values for a wet track
    """
    layouts = get_layouts_of_tabs(widget_containing_tw=widget_containing_tw)
    setup_vals = get_data_from_tab_layouts(layouts)

    result_dict = dict()

    new_aero_values = update_aerodynamics(setup_vals["Aerodynamics"])
    new_transmission_values = update_transmission(setup_vals["Transmission"])
    new_suspension_geometry_values = update_suspension_geometry(
        setup_vals["Suspension Geometry"]
    )
    new_suspension_values = update_suspension(setup_vals["Suspension"])
    new_brake_values = update_brakes(setup_vals["Brakes"])
    new_tire_pressure_values = update_tires(setup_vals["Tires"])

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


def create_converted_setup_window():
    new_window_widget = QWidget()
    new_window_layout = QVBoxLayout()
    new_window_widget.setObjectName("converted setup window")
    new_window_widget.setLayout(new_window_layout)
    back_to_conversion_button = QPushButton("Back to Enter Setup")
    back_to_conversion_button.setObjectName("new_setup_back_to_enter_button")

    new_window_layout.addWidget(back_to_conversion_button)

    return new_window_widget


def build_converted_window_widget(new_setup):
    # print(new_setup)

    new_setup_window = create_converted_setup_window()
    new_setup_window.setWindowTitle("Converted Setup")
    new_setup_win_layout = new_setup_window.layout()

    # {setup_area : setup_item}
    # in setup_item => {setup_item_name : setup_item_value, ..}
    # eg: {"Aerodynamics" : {Front wing: 1, Rear wing: 2, ..}}
    for setup_area, setup_item in new_setup.items():
        area_frame = QFrame(new_setup_window)
        area_layout = QVBoxLayout()
        area_frame.setLayout(area_layout)

        setup_area_label = create_label(setup_area)
        area_layout.addWidget(setup_area_label)

        # The setup values under each section, eg front wing aero, rear wing aero
        item_frame_layout = QHBoxLayout()
        for setup_item_name, setup_item_value in setup_item.items():
            item_frame = QFrame(area_frame)
            item_frame.setLayout(item_frame_layout)

            item_name_text = str(setup_item_name) + ": "
            setup_item_name_label = create_label(item_name_text)

            setup_item_value_label = create_label(str(setup_item_value))

            item_frame_layout.addWidget(setup_item_name_label)
            item_frame_layout.addWidget(setup_item_value_label)

            area_layout.addWidget(item_frame)
        new_setup_win_layout.addWidget(area_frame)

    return new_setup_window


def build_overlay_page(overlay_widget: QWidget, overlay_layout: QVBoxLayout):
    return


def find_back_button(widget_stack: QStackedWidget):
    converted_setup_window_widget = None
    for widget in widget_stack.children():
        if widget.objectName() == "converted setup window":
            converted_setup_window_widget = widget

    widgets = converted_setup_window_widget.children()
    back_button = None
    for w in widgets:
        if (
            isinstance(w, QPushButton)
            and w.objectName() == "new_setup_back_to_enter_button"
        ):
            back_button = w
    return back_button


def show_new_setup_window(display_w_existing_setup, widget_stack: QStackedWidget):
    new_setup = convert_setup(display_w_existing_setup)
    new_setup_window = build_converted_window_widget(new_setup)
    widget_stack.addWidget(new_setup_window)
    widget_stack.setCurrentWidget(new_setup_window)
    back_button = find_back_button(widget_stack=widget_stack)
    back_button.clicked.connect(
        lambda: widget_stack.setCurrentWidget(display_w_existing_setup)
    )

    return


def main():

    app = QApplication([])
    # main window
    root = QMainWindow()
    setup_input_window_layout = QVBoxLayout()
    stacked_widget = QStackedWidget()

    # menu page
    menu_page = QWidget()
    menu_page_layout = QVBoxLayout()
    menu_page.setLayout(menu_page_layout)
    build_menu_page(menu_page_layout)
    stacked_widget.addWidget(menu_page)

    # setup page for if you click the setup converter option
    setup_page_widget = QWidget()
    setup_page_widget.setLayout(setup_input_window_layout)
    build_setup_input_window(setup_input_window_layout, stacked_widget)
    stacked_widget.addWidget(setup_page_widget)

    stacked_widget.setCurrentWidget(menu_page)

    overlay_page_widget, overlay_page_layout = QWidget(), QVBoxLayout()
    overlay_page_widget.setLayout(overlay_page_layout)
    build_overlay_page(overlay_page_widget, overlay_page_layout)

    # handling the menu page clicks
    setup_menu_option_button = menu_page.findChild(
        QPushButton, name="setup menu option button"
    )
    setup_menu_option_button.clicked.connect(
        lambda: stacked_widget.setCurrentWidget(setup_page_widget)
    )

    convert_button = setup_page_widget.findChild(QPushButton, name="convert button")

    # if the button is pressed convert the setup and display it
    convert_button.clicked.connect(
        lambda: show_new_setup_window(
            display_w_existing_setup=setup_page_widget, widget_stack=stacked_widget
        )
    )

    root.setCentralWidget(stacked_widget)
    root.show()

    app.exec()


if __name__ == "__main__":
    main()
