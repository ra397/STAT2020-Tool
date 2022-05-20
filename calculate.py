from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import binom, nbinom


def graph_Bin(n, p):
    fig = plt.figure()
    x = np.arange(binom.ppf(0.01, n, p),
                  binom.ppf(0.99, n, p))
    plt.bar(x, binom.pmf(x, n, p))
    plt.xlabel('x (# of successes)')
    plt.ylabel('P(X=x)')
    return fig


def graph_NB(r, p):
    fig, ax = plt.subplots()
    x = np.arange(nbinom.ppf(0.01, r, p),
                  nbinom.ppf(0.99, r, p))
    plt.bar(x, nbinom.pmf(x, r, p))
    plt.xlabel('x (trail in which you get rth success)')
    plt.ylabel('P(X=x)')
    return fig


# x = # of occurrences of an event in an interval
# expected_x = # of expected occurrences of an event in an interval
def Pois(x, expected_x):
    return (pow(e, -expected_x) * pow(expected_x, x)) / factorial(x)


# specification: 0 <= expected_mean <= 105
def graph_Pois(expected_mean):
    fig = plt.figure()
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
    return fig


def exponential(x, mean):
    return mean * pow(e, -mean * x)


def graph_exponential(mean):
    fig = plt.figure()
    # Based on mean, find the closest integer number i where function will = 0
    i = 0
    while exponential(i, mean) > 0.0001:
        i += 1
    # create dataset
    x = np.linspace(0, i)
    y = []
    for each_val in x:
        y.append(exponential(each_val, mean))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('P(X=x)')
    return fig


def graph_normal(mean, variance, critical_point, left=True):
    sd = sqrt(variance)
    x = np.linspace(mean + (-3 * sd), mean + (3 * sd))
    y = stats.norm.pdf(x, mean, sd)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    if left is True:
        x_fill = np.linspace(mean + (-3 * sd), critical_point)
        plt.fill_between(x_fill, stats.norm.pdf(x_fill, mean, sd))
    else:
        x_fill = np.linspace(critical_point, mean + (3 * sd))
        plt.fill_between(x_fill, stats.norm.pdf(x_fill, mean, sd))
    plt.xlabel('x')
    plt.ylabel('P(X = x)')
    return fig
