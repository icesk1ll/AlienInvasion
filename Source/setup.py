from cx_Freeze import setup, Executable

setup(
    name = "Alien_Invasion",
    version = "1.0",
    description = "Game",
    executables = [Executable("alien_invasion.py")]
)