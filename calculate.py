from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


# x = # of successes
# n = # of trials
# p = p(success)
def Bin(x, n, p):
    return float(format(pow(p, x) * pow(1 - p, n - x) * (factorial(n) / (factorial(n - x) * factorial(x))), '0.4f'))


# specifications: n must be 1-500, p must be 0-1
def graph_Bin(n, p):
    if n not in range(1, 501):
        return
    if p < 0 or p > 1:
        return
    # create dataset
    x_axis = []
    y_axis = []
    i = 0
    while Bin(i, n, p) <= 0:
        i += 1
    x_axis.append(i)
    y_axis.append(Bin(i, n, p))
    while n - i >= 1 and Bin(i, n, p) > 0:
        i += 1
        x_axis.append(i)
        y_axis.append(Bin(i, n, p))
    # create graph
    plt.bar(x_axis, y_axis, color='blue', width=0.4)
    plt.xlabel('x (# of successes)')
    plt.ylabel('P(X=x)')
    plt.title('Binomial Distribution\nTrials={}\nP(success)={}\n'.format(n, p))
    plt.show()


# x = trial in which you get r(th) success
# p = p(success)
def NB(x, r, p):
    return pow(p, r) * pow(1 - p, x - r) * (factorial(x - 1) / (factorial(r - 1) * factorial(x - r)))


# specification: High values of r and low values of p will cause mass inefficiency
def graph_NB(r, p):
    # create dataset
    x_axis = []
    y_axis = []
    i = r
    while NB(i, r, p) < 0:
        i += 1
    x_axis.append(i)
    y_axis.append(NB(i, r, p))
    # IF P is tiny and/or R is large, allow a larger threshold of values to be displayed
    # if P and R are ordinary inputs, make the threshold smaller
    if p < 0.1 and r > 10:
        threshold = 10e-22
    elif p < 0.1 or r > 10:
        threshold = 10e-16
    else:
        threshold = 10e-12
    while NB(i, r, p) > threshold:
        i += 1
        x_axis.append(i)
        y_axis.append(NB(i, r, p))
    # graph dataset
    plt.bar(x_axis, y_axis, color='blue', width=0.4)
    plt.xlabel('x (trail in which you get rth success)')
    plt.ylabel('P(X=x)')
    plt.title('Negative Binomial Distribution\nr={}\nP(success)={}'.format(r, p))
    plt.show()


# x = # of occurrences of an event in an interval
# expected_x = # of expected occurrences of an event in an interval
def Pois(x, expected_x):
    return (pow(e, -expected_x) * pow(expected_x, x)) / factorial(x)


# specification: 0 <= expected_mean <= 105
def graph_Pois(expected_mean):
    if expected_mean < 0 or expected_mean > 105:
        return
    # create dataset
    x_axis = []
    y_axis = []
    i = 0
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
    plt.show()


def exponential(x, mean):
    return mean * pow(math.e, -mean * x)


def graph_exponential(mean):
    # Based on mean, find the closest integer number i where function will = 0
    i = 0
    while exponential(i, mean) > 0.0001:
        i += 1
    # create dataset
    x = np.linspace(0, i)
    plt.plot(x, exponential(x, mean))
    plt.xlabel('x')
    plt.ylabel('P(X=x)')
    plt.title('Exponential function\nrate={}'.format(mean))
    plt.show()


def graph_normal(mean, variance):
    sd = sqrt(variance)
    x = np.linspace(mean + (-3 * sd), mean + (3 * sd))
    y = stats.norm.pdf(x, mean, sd)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return fig

