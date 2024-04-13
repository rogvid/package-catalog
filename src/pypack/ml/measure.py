## Python Function ##
from numpy import array, random, arange


def xicor(X, Y, ties=True):
    """Compute the Xi correlation measure.

    New correlation metric for estimating the correlation of points in a dataset.

    Conceptually it is very simple, in the sense that it simply evaluates the
    difference in Y as a function of an ordered X.

    Article here: https://towardsdatascience.com/a-new-coefficient-of-correlation-64ae4f260310

    Parameters
    ----------
    X : np.ndarray
        The independent variable `x`
    Y : np.ndarray
        The dependent variable `y`

    TODO: Add tests

    """
    random.seed(42)
    n = len(X)
    order = array([i[0] for i in sorted(enumerate(X), key=lambda x: x[1])])
    if ties:
        left = array([sum(y >= Y[order]) for y in Y[order]])
        right = left.copy()
        for j in range(n):
            if sum([right[j] == right[i] for i in range(n)]) > 1:
                tie_index = array([right[j] == right[i] for i in range(n)])
                right[tie_index] = random.choice(
                    right[tie_index]
                    - arange(0, sum([right[j] == right[i] for i in range(n)])),
                    sum(tie_index),
                    replace=False,
                )
        return 1 - n * sum(abs(right[1:] - right[: n - 1])) / (
            2 * sum(left * (n - left))
        )
    else:
        right = array([sum(y >= Y[order]) for y in Y[order]])
        return 1 - 3 * sum(abs(right[1:] - right[: n - 1])) / (n**2 - 1)
