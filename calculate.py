from math import e, factorial
import matplotlib.pyplot as plt
import mplcursors


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
    mplcursors.cursor(hover=True)  # add hover effect
    plt.show()


# x = trial in which you get r(th) success
# p = p(success)
def NB(x, r, p):
    return pow(p, r) * pow(1 - p, x - r) * (factorial(x - 1) / (factorial(r - 1) * factorial(x - r)))


# specifications:
def graph_NB(r, p):
    # create dataset
    x_axis = []
    y_axis = []
    i = r
    while NB(i, r, p) < 0:
        i += 1
    x_axis.append(i)
    y_axis.append(NB(i, r, p))
    # IF P is extremely small, allow a larger threshold of values to be displayed
    # if p is an ordinary input, make the threshold smaller
    while NB(i, r, p) > 10e-20:
        i += 1
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


graph_NB(15, 0.05)