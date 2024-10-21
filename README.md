# Cellular Automaton Planter

This planter or vase is a 1D cellular automaton, fully parametric and intended for 3D printing. 

## The Cellular automaton and 256 rules

Each ring on the vase represents a generation of the automaton. 
Each cell can be active or inactive, and the state at the next generation is determine by the states of a given cell and its
two neighbours and the transition rule that you decide. These 3 cells can therefore be in one of 8 ($2^3$) states.

Representing inactive as 0, and active as 1, the states are: `000, 001, 010, 011, 100, 101, 110` and `111`.

For each state of 3 cells, you can decide on a rule to apply to determine the subsequent state of the given cell - e.g. state 110 produces state 0 or 1.

For example, consider the following transition behaviours:

```
input state -> output state
000 -> 0
001 -> 0
010 -> 0
011 -> 1
100 -> 1
101 -> 1
110 -> 1 
111 -> 0
```

This means you can encode the rules for each state as a binary string of length 8, e.g. `00011110`, which is 30 in base 10, so we consider this Rule 30.

Given there are 8 states, and 2 possible transition rules for each cell, there are 256 ($2^8$) different rules. You can explore these further at my demo [here](https://jsinkers.github.io/conway/rule.html).

You can think of the cellular automaton like a toy world with a law of physics which acts simply and locally, but produces complex behaviours at a large scale as the system evolves over time. Note that the rule applies globally, i.e. the same law of physics applies throughout the world. 

In different rules we can find:
- chaotic behaviour, i.e. a small deviations in the initial state produces rapid divergence in later states
- aperiodic behaviour, i.e. the pattern observed never repeats
- oscillations
- steady states

## Prerequisites to use the parametric model

- FreeCAD
- Install the Curves Workbench using the Addon manager

## Generating a model

- The script is written in Python to run in FreeCAD. Note that it takes ~ 1 hr to run at the current settings
- Adjust parameters at the top of the script. You will have to modify the export path for it to export correctly.
- Use the `Macro -> Macros` dialog to point to the script and then execute it 

## Deprecated OpenSCAD script

- I've also included an OpenSCAD script and python code to generate the CA but 
