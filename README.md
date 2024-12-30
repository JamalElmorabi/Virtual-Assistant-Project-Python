# Virtual Assistant Project

## Description

The Virtual Assistant project is a Python-based desktop application that interacts with users via speech and text. It can respond to user queries, provide weather updates, open websites like Spotify, YouTube, and Google, and perform text-to-speech and speech-to-text tasks. The assistant is built using Python libraries and features a graphical interface created with `tkinter`.

---

## Features

- Voice and text interaction.
- Retrieves current weather information using Google search.
- Opens popular websites such as Spotify, YouTube, and Google.
- Displays the current time.
- Graphical User Interface (GUI) built with `tkinter`.
- Supports text-to-speech for responses.

---

## Installation Instructions

### Prerequisites

- Python 3.8 or higher installed on your system.
- A working microphone for voice input functionality.

### Step 1: Clone the Repository

```bash
git clone https://github.com/JamalElmorabi/Virtual-Assistant-Project-Python.git
cd Virtual-Assistant-Project-Python
```

### Step 2: Install Required Dependencies

Run the following command to install all required Python packages:

```bash
pip install requests-html SpeechRecognition pyttsx3 Pillow
```

### Step 3: Ensure Additional Libraries Are Installed

Check if your Python installation includes `tkinter`. If not, install it based on your operating system:

- For Linux:
  ```bash
  sudo apt-get install python3-tk
  ```
- For Windows and macOS, `tkinter` is typically included with Python.

---

## How to Run the Project

1. Ensure you are in the project directory.
2. Run the main application file using:
   ```bash
   python Virtual Assistant.py
   ```

---

## Dependencies

Here’s the full list of libraries used in the project, along with installation commands:

1. **`requests-html`**  
   For web scraping to fetch weather information.  
   ```bash
   pip install requests-html
   ```

2. **`SpeechRecognition`**  
   For speech-to-text functionality.  
   ```bash
   pip install SpeechRecognition
   ```

3. **`pyttsx3`**  
   For text-to-speech functionality.  
   ```bash
   pip install pyttsx3
   ```

4. **`Pillow`**  
   To handle images in the GUI.  
   ```bash
   pip install Pillow
   ```

### Additional Standard Libraries

These libraries are included in Python’s standard library and require no installation:
- `tkinter` – Used for the graphical interface.
- `webbrowser` – For opening websites.
- `datetime` – For fetching the current time.
- `os` and `sys` – For resource management and system path handling.
