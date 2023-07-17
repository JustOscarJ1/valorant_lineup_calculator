import tkinter as tk
from tkinter import simpledialog
import keyboard
import pyautogui
import customtkinter
from PIL import ImageTk, Image
from logic_helpers import create_main_menu, shoot_projectile, convert_text_to_speech

# DistanceInputGUI class for inputting distance
class DistanceInputGUI:
    def __init__(self):
        """
        Class representing a GUI window for inputting distance.
        """
        self.distance = None
        self.root = tk.Tk()
        self.root.title("Distance Input")
        self.root.geometry("200x100")
        self.root.attributes('-topmost', True)  # Force the window to stay on top
        self.root.overrideredirect(True)
        self.create_widgets()

    def create_widgets(self):
        """
        Create widgets (labels, entry, buttons) for the distance input window.
        """
        # Create label and entry for distance input
        self.label = tk.Label(self.root, text="Enter a distance:")
        self.label.pack()

        self.distance_entry = tk.Entry(self.root)
        self.distance_entry.pack()

        # Create OK and Cancel buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.BOTTOM, pady=10)

        self.ok_button = tk.Button(self.button_frame, text="OK", width=10, command=self.ok_button_clicked)
        self.ok_button.pack(side=tk.LEFT, padx=10)

        self.cancel_button = tk.Button(self.button_frame, text="Cancel", width=10, command=self.cancel_button_clicked)
        self.cancel_button.pack(side=tk.RIGHT, padx=10)

    def ok_button_clicked(self):
        """
        Event handler for the OK button click.
        Retrieves the entered distance and closes the window.
        """
        # Retrieve the entered distance
        self.distance = self.distance_entry.get()
        self.root.attributes('-topmost', False)  # Allow other windows to be on top
        self.root.destroy()
        self.root.quit()

    def cancel_button_clicked(self):
        """
        Event handler for the Cancel button click.
        Closes the window without setting the distance.
        """
        # Cancel button clicked, close the window
        self.root.attributes('-topmost', False)  # Allow other windows to be on top
        self.root.destroy()
        self.root.quit()

    def run(self):
        """
        Runs the distance input window.
        """
        # Run the distance input window
        self.root.mainloop()


# SettingsViewer class for displaying settings
class SettingsViewer:
    def __init__(self, settings_manager):
        """
        Class for displaying the current settings.
        Args:
            settings_manager (SettingsManager): The settings manager object containing the settings to be displayed.
        """
        self.settings_manager = settings_manager
        self.root = None
        self.frame = None
        self.ability_label = None
        self.ability_placeholder = None
        self.sensitivity_label = None
        self.sensitivity_placeholder = None
        self.inactive_time_label = None
        self.inactive_time_placeholder = None
        self.ping_time_label = None
        self.ping_time_placeholder = None
        self.close_button = None

    def close_window(self):
        """
        Closes the window and goes back to the main menu.
        """
        # Close the window and go back to the main menu
        self.root.destroy()
        create_main_menu()

    def setup_gui(self):
        """
        Sets up the GUI by creating the main window, labels, and buttons.
        """
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        # Create the main window and frame
        self.root = customtkinter.CTk()
        self.root.geometry("425x275")
        self.root.title("Settings Viewer")
        self.root.overrideredirect(True)

        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")

        self.frame = customtkinter.CTkFrame(self.root, width=500, height=300, corner_radius=10)
        self.frame.pack(pady=20, padx=20)

        # Create labels for each setting
        self.ability_label = customtkinter.CTkLabel(self.frame, text="Ability:")
        self.ability_label.grid(row=0, column=0, padx=10, pady=10)

        self.ability_placeholder = customtkinter.CTkLabel(self.frame, text=self.settings_manager.hero_ability.name)
        self.ability_placeholder.grid(row=0, column=1, padx=10, pady=10)

        self.sensitivity_label = customtkinter.CTkLabel(self.frame, text="Valorant Sensitivity:")
        self.sensitivity_label.grid(row=1, column=0, padx=10, pady=10)

        self.sensitivity_placeholder = customtkinter.CTkLabel(self.frame, text=str(self.settings_manager.valorant_sens))
        self.sensitivity_placeholder.grid(row=1, column=1, padx=10, pady=10)

        self.inactive_time_label = customtkinter.CTkLabel(self.frame, text="Minimum inactive time for mouse to be on top:")
        self.inactive_time_label.grid(row=2, column=0, padx=10, pady=10)

        self.inactive_time_placeholder = customtkinter.CTkLabel(self.frame, text=str(self.settings_manager.minimum_inactive_time_for_mouse_on_top))
        self.inactive_time_placeholder.grid(row=2, column=1, padx=10, pady=10)

        self.ping_time_label = customtkinter.CTkLabel(self.frame, text="Allowed time to move mouse to ping:")
        self.ping_time_label.grid(row=3, column=0, padx=10, pady=10)

        self.ping_time_placeholder = customtkinter.CTkLabel(self.frame, text=str(self.settings_manager.allowed_time_to_move_mouse_to_ping))
        self.ping_time_placeholder.grid(row=3, column=1, padx=10, pady=10)

        # Create the close button
        self.close_button = customtkinter.CTkButton(self.root, text="Close", command=self.close_window)
        self.close_button.pack(pady=10)

    def run(self):
        """
        Runs the settings viewer.
        """
        # Run the settings viewer
        self.setup_gui()
        self.root.mainloop()


