"""
Portfolio analysis helpers used across the notebooks of this repository.

Every function takes periodic returns (daily by default) as a pandas Series
or DataFrame, except the optimisation functions, which take annualized
expected returns and an annualized covariance matrix.

Usage, from a notebook in projets/ or apprentissage/:

    import sys
    sys.path.append("..")
    from outils_portefeuille import *
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize


# ---------------------------------------------------------------------------
# Return and risk measures
# ---------------------------------------------------------------------------

def annualize_rets(r, periods_per_year=252):
    """Annualized compounded return from periodic returns."""
    return (1 + r).prod() ** (periods_per_year / r.shape[0]) - 1


def annualize_vol(r, periods_per_year=252):
    """Annualized volatility from periodic returns."""
    return r.std() * np.sqrt(periods_per_year)


def sharpe_ratio(r, riskfree_rate=0.02, periods_per_year=252):
    """Annualized excess return divided by annualized volatility."""
    return (annualize_rets(r, periods_per_year) - riskfree_rate) / annualize_vol(r, periods_per_year)


def drawdown(r):
    """Loss from the running peak at each date, from periodic returns."""
    wealth = (1 + r).cumprod()
    peaks = wealth.cummax()
    return (wealth - peaks) / peaks


def max_drawdown(r):
    """Worst drawdown over the period and the date it was reached."""
    dd = drawdown(r)
    return pd.DataFrame({"Maximum drawdown": dd.min(), "Date du creux": dd.idxmin()})


def tracking_error(r, reference, periods_per_year=252):
    """Annualized volatility of return differences with a reference series."""
    diff = r.sub(reference, axis=0)
    return diff.std() * np.sqrt(periods_per_year)


def summary(r, riskfree_rate=0.02, periods_per_year=252):
    """One table with return, volatility, Sharpe ratio and maximum drawdown."""
    return pd.DataFrame({
        "Rendement annualisé": annualize_rets(r, periods_per_year),
        "Volatilité annualisée": annualize_vol(r, periods_per_year),
        "Sharpe": sharpe_ratio(r, riskfree_rate, periods_per_year),
        "Maximum drawdown": drawdown(r).min(),
    })


# ---------------------------------------------------------------------------
# Portfolio construction
# ---------------------------------------------------------------------------

def portfolio_return(weights, er):
    """Expected return of a portfolio."""
    return weights @ er


def portfolio_vol(weights, cov):
    """Volatility of a portfolio."""
    return np.sqrt(weights @ cov @ weights)


def minimize_vol(target_return, er, cov):
    """Long-only weights with the lowest volatility for a target return."""
    n = er.shape[0]
    bounds = ((0.0, 1.0),) * n
    constraints = (
        {"type": "eq", "fun": lambda w: np.sum(w) - 1},
        {"type": "eq", "fun": lambda w: portfolio_return(w, er) - target_return},
    )
    res = minimize(portfolio_vol, np.repeat(1 / n, n), args=(cov,),
                   method="SLSQP", bounds=bounds, constraints=constraints)
    return res.x


def msr(riskfree_rate, er, cov):
    """Long-only weights of the maximum Sharpe ratio portfolio."""
    n = er.shape[0]
    bounds = ((0.0, 1.0),) * n
    constraints = ({"type": "eq", "fun": lambda w: np.sum(w) - 1},)

    def neg_sharpe(w):
        return -(portfolio_return(w, er) - riskfree_rate) / portfolio_vol(w, cov)

    res = minimize(neg_sharpe, np.repeat(1 / n, n),
                   method="SLSQP", bounds=bounds, constraints=constraints)
    return res.x


def gmv(cov):
    """Long-only weights of the global minimum variance portfolio."""
    n = cov.shape[0]
    return msr(0, np.repeat(1.0, n), cov)


def efficient_frontier(er, cov, n_points=50):
    """Return and volatility of minimum-volatility portfolios across target returns."""
    targets = np.linspace(er.min(), er.max(), n_points)
    weights = [minimize_vol(t, er, cov) for t in targets]
    return pd.DataFrame({
        "Rendement": [portfolio_return(w, er) for w in weights],
        "Volatilité": [portfolio_vol(w, cov) for w in weights],
    })
