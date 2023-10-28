# Import necessary libraries
import datetime

# Define the smart home class
class SmartHome:
    def __init__(self):
        self.lights = False
        self.air_conditioner = False
        self.heater = False
        self.energy_saving_mode = False

    def turn_on_lights(self):
        self.lights = True
        print("Lights turned on.")

    def turn_off_lights(self):
        self.lights = False
        print("Lights turned off.")

    def turn_on_air_conditioner(self):
        self.air_conditioner = True
        print("Air conditioner turned on.")

    def turn_off_air_conditioner(self):
        self.air_conditioner = False
        print("Air conditioner turned off.")

    def turn_on_heater(self):
        self.heater = True
        print("Heater turned on.")

    def turn_off_heater(self):
        self.heater = False
        print("Heater turned off.")

    def enable_energy_saving_mode(self):
        self.energy_saving_mode = True
        print("Energy saving mode enabled.")

    def disable_energy_saving_mode(self):
        self.energy_saving_mode = False
        print("Energy saving mode disabled.")

    def check_time(self):
        current_time = datetime.datetime.now().time()
        if self.energy_saving_mode and current_time >= datetime.time(22, 0) or current_time <= datetime.time(6, 0):
            self.turn_off_lights()
            self.turn_off_air_conditioner()
            self.turn_on_heater()

# Create an instance of the smart home
my_home = SmartHome()

# Turn on lights
my_home.turn_on_lights()

# Turn on air conditioner
my_home.turn_on_air_conditioner()

# Enable energy saving mode
my_home.enable_energy_saving_mode()

# Check the time and automatically adjust energy usage
my_home.check_time()

