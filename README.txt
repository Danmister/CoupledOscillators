Coupled Oscillators Simulation

This project implements a Python simulation based on the Mirollo & Strogatz (1990) model of pulse-coupled biological oscillators.
The simulation shows agents (oscillators) flashing in a grid, and the system synchronizes over time.
A GIF is created showing the flashes over time, along with a graph of how many agents are flashing in each step.

Getting Started

Prerequisites
To run this code, you need the following dependencies installed (see requirements.txt):

- Python 3.x: Make sure you have Python 3.6 or higher.
- NumPy: To handle numerical operations.
- Matplotlib: For visualizing the grid and the results.
- Imageio: For creating and saving GIFs.

Installing Dependencies
You can install the required dependencies using pip. Run the following command to install them:

pip install numpy matplotlib imageio

Running the Simulation
1. Clone or download this repository.
2. Navigate to the folder where the simulation.py file is located.
3. Run the Python script by executing:

python oscillators.py

By default the simulation will run for what is 100 steps and the best k value found

You can override the default values by passing new values, for example:
run_simulation(steps=200, k=0.5)

Parameters You Can Change
- Grid Size: Modify the variable grid_size in the code to change the size of the grid. The default value is a 10x10 grid.
- T (Maximum Counter): This value determines the threshold when an agent flashes. It is set to 100 by default.
- k: This constant affects how strongly agents are influenced by their neighbors. It is set to 0.1 by default, but you
    can adjust it to any value between 0 and 1.

The directory structure for the results will be created automatically.

Output Data
After running the simulation, the following files will be created:

- A GIF showing the flashing agents over time.
- A Graph showing the number of flashing agents as a function of time steps.

These files will be saved inside the runs/ directory, organized by subfolders named after the value of k. For example,
if k = 0.1, the results will be saved inside the runs/k_0.1 folder.

Example Output Directory Structure
If you run the simulation with k = 0.1, you will find the output in the following directory:

runs/
  └── k_0.1/
      ├── flashing_agents.gif
      └── flashing_agents_graph.png

- flashing_agents.gif: This is a GIF showing the simulation's visual representation of the flashing agents over time.
- flashing_agents_graph.png: This graph shows the number of agents flashing at each time step throughout the simulation.

Modifying the Code
To modify parameters like the number of steps, the value of k, or the grid size, edit the oscillators.py file.
\You can find these parameters at the top of the file and adjust them to your needs.

Additional Notes:

•	Make sure to run the script in a directory where you have write permissions,
    as the script will create folders to store the output.
•	If you want to experiment with different values of k, simply change the k variable in the # Grid and simulation
    parameters section on top of the file, and a new folder for that specific value of k will be generated.
