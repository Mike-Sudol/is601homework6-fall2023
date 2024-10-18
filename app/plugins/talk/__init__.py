"""Talk Command, used for testing args"""
from app.commands import Command

class TalkCommand(Command):
    """Talk Class"""
    def __init__(self):
        """Initialize MenuCommand.""" 

    def execute(self, args):
        """ Execute Talk """
        print("Hello World!")
        print(args)
