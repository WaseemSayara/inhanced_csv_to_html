import main
import pytest


@pytest.fixture
def values():
    array, headers = main.csv_to_objects("Employee.csv")
    read = main.read_from_file("template.html")
    return [array, headers, read]


def test_read_file_method1(values):
    assert len(values[2]) >= 20


def test_read_file_method2():
    read = main.read_from_file("template55.html")
    assert read == "file not found"


def test_csv_to_objects_method1(values):
    assert values is not None


def test_csv_to_objects_method2(values):
    assert len(values[0]) > 0
    assert len(values[1]) > 0


def test_csv_to_objects_method3():
    values = main.csv_to_objects("Employee55.csv")
    assert values is None


def test_write_file_method1():
    write = main.write_in_file("output_test.html", "Testing test")
    assert write is True


def test_edit_html_method1(values):
    new_html = main.edit_html(values[0], values[1], values[2])
    assert len(new_html) > len(values[2])


def test_edit_html_method2(values):
    new_html = main.edit_html(values[0], values[1], values[2])
    assert new_html.startswith("<!DOCTYPE html>")


def test_edit_html_method3(values):
    new_html = main.edit_html(values[0], values[1], values[2])
    assert values[2].__contains__("{headings}")
    assert not new_html.__contains__("{headings}")
    assert values[2].__contains__("{body_rows}")
    assert not new_html.__contains__("{body_rows}")
