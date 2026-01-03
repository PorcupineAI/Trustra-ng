#!/bin/bash
set -e

echo "Setting up Python environment..."
python --version

echo "Installing dependencies..."
pip install --upgrade pip
pip install wheel setuptools

# Install requirements with --no-build-isolation
pip install --no-build-isolation -r requirements.txt

echo "Build completed successfully!"
