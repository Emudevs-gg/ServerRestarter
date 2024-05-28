import os
import subprocess
import time
import sys

# Created by Allelujah/Azayaka
# Github: Techett
# emudevs.gg


class Server:
    """
    Create the server object
    :param name: Name of the app targeted
    :param ext: Extension of the app targeted
    """
    def __init__(self, name, ext):
        self.name = name
        self.ext = ext
        self.process_instance = None

    def start_server(self):
        while True:
            try:
                self.process_instance = self.process()
                if self.process_instance:
                    print(f"\"{self.name}\" started successfully")
                    print("""
                      ___ __  __ _   _ ___  _____   _____   ___  ___ 
                     | __|  \/  | | | |   \| __\ \ / / __| / __|/ __|
                     | _|| |\/| | |_| | |) | _| \ V /\__ \| (_ | (_ |
                     |___|_|  |_|\___/|___/|___| \_/ |___(_)___|\___|
                                                By: Azayaka """)
                    running = True
                    while running:
                        if self.process_instance.poll() is None:
                            time.sleep(10)  # Preventing busy-waiting
                        else:
                            running = False  # Process has terminated
                    print(f"\"{self.name}\" has stopped running.")
                else:
                    print(f"\"{self.name}\" failed to start. Check that the file exists.")
                    sys.exit(1)
            except FileNotFoundError:
                print(f"\"{self.get_name()}\" not found. Make sure you're targeting the correct application.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")
                sys.exit(1)

    def process(self):
        try:
            # Get the path to the executable
            executable_path = self.get_name()

            # Set the working directory to the directory containing the executable
            working_directory = os.path.dirname(executable_path)

            # Start the process with the correct working directory
            return subprocess.Popen(executable_path, cwd=working_directory)
        except FileNotFoundError:
            return None

    def get_name(self):
        # Construct the path to the executable
        return f"../{self.name}.{self.ext}"
