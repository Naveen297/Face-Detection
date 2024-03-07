
# Face Detection Project

This face detection project utilizes OpenCV to detect faces in real-time using your laptop's webcam. When a face is detected, you can press the 'c' key to capture and save the image to a directory.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x installed on your Windows machine
- Pip (Python package installer), which comes with Python 3.4 and above

### Setting Up Your Virtual Environment

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.

#### Step 1: Install virtualenv

Open your command prompt (CMD) and install `virtualenv` using pip.

```
pip install virtualenv
```

#### Step 2: Creating a Virtual Environment

Navigate to your project's directory from the command prompt and run the following command to create a virtual environment named 'venv' for the project.

```
python -m venv venv
```

#### Step 3: Activating the Virtual Environment

Before you can start installing or using packages in your virtual environment, you'll need to activate it. To activate the virtual environment on Windows, run:

```
venv\Scripts\activate
```

You should see `(venv)` appears at the beginning of the command line prompt, indicating that you are now working within the virtual environment.

### Installing Dependencies

With your virtual environment active, install the required package (OpenCV) using pip:

```
pip install opencv-python
```

### Running the Face Detection Script

With the virtual environment set up and dependencies installed, you are ready to run the face detection script.

1. Ensure your script `LiveDetection.py` is in the project directory.
2. Run the script using Python:

```
python LiveDetection.py
```

### Using the Face Detection Script

- The webcam will activate, and the program will start detecting faces in real-time.
- Press 'c' to capture and save an image when a face is detected.
- Press 'q' to quit the program.

## Built With

* [OpenCV](https://opencv.org/) - The Open Source Computer Vision Library used for face detection