# CoordinateWindow class for displaying coordinates
class CoordinateWindow:
    def __init__(self, goal_coordinate_x, goal_coordinate_y):
        """
        Class representing a window that displays the coordinates.
        Args:
            goal_coordinate_x (int): The goal X-coordinate.
            goal_coordinate_y (int): The goal Y-coordinate.
        """
        # Create the window
        self.root = tk.Tk()
        self.root.title("Number Window")
        self.root.attributes("-topmost", True)  # Make the window always on top
        self.difference_x = 0
        self.difference_y = 0
        self.goal_coordinate_x = goal_coordinate_x
        self.goal_coordinate_y = goal_coordinate_y

        # Create labels for displaying coordinates
        self.label_x = tk.Label(self.root, text=f"X: {self.difference_x}", font=("Arial", 24))
        self.label_x.pack(padx=10, pady=5)

        self.label_y = tk.Label(self.root, text=f"Y: {self.difference_y}", font=("Arial", 24))
        self.label_y.pack(padx=10, pady=5)

        self.root.after(100, self.update_differences_on_mouse_movement)

        self.root.overrideredirect(True)

    def update_differences(self, difference_x, difference_y):
        """
        Updates the difference labels with new values.
        Args:
            difference_x (int): The difference in X-coordinates.
            difference_y (int): The difference in Y-coordinates.
        """
        # Update the difference labels with new values
        self.difference_x = difference_x
        self.difference_y = difference_y
        self.label_x.config(text=f"X: {self.difference_x}")
        self.label_y.config(text=f"Y: {self.difference_y}")

    def close_window(self):
        """
        Closes the window.
        """
        # Close the window
        self.root.quit()

    def update_differences_on_mouse_movement(self):
        """
        Updates the differences on the GUI until they are both below an error of 2.
        """
        # Update the differences on the GUI until they are both below the error
        mouse_coordinate_x = pyautogui.position().x
        mouse_coordinate_y = pyautogui.position().y
        difference_x = mouse_coordinate_x - self.goal_coordinate_x
        difference_y = mouse_coordinate_y - self.goal_coordinate_y
        self.update_differences(difference_x, difference_y)
        self.root.after(100, self.update_differences_on_mouse_movement)
        if abs(difference_x) <= 2 and abs(difference_y) <= 2:
            # Close the window when the differences are below the error
            self.root.destroy()
            self.close_window()


def get_distance():
    """
    Gets the distance input from the user.
    Returns:
        float or False: The entered distance as a float if valid, False if cancelled.
    """
    # Create the distance input window
    distance_input_window = DistanceInputGUI()
    distance_input_window.run()
    input_value = distance_input_window.distance

    # Check if the user clicked cancel
    if not input_value:
        convert_text_to_speech("Cancelled")
        return "cancelled"

    # Check if the input is a number, if not, get a new input
    try:
        float(input_value)
    except ValueError:
        convert_text_to_speech("Invalid input, input again.")
        return False

    return float(input_value)


