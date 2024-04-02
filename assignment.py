import matplotlib.pyplot as plt
import numpy as np

# Define the functions to solve the problems
def f1(x):
    return x**2 + 7*x + 2

def f2(x):
    return 3*x + 2

def f3(x):
    return x**2

def f4(x):
    return x**3

def f5(x):
    return x**5

def f6(x):
    return x**3 + 2*x**2 + x + 10

def f7(x):
    return x**4 - 3*x**3 + 2*x**2 - x + 11

def f8(x):
    return np.sin(x)

def f9(x):
    return np.cos(x)

def f10(x):
    return x**5 + 4*x**4 + x**3 - 2*x**2 + 100

# Define the function to solve the problems
def solve(problem_func, x_range):
    return [problem_func(x) for x in x_range]

# Define the function to plot all problems
def plot_all_problems():
    x = np.linspace(1, 50, 50)
    for i in range(1, 11):
        plt.plot(x, eval(f"f{i}")(x), label=f'Problem {i}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Graph of All Problems')
    plt.legend()
    plt.show()

    # Write the solutions to the text file
    with open('solution.txt', 'w', encoding='utf-8') as f:
        for i, problem in enumerate(problems):
            f.write("Problem {:<3}: {}\nSolutions: {}\n".format(i + 1, problem, str(solutions[i])))

# Read the problems from the text file
problems = []
with open("probs.txt", "rb") as f:
    for line in f:
        problems.append(line.decode("utf-8").strip())

# Solve the problems
solutions = []
for problem in problems:
    if "Sin" in problem:
        solutions.append(solve(f8, range(1, 51)))
    elif "Cos" in problem:
        solutions.append(solve(f9, range(1, 51)))
    else:
        problem_func = eval(f"f{problems.index(problem)+1}")
        solutions.append(solve(problem_func, range(1, 51)))

# Display options for the user to choose which problem to plot
print("Choose an option:")
print("1. Plot all graphs")
print("2. Plot a specific problem")

choice = int(input("Enter your choice: "))

if choice == 1:
    # Plot all problems and write solutions to the text file
    plot_all_problems()
elif choice == 2:
    print("Choose a problem to display:")
    for i, problem in enumerate(problems):
        print(f"{i+1}. {problem}")

    # Ask the user for the problem number to display
    problem_num = int(input("Enter the problem number to display: "))

    # Plot the chosen problem
    x = np.linspace(1, 50, 50)
    plt.plot(x, eval(f"f{problem_num}")(x))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Graph of {problems[problem_num - 1]}')
    plt.show()

    # Write the solution to the text file
    with open('solution.txt', 'w', encoding='utf-8') as f:
        f.write("Problem {:<3}: {}\nSolutions: {}\n".format(problem_num, problems[problem_num - 1], str(solutions[problem_num - 1])))
