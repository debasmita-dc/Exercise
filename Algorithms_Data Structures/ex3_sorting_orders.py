"""
Exercise 3: Sorting Customer Orders
-------------------------------------
Sorting algorithm overview:
    - Bubble Sort:    repeatedly swaps adjacent out-of-order elements.
                       O(n^2) time, O(1) space, stable, simple but slow.
    - Insertion Sort: builds a sorted prefix by inserting each new
                       element into its correct position. O(n^2) worst
                       case but O(n) on nearly-sorted data, O(1) space.
    - Quick Sort:      partitions around a pivot, recursively sorts each
                       side. O(n log n) average, O(n^2) worst case
                       (rare with good pivot choice), O(log n) space.
    - Merge Sort:      divides in half, sorts each half, merges.
                       O(n log n) guaranteed, O(n) extra space, stable.
"""

from dataclasses import dataclass


@dataclass
class Order:
    order_id: str
    customer_name: str
    total_price: float


def bubble_sort(orders: list[Order]) -> list[Order]:
    """O(n^2) time, O(1) extra space. Sorts ascending by total_price."""
    result = orders.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if result[j].total_price > result[j + 1].total_price:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def quick_sort(orders: list[Order]) -> list[Order]:
    """O(n log n) average, O(n^2) worst case. Sorts ascending by total_price."""
    if len(orders) <= 1:
        return orders.copy()

    pivot = orders[len(orders) // 2].total_price
    less = [o for o in orders if o.total_price < pivot]
    equal = [o for o in orders if o.total_price == pivot]
    greater = [o for o in orders if o.total_price > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


"""
Analysis:
    Bubble Sort: O(n^2) comparisons/swaps in the worst and average case,
    O(n) only on already-sorted input with the early-exit optimization.

    Quick Sort: O(n log n) average case, which is dramatically faster
    than Bubble Sort for large order volumes. Worst case O(n^2) can occur
    with a poor pivot choice on adversarial/sorted input, but random or
    median-of-three pivot selection makes this rare in practice.

    Quick Sort is generally preferred because real e-commerce order
    volumes are large, and O(n log n) scales far better than O(n^2). It
    also sorts in-place (excluding recursion stack), whereas Bubble Sort
    wastes many redundant comparisons even after the array is nearly sorted.
"""


if __name__ == "__main__":
    orders = [
        Order("O1", "Alice", 250.0),
        Order("O2", "Bob", 75.5),
        Order("O3", "Carol", 999.99),
        Order("O4", "Dave", 10.0),
    ]

    print("Bubble sorted:", [(o.order_id, o.total_price) for o in bubble_sort(orders)])
    print("Quick sorted: ", [(o.order_id, o.total_price) for o in quick_sort(orders)])
