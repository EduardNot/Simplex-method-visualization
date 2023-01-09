from tabulate import tabulate
import numpy as np

table_headers = ['x1', 'x_2', 'x_3', 'z_1', 'z_2', 'z_3', 'b']
inf = float('inf')


def to_tableau(c, A, b):
    Ab = [_A + [0] * len(A) + [_b] for _A, _b in zip(A, b)]
    for i in range(len(A)):
        Ab[i][i + len(A)] = 1
    z = c + [0] * (len(A) + 1)
    return Ab + [z]


def can_be_improved(tableau):
    *constraints, objective_function = tableau
    for i, val in enumerate(objective_function):
        if val > 0:
            for row in constraints:
                if row[i] > 0:
                    return True
    return False


def pivot_step(tableau):
    *constraints, objective_function = tableau
    pivot_col = np.argmax(objective_function[:3])
    ratios = [x[-1] / x[pivot_col] if x[pivot_col] else inf for x in constraints]
    pivot_row = np.argmin([inf if ratio <= 0 else ratio for ratio in ratios])

    # print('Ratios:', ratios)
    # print(f'Pivot col: {pivot_col}, pivot row: {pivot_row}\n')

    new_tableau = [[] for _ in tableau]
    new_tableau[pivot_row] = np.array(tableau[pivot_row]) / tableau[pivot_row][pivot_col]
    for i, row in enumerate(tableau):
        if i == pivot_row: continue
        multiplier = new_tableau[pivot_row] * row[pivot_col]
        new_tableau[i] = np.array(row) - multiplier
    return new_tableau


def print_solution(tableau, c, is_final=False):
    *constraints, objective_function = tableau
    optimal_value = objective_function[-1] * -1
    coefficients = [0] * len(c)
    columns = np.array(tableau).T[:len(c)]
    for i, col in enumerate(columns):
        if (col == 0).sum() == len(col[:-1]) and 1 in col[:-1]:
            coefficients[i] = tableau[col.tolist().index(1)][-1]
        elif col[-1] > 0 and all(col[:-1] <= 0) and is_final:
            print('This problem is unbounded')
            return
    print()
    if is_final:
        print(f'Optimal value for the objective functions is {optimal_value}')
        print('We have for this solution ', end='')
        for i, coefficient in enumerate(coefficients):
            print(f'x{i + 1} = {coefficient}, ', end='')
    else:
        print('Move to vertex ', end='')
        for i, coefficient in enumerate(coefficients):
            print(f'x{i + 1} = {coefficient}, ', end='')
        print()


def simplex(c, A, b):
    tableau = to_tableau(c, A, b)
    print('Initial')
    print(tabulate(tableau, tablefmt='pipe', headers=table_headers))
    while can_be_improved(tableau):
        tableau = pivot_step(tableau)
        print_solution(tableau, c)
        print(tabulate(tableau, tablefmt='pipe', headers=table_headers))
    print()
    print('Solved')
    print_solution(tableau, c, is_final=True)


# HW 5
def daa_ex1():
    c = [100, 150]
    A = [[3, 5], [2, 3]]
    b = [160, 100]
    return c, A, b


def daa_ex2():
    c = [1, 1, 2]
    A = [[1, -1, 0], [-1, 1, 0], [-1, -3, 2]]
    b = [0, 1, 5]
    return c, A, b


def daa_ex3():
    c = [1, 1, -2]
    A = [[1, 1, 0], [1, 0, 1], [-1, 1, 2]]
    b = [5, 3, 0]
    return c, A, b


# simplex(*daa_ex1())
# simplex(*daa_ex2())
simplex(*daa_ex3())
