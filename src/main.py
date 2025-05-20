import tkinter as tk


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

    front_wing_label = tk.Label(master=root, text="Front Wing Aero")
    front_wing_label.pack()
    front_wing_slider = tk.Scale(
        root, from_=1, to=11, orient="horizontal", resolution=1
    )
    front_wing_slider.pack()

    rear_wing_label = tk.Label(master=root, text="Rear Wing Aero")
    rear_wing_label.pack()
    rear_wing_slider = tk.Scale(master=root, from_=1, to=11, orient="horizontal")
    rear_wing_slider.pack()

    # transmission
    diff_adjust_on_label = tk.Label(
        master=root, text="Differential Adjustment On Throttle (%)"
    )
    diff_adjust_on_input = tk.Scale(master=root, from_=50, to=100, orient="horizontal")
    diff_adjust_on_label.pack()
    diff_adjust_on_input.pack()

    diff_adjust_off_label = tk.Label(
        master=root, text="Differential Adjustment Off throttle"
    )
    diff_adjust_off_input = tk.Scale(master=root, from_=50, to=100, orient="horizontal")
    diff_adjust_off_label.pack()
    diff_adjust_off_input.pack()

    # suspension geometry

    # camber
    front_camber_label = tk.Label(master=root, text="Front Camber")
    front_camber_slider = tk.Scale(
        master=root, from_=-3.50, to=-2.50, resolution=0.1, orient="horizontal"
    )
    front_camber_label.pack()
    front_camber_slider.pack()

    rear_camber_label = tk.Label(master=root, text="Rear Camber")
    rear_camber_slider = tk.Scale(
        master=root, from_=-3.50, to=-2.5, resolution=0.1, orient="horizontal"
    )
    rear_camber_label.pack()
    rear_camber_slider.pack()

    # toe
    front_toe_label = tk.Label(master=root, text="Front Toe")
    front_toe_slider = tk.Scale(
        master=root, orient="horizontal", from_=0.05, to=0.15, resolution=0.01
    )
    front_toe_label.pack()
    front_toe_slider.pack()

    rear_toe_label = tk.Label(master=root, text="Rear Toe")
    rear_toe_slider = tk.Scale(
        master=root, orient="horizontal", from_=0.20, to=0.50, resolution=0.1
    )
    rear_toe_label.pack()
    rear_toe_slider.pack()
    # Suspension
    front_suspension_label = tk.Label(
        master=root, text="Front Suspension (soft - firm)"
    )
    front_suspension_label.pack()
    front_suspension_input = tk.Scale(
        master=root, orient="horizontal", from_=1, to=11, resolution=1
    )
    front_suspension_input.pack()

    rear_suspension_label = tk.Label(master=root, text="rear Suspension (soft - firm)")
    rear_suspension_label.pack()
    rear_suspension_input = tk.Scale(
        master=root, orient="horizontal", from_=1, to=11, resolution=1
    )
    rear_suspension_input.pack()

    front_arb_label = tk.Label(master=root, text="Front Anti Roll Bar")
    front_arb_label.pack()
    front_arb_input = tk.Scale(
        master=root, from_=1, to=11, resolution=1, orient="horizontal"
    )
    front_arb_input.pack()

    rear_arb_label = tk.Label(master=root, text="rear Anti Roll Bar")
    rear_arb_label.pack()
    rear_arb_input = tk.Scale(
        master=root, from_=1, to=11, resolution=1, orient="horizontal"
    )
    rear_arb_input.pack()
    # TODO: Brake pressure / bias
    # TODO: Tires

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
