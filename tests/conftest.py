""" Test using Fake Data """
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """ Make Fake Data """
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    for idx in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = (
            Decimal(fake.random_number(digits=1))
            if idx % 4 == 3
            else Decimal(fake.random_number(digits=2))
        )
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func is divide and b == Decimal('0'):
            b = Decimal('1')

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """ Terminal Test """
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    """ Make Tests """
    required_fixtures = {"a", "b", "expected"}
    if required_fixtures.intersection(metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        test_cases = list(generate_test_data(num_records))
        if 'operation_name' in metafunc.fixturenames:
            parameters = [
                (a, b, op_name, expected)
                for a, b, op_name, op_func, expected in test_cases
            ]
            metafunc.parametrize("a,b,operation_name,expected", parameters)
        else:
            parameters = [
                (a, b, op_func, expected)
                for a, b, op_name, op_func, expected in test_cases
            ]
            metafunc.parametrize("a,b,operation,expected", parameters)
