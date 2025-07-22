import pytest
from f1sc.main import (
    update_aerodynamics,
    update_transmission,
    update_suspension_geometry,
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
