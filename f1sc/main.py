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


from f1sc.tabs.AeroTab import AeroTab
from f1sc.tabs.TransmissionTab import TransmissionTab
from f1sc.tabs.SuspensionTab import SuspensionTab
from f1sc.tabs.SuspensionGeoTab import SuspensionGeometryTab
from f1sc.tabs.BrakesTab import BrakesTab
from f1sc.tabs.TiresTab import TiresTab

from f1sc.SetupUpdater import F1SetupUpdater


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

    aero_tab_instance = AeroTab()
    aero_tab = aero_tab_instance.init_tab()

    transmission_tab_instance = TransmissionTab()
    transmission_tab = transmission_tab_instance.init_tab()

    suspension_geometry_tab_instance = SuspensionGeometryTab()
    suspension_geometry_tab = suspension_geometry_tab_instance.init_tab()

    suspension_tab_instance = SuspensionTab()
    suspension_tab = suspension_tab_instance.init_tab()

    brakes_tab_instance = BrakesTab()
    brakes_tab = brakes_tab_instance.init_tab()

    tires_tab_instance = TiresTab()
    tires_tab = tires_tab_instance.init_tab()

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
                    data_category = widget_in_layout.text()
                elif isinstance(widget_in_layout, Slider):
                    value_of_category = widget_in_layout.getValue()
            if data_category != "" and value_of_category != 0:
                setup_values[title][data_category] = value_of_category

    return setup_values


# TODO: FIX THIS FUNCTION
def convert_setup(widget_containing_tw):
    """
    This function will take the values entered, and on a button press, convert the values,
    which should be for a dry setup, into generally suitable values for a wet track
    """
    layouts = get_layouts_of_tabs(widget_containing_tw=widget_containing_tw)
    setup_vals = get_data_from_tab_layouts(layouts)
    setup_updater = F1SetupUpdater(setup_vals)

    result_dict = dict()

    new_setup_values = setup_updater.convert_dry_setup_to_wet()
    exit(0)
    # TODO Fix result dictionary building logic contained in =====
    # ================================================================================
    new_aero_values = setup_updater.update_aerodynamics(setup_vals["Aerodynamics"])
    new_transmission_values = setup_updater.update_transmission(
        setup_vals["Transmission"]
    )
    new_suspension_geometry_values = setup_updater.update_suspension_geometry(
        setup_vals["Suspension Geometry"]
    )
    new_suspension_values = setup_updater.update_suspension(setup_vals["Suspension"])
    new_brake_values = setup_updater.update_brakes(setup_vals["Brakes"])
    new_tire_pressure_values = setup_updater.update_tires(setup_vals["Tires"])

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
    # ================================================================
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


# TODO: Implement Overlay Page
def build_overlay_page(overlay_widget: QWidget, overlay_layout: QVBoxLayout):
    NotImplemented


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
