# README – README Generator (Streamlit)

## Overview
A simple Streamlit app that helps you generate clean, consistent `README.md` files for your projects. Fill in a short form, preview the output, and download the Markdown in one click.

## Features
- Guided form for key README sections (Title, Description, Installation, Features, Licence, Tech Stack).
- Live Preview of the Markdown output.
- One-click download of the generated `README.md`.
- Lightweight single-file Streamlit application.

## Demo (How It Works)
1. Launch the app with Streamlit.
2. Complete the fields under **Project Details**.
3. Press **Generate README** to render the Markdown.
4. Use **Download README.MD** to save your file, or copy from the code preview.

## Tech Stack

### Languages & Frameworks
- **Python 3.9+**
- **Streamlit** – For creating the interactive web interface.

## Installation

### Prerequisites
- Python 3.9+ (recommended)

### Setup
```bash
# 1) Create and activate a virtual environment (optional but recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt
```

## Running the App
```bash
streamlit run readme_generator.py
```
Then open the local URL displayed in your terminal (usually `http://localhost:8501`).

## Project Structure
```text
.
├── readme_generator.py   # Streamlit app (README generator)
├── requirements.txt  # Requirements (includes Streamlit pin)
└── README.md                                  # (You are here)
```

## Usage Notes
- Required fields: The app validates that all fields are filled before generating the README.
- Output format: The generated Markdown includes the sections you provide and uses your exact text (no auto-reformatting).

## Known Issues / Fixes
- Minor typos in variable names: The form stores licence text in a variable named `lisense`. Functionality works, but consider renaming this to `license` throughout for clarity.
- String split over lines: If you encounter a syntax error at the `st.subheader("Project Details")` line, ensure the full string literal is on one line (no stray newline between the opening quote and text).

## Acknowledgements
- Built with [Streamlit].
- Thanks to the open-source community for inspiration on lightweight documentation tools.
