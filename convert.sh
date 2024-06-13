#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install necessary packages
# pip install pandas beautifulsoup4

# Run the Python script
python3 convertor.py

# Deactivate the virtual environment
deactivate
