
# Project1
# Screenshot Taker

A Python project that allows you to take screenshots on your device with ease. This tool captures your screen and saves the image in the desired location.

## Features

- Take screenshots of the full screen or a selected region.
- Save the screenshot in various formats (PNG, JPEG, etc.).
- Easy-to-use command-line interface.

## Prerequisites

Before running the project, make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

Additionally, you'll need to install the required dependencies:

- `Pillow` for image processing
- `pyautogui` for capturing screenshots

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/vijaychandra1910/project1.git
cd screenshot-taker
```

### Step 2: Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Project

To take a screenshot, simply run the script:

```bash
python screenshot_taker.py
```

You can specify additional arguments, such as the file name or format.

## Usage

### Full Screen Screenshot

To take a full-screen screenshot, use the default command:

```bash
python screenshot_taker.py
```

### Select a Region

You can take a screenshot of a selected region by using the following command:

```bash
python screenshot_taker.py --region
```

### Save to a Specific Location

To specify a save location or filename:

```bash
python screenshot_taker.py --save path/to/directory/filename.png
```

## File Formats

You can save your screenshot in various formats such as PNG or JPEG by specifying the file extension in the save path (e.g., `filename.png`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
