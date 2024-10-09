import pkgutil
import importlib
from app.commands import Command, CommandHandler
from app.plugins.menu import MenuCommand


class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Load Plugins from Subdirectory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try: 
                        if issubclass(item, (Command)):  
                            self.command_handler.register_command(plugin_name, item()) 
                    except TypeError:
                        continue 


    def start(self):
        # Start Application
        self.load_plugins() 
        print("Type 'menu' to see existing commands, type 'exit' to quit")
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        while True: 
            try:
                user_input = input(">>> ").strip().split()
                if user_input:
                    command = user_input[0].lower()
                    args = user_input[1:] 
                    self.command_handler.execute_command(command, args) 
            except Exception as e:
                print(f"Error while executing command: {e}")