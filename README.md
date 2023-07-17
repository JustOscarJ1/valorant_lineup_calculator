<a href="https://www.buymeacoffee.com/flamingjark" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

WARNING: This will (probably) only work on 1920x1080 monitors, if someone with a larger monitor tests, this can probably be fixed pretty easily.
# Valorant Lineup Tool

Valorant Lineup Tool is a Python-based application that assists players in shooting projectiles with parabolic trajectories in the game Valorant. The tool provides a user-friendly interface for inputting desired distances, calculates the optimal angles for shooting projectiles, and guides players in positioning their mouse accurately for precise shots.

![image](https://github.com/JustOscarJ1/valorant_lineup_calculator/assets/30467017/f4b7739f-4a3d-4471-accb-b471f7e16477)


## Features

- **Distance Input**: The tool allows users to input the desired distance for the projectile to be shot. It provides a graphical interface for users to enter the distance easily.

- **Angle Calculation**: Using predefined parabolic trajectory equations and constant parameters, the tool calculates the optimal angle for shooting the projectile to achieve the desired distance.

- **Mouse Guidance**: Once the angle is calculated, the tool guides the user in positioning their mouse accurately for the optimal shot. It displays real-time coordinate differences between the mouse position and the desired position, helping users adjust their aim effectively.

- **Settings Management**: The tool includes a settings manager that allows users to customize sensitivity, minimum inactive time for the mouse to be on top, and the allowed time to move the mouse to ping. Users can save and load settings for their preferences.

## Getting Started

### Prerequisites

- Python 3.x
- Libraries: `keyboard`, `pyautogui`, `pyttsx3`, `tkinter`, `customtkinter`, `PIL`

### Installation

1. Download the files and keep them in one folder together, keep images in a folder named "images"
2. Open command prompt, type `cd your_folder`
3. In the command prompt type `pip install -r requirements.txt` to download the required packages

## Usage

1. Launch the Valorant Lineup Tool by running the `main.py` script.

2. Main Menu:
   - **Current Settings**: Displays the current settings, including the selected ability, sensitivity, inactive time, and ping time.
   - **Set Settings**: Allows users to set new values for the sensitivity, inactive time, and ping time.
   - **Send Projectile**: Triggers the projectile shooting process. Users will be prompted to enter the desired distance, move the mouse to ping, and position the mouse accurately for the shot.

3. Shooting Process:
    - Enter the distance to the goal location in meters. Find this using an in-game ping.
    - Place your mouse directly on the ping.
    - Move your mouse to the top of the screen, then stop moving your mouse. Be careful not to sway too much doing this or move to the left or right when at the top of the screen, as it will cause issues.
    - Move your mouse as directed, trying to get the X and Y as close to 0 as possible.
    - Shoot the projectile.

## Customization

### Settings

To change settings press the "set settings" button in the main menu, then select the desired settings and press "save". These will be saved for future launches in `settings.txt`.

####Ability
You can change the ability you want the program to calculate for, to do this press the image of the desired ability in the settings menu. The text will appear bold to show the selection.
#### Valorant sensitivity
For the calculations to work properly, you need to input your Valorant sensitivity, do not enter DPI, EDPI or anything else, just the in-game sensitivity.
#### Minimum inactive time for mouse to be on top
The program has to detect when the mouse is on the top of the screen. It does this by checking how long the mouse has been inactive (not moving) for. You can change how much inactivity it waits for before it assumes the mouse is on the top of the screen.
#### Allowed time to move mouse to ping
When the program tells you to move the mouse to the ping, it starts a countdown. Once that countdown is complete it assumes you're looking at the ping. This setting is the length of that cooldown.

## Contributing

Contributions to the tool are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

The Valorant Lineup Tool is released under the [MIT License](LICENSE).

## Acknowledgments

All programming was done by me, thanks to feedback on Reddit and Intelligenti Pauca on stackoverflow for help with math.

## Contact

For any inquiries or feedback, please contact JustOscarJs:

- Discord: JustOscarJ
- GitHub: JustOscarJ1
- Reddit: FlamingJark

Feel free to reach out with any questions or suggestions related to the project.
