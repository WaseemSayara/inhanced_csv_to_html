import csv
import employee
import pytest


def csv_to_objects(file_name):
    """a function the creates objects of from the csv file"""
    with open('resources/' + file_name, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = list(next(csv_reader, None))
        arr_of_employees = []
        for row in csv_reader:
            new_employee = employee.Employee(int(row[0]), row[1], int(row[2]), row[3],
                                             row[4], row[5], row[6])
            arr_of_employees.append(new_employee)
        return [arr_of_employees, headers]


def read_from_file(file_name):
    """a function to read from a file"""
    file = open('resources/' + file_name, "r")
    file_string = file.read()
    file.close()
    return file_string


def write_in_file(file_name, string):
    """a function to write in a file"""
    file = open('resources/' + file_name, "w")
    file.write(string)
    file.close()


def edit_html(array, headers, file_string):
    headers_str = "<tr>"
    body_rows_str = ""

    for i in headers:
        headers_str += "<th>" + i + "</th>"
    headers_str += "</tr>\n"

    for i in array:
        body_rows_str += "<tr>"
        body_rows_str += "<th>" + str(i.id_) + "</th> "
        body_rows_str += "<th>" + i.name + "</th> "
        body_rows_str += "<th>" + str(i.salary) + "</th>"
        body_rows_str += "<th>" + i.address + "</th> "
        body_rows_str += "<th>" + i.department + "</th> "
        body_rows_str += "<th>" + i.email + "</th> "
        body_rows_str += "<th>" + i.phone + "</th> "
        body_rows_str += "</tr> \n"

    file_string = str(file_string).format(headings=headers_str, body_rows=body_rows_str)

    return file_string


def main():
    csv_file = 'Employee.csv'
    input_template = 'template.html'
    output_html = 'outcome.html'

    arr_of_employees, headers = csv_to_objects(csv_file)
    new_html = read_from_file(input_template)
    new_html = edit_html(arr_of_employees, headers, new_html)
    write_in_file(output_html, new_html)


def test_func1():
    x, headers = csv_to_objects('Employee.csv')
    assert len(headers) > 0

def test_func2():
    x, headers = csv_to_objects('Employee.csv')
    assert headers[0] == "ID"

main()
