"""
Exercise 7: Financial Forecasting
-------------------------------------
Recursion: a function solving a problem by calling itself on a smaller
sub-problem, with a base case that stops the recursion. It simplifies
problems that have a naturally repeating/self-similar structure - here,
compound growth over n periods is just "grow once, then solve for n-1
periods."
"""

from functools import lru_cache


def future_value_recursive(present_value: float, growth_rate: float, periods: int) -> float:
    """
    Recursively computes the future value of an investment/metric that
    grows at a fixed rate per period (compound growth).

    future_value(pv, r, n) = pv                              if n == 0
                            = future_value(pv, r, n-1) * (1+r) otherwise

    Time complexity:  O(n) - one call per period, no branching.
    Space complexity: O(n) - recursion call stack depth n.
    """
    if periods < 0:
        raise ValueError("periods must be non-negative")
    if periods == 0:
        return present_value
    return future_value_recursive(present_value, growth_rate, periods - 1) * (1 + growth_rate)


@lru_cache(maxsize=None)
def _future_value_memo(present_value: float, growth_rate: float, periods: int) -> float:
    if periods == 0:
        return present_value
    return _future_value_memo(present_value, growth_rate, periods - 1) * (1 + growth_rate)


def future_value_iterative(present_value: float, growth_rate: float, periods: int) -> float:
    """
    Iterative equivalent - avoids recursion/call-stack overhead entirely.
    Time complexity:  O(n)
    Space complexity: O(1)
    """
    value = present_value
    for _ in range(periods):
        value *= (1 + growth_rate)
    return value


"""
Analysis:
    The naive recursive solution above is O(n) time and O(n) space
    because each call adds a stack frame until the base case, then
    unwinds. For large `periods` (e.g. forecasting decades of monthly
    growth), this risks hitting Python's recursion limit and wastes
    memory on frames that don't share overlapping subproblems (this
    particular recursion isn't exponential like naive Fibonacci, so
    memoization doesn't reduce its O(n) time - it only helps if the same
    (present_value, growth_rate, periods) triple is recomputed across
    calls).

    Optimizations:
    - Convert to an iterative loop (future_value_iterative): same O(n)
      time, but O(1) space and no call-stack overhead - preferred for
      production use.
    - Use the closed-form formula directly: pv * (1 + r) ** n, which is
      O(1) time (or O(log n) if you count the cost of exponentiation by
      squaring at the bit level) and avoids the loop entirely.
    - If forecasting many different scenarios that share sub-periods,
      memoization avoids recomputation across repeated calls.
"""


def future_value_closed_form(present_value: float, growth_rate: float, periods: int) -> float:
    """O(1) - direct formula, the preferred approach in practice."""
    return present_value * (1 + growth_rate) ** periods


if __name__ == "__main__":
    pv, rate, n = 10000.0, 0.05, 10

    print("Recursive:  ", future_value_recursive(pv, rate, n))
    print("Iterative:  ", future_value_iterative(pv, rate, n))
    print("Closed-form:", future_value_closed_form(pv, rate, n))
