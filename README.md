Collatz Conjecture Visualizer
This Python program explores the Collatz Conjecture, a mathematical sequence that starts with any integer 
𝑛
n. The conjecture follows these rules:

If 
𝑛
n is even, divide it by 2.
If 
𝑛
n is odd, multiply it by 3 and add 1.
Repeat the process until 
𝑛
n reaches 1 or falls into a cycle.
The program provides a visualization of the sequence, detects cycles, and displays key statistics about the sequence.

Features
Input Handling: Accepts any integer (positive or negative) as input.
Cycle Detection: Identifies when the sequence falls into a cycle and specifies:
The step at which the cycle begins.
The number that initiates the cycle.
Statistics:
Total steps taken in the sequence.
The highest and lowest numbers reached.
Sequence Visualization:
Displays the sequence progression on a linear scale using matplotlib.
Detailed Output: Prints each step of the sequence, showing the numbers involved and where cycles occur.
Requirements
Python 3.x
Matplotlib library (pip install matplotlib)
How to Use
Clone or download this repository to your local machine.
Run the collatz_conjecture.py file:
bash
Copy code
python collatz_conjecture.py
Enter any integer when prompted:
Example: 6
The program will:
Calculate the sequence.
Detect cycles and print information.
Display a plot of the sequence.
