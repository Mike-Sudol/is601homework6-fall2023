""" Subtraction Command Class"""
from decimal import Decimal, InvalidOperation
from app.commands import Command

class SubtractionCommand(Command):
    ''' Command for Subtraction'''

    def execute(self, args):
        ''' Subtract 2 Numbers, Returns the result'''
        if len(args) != 2:
            raise ValueError("Two arguments are required")

        try:
            number1 = Decimal(args[0])
            number2 = Decimal(args[1])
        except InvalidOperation as exc:
            raise ValueError("Error: Invalid number format. Please enter valid decimal numbers.") from exc
        result = number1 - number2
        return result
