import random
import matplotlib.pyplot as plt

random.seed(42)

def setup_doors(num_doors):
    # Generate a list of doors, initially with all goats
    doors = ['goat'] * num_doors
    
    # generate a random prize door and assign it to the car
    prize_door = random.randint(0, num_doors - 1)
    doors[prize_door] = 'car'
    return doors

# Define a function to simulate the Monty Hall problem
def monty_hall(num_doors, switch_door):
    doors = setup_doors(num_doors)
    
    # Make initial door selection
    initial_selection = random.randint(0, num_doors - 1)
        
    # Host opens a goat door
    revealed_door = None
    for i in range(num_doors):
        if i != initial_selection and doors[i] == 'goat':
            revealed_door = i
            break
    
    # Player either sticks with initial door or switches
    final_selection = initial_selection
    if switch_door:
        for i in range(num_doors):
            if i != initial_selection and i != revealed_door:
                final_selection = i
                break
    
    # Determine if player won or not
    if doors[final_selection] == 'car':
        return 1
    else:
        return 0


# Monty Hall with host opening a random door
def monty_hall_variant(num_doors, switch_door):
    doors = setup_doors(num_doors)
    
    # Make initial door selection
    initial_selection = random.randint(0, num_doors - 1)
    
    # Host accidentally opens another door
    revealed_door = None
    while True:
        revealed_door = random.randint(0, num_doors - 1)
        if revealed_door != initial_selection:
            break
    result = None
    if doors[revealed_door] == 'car':
        result = 0
    else:
        # Player either sticks with initial door or switches
        final_selection = initial_selection
        
        if switch_door:
            for i in range(num_doors):
                if i != initial_selection and i != revealed_door:
                    final_selection = i
                    break
        
        # Determine if player won or not
        if doors[final_selection] == 'car':
            result = 1
        else:
            result = 0
    return result


# Define a function to run Monte Carlo simulations and calculate the probability of winning
def run_monte_carlo(num_doors, num_iterations, switch_door, variant):
    total_wins = 0
    
    for _ in range(num_iterations):
        if variant:
            total_wins += monty_hall_variant(num_doors, switch_door)
        else:
            total_wins += monty_hall(num_doors, switch_door)
    
    print("total wins: ", total_wins)
    
    win_prob = float(total_wins) / num_iterations
    return win_prob

# Define a function to plot the win probabilities for a range of numbers of doors
def plot_win_probabilities(num_doors_list, num_iterations, variant):
    switch_probs = []
    stick_probs = []
    for num_doors in num_doors_list:
        # Run simulations for the specified number of doors
            print('Running simulations for {} doors with switching policy...'.format(num_doors))
            
    # With switching policy
    switch_prob = run_monte_carlo(num_doors, num_iterations, True, variant)
    switch_probs.append(switch_prob)
    
    # With sticking policy
    print('Running simulations for {} doors with sticking policy...'.format(num_doors))
    stick_prob = run_monte_carlo(num_doors, num_iterations, False, variant)
    stick_probs.append(stick_prob)



num_iterations = 1000

# standard Monty Hall  with switch and stick policy
print('=================Standard Monty Hall=================')
switch_probs = []
stick_probs = []
for num_doors in [3, 6, 9, 20, 100]:
    # Run simulations for the original Monty Hall problem
    
    # With switching policy
    print('+-----------------Switching----------------+')
    print("Number of doors:", num_doors)
    print("Switch door:", True)
    win_prob_switch = run_monte_carlo(num_doors, num_iterations, True, False)
    switch_probs.append(win_prob_switch)
    print("Win probability with switch policy: {:.4f}".format(win_prob_switch))
    
    # With sticking policy
    print('+-----------------Sticking----------------+')
    print("Number of doors:", num_doors)
    print("Switch door:", False)
    win_prob_stick = run_monte_carlo(num_doors, num_iterations, False, False)
    stick_probs.append(win_prob_stick)
    print("Win probability with stick policy: {:.4f}".format(win_prob_stick))

print('\n=================Variant=================')
variant_switch_probs = []
variant_stick_probs = []
for num_doors in [3, 6, 9, 20, 100]:
    # Run simulations for the variant Monty Hall
    
    # With switching policy
    print('+-----------------Switching----------------+')
    print("Number of doors:", num_doors)
    print("Switch door:", True)
    win_prob_switch = run_monte_carlo(num_doors, num_iterations, True, True)
    variant_switch_probs.append(win_prob_switch)
    print("Win probability with switch policy: {:.4f}".format(win_prob_switch))
    
    # With sticking policy
    print('+-----------------Sticking----------------+')
    print("Number of doors:", num_doors)
    print("Switch door:", False)
    win_prob_stick = run_monte_carlo(num_doors, num_iterations, False, True)
    variant_stick_probs.append(win_prob_stick)
    print("Win probability with stick policy: {:.4f}".format(win_prob_stick))
    
import matplotlib.pyplot as plt

num_doors_list = [3, 6, 9, 20, 100]

def plot_monte_carlo_results(num_doors_list, switch_probs, stick_probs, variant_switch_probs, variant_stick_probs):
    plt.plot(num_doors_list, switch_probs, label='Switching (Original)')
    plt.plot(num_doors_list, stick_probs, label='Sticking (Original)')
    plt.plot(num_doors_list, variant_switch_probs, label='Switching (Variant)')
    plt.plot(num_doors_list, variant_stick_probs, label='Sticking (Variant)')
    plt.xlabel('Number of doors')
    plt.ylabel('Probability of winning')
    plt.title('Monty Hall Problem')
    plt.legend()
    plt.show()

# plot_monte_carlo_results(num_doors_list, switch_probs, stick_probs, variant_switch_probs, variant_stick_probs)

import numpy as np

def plot_results(num_doors_list, switch_probs, stick_probs, variant):
    # Set width of bar
    bar_width = 0.35
    
    # Set x-axis values
    x = np.arange(len(num_doors_list))
    
    # Create figure and axis objects
    fig, ax = plt.subplots()
    
    # Plot the data
    rects1 = ax.bar(x - bar_width/2, switch_probs, bar_width, label='Switch', color=(0.2, 0.4, 0.6, 1))
    rects2 = ax.bar(x + bar_width/2, stick_probs, bar_width, label='Stick', color=(0.8, 0.4, 0.0, 1))
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Win Probability')
    ax.set_xlabel('Number of Doors')
    ax.set_title('Monty Hall Simulation Results ({})'.format('Variant' if variant else 'Original'))
    ax.set_xticks(x)
    ax.set_xticklabels(num_doors_list)
    ax.legend()
    
    # Add labels on top of the bars
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{:.3f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    # Show the plot
    plt.show()
    
plot_results(num_doors_list, variant_switch_probs, variant_stick_probs, True)