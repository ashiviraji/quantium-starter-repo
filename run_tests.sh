#!/bin/bash

echo "Activating virtual environment..."

source venv/Scripts/activate

echo "Running Dash application tests..."

python -m pytest

RESULT=$?

if [ $RESULT -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed."
    exit 1
fi