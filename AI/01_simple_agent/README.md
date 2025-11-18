# Simple Intelligent Agent

This project implements a simple intelligent agent that interacts with a simulated environment, demonstrating rational behavior.

## Description

The agent operates in a 5x5 grid environment where some cells are dirty. The agent perceives the state of its current cell and acts accordingly:
- If the cell is dirty, it cleans it.
- If the cell is clean, it moves to a random adjacent cell.

The agent continues until the environment is clean or a maximum number of steps (100) is reached.

## Files

- `main.py`: Contains the Environment and SimpleAgent classes, and the main execution logic.

## How to Run

1. Ensure Python is installed.
2. Navigate to the project directory: `cd 01_simple_agent`
3. Run the script: `python main.py`

## Output

The program will print the agent's actions (moving or cleaning) and indicate if the environment is fully cleaned or if max steps were reached.
