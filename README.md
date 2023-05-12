# CSCI 154 Project: Monty Hall

A Monte Carlo simulation is employed, consisting of 1000 iterations, to evaluate the best strategy for winning the Monty Hall problem under various conditions.
The simulation evaluates the performance of both the "stick" and "switch" strategies under two versions of the Monty Hall problem: 
* the original version where the host will only open a door that is neither the player’s selection or a winning door
* the variant version where the host will only open a non-player-selected door 
  * If the host opens the winning door, the game ends and is counted as a loss to the player.

## Result Diagrams
Host only opens a single door during each iteration of the program.

Original Monty Hall

![og_win_probs](https://github.com/EvanaHolevas/csci154-monty-hall/assets/70241021/28db29fa-dbfa-4386-b58c-b95c53b153c4)

Variant Monty Hall

![variant_win_probs](https://github.com/EvanaHolevas/csci154-monty-hall/assets/70241021/8291d2a2-79ed-4e2a-a5a0-ff88db48da93)
