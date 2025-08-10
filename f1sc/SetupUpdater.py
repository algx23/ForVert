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
        return {"Front Wing": front_wing, "Rear Wing": rear_wing}

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
        return {
            "Diff On Throttle": diff_on_throttle,
            "Diff Off Throttle": diff_off_throttle,
        }

    def update_suspension_geometry(self):
        init_sg_vals = self.initial_setup_vals["Suspension Geometry"]
        front_camber = init_sg_vals["Front Camber"]
        rear_camber = init_sg_vals["Rear Camber"]
        front_toe = init_sg_vals["Front Toe"]
        rear_toe = init_sg_vals["Rear Toe"]

        if rear_camber > -3.5:
            rear_camber -= 0.10
        return {
            "Front Camber": front_camber,
            "Rear Camber": rear_camber,
            "Front Toe": front_toe,
            "Rear Toe": rear_toe,
        }

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

        return {
            "Front Suspension": front_suspension,
            "Rear Suspension": rear_suspension,
            "Front Anti Roll Bar": front_arb,
            "Rear Anti Roll Bar": rear_arb,
            "Front Ride Height": front_rh,
            "Rear Ride Height": rear_rh,
        }

    def update_brakes(self):
        init_brake_vals = self.initial_setup_vals["Brakes"]
        brake_pressure = init_brake_vals["Brake Pressure %"]
        brake_bias = init_brake_vals["Brake Bias (Front ---  Rear) %"]

        brake_pressure = 89
        brake_bias = 52 if brake_bias >= 53 else brake_bias
        return {"Brake Pressure": brake_pressure, "Brake Bias": brake_bias}

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
        return {
            "Front Tire Pressure": front_tire_pressure,
            "Rear Tire Pressure": rear_tire_pressure,
        }

    def convert_dry_setup_to_wet(self):
        """This function will update all of the individual parts of the F1 Setup
          and return the converted values, to the user, to use in wet conditions

        Returns:
            dict[Setup Area : {setup item name : setup item value}]: A dictionary
            containing all the updated setup values for each setup item in the F1
            Game.
        """
        new_aero_vals = self.update_aerodynamics()
        new_transmission_vals = self.update_transmission()

        new_suspension_geo_vals = self.update_suspension_geometry()
        new_suspension_vals = self.update_suspension()
        new_brakes_vals = self.update_brakes()
        new_tires_vals = self.update_tires()

        new_setup_vals = {
            "Aerodynamics": new_aero_vals,
            "Transmission": new_transmission_vals,
            "Suspension": new_suspension_vals,
            "Suspension Geometry": new_suspension_geo_vals,
            "Brakes": new_brakes_vals,
            "Tires": new_tires_vals,
        }
        print(f"New SETUP: {new_setup_vals}")
        return new_setup_vals
