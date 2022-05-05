from math import e, factorial
import matplotlib.pyplot as plt
import mplcursors


# x = # of successes
# n = # of trials
# p = p(success)
def Bin(x, n, p):
    if n < 0 or n - int(n) != 0:
        return 'N must be a natural number'
    if x not in range(n):
        return 'X must be 0, 1, ..., n'
    if p > 1 or p < 0:
        return '0 <= p <= 1'
    return float(format(pow(p, x) * pow(1 - p, n - x) * (factorial(n) / (factorial(n - x) * factorial(x))), '0.4f'))


def graph_Bin(n, p):
    # create dataset
    x_axis = []
    y_axis = []
    i = 0
    if isinstance(Bin(i, n, p), str):
        return Bin(i, n, p)
    while Bin(i, n, p) < 0:
        i += 1
    x_axis.append(i)
    y_axis.append(Bin(i, n, p))
    while n - i >= 0 and Bin(i, n, p) > 0.0001:
        x_axis.append(i)
        y_axis.append(Bin(i, n, p))
        i += 1
    # create graph
    plt.bar(x_axis, y_axis, color='blue', width=0.4)
    plt.xlabel('x (# of successes)')
    plt.ylabel('P(X=x)')
    plt.title('Binomial Distribution\nTrials={}\nP(success)={}\n'.format(n, p))
    mplcursors.cursor(hover=True)  # add hover effect
    plt.show()


# x = trial in which you get r(th) success
# p = p(success)
def NB(x, r, p):
    if r < 0 or r - int(r) != 0:
        return 'r must be a natural number'
    if x not in range(r):
        return 'Error: x < r'
    if p > 1 or p < 0:
        return '0 <= p <= 1'
    return pow(p, r) * pow(1 - p, x - r) * (factorial(x - 1) / (factorial(r - 1) * factorial(x - r)))


def graph_NB(r, p):
    # create dataset
    x_axis = []
    y_axis = []
    i = r + 1
    while NB(i, r, p) < 0.00001:
        i += 1
    x_axis.append(i)
    y_axis.append(NB(i, r, p))
    while NB(i, r, p) > 0.01:
        x_axis.append(i)
        y_axis.append(NB(i, r, p))
        i += 1
    # graph dataset
    plt.bar(x_axis, y_axis, color='blue', width=0.4)
    plt.xlabel('x (trail in which you get rth success)')
    plt.ylabel('P(X=x)')
    plt.title('Negative Binomial Distribution\nr={}\nP(success)={}'.format(r, p))
    mplcursors.cursor(hover=True)  # add hover effect
    plt.show()


# x = # of occurrences of an event in an interval
# expected_x = # of expected occurrences of an event in an interval
def Pois(x, expected_x):
    if expected_x < 0 or expected_x > 105:
        return 'Error: 0 <= expected_x <= 105'
    return (pow(e, -expected_x) * pow(expected_x, x)) / factorial(x)


def graph_Pois(expected_mean):
    # create dataset
    x_axis = []
    y_axis = []
    i = 0
    if isinstance(Pois(i, expected_mean), str):
        return Pois(i, expected_mean)
    while Pois(i, expected_mean) < 0.00001:
        i += 1
    x_axis.append(i)
    y_axis.append(Pois(i, expected_mean))
    while Pois(i, expected_mean) > 0.00001:
        x_axis.append(i)
        y_axis.append(Pois(i, expected_mean))
        i += 1
    # graph dataset
    plt.bar(x_axis, y_axis, color='blue', width=0.4)
    plt.xlabel('x (number of occurrences)')
    plt.ylabel('P(X=x)')
    plt.title('Poisson Distribution\nExpected mean: {}'.format(expected_mean))
    mplcursors.cursor(hover=True)  # add hover effect
    plt.show()


