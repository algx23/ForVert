import pytest
from f1sc.main import (
    update_aerodynamics,
    update_transmission,
    update_suspension_geometry,
    update_brakes,
    update_suspension,
)


def test_aero_update():
    input_aero_vals: dict = {"Front Wing Aero": 3, "Rear Wing Aero": 5}
    updated_aero_vals: tuple = update_aerodynamics(input_aero_vals)
    assert updated_aero_vals[0] == 5 and updated_aero_vals[1] == 7


def test_transmission_update():
    input_transmission_vals: dict = {
        "Differential Adjustment On Throttle (%)": 75,
        "Differential Adjustment Off throttle (%)": 69,
    }
    update_diff_on, update_diff_off = update_transmission(input_transmission_vals)

    assert update_diff_on == 50
    assert update_diff_off == 69


def test_transmission_over_70():
    input_transmission_vals: dict = {
        "Differential Adjustment On Throttle (%)": 75,
        "Differential Adjustment Off throttle (%)": 76,  # this is the thing to test
    }
    update_diff_off = update_transmission(input_transmission_vals)[1]
    assert update_diff_off == 65


def test_suspension_geometry():
    input_sus_geo = {
        "Front Camber": 1,
        "Rear Camber": -2.5,
        "Front Toe": 1,
        "Rear Toe": 1,
    }
    updated_sus_geo = update_suspension_geometry(input_sus_geo)
    assert updated_sus_geo[1] == -2.6


def test_sus_geo_limit():
    input_sus_geo = {
        "Front Camber": 1,
        "Rear Camber": -3.5,
        "Front Toe": 1,
        "Rear Toe": 1,
    }
    updated_sus_geo = update_suspension_geometry(input_sus_geo)
    assert updated_sus_geo[1] == -3.5


# TODO: suspension tests
def test_suspension():
    input_sus_vals = {
        "Front Suspension (soft - firm)": 3,
        "Rear Suspension (soft - firm)": 3,
        "Front Anti Roll Bar": 1,
        "Rear Anti Roll Bar": 4,
        "Front Ride Height": 1,
        "Rear Ride Height": 1,
    }

    front_sus, rear_sus, front_arb, rear_arb, front_rh, rear_rh = update_suspension(
        input_sus_vals
    )
    assert front_sus == 2
    assert rear_sus == 2
    assert rear_arb == 4
    assert front_rh == 6
    assert rear_rh == 6


def test_suspension_conditional_update():
    input_sus_vals = {
        "Front Suspension (soft - firm)": 7,
        "Rear Suspension (soft - firm)": 8,
        "Front Anti Roll Bar": 1,
        "Rear Anti Roll Bar": 9,
        "Front Ride Height": 1,
        "Rear Ride Height": 1,
    }

    front_sus, rear_sus, front_arb, rear_arb, front_rh, rear_rh = update_suspension(
        input_sus_vals
    )

    assert front_sus == 5
    assert rear_sus == 6
    assert rear_arb == 8


def test_brakes():
    input_brake_vals = {"Brake Pressure %": 55, "Brake Bias (Front ---  Rear) %": 98}
    updated_pressure, updated_bias = update_brakes(input_brake_vals)
    assert updated_pressure == 89
    assert updated_bias == 52
