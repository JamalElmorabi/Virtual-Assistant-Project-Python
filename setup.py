from cx_Freeze import setup, Executable
import sys
import os

image_folder = os.path.join(os.getcwd(), 'image')

include_files = [
    image_folder
]

script_name = 'Virtual Assistant.py'

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [Executable(script_name, base=base)]

setup(
    name="Virtual Assistant",
    version="1.0",
    description="A virtual assistant project",
    options={
        'build_exe': {
            'include_files': include_files,
            'packages': ['requests', 'pyttsx3', 'speech_recognition', 'PIL', 'datetime', 'webbrowser'],  # Add your dependencies here
        }
    },
    executables=executables
)
