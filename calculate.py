from itertools import combinations
from math import e, factorial
import matplotlib.pyplot as plt
import mplcursors


# x = # of successes
# n = # of trials
# p = p(success)
def Bin(x, n, p):
    return pow(p, x) * pow(1 - p, n - x) * len(list(combinations(range(n), x)))


def graph_Bin(n, p):
    # create dataset
    x_axis = []
    y_axis = []
    for i in range(n):
        if Bin(i, n, p) != 0:
            x_axis.append(i)
            y_axis.append(Bin(i, n, p))
    # graph dataset
    plt.bar(x_axis, y_axis, color='blue', width=0.4)
    plt.xlabel('x (# of successes)')
    plt.ylabel('P(X=x)')
    plt.title('Binomial Distribution\nTrials={}\nP(success)={}'.format(n, p))
    mplcursors.cursor(hover=True)  # add hover effect
    plt.show()


# x = trial in which you get r(th) success
# p = p(success)
def NB(x, r, p):
    return pow(p, r) * pow(1 - p, x - r) * len(list(combinations(range(x - 1), r - 1)))


def graph_NB(r, p):
    # create dataset
    x_axis = []
    y_axis = []
    for i in range(100):
        if NB(i, r, p) > 0.0001:
            x_axis.append(i)
            y_axis.append(NB(i, r, p))
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
    return (pow(e, -expected_x) * pow(expected_x, x)) / factorial(x)


def graph_Pois(expected_mean):
    # create dataset
    x_axis = []
    y_axis = []
    for i in range(2*expected_mean):
        if Pois(i, expected_mean) != 0:
            x_axis.append(i)
            y_axis.append(Pois(i, expected_mean))
    # graph dataset
    plt.bar(x_axis, y_axis, color='blue', width=0.4)
    plt.xlabel('x (number of occurrences)')
    plt.ylabel('P(X=x)')
    plt.title('Negative Binomial Distribution\nExpected mean: {}'.format(expected_mean))
    mplcursors.cursor(hover=True)  # add hover effect
    plt.show()