# MainMenu class for the main menu
class MainMenu:
    def __init__(self, settings):
        """
        Class representing the main menu.
        Args:
            settings (SettingsManager): The settings manager object.
        """
        # Set the appearance mode to dark
        self.settings = settings

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Create the main window
        self.root = customtkinter.CTk()
        self.root.geometry("400x240")
        self.root.title("JustOscarJs Lineup Tool")

        # Use CTkButton from CustomTkinter for customized buttons
        self.current_settings_button = customtkinter.CTkButton(master=self.root, text="Current Settings",
                                                               command=self.current_settings,
                                                               fg_color=("dark blue", "dark blue"))
        self.current_settings_button.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.set_settings_button = customtkinter.CTkButton(master=self.root, text="Set Settings",
                                                            command=self.set_settings,
                                                            fg_color=("dark blue", "dark blue"))
        self.set_settings_button.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.send_projectile_button = customtkinter.CTkButton(master=self.root, text="Send Projectile",
                                                              command=self.send_projectile,
                                                              fg_color=("dark blue", "dark blue"))
        self.send_projectile_button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        # Small text label for credits
        credits_text = "Credits:\nDiscord: JustOscarJ\nGitHub: JustOscarJ1\nReddit: FlamingJark"
        self.credits_label = customtkinter.CTkLabel(master=self.root, text=credits_text, corner_radius=4)
        self.credits_label.place(relx=0.5, rely=0.85, anchor=customtkinter.CENTER)
        self.hot_key_active = True

        keyboard.on_press_key("F5", self.on_hotkey_pressed)

    def on_hotkey_pressed(self, event):
        """
        Event handler for the hotkey pressed (F5).
        Calls the shoot_projectile method.
        Args:
            event (keyboard.KeyboardEvent): The keyboard event object.
        """
        # Check if the hotkey pressed is the "F5" key
        if event.name == "f5" and self.hot_key_active:
            # Call the shoot_projectile method
            self.send_projectile()
        self.hot_key_active = not self.hot_key_active

    # Button click event handlers
    def current_settings(self):
        """
        Event handler for the Current Settings button click.
        Goes to the settings viewer to display current settings.
        """
        # Go to the settings viewer to display current settings
        self.root.destroy()
        self.settings.updates_values_from_file('settings.txt')
        settings_viewer = SettingsViewer(self.settings)
        settings_viewer.run()

    def set_settings(self):
        """
        Event handler for the Set Settings button click.
        Goes to the settings GUI to set new settings.
        """
        # Go to the settings GUI to set new settings
        self.root.destroy()
        settings_gui = SettingsGUI()
        settings_gui.start()

    def send_projectile(self):
        """
        Event handler for the Send Projectile button click.
        Updates the settings from file and shoots the projectile.
        """
        # Update the settings from file and shoot the projectile
        self.settings.updates_values_from_file('settings.txt')
        shoot_projectile(self.settings)

    def start(self):
        """
        Starts the main menu.
        """
        # Start the main menu
        self.root.mainloop()


