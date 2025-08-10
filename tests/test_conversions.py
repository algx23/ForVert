import pytest

from f1sc.SetupUpdater import F1SetupUpdater


def test_aero_update():
    input_aero_vals: dict = {
        "Aerodynamics": {"Front Wing Aero": 3, "Rear Wing Aero": 5}
    }
    updater = F1SetupUpdater(input_aero_vals)
    updated_aero_vals = updater.update_aerodynamics()
    assert updated_aero_vals["Front Wing"] == 5
    assert updated_aero_vals["Rear Wing"] == 7


def test_transmission_update():
    input_transmission_vals: dict = {
        "Transmission": {
            "Differential Adjustment On Throttle (%)": 75,
            "Differential Adjustment Off throttle (%)": 69,
        }
    }
    updater = F1SetupUpdater(input_transmission_vals)

    updated_transmission_vals = updater.update_transmission()
    update_diff_on, update_diff_off = (
        updated_transmission_vals["Diff On Throttle"],
        updated_transmission_vals["Diff Off Throttle"],
    )
    assert update_diff_on == 50
    assert update_diff_off == 69


def test_transmission_over_70():
    input_transmission_vals: dict = {
        "Transmission": {
            "Differential Adjustment On Throttle (%)": 75,
            "Differential Adjustment Off throttle (%)": 76,  # this is the thing to test
        }
    }
    updater = F1SetupUpdater(input_transmission_vals)
    update_diff_off = updater.update_transmission()["Diff Off Throttle"]
    assert update_diff_off == 65


def test_suspension_geometry():
    input_sus_geo = {
        "Suspension Geometry": {
            "Front Camber": 1,
            "Rear Camber": -2.5,
            "Front Toe": 1,
            "Rear Toe": 1,
        }
    }
    updater = F1SetupUpdater(input_sus_geo)
    updated_sus_geo = updater.update_suspension_geometry()
    assert updated_sus_geo["Rear Camber"] == -2.6


def test_sus_geo_limit():
    input_sus_geo = {
        "Suspension Geometry": {
            "Front Camber": 1,
            "Rear Camber": -3.5,
            "Front Toe": 1,
            "Rear Toe": 1,
        }
    }
    updater = F1SetupUpdater(input_sus_geo)
    updated_sus_geo = updater.update_suspension_geometry()
    assert updated_sus_geo["Rear Camber"] == -3.5


def test_suspension():
    input_sus_vals = {
        "Suspension": {
            "Front Suspension (soft - firm)": 3,
            "Rear Suspension (soft - firm)": 3,
            "Front Anti Roll Bar": 1,
            "Rear Anti Roll Bar": 4,
            "Front Ride Height": 1,
            "Rear Ride Height": 1,
        }
    }
    updater = F1SetupUpdater(input_sus_vals)

    updated_sus = updater.update_suspension()
    front_sus, rear_sus = (
        updated_sus["Front Suspension"],
        updated_sus["Rear Suspension"],
    )
    rear_arb = updated_sus["Rear Anti Roll Bar"]
    front_rh = updated_sus["Front Ride Height"]
    rear_rh = updated_sus["Rear Ride Height"]
    assert front_sus == 2
    assert rear_sus == 2
    assert rear_arb == 4
    assert front_rh == 6
    assert rear_rh == 6


def test_suspension_conditional_update():
    input_sus_vals = {
        "Suspension": {
            "Front Suspension (soft - firm)": 7,
            "Rear Suspension (soft - firm)": 8,
            "Front Anti Roll Bar": 1,
            "Rear Anti Roll Bar": 9,
            "Front Ride Height": 1,
            "Rear Ride Height": 1,
        }
    }
    updater = F1SetupUpdater(input_sus_vals)

    updated_sus = updater.update_suspension()
    front_sus = updated_sus["Front Suspension"]
    rear_sus = updated_sus["Rear Suspension"]
    rear_arb = updated_sus["Rear Anti Roll Bar"]

    assert front_sus == 5
    assert rear_sus == 6
    assert rear_arb == 8


def test_brakes():
    input_brake_vals = {
        "Brakes": {"Brake Pressure %": 55, "Brake Bias (Front ---  Rear) %": 98}
    }
    updater = F1SetupUpdater(input_brake_vals)
    updated_brakes = updater.update_brakes()
    assert updated_brakes["Brake Pressure"] == 89
    assert updated_brakes["Brake Bias"] == 52


def test_tires():
    input_tire_vals = {
        "Tires": {"Front Tire Pressure": 21.8, "Rear Tire Pressure": 21.1}
    }
    updater = F1SetupUpdater(input_tire_vals)
    updated_tires = updater.update_tires()
    assert updated_tires["Front Tire Pressure"] == 21.4
    assert updated_tires["Rear Tire Pressure"] == 20.3
