from employee import Employee
import pytest


@pytest.fixture
def employee():
    emp = Employee('John', 'Doe', 5000)
    return emp


def test_employee_default_salary_increment(employee):
    """Test employee default salary increment"""
    employee.give_raise()
    assert employee.get_salary() == 10000


def test_empoyee_custom_salary_increment(employee):
    """Test employee custom salary increment"""
    employee.give_raise(10000)
    assert employee.get_salary() == 15000
