import numpy as np
import random
import matplotlib.pyplot as plt

# Grid and simulation parameters
grid_size = 10  # 10x10 grid for 100 agents
T = 100  # Maximum value for counter c
k = 0.1  # Constant between 0 and 1, easy to modify

# Initialize agents' state and counters
agents_state = np.zeros((grid_size, grid_size))  # 0: not flashing, 1: flashing
agents_counters = np.random.randint(0, T, (grid_size, grid_size))  # random initial c values


# Function to get the neighbors (north, south, east, west) of an agent
def get_neighbors(i, j):
    neighbors = []
    if i > 0:  # north
        neighbors.append((i - 1, j))
    if i < grid_size - 1:  # south
        neighbors.append((i + 1, j))
    if j > 0:  # west
        neighbors.append((i, j - 1))
    if j < grid_size - 1:  # east
        neighbors.append((i, j + 1))
    return neighbors


# Simulation step
def simulation_step():
    global agents_state, agents_counters

    # Create a copy of counters to update simultaneously
    new_counters = np.copy(agents_counters)
    new_state = np.copy(agents_state)

    for i in range(grid_size):
        for j in range(grid_size):
            # Increase the counter
            new_counters[i, j] += 1

            # Check if any neighbor flashed
            neighbors = get_neighbors(i, j)
            neighbor_flashed = any(agents_state[x, y] == 1 for x, y in neighbors)

            # Update the counter if a neighbor flashed
            if neighbor_flashed:
                new_counters[i, j] += k * new_counters[i, j]

            # Flash if the counter exceeds T
            if new_counters[i, j] >= T:
                new_state[i, j] = 1  # Flash
                new_counters[i, j] = 0  # Reset counter
            else:
                new_state[i, j] = 0  # Not flashing

    agents_counters = new_counters
    agents_state = new_state


# Run the simulation and visualize
def run_simulation(steps=100):
    flashing_counts = []
    for step in range(steps):
        simulation_step()
        # Count how many agents are flashing
        flashing_counts.append(np.sum(agents_state))
        # Optionally, display the grid
        plt.imshow(agents_state, cmap='Greys', interpolation='none')
        plt.title(f'Step: {step}, Flashing agents: {np.sum(agents_state)}')
        plt.pause(0.1)
    return flashing_counts


# Set up plotting
plt.ion()  # Turn on interactive mode

# Run for 100 steps and record how many agents are flashing
flashing_counts = run_simulation(steps=100)

# Plot the results after the simulation
plt.figure()
plt.plot(flashing_counts)
plt.title('Number of Flashing Agents Over Time')
plt.xlabel('Time Steps')
plt.ylabel('Flashing Agents')
plt.show()