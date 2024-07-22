# Research Work

## Overview

This repository contains the source code and resources related to the research on 2D Euclidean Traveling Salesman Problem optimization techniques. The primary focus is on implementing and comparing different heuristic and approximation algorithms to solve the TSP.

## File Descriptions

- `Generate_Input.py`: This script reads TSP coordinates from a file and creates a distance matrix.
- `Random_Tour.py`: Contains a function to generate a random tour of the given nodes.
- `Construct_Tour.py`: Implements the construction of an initial tour using a Double Tree Shortcut algorithm.
- `Tour_Optimization.py`: Provides a function to optimize a given tour using the 2-opt algorithm.
- `Main.py`: The main script includes generating initial tours, optimizing them, and compare the results with known solutions.

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/Himanshu-0502/Research-Work.git
    cd Research-Work
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the main script:
   ```sh
   python Main.py
   ```

## Acknowledgements

We would like to thank everyone who supported and contributed to this research project. Your guidance, resources, and encouragement have been invaluable.