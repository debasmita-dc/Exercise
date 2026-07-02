"""
Exercise 6: Library Management System
-----------------------------------------
Linear search scans sequentially and works on any (sorted or unsorted)
list, O(n) worst case. Binary search requires the list to be sorted by
the search key, and repeatedly halves the search interval, O(log n)
worst case.
"""

from dataclasses import dataclass


@dataclass
class Book:
    book_id: str
    title: str
    author: str


def linear_search_by_title(books: list[Book], title: str) -> Book | None:
    """O(n) worst case. No ordering required."""
    for book in books:
        if book.title == title:
            return book
    return None


def binary_search_by_title(sorted_books: list[Book], title: str) -> Book | None:
    """O(log n) worst case. Requires books sorted by title."""
    low, high = 0, len(sorted_books) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_title = sorted_books[mid].title
        if mid_title == title:
            return sorted_books[mid]
        if mid_title < title:
            low = mid + 1
        else:
            high = mid - 1
    return None


"""
Analysis:
    Linear search: O(n), simple, no pre-processing needed, good for
    small or frequently-changing (unsorted) catalogs.

    Binary search: O(log n), but the catalog must be kept sorted by
    title, which costs O(n log n) to sort initially and O(n) to keep
    sorted after each insertion into a plain array (or O(log n) with a
    balanced BST-backed index).

    Guidance: for a small library or one with frequent additions/removals,
    linear search (or a hash map keyed by title/ID) is simpler and
    sufficiently fast. For a large, relatively static catalog where
    searches vastly outnumber updates, sort once and use binary search
    (or maintain a persistent sorted index / database index) for O(log n)
    lookups.
"""


if __name__ == "__main__":
    books = [
        Book("B1", "Clean Code", "Robert C. Martin"),
        Book("B2", "The Pragmatic Programmer", "Andrew Hunt"),
        Book("B3", "Introduction to Algorithms", "Cormen et al."),
        Book("B4", "Design Patterns", "Erich Gamma"),
    ]
    sorted_books = sorted(books, key=lambda b: b.title)

    print("Linear search 'Design Patterns' ->", linear_search_by_title(books, "Design Patterns"))
    print("Binary search 'Clean Code' ->", binary_search_by_title(sorted_books, "Clean Code"))
    print("Binary search missing ->", binary_search_by_title(sorted_books, "Nonexistent"))
