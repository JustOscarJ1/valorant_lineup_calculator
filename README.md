
<a href="https://www.buymeacoffee.com/flamingjark" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

**Support and updates Discord: https://discord.gg/83WdsEnXac**
**Due to too many support requests and unknowing users the source code is temporarily hidden, PLEASE use the EXE if you want to try the program**

# Valorant Lineup Tool

Valorant Lineup Tool is a Python-based application that assists players in shooting projectiles with parabolic trajectories in the game Valorant. The tool provides a user-friendly interface for inputting desired distances, calculates the optimal angles for shooting projectiles, and guides players in positioning their mouse accurately for precise shots.

![image](https://github.com/JustOscarJ1/valorant_lineup_calculator/assets/30467017/f4b7739f-4a3d-4471-accb-b471f7e16477)


## Features

- **Distance Input**: The tool allows users to input the desired distance for the projectile to be shot. It provides a graphical interface for users to enter the distance easily.

- **Angle Calculation**: Using predefined parabolic trajectory equations and constant parameters, the tool calculates the optimal angle for shooting the projectile to achieve the desired distance.

- **Mouse Guidance**: Once the angle is calculated, the tool guides the user in positioning their mouse accurately for the optimal shot. It displays real-time coordinate differences between the mouse position and the desired position, helping users adjust their aim effectively.

- **Settings Management**: The tool includes a settings manager that allows users to customize sensitivity, minimum inactive time for the mouse to be on top, and the allowed time to move the mouse to ping. Users can save and load settings for their preferences.

## Getting Started
### Basic Installation (reccomended)
- Navigate to https://github.com/JustOscarJ1/valorant_lineup_calculator/releases and download the latest release.
- Unzip the file in any location
- Run the provided "Valorant Lineups.exe"
---

### Python Installation (not recommended, source code currently removed)
 ### Prerequisites 
- Python 3.x
- Libraries: `keyboard`, `pyautogui`, `pyttsx3`, `tkinter`, `customtkinter`, `PIL`

### Installation
1. Download Python **with pip and add to path**, search a tutorial if you don't know how
2. Download the files and keep them in one folder together, keep images in a folder named "images"
3. Open command prompt, type `cd your_folder`
4. In the command prompt type `pip install -r requirements.txt` to download the required packages

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

To change settings press the "set settings" button in the main menu, then select the desired settings and press "save". These will be saved for future launches in `settings.txt`. You can also change settings directly in the `settings.txt` file.

#### Ability
You can change the ability you want the program to calculate for, to do this press the image of the desired ability in the settings menu. The text will appear bold to show the selection.
#### Valorant sensitivity
For the calculations to work properly, you need to input your Valorant sensitivity, do not enter DPI, EDPI or anything else, just the in-game sensitivity.
#### Minimum inactive time for mouse to be on top
The program has to detect when the mouse is on the top of the screen. It does this by checking how long the mouse has been inactive (not moving) for. You can change how much inactivity it waits for before it assumes the mouse is on the top of the screen.
#### Allowed time to move mouse to ping
When the program tells you to move the mouse to the ping, it starts a countdown. Once that countdown is complete it assumes you're looking at the ping. This setting is the length of that cooldown.
#### Beep or TTS
The program will instruct you on what to do in the shooting process with a TTS voice, if this is too distracting or takes too long for your liking, you can change the TTS to beeps with this setting.

## Is this bannable?

This program is **not** bannable. According to the [Riot TOS](https://www.riotgames.com/en/terms-of-service):

> The following are examples of behaviour that warrant disciplinary measures:
> 
> Using any unauthorized third party programs, including mods, hacks, cheats, scripts, bots, trainers and automation programs that interact with the Riot Services in any way, for any purpose, including any unauthorized third party programs that intercept, emulate, or redirect any communication relating to the Riot Services and any unauthorized third party programs that collect info about the Riot Services by reading areas of memory used by the Riot Services to store info;

This program does not intercept, emulate or redirect any communication to any Riot services. It does not read any memory or collect any information used by Riot services. Whilst this does give an in-game advantage, the way it is made makes it not bananble according to Riots TOS. There are other very popular applications which may not be as direct in their methods, but have the same end-goal, like Valorant Tracker.

## Contributing

Contributions to the code are currently closed, however if you have any ideas, issues or suggestions please open an issue.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

## Acknowledgments

All programming was done by me, thanks to feedback on Reddit and Intelligenti Pauca on stackoverflow for help with math.

## Contact

For any inquiries or feedback, please contact JustOscarJs:

- Discord: JustOscarJ
- Support Discord Server: https://discord.gg/83WdsEnXac
- GitHub: JustOscarJ1
- Reddit: FlamingJark

Feel free to reach out with any questions or suggestions related to the project.
