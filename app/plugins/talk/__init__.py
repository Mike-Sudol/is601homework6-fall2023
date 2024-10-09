"""Talk Command, used for testing args"""
from app.commands import Command

class TalkCommand(Command):
    
    def __init__(self):
        """Initialize MenuCommand."""
        super().__init__() 

    def execute(self, args):
        """ Execute Talk """ 
        print("Hello World!")
        print(args)