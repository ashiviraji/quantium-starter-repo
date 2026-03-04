import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    # If your file name is Task3.py use "Task3"
    return import_app("Task4")


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)

    header = dash_duo.find_element("#header-title")
    assert header.text == "Pink Morsels Sales Dashboard"


def test_visualisation_present(dash_duo, app):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)

    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None