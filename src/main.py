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
    root = tk.Tk()
    root.minsize(width=WIDTH, height=HEIGHT)
    root.title("F1 Setup Hub")

    notebook = Notebook(master=root, height=HEIGHT, width=WIDTH)

    # tabs for the different areas of setup
    aero_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)
    transmission_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)
    suspension_geo_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)
    suspension_tab = Frame(master=notebook, width=WIDTH, height=HEIGHT)

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
        from_=-3.50,
        to=-2.5,
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
        resolution=0.1,
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
    # TODO: Brake pressure / bias
    # TODO: Tires

    notebook.pack()
    notebook.add(aero_tab, text="Aerodynamics")
    notebook.add(transmission_tab, text="Transmission")
    notebook.add(suspension_geo_tab, text="Suspension Geometry")
    notebook.add(suspension_tab, text="Suspension")

    return root


def convertSetup():
    """
    This function will take the values entered, and on a button press, convert the values,
    which should be for a dry setup, into generally suitable values for a wet track
    """
    # TODO implement setup conversion logic
    NotImplemented


def main():
    root = set_up_window()
    root.mainloop()


if __name__ == "__main__":
    main()
