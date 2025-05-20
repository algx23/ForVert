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

    # front wing text
    front_wing_label = tk.Label(master=root, text="Front Wing Aero")
    front_wing_label.pack()
    # front wing slider
    front_wing_slider = tk.Scale(
        root, from_=0, to=12, orient="horizontal", resolution=1
    )
    front_wing_slider.pack()

    # rear wing text and slider
    rear_wing_label = tk.Label(master=root, text="Rear Wing Aero")
    rear_wing_label.pack()
    rear_wing_slider = tk.Scale(master=root, from_=0, to=12, orient="horizontal")
    rear_wing_slider.pack()

    # transmission
    diff_adjust_on_label = tk.Label(
        master=root, text="Differential Adjustment On Throttle"
    )
    diff_adjust_on_input = tk.Entry(master=root)
    diff_adjust_on_label.pack()
    diff_adjust_on_input.pack()

    diff_adjust_off_label = tk.Label(
        master=root, text="Differential Adjustment Off throttle"
    )
    diff_adjust_off_input = tk.Entry(master=root)
    diff_adjust_off_label.pack()
    diff_adjust_off_input.pack()

    # suspension geometry
    # camber
    front_camber_label = tk.Label(master=root, text="Front Camber")
    front_camber_slider = tk.Scale(master=root, from_=-5, to=5, orient="horizontal")
    front_camber_label.pack()
    front_camber_slider.pack()

    rear_camber_label = tk.Label(master=root, text="Rear Camber")
    rear_camber_slider = tk.Scale(master=root, from_=-5, to=5, orient="horizontal")
    rear_camber_label.pack()
    rear_camber_slider.pack()

    # toe
    front_toe_label = tk.Label(master=root, text="Front Toe")
    front_toe_slider = tk.Entry(master=root)
    front_toe_label.pack()
    front_toe_slider.pack()

    rear_toe_label = tk.Label(master=root, text="Rear Toe")
    rear_toe_slider = tk.Entry(master=root)
    rear_toe_label.pack()
    rear_toe_slider.pack()
    # TODO: Suspension
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
