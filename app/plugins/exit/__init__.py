""" Exit Command Class """
import sys
from app.commands import Command


class ExitCommand(Command):
    """ Exit Command"""
    def execute(self, args):
        raise SystemExit("Exiting...")
    