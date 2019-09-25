# Assignment 1 - Problem Solving Agents using Search Techniques

 **Problem State**					

| 9  | 24 | 3  | 5  | 17 |
| -- | -- | -- | -- | -- |
| 6  | 0  | 13 | 19 | 10 |
| 11 | 21 | 12 | 1  | 20 |
| 16 | 4  | 14 | 12 | 15 |
| 8  | 18 | 23 | 2  |  7 |

**Goal State**

| 1  | 2  | 3  | 4  | 5  |
| -- | -- | -- | -- | -- |
| 6  | 7  | 8  | 9  | 10 |
| 11 | 12 | 13 | 14 | 15 |
| 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | 24 | 0  |

- Implementing a agent to solve 24 puzzle problem using Search Techniques like below
  1. Breadth First Search
  2. Depth First Search
  3. Informed search algorithms using
      - h1(x) = number of misplaced tiles
      - h2(x) = sum of the distances of every tile to its goal position.
	  
- Hints:
1.	It is much better to model the problem of moving the blank around than moving movable tiles.
2.	Good data structure representation can make your life easy.
3.	You may want to start from the 8-puzzle problem.

### Files
------
Here we have 2 files who solve 2 types of puzzles
1. **sherlock.py** - solves 5x5 puzzles(24 puzzle) using the search techniques.
2. **watson.py** - solves 3x3 puzzles(8 puzzle) using the search techniques.

### Solution
------
To tackle the problem, we start with 8 puzzle problem and started implementing blind search techniques - breadth first search(bfs) and depth first search(dfs) and then we go through the greedy search algorithms where we have introduce heuristic search functions.

In the code we define a state for every problem statement, each state has below attributes.
1. state  - has location of all the tiles, including blank one
2. parent - parent of the current state
3. move   - from which move did we obtain the current state
4. depth  - depth of current state
5. cost   - cost of current state
6. key    - decided by the heuristic function

The state given above is defined for every valid state in statespace.


### Steps to execute
------
1. execute sherlock.py
2. prompts user to select any choice of algorithm as shown below.
3. enter the algorithm choice

![Algorithm Prompt](https://github.com/Heramb001/cs580-Artificial-Intelligence/tree/master/01/images/prompt1.PNG "Algorithm Prompt")

4. If choice is a greedy search or A star, program prompts for heuristic function as shown below, user can select one.
   else Code moves to step 5

![Heuristic Prompt](https://github.com/Heramb001/cs580-Artificial-Intelligence/tree/master/01/images/prompt2.png "Heuristic Prompt")

5. Prompts user to enter the puzzle elements.

![Puzzle Prompt](https://github.com/Heramb001/cs580-Artificial-Intelligence/tree/master/01/images/prompt3.png "Puzzle Prompt")

6. press enter code gets executed and an output file is generated.

![Output](https://github.com/Heramb001/cs580-Artificial-Intelligence/tree/master/01/images/output.png "Output")
### Conclusion
------
From the initiaal analysis done on the 3x3 we were able to solve all the valid statespaces to reach the goal state using bfs, dfs, A star, Greedy search. but when we implement the same code for 5x5 :  
- using bfs we were not able to solve all the problems because in worst case, we need to traverse all the combinations in each level and creating many such levels leads to utilize more memory (space complexity O(b^d))
- using dfs it runs forever as it has to reach the depth first(time complexity).
- using Informed searches we were able to solve the problem as we defined good heuristic function. we can see that in the given heuristic functions, 2nd heuristic function outperforms 1st as we can get the best solution in less time.
- we can see how defining a good heuristic function can help us solving the problem also saving time and space.










