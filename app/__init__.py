""" Main Application"""
import pkgutil
import importlib
from app.commands import Command, CommandHandler
from app.plugins.menu import MenuCommand


class App:
    """ Application Class """
    def __init__(self):
        """ Initialize """
        self.command_handler = CommandHandler()

    class Error(Exception):
        """Custom exception for bad input"""

    def load_plugins(self):
        """ Load Plugins """
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue


    def start(self):
        """ Start Application """
        self.load_plugins()
        print("Type 'menu' to see available commands, type 'exit' to quit")
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        while True:
            try:
                user_input = input(">>> ").strip().split()
                if user_input:
                    command = user_input[0].lower()
                    args = user_input[1:]
                    self.command_handler.execute_command(command, args)
            except App.Error:
                print("Error while executing command")
