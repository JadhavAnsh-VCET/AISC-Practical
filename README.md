# AI Practical Exam — Python Programs

This repository contains 16 standalone Python files matching the experiments in `Exp List_Practical Exam.pdf`.

## Setup

Python 3.10+ recommended.

Install dependencies:
```bash
pip install numpy matplotlib
```

Run an experiment:
```bash
python 01_Implement_Breadth_First_Search_BFS.py
```

Each Python file:
- asks for user input where applicable,
- prints results to the terminal,
- ends with comments showing sample input and expected output.

## Files

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. Greedy Best-First Search
4. A* Search
5. Single Layer Perceptron (SLP), AND gate using Delta Rule
6. Single Layer Perceptron (SLP), OR gate using Delta Rule
7. Compare learning rates for AND gate
8. Multi-Layer Perceptron with Backpropagation
9. Student Pass/Fail MLP
10. Loan Application Classification MLP
11. Email Spam Classification MLP
12. Kohonen Self-Organizing Map (SOM)
13. Hopfield Network using Hebbian Learning
14. Fuzzy Membership Functions — Washing Machine
15. Fuzzy Membership Functions — Room Temperature
16. Fuzzy Membership Functions — Traffic Density

## Notes

- Graph adjacency order affects which valid path DFS/BFS displays.
- A* may display a different optimal path when multiple paths have equal cost.
- Experiment 8 uses an XOR dataset as an example because the PDF says to assume suitable input data.
- Experiment 9's source PDF has a discrepancy: prose says attendance=1 and assignment=0, but the explicit test line says `X=(0,1)`. The program lets you enter the test features.
- Experiments 12–16 use suitable assumed data/ranges as permitted by the PDF.
