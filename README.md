# Valorant Lineup Tool

Valorant Lineup Tool is a Python-based application that assists players in shooting projectiles with parabolic trajectories in the game Valorant. The tool provides a user-friendly interface for inputting desired distances, calculates the optimal angles for shooting projectiles, and guides players in positioning their mouse accurately for precise shots.

![Valorant Lineup Tool](<Image of Valorant Lineup Tool>)

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

## Customization

### Settings

The tool allows users to customize sensitivity, minimum inactive time for the mouse to be on top, and the allowed time to move the mouse to ping. These settings can be modified through the "Set Settings" option in the main menu.

## Contributing

Contributions to the tool are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

The Valorant Lineup Tool is released under the [MIT License](LICENSE).

## Acknowledgments

All programming was done by me, thanks to feedback on Reddit and Intelligenti Pauca on stackoverflow for help with math.

## Contact

For any inquiries or feedback, please contact JustOscarJs:

- Discord: JustOscarJ1
- GitHub: JustOscarJ
- Reddit: FlamingJark

Feel free to reach out with any questions or suggestions related to the project.
