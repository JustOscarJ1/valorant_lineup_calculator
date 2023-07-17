import math
import time
import pyttsx3
import GUIHelpers as guihelpers
import pyautogui

def convert_text_to_speech(text):
    """
    Function to convert text to speech using pyttsx3 library.

    Args:
        text (str): The text to be converted to speech.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 350)  # You can adjust the speech rate (default is 200)
    engine.say(text)
    engine.runAndWait()

def create_main_menu():
    """
    Function to create and start the main menu.
    """
    settings = SettingsManager('settings.txt')
    menu = guihelpers.MainMenu(settings)
    menu.start()

def calculate_prediction(angle, k, m):
    """
    Function to calculate the predicted distance of a parabolic trajectory.

    Args:
        angle (int): The angle of the trajectory in degrees.
        k (float): Constant parameter of the trajectory.
        m (float): Constant parameter of the trajectory.

    Returns:
        float: The predicted distance of the parabolic trajectory.
    """
    if m - angle**2 < 0:
        return float("inf")
    return k * angle * math.sqrt(m - angle**2)

class Parabola:
    def __init__(self, constants: dict[int, list]):
        """
        Class representing a parabolic trajectory.

        Args:
            constants (dict[int, list]): Dictionary of constants for different ranges of distances.
                The keys represent the maximum distance for each range, and the values are lists
                containing the corresponding constants for the parabolic trajectory in that range.
                The list format is [k, m, max_angle].
        """
        self.constants = constants
        self.m = 0
        self.k = 0
        self.min_angle = 0
        self.max_angle = 0
        self.max_distance = 0

    def update_variables(self, distance):
        """
        Method to update the parabolic trajectory variables based on the desired distance.

        Args:
            distance (int): The desired distance for the parabolic trajectory.
        """
        previous_min_angle = 0
        self.max_distance = max(self.constants.keys())
        for i in self.constants.keys():
            if len(self.constants[i]) == 1:
                if self.constants[i][0] < distance:
                    self.m = self.constants[i][0]
                    self.k = self.constants[i][0]
                    break
                continue

            if distance <= i:
                self.k = self.constants[i][0]
                self.m = self.constants[i][1]
                self.max_angle = self.constants[i][2]
                self.min_angle = previous_min_angle
                break

            previous_min_angle = self.constants[i][2]

    def calculate_angle(self, distance: int, settings):
        """
        Method to calculate the angle of the parabolic trajectory given a desired distance.

        Args:
            distance (int): The desired distance for the parabolic trajectory.
            settings (SettingsManager): The settings manager object containing the sensitivity adjustment.

        Returns:
            float: The calculated angle of the parabolic trajectory.
        """
        self.update_variables(distance)
        if distance > self.max_distance:
            convert_text_to_speech(f"Maximum distance is {self.max_distance}")
            exit()

        if self.m == self.k:
            return self.m

        best_prediction = float("inf")
        best_angle = 0
        for i in range(self.min_angle, self.max_angle):
            prediction = calculate_prediction(i, self.k, self.m)
            if abs(prediction - distance) < best_prediction:
                best_prediction = abs(prediction - distance)
                best_angle = i

        #print(best_angle)
        return best_angle / settings.sens_adjustment

class Ability:
    def __init__(self, parabola: Parabola, name: str):
        """
        Class representing an ability with a parabolic trajectory.

        Args:
            parabola (Parabola): The Parabola object representing the trajectory of the ability.
            name (str): The name of the ability.
        """
        self.parabola = parabola
        self.name = name

class SettingsManager:
    def __init__(self, file_name):
        """
        Class for managing settings.

        Args:
            file_name (str): The name of the settings file.
        """
        self.valorant_sens = None
        self.hero_ability = None
        self.allowed_time_to_move_mouse_to_ping = None
        self.minimum_inactive_time_for_mouse_on_top = None
        self.updates_values_from_file(file_name)
        self.sens_adjustment = self.valorant_sens / 0.623

    def updates_values_from_file(self, file_name):
        """
        Method to update settings from a file.

        Args:
            file_name (str): The name of the settings file.
        """
        with open(file_name, 'r') as f:
            settings = f.readlines()

        self.valorant_sens = float(settings[3])
        for ability in abilities:
            if ability.name == settings[1].strip():
                self.hero_ability = ability
                break

        self.allowed_time_to_move_mouse_to_ping = float(settings[7])
        self.minimum_inactive_time_for_mouse_on_top = float(settings[5])

def shoot_projectile(settings):
    """
    Function to shoot a projectile based on the selected settings.

    Args:
        settings (SettingsManager): The settings manager object containing the selected settings.
    """
    desired_distance = False

    while not desired_distance:
        desired_distance = guihelpers.get_distance()

    if desired_distance == 'cancelled':
        return

    angle = settings.hero_ability.parabola.calculate_angle(desired_distance, settings)

    convert_text_to_speech(f"{desired_distance}")
    convert_text_to_speech("Move mouse to ping.")
    time.sleep(settings.allowed_time_to_move_mouse_to_ping)

    ping_x = pyautogui.position()[0]
    convert_text_to_speech("Coordinates locked, move mouse to top of screen.")
    previous_x = pyautogui.position().x
    iterations_since_movement = 0
    while True:
        if previous_x == pyautogui.position().x:
            iterations_since_movement += 1
        else:
            print(previous_x, pyautogui.position().x)
            iterations_since_movement = 0
        previous_x = pyautogui.position().x
        if iterations_since_movement == settings.minimum_inactive_time_for_mouse_on_top * 10:
            break
        time.sleep(0.1)

    convert_text_to_speech("Top of screen detected, move mouse to optimal position.")
    number_window = guihelpers.CoordinateWindow(ping_x, angle)
    number_window.root.mainloop()
    convert_text_to_speech("Shoot the utility")

VIPER_BRIMSTONE_STAGE_PARABOLA = Parabola({15: [77], 69: [0.000245, 556800, 550], 78: [0.0002, 749850, 700]})
KILLJOY_VIPER_DEADLOCK_GECKO_PARABOLA = Parabola({9: [77], 39: [0.00014, 567320, 475], 44: [0.00012, 718950, 625]})
CYPHER_PARABOLA = Parabola({5: [77], 24: [0.000068, 694550, 575]})

cypher_cage = Ability(CYPHER_PARABOLA, "cypher_smoke")
deadlock_net = Ability(KILLJOY_VIPER_DEADLOCK_GECKO_PARABOLA, "deadlock_net")
killjoy_swarm_grenade = Ability(KILLJOY_VIPER_DEADLOCK_GECKO_PARABOLA, "killjoy_molotov")
gecko_moshpit = Ability(KILLJOY_VIPER_DEADLOCK_GECKO_PARABOLA, "gecko_moshpit")
viper_poison_orb = Ability(KILLJOY_VIPER_DEADLOCK_GECKO_PARABOLA, "viper_poison_orb")
viper_snakebite = Ability(VIPER_BRIMSTONE_STAGE_PARABOLA, "viper_snakebite")
brimstone_molotov = Ability(VIPER_BRIMSTONE_STAGE_PARABOLA, "brimstone_molotov")
sage_slow_orb = Ability(VIPER_BRIMSTONE_STAGE_PARABOLA, "sage_slow")

abilities = [cypher_cage, deadlock_net, killjoy_swarm_grenade, gecko_moshpit, viper_snakebite, viper_poison_orb, brimstone_molotov, sage_slow_orb]
