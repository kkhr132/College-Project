# Basic Feedforward Neural Network with PyTorch

This project implements a basic feedforward neural network using PyTorch and trains it on a simple dataset.

## Description

The network consists of:
- Input layer with 20 features
- Hidden layer with 64 neurons (ReLU activation)
- Hidden layer with 32 neurons (ReLU activation)
- Output layer with 1 neuron (Sigmoid activation for binary classification)

The model is trained on a generated dataset and evaluated on a test set.

## Files

- `main.py`: Contains the neural network implementation and training code.
- `requirements.txt`: Lists the required dependencies.

## Dependencies

- torch
- scikit-learn
- numpy

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Navigate to the project directory: `cd 06_nn_pytorch`
3. Run the script: `python main.py`

## Output

The program will train the model and print the test accuracy, along with predictions for the first 5 test samples.