# SettingsGUI class for setting new values
class SettingsGUI:
    def __init__(self):
        """
        Class representing the settings GUI for setting new values.
        """
        self.button_images = {
            "Viper Snakebite": "viper_snakebite.png",
            "Viper Poison Orb": "viper_poison_orb.png",
            "Brimstone Molotov": "brimstone_molotov.png",
            "Sage Slow": "sage_slow.png",
            "Deadlock Net": "deadlock_net.png",
            "Killjoy Molotov": "killjoy_molotov.png",
            "Cypher Smoke": "cypher_smoke.png",
            "Gecko Moshpit": "gecko_moshpit.png"
        }

        self.root = tk.Tk()
        self.root.title("Valorant Abilities")
        self.root.overrideredirect(True)
        self.root.resizable(False, False)
        self.selected_ability = tk.StringVar()
        self.create_buttons()
        self.create_separator()
        self.create_sensitivity_input()
        self.create_inactive_time_slider()
        self.create_ping_time_slider()
        self.create_save_button()

    def create_buttons(self):
        """
        Create buttons for each ability with images.
        """
        image_size = (50, 50)
        self.button_frames = []

        for i, (button_name, image_filename) in enumerate(self.button_images.items()):
            image_path = f"images/{image_filename}"
            img = Image.open(image_path)
            img.thumbnail(image_size, Image.LANCZOS)

            width, height = img.size
            if width > height:
                left = (width - height) // 2
                right = left + height
                img = img.crop((left, 0, right, height))
            else:
                top = (height - width) // 2
                bottom = top + width
                img = img.crop((0, top, width, bottom))

            photo = ImageTk.PhotoImage(img)

            button_frame = tk.Frame(self.root)
            button_frame.grid(row=i, column=0, sticky="w", pady=5)

            image_label = tk.Label(button_frame, image=photo)
            image_label.grid(row=0, column=0, padx=5)

            text_label = tk.Label(button_frame, text=button_name)
            text_label.grid(row=0, column=1, padx=5)

            image_label.bind("<Button-1>", lambda event, name=button_name: self.image_click(name))
            image_label.image = photo

            self.button_frames.append(button_frame)

    def create_separator(self):
        """
        Create a separator between buttons and other settings.
        """
        separator_frame = tk.Frame(self.root, height=2, relief="sunken")
        separator_frame.grid(row=len(self.button_frames), column=0, padx=5, pady=10, sticky="we")

    def create_sensitivity_input(self):
        """
        Create an input for Valorant sensitivity.
        """
        label_sensitivity = tk.Label(self.root, text="Valorant Sensitivity")
        label_sensitivity.grid(row=len(self.button_frames) + 1, column=0, padx=5, pady=5, sticky="w")

        self.input_sensitivity = tk.Entry(self.root)
        self.input_sensitivity.grid(row=len(self.button_frames) + 2, column=0, padx=5, pady=5, sticky="w")

    def create_inactive_time_slider(self):
        """
        Create a slider for minimum inactive time for the mouse to be on top.
        """
        label_inactive_time = tk.Label(self.root, text="Minimum inactive time for mouse to be on top")
        label_inactive_time.grid(row=len(self.button_frames) + 3, column=0, padx=5, pady=5, sticky="w")

        self.scale_inactive_time = tk.Scale(self.root, from_=1, to=10, orient="horizontal", resolution=0.1)
        self.scale_inactive_time.grid(row=len(self.button_frames) + 4, column=0, padx=5, pady=5, sticky="w")

    def create_ping_time_slider(self):
        """
        Create a slider for the allowed time to move the mouse to ping.
        """
        label_ping_time = tk.Label(self.root, text="Allowed time to move mouse to ping")
        label_ping_time.grid(row=len(self.button_frames) + 5, column=0, padx=5, pady=5, sticky="w")

        self.scale_ping_time = tk.Scale(self.root, from_=1, to=10, orient="horizontal", resolution=0.1)
        self.scale_ping_time.grid(row=len(self.button_frames) + 6, column=0, padx=5, pady=5, sticky="w")

    def create_save_button(self):
        """
        Create a save button to save the settings.
        """
        self.save_button = tk.Button(self.root, text="Save", command=self.save_values, state="disabled")
        self.save_button.grid(row=len(self.button_frames) + 7, column=0, pady=10)

    def image_click(self, button_name):
        """
        Event handler for the ability image click.
        Args:
            button_name (str): The name of the selected ability.
        """
        for button_frame in self.button_frames:
            label = button_frame.winfo_children()[1]
            label.config(font=("TkDefaultFont", 11))

        for button_frame in self.button_frames:
            label = button_frame.winfo_children()[1]
            if label['text'] == button_name:
                label.config(font=("TkDefaultFont", 11, "bold"))

        self.selected_ability.set(button_name)
        self.save_button.config(state="normal")

    def save_values(self):
        """
        Save the selected values to a settings file.
        """
        val_sensitivity = self.input_sensitivity.get()
        min_inactive_time = self.scale_inactive_time.get()
        allowed_ping_time = self.scale_ping_time.get()
        selected_ability_str = self.selected_ability.get()

        if not val_sensitivity:
            val_sensitivity = '1'

        with open('settings.txt', 'w') as f:
            to_write = ['ability: (viper_snakebite, viper_poisonorb, brimstone_molotov, sage_slow, deadlock_net, killjoy_molotov, cypher_smoke, gecko_moshpit)',
                          self.button_images[selected_ability_str][:-4],
                          'valorant_sens:',
                          val_sensitivity,
                          'minimum inactive time for mouse to be on top (1-10)',
                          str(min_inactive_time),
                          'allowed time to move mouse to ping (1-10)',
                          str(allowed_ping_time)]

            for text_to_write in to_write:
                f.write(text_to_write + '\n')

        # print("Valorant Sensitivity:", val_sensitivity)
        # print("Minimum inactive time for mouse to be on top:", min_inactive_time)
        # print("Allowed time to move mouse to ping:", allowed_ping_time)
        # print("Selected Ability:", selected_ability_str)
        self.root.destroy()
        create_main_menu()

    def start(self):
        """
        Start the settings GUI.
        """
        self.root.mainloop()


