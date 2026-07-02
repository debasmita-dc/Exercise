"""
Exercise 4: Employee Management System
-----------------------------------------
Arrays store elements in contiguous memory, so each element is accessed
via base_address + index * element_size, giving O(1) random access.
Advantages: cache-friendly (locality of reference), predictable memory
layout, minimal per-element overhead. Disadvantages: fixed/expensive-to-
resize capacity, and insertion/deletion in the middle requires shifting
subsequent elements, O(n).
"""

from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    name: str
    position: str
    salary: float


class EmployeeArray:
    """Employee records stored in a plain array (Python list used as a
    fixed-purpose array to keep memory contiguous / list semantics)."""

    def __init__(self):
        self._employees: list[Employee] = []

    def add(self, employee: Employee) -> None:
        # O(1) amortized (Python lists over-allocate on append)
        self._employees.append(employee)

    def search(self, employee_id: str) -> Employee | None:
        # O(n) - unsorted array requires linear scan
        for emp in self._employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def traverse(self) -> list[Employee]:
        # O(n)
        return list(self._employees)

    def delete(self, employee_id: str) -> bool:
        # O(n) - must find the element, then shift subsequent elements left
        for i, emp in enumerate(self._employees):
            if emp.employee_id == employee_id:
                del self._employees[i]
                return True
        return False


"""
Time complexity summary:
    add      -> O(1) amortized (append)
    search   -> O(n) (unsorted linear scan)
    traverse -> O(n)
    delete   -> O(n) (find + shift)

Limitations of arrays:
    - Insertion/deletion at arbitrary positions is O(n) due to shifting.
    - Fixed-capacity arrays require costly resize/copy when they overflow
      (Python lists hide this via amortized append, but the cost still
      exists under the hood).
    - Search is O(n) unless the array is kept sorted (enabling O(log n)
      binary search) or paired with an auxiliary hash index.

    Use arrays when: access pattern is mostly indexed/sequential reads,
    the data set size is roughly known, and few insertions/deletions
    happen in the middle. Prefer a hash map (dict) when lookups by ID
    dominate, or a linked list when frequent insert/delete at arbitrary
    positions is required without shifting costs.
"""


if __name__ == "__main__":
    system = EmployeeArray()
    system.add(Employee("E01", "Priya Sharma", "Engineer", 65000))
    system.add(Employee("E02", "Rahul Verma", "Manager", 90000))

    print("Search E02:", system.search("E02"))
    print("All employees:", system.traverse())

    system.delete("E01")
    print("After delete:", system.traverse())
