## URBAN 5123 Programming Tools for Urban Analytics
## Spring 2021
## Lab03-2: Conditional Execution

### Instructions

This exercise will extend the Monte Carlo simulation of the value of Pi from class in two ways.

1. Extend the Python [notebook] from class to prompt the user for two input values
   - The convergence criterion (i.e., percentage difference for stopping the loop)
   - A sentinel value that limits the number of draws to avoid a long running program. Once the number of draws reaches this value you should have the program stop and print a message that draw limit was exceeded and report the percentage difference between the current estimate of Pi and the true value.

2. In a second notebook write code does the following experiment
 
  - For different values of the convergence criteria [0.01, 0.001, 0.0001, 0.00001] generate 10 estimates of Pi.
  - For the four different convergence criteria have your script print the following statistics
    - average number of draws required from the 10 runs
    - standard deviation of the number of draws required from the 10 runs.

For this second program do not use a sentinel to cap the number of draws.

### Due

1. Create a branch called `Lab03` that contains your Jupyter Notebook.
2. Commit and push your Jupyter Notebook to your personal repository via git
3. Submit a pull request

[notebook]: https://github.com/qszhao/PTUA2021/blob/master/Lab03/simulate_pi.ipynb
