class F1SetupUpdater:
    def __init__(self, initial_setup_vals: dict):
        self.initial_setup_vals = initial_setup_vals
        return

    def update_aerodynamics(self):
        init_aero_vals: dict = self.initial_setup_vals["Aerodynamics"]
        front_wing = init_aero_vals["Front Wing Aero"]
        rear_wing = init_aero_vals["Rear Wing Aero"]

        if front_wing + 2 < 11:
            front_wing += 2
        if rear_wing + 2 < 11:
            rear_wing += 2
        return (front_wing, rear_wing)

    def update_transmission(self):
        init_transmission_vals = self.initial_setup_vals["Transmission"]
        diff_on_throttle = init_transmission_vals[
            "Differential Adjustment On Throttle (%)"
        ]
        diff_off_throttle = init_transmission_vals[
            "Differential Adjustment Off throttle (%)"
        ]

        diff_on_throttle = 50
        if diff_off_throttle >= 70:
            diff_off_throttle = 65
        return (diff_on_throttle, diff_off_throttle)

    def update_suspension_geometry(self):
        init_sg_vals = self.initial_setup_vals["Suspension Geometry"]
        front_camber = init_sg_vals["Front Camber"]
        rear_camber = init_sg_vals["Rear Camber"]
        front_toe = init_sg_vals["Front Toe"]
        rear_toe = init_sg_vals["Rear Toe"]

        if rear_camber > -3.5:
            rear_camber -= 0.10
        return (front_camber, rear_camber, front_toe, rear_toe)

    def update_suspension(self):
        init_suspension_val = self.initial_setup_vals["Suspension"]
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

        return (
            front_suspension,
            rear_suspension,
            front_arb,
            rear_arb,
            front_rh,
            rear_rh,
        )

    def update_brakes(self):
        init_brake_vals = self.initial_setup_vals["Brakes"]
        brake_pressure = init_brake_vals["Brake Pressure %"]
        brake_bias = init_brake_vals["Brake Bias (Front ---  Rear) %"]

        brake_pressure = 89
        brake_bias = 52 if brake_bias >= 53 else brake_bias
        return (brake_pressure, brake_bias)

    def update_tires(self):
        init_tire_pressures = self.initial_setup_vals["Tires"]
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

    # TODO: FIX THIS
    def convert_dry_setup_to_wet(self):
        """This function will update all of the individual parts of the F1 Setup
          and return the converted values, to the user, to use in wet conditions

        Returns:
            dict[Setup Area : {setup item name : setup item value}]: A dictionary
            containing all the updated setup values for each setup item in the F1
            Game.
        """
        new_setup_vals: dict = {}
        new_aero_vals = self.update_aerodynamics()
        new_transmission_vals = self.update_transmission()

        new_suspension_geo_vals = self.update_suspension_geometry()
        new_suspension_vals = self.update_suspension()
        new_brakes_vals = self.update_brakes()
        new_tires_vals = self.update_tires()

        new_setup_vals_tuple = (
            new_aero_vals,
            new_transmission_vals,
            new_suspension_vals,
            new_suspension_geo_vals,
            new_brakes_vals,
            new_tires_vals,
        )
        # for i in range(len(new_setup_vals_tuple)):
        #     new_setup_vals | new_setup_vals_tuple[i]
        print(f"New SETUP: {new_setup_vals_tuple}")
        return new_setup_vals
