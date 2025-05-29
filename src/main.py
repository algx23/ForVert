import tkinter as tk
from tkinter.ttk import Notebook
from tkinter.ttk import Frame
from tkinter.ttk import Label


def set_up_window():
    """
    This function sets up the window by adding the labels and widgets to enter
    the dry setup details
    """
    HEIGHT: int = 1000
    WIDTH: int = 1000
    TAB_HEIGHT: int = 500
    TAB_WIDTH: int = 500
    root = tk.Tk()
    root.minsize(width=WIDTH, height=HEIGHT)
    root.title("F1 Setup Hub")

    notebook = Notebook(master=root, height=TAB_HEIGHT, width=TAB_WIDTH)

    # tabs for the different areas of setup
    aero_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)
    transmission_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)
    suspension_geo_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)
    suspension_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)
    brakes_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)
    tires_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)

    # aerodynamics
    front_wing_label = Label(master=aero_tab, text="Front Wing Aero")
    front_wing_label.pack()
    front_wing_slider = tk.Scale(
        master=aero_tab, from_=1, to=11, orient="horizontal", resolution=1
    )
    front_wing_slider.pack()

    rear_wing_label = Label(master=aero_tab, text="Rear Wing Aero")
    rear_wing_label.pack()
    rear_wing_slider = tk.Scale(master=aero_tab, from_=1, to=11, orient="horizontal")
    rear_wing_slider.pack()

    # transmission
    diff_adjust_on_label = Label(
        master=transmission_tab, text="Differential Adjustment On Throttle (%)"
    )
    diff_adjust_on_input = tk.Scale(
        master=transmission_tab, from_=50, to=100, orient="horizontal"
    )
    diff_adjust_on_label.pack()
    diff_adjust_on_input.pack()

    diff_adjust_off_label = Label(
        master=transmission_tab, text="Differential Adjustment Off throttle"
    )
    diff_adjust_off_input = tk.Scale(
        master=transmission_tab, from_=50, to=100, orient="horizontal"
    )
    diff_adjust_off_label.pack()
    diff_adjust_off_input.pack()

    # suspension geometry

    # camber
    front_camber_label = Label(master=suspension_geo_tab, text="Front Camber")
    front_camber_slider = tk.Scale(
        master=suspension_geo_tab,
        from_=-3.50,
        to=-2.50,
        resolution=0.1,
        orient="horizontal",
    )
    front_camber_label.pack()
    front_camber_slider.pack()

    rear_camber_label = Label(master=suspension_geo_tab, text="Rear Camber")
    rear_camber_slider = tk.Scale(
        master=suspension_geo_tab,
        from_=-2,
        to=-1.0,
        resolution=0.1,
        orient="horizontal",
    )
    rear_camber_label.pack()
    rear_camber_slider.pack()

    # toe
    front_toe_label = Label(master=suspension_geo_tab, text="Front Toe")
    front_toe_slider = tk.Scale(
        master=suspension_geo_tab,
        orient="horizontal",
        from_=0.05,
        to=0.15,
        resolution=0.01,
    )
    front_toe_label.pack()
    front_toe_slider.pack()

    rear_toe_label = Label(master=suspension_geo_tab, text="Rear Toe")
    rear_toe_slider = tk.Scale(
        master=suspension_geo_tab,
        orient="horizontal",
        from_=0.20,
        to=0.50,
        resolution=0.01,
    )
    rear_toe_label.pack()
    rear_toe_slider.pack()

    # Suspension
    front_suspension_label = Label(
        master=suspension_tab, text="Front Suspension (soft - firm)"
    )
    front_suspension_label.pack()
    front_suspension_input = tk.Scale(
        master=suspension_tab, orient="horizontal", from_=1, to=11, resolution=1
    )
    front_suspension_input.pack()

    rear_suspension_label = Label(
        master=suspension_tab, text="rear Suspension (soft - firm)"
    )
    rear_suspension_label.pack()
    rear_suspension_input = tk.Scale(
        master=suspension_tab, orient="horizontal", from_=1, to=11, resolution=1
    )
    rear_suspension_input.pack()

    front_arb_label = Label(master=suspension_tab, text="Front Anti Roll Bar")
    front_arb_label.pack()
    front_arb_input = tk.Scale(
        master=suspension_tab, from_=1, to=11, resolution=1, orient="horizontal"
    )
    front_arb_input.pack()

    rear_arb_label = Label(master=suspension_tab, text="rear Anti Roll Bar")
    rear_arb_label.pack()
    rear_arb_input = tk.Scale(
        master=suspension_tab, from_=1, to=11, resolution=1, orient="horizontal"
    )
    rear_arb_input.pack()

    front_rh_label = Label(master=suspension_tab, text="Front Ride Height")
    front_rh_input = tk.Scale(
        master=suspension_tab, from_=1, to=11, resolution=1, orient="horizontal"
    )
    front_rh_label.pack()
    front_rh_input.pack()

    rear_rh_label = Label(master=suspension_tab, text="Rear Ride Height")
    rear_rh_input = tk.Scale(
        master=suspension_tab, from_=1, to=11, resolution=1, orient="horizontal"
    )
    rear_rh_label.pack()
    rear_rh_input.pack()

    # Brakes
    brake_pressure_label = Label(master=brakes_tab, text="Brake Pressure")
    brake_pressure_input = tk.Scale(
        master=brakes_tab, from_=50, to=100, resolution=1, orient="horizontal"
    )
    brake_pressure_label.pack()
    brake_pressure_input.pack()

    brake_bias_label = Label(master=brakes_tab, text="Brake Pressure (Front ---  Rear)")
    brake_bias_input = tk.Scale(
        master=brakes_tab, from_=70, to=50, resolution=1, orient="horizontal"
    )
    brake_bias_label.pack()
    brake_bias_input.pack()

    # Tires
    front_tp_label = Label(master=tires_tab, text="Front Tire Pressure")
    front_tp_input = tk.Scale(
        master=tires_tab, from_=21, to=25, resolution=0.4, orient="horizontal"
    )
    front_tp_label.pack()
    front_tp_input.pack()

    rear_tp_label = Label(master=tires_tab, text="Rear Tire Pressure")
    rear_tp_input = tk.Scale(
        master=tires_tab, from_=19.5, to=23.5, resolution=0.4, orient="horizontal"
    )
    rear_tp_label.pack()
    rear_tp_input.pack()

    notebook.pack()
    notebook.add(child=aero_tab, text="Aerodynamics")
    notebook.add(child=transmission_tab, text="Transmission")
    notebook.add(child=suspension_geo_tab, text="Suspension Geometry")
    notebook.add(child=suspension_tab, text="Suspension")
    notebook.add(child=brakes_tab, text="Brakes")
    notebook.add(child=tires_tab, text="Tires")

    b = tk.Button(
        master=root,
        command=lambda: convert_and_display_setup(notebook, root),
        text="Convert Setup",
    )
    b.pack()

    return root


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

    # check that you don't go over the limit when changing the rear camber
    if rear_camber - 0.1 <= -2.0:
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

    front_tire_pressure -= 0.4
    rear_tire_pressure -= 0.8  # lower rear tire pressure by 2pts

    front_tire_pressure = (
        21 if front_tire_pressure < 21 else round(front_tire_pressure, 1)
    )
    rear_tire_pressure = (
        19.5 if rear_tire_pressure < 19.5 else round(rear_tire_pressure, 1)
    )
    return (front_tire_pressure, rear_tire_pressure)


def convertSetup(notebook):
    """
    This function will take the values entered, and on a button press, convert the values,
    which should be for a dry setup, into generally suitable values for a wet track
    """
    widgets = getEntryWidgetsFromTabs(notebook)

    #################################
    # Update key index => tab title #
    # 0 => Aero                     #
    # 1 => Transmission             #
    # 2 => Suspension Geometry      #
    # 3 => Suspension               #
    # 4 => Brakes                   #
    # 5 => Tires                    #
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
    root = set_up_window()
    root.mainloop()


if __name__ == "__main__":
    main()
