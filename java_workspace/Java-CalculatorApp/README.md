# Simple Interactive Calculator

## Description
This is a robust, console-based Java application that performs basic arithmetic operations. The program is designed with an infinite loop to allow continuous calculations and includes error handling for invalid inputs and mathematical impossibilities.

## Features
* **Continuous Calculation:** Keeps the current result in memory and allows further operations until the user chooses to exit.
* **Basic Arithmetic:** Supports Addition (+), Subtraction (-), Multiplication (*), and Division (/).
* **Zero Division Protection:** Uses a `continue` flow control to prevent the program from crashing or producing `Infinity` results when dividing by zero.
* **Smart Exit:** Program structure ensures that selecting 'Exit' terminates the application immediately without asking for further numerical input.
* **Input Validation:** Includes a defensive `else` block to handle invalid operation selections.

## How to Use
1. **Initial Input:** Enter the first number to start the calculation.
2. **Select Operation:** Choose from the menu (1-4 for math, 0 to exit).
3. **Continuous Math:** Enter the next number. The program will display the updated "Current result" and prompt for the next operation.
4. **Exit:** Enter `0` at the operation selection screen to close the application.

## Prerequisites
* Java Development Kit (JDK) installed.
* Any Java IDE (IntelliJ IDEA, Eclipse, NetBeans) or a Terminal.

## Usage Example
```text
---CALCULATOR APP---
Number: 10
Operations: 
1-) +
2-) -
3-) *
4-) /
0-) Exit
Select Operation: 1
Number: 5
Current result is: 15.0
