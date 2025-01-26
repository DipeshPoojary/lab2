name: My First Github Action
on: [push]

jobs:
  build:
    runs-on:ubuntu-latest

  strategy:
    matrix:
      python-version: [3.8, 3.9]

  steps:
  - uses: actions/checkout@v3
  - name: setup Python
  - uses: actions/setup-python@v2
   with:
      python-version: ${{matrix: python-version}}

  - uses: Install Dependencies
  run: |
      python -m pip install --upgrade pip
      pip install pytest

  - uses: Run tests
  run: |
    cd src
    python -m pytest addition.py
      
