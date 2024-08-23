# 3D-Hausdorff-Distance-Calculator

## Description
`3D-Hausdorff-Distance-Calculator` is a Python tool designed to calculate the Hausdorff distance between two 3D models provided in STL format. The Hausdorff distance is a measure of the maximum discrepancy between two sets of points, making it useful for comparing 3D shapes, particularly when evaluating the fidelity of 3D printed objects to their original designs.

## Features
- Load and process STL files to extract 3D mesh data.
- Calculate the Hausdorff distance between two 3D models.
- Useful for quality control in 3D printing, scanning, and reverse engineering.

## Requirements
- Python 3.7+
- numpy
- scipy
- numpy-stl

You can install the required packages using `pip`:

```bash
pip install numpy scipy numpy-stl
```

## Setting Up the Environment with Anaconda (miniforge for macOS)
For macOS users, it is recommended to use miniforge to create a clean Anaconda environment for running the script. Follow these steps to set up the environment:

1. Install Miniforge: follow the instructions on the [Miniforge GitHub page](https://github.com/conda-forge/miniforge)

2. Create a new conda environment:
Create a New Conda Environment:
```bash
conda create -n hausdorff-env python=3.9
```

3. Activate the new environment:
```bash
conda activate hausdorff-env
```

4. Install the required packages:
```bash
pip install numpy scipy numpy-stl
```


## Usage
1. Place your STL files in the same directory as the script.
2. Run the Python script to calculate the Hausdorff distance:

```bash
python main.py
```

## Sample STL Files
You can use the provided sample STL files to test the script. The `cube.stl` and `sphere_[mesh_size].stl` files contain two simple 3D models for testing the Hausdorff distance calculation.
