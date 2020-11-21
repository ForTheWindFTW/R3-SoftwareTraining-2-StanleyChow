# R3 Software Training 2
## Maze Generation, TCP Commands
### Stanley Chow

## Progess
- [x] Milestone 1: create a random maze generator
![Image of a 10 by 10 maze in 400x600 pixels](/images/generated_maze1.png)
10 by 10 maze in 400x600 pixels
![Image of a 20 by 20 maze in 800x600 pixels](/images/generated_maze2.png)
20 by 20 maze in 800x600 pixels
- [ ] Milestone 2: transmit PWM commands over TCP to traverse a maze

## Milestone 1
### Objective
Using the pygame library, develop a random maze generator algorithm which is able to create mazes of variable size.

### Requirements
- Create and draw a random maze given a n by n grid
- Use the base pygame code found [here](/snippets/base_pygame_code.py) as the basis for my code
- The grid width and height should **not** be hardcoded
- A good resource for maze generation algorithms can be found
[here](http://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap)

### Steps
- Installed and added the [pygame](https://www.pygame.org/docs/) library to the python interpreter
- From the [base pygame code](/snippets/base_pygame_code.py) provided, I made a function to draw each edge of a grid
- Researched on maze generation algorithms and used a
[variation](https://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm) of Prim's algorithm in
[scmaze.py](/scmaze.py)

### How it Works
- The pre-set values WIDTH and HEIGHT are the respective dimensions of the window which pygame uses.
- After the initialization, the window generates an initial maze that is displayed and enters the main control loop.
This loop handles actions on the window, with the only action currently implemented is left click (mouse1). Left
clicking will randomly generate a new maze of the same dimensions.
- To create a maze, `scmaze.gen_prim_maze' is called, returning a graph where the edges are where there is no wall.
- Those walls are excluded from rendering the lines while iterating through all of the edges

## Milestone 2
### Objective
Using the Python Socket library, create a program which takes in the array of the solution path and sends a stream of
strings. These strings will go to the Arduino, similar to training #1 and contain commands which will explain how the
motors should move.

### Requirements
- A send and receive program using TCP
- Use the TCP stream to send commands for the solution path to solve a maze
- Assume that each step will take 1 second
- Send `[0][0][0][0]` to stop the motors (in general, use strings with format `[M1_A][M1_B][M2_A][M2_B]`)
- The path solution code will be <span style="text-decoration: underline;">provided</span>, so **only the TCP stream**
**needs to be programmed**.
- Also create a program that recieves the TCP packet and prints it out (to test if it works) 

### Steps
- WIP

### How it Works
- WIP

## Reflection
So far, this second software training module has allowed me to utilize my previous experience. I have previously used
JavaFX and Swing, which allows me to feel much more comfortable with the gui drawing in the pygame library. Installing
the pygame module was a bit confusing, as simply downloading with pip was not enough for it to work, but I found a
solution after some online searching. I did not face many other difficulties, as I have also had previous experience
with some graph theory algorithms, understanding how to modify Prim's Algorithm was not very difficult for me. However,
for the second milestone, I will likely experience many more obstacles and difficulties, since I have not been able to
grasp the concepts of networking, sockets, and packet communication.

