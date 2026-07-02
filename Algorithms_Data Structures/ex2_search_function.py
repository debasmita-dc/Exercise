"""
Exercise 2: E-commerce Platform Search Function
------------------------------------------------
Big O notation describes how an algorithm's running time (or space) grows
relative to input size n, ignoring constant factors and lower-order terms.
It lets us compare algorithms independent of hardware.

    - Best case: the minimum time for a given input size (e.g. target is
      the first element checked).
    - Average case: expected time over a random/typical input distribution.
    - Worst case: the maximum time for any input of size n; the usual
      basis for Big O guarantees, since it bounds the algorithm reliably.
"""

from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    product_name: str
    category: str


def linear_search(products: list[Product], product_id: str) -> Product | None:
    """
    Scan every element until a match is found.
    Best:    O(1)  - target is first element
    Average: O(n)
    Worst:   O(n)  - target is last element or absent
    Works on unsorted data.
    """
    for product in products:
        if product.product_id == product_id:
            return product
    return None


def binary_search(sorted_products: list[Product], product_id: str) -> Product | None:
    """
    Requires products sorted by product_id. Repeatedly halves the search
    space.
    Best:    O(1)  - target is the middle element
    Average: O(log n)
    Worst:   O(log n)
    """
    low, high = 0, len(sorted_products) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_products[mid].product_id
        if mid_id == product_id:
            return sorted_products[mid]
        if mid_id < product_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


"""
Analysis:
    Linear search: O(n) worst case, no ordering requirement, cheap to
    maintain (new products can be appended in O(1)).

    Binary search: O(log n) worst case, but requires the array to stay
    sorted, which costs O(n) per insertion if maintained as a plain
    sorted array (or O(log n) with a balanced BST / skip list).

    For a search-heavy e-commerce platform with relatively infrequent
    catalog updates, binary search (or better, an index such as a hash
    map for exact match / a B-tree or search engine like Elasticsearch
    for prefix/fuzzy search) is far more suitable at scale than linear
    search once the catalog exceeds a few hundred items.
"""


if __name__ == "__main__":
    catalog = [
        Product("A100", "Wireless Mouse", "Electronics"),
        Product("A200", "Mechanical Keyboard", "Electronics"),
        Product("B300", "Yoga Mat", "Fitness"),
        Product("C400", "Water Bottle", "Fitness"),
    ]
    sorted_catalog = sorted(catalog, key=lambda p: p.product_id)

    print("Linear search A200 ->", linear_search(catalog, "A200"))
    print("Binary search C400 ->", binary_search(sorted_catalog, "C400"))
    print("Binary search missing ->", binary_search(sorted_catalog, "Z999"))
