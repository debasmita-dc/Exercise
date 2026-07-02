"""
Exercise 5: Task Management System
--------------------------------------
Linked list types:
    - Singly Linked List: each node holds a value and a pointer to the
      next node only. Traversal is forward-only.
    - Doubly Linked List: each node also holds a pointer to the previous
      node, enabling O(1) backward traversal and O(1) deletion given a
      direct node reference (no need to scan for the predecessor).
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    task_id: str
    task_name: str
    status: str


class _Node:
    __slots__ = ("task", "next")

    def __init__(self, task: Task):
        self.task = task
        self.next: Optional["_Node"] = None


class TaskLinkedList:
    """Singly linked list of tasks."""

    def __init__(self):
        self._head: Optional[_Node] = None
        self._size = 0

    def add(self, task: Task) -> None:
        # O(1) - insert at head
        node = _Node(task)
        node.next = self._head
        self._head = node
        self._size += 1

    def search(self, task_id: str) -> Optional[Task]:
        # O(n) - must traverse from head
        current = self._head
        while current:
            if current.task.task_id == task_id:
                return current.task
            current = current.next
        return None

    def traverse(self) -> list[Task]:
        # O(n)
        result = []
        current = self._head
        while current:
            result.append(current.task)
            current = current.next
        return result

    def delete(self, task_id: str) -> bool:
        # O(n) - must find node and its predecessor to relink
        prev, current = None, self._head
        while current:
            if current.task.task_id == task_id:
                if prev is None:
                    self._head = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                return True
            prev, current = current, current.next
        return False

    def __len__(self):
        return self._size


"""
Time complexity summary:
    add      -> O(1) (insert at head)
    search   -> O(n)
    traverse -> O(n)
    delete   -> O(n) (find node + relink)

Advantages of linked lists over arrays for dynamic data:
    - O(1) insertion/deletion once the position is known (no shifting of
      subsequent elements, unlike arrays).
    - No need to pre-allocate or resize/copy a contiguous block; memory
      grows one node at a time.
    - Well suited when the number of tasks changes frequently and is
      unpredictable in size.

    Trade-off: no O(1) random access by index (must traverse), and each
    node carries pointer overhead plus worse cache locality than arrays.
"""


if __name__ == "__main__":
    tasks = TaskLinkedList()
    tasks.add(Task("T1", "Design schema", "pending"))
    tasks.add(Task("T2", "Write API", "pending"))
    tasks.add(Task("T3", "Deploy", "pending"))

    print("Search T2:", tasks.search("T2"))
    print("All tasks:", tasks.traverse())

    tasks.delete("T1")
    print("After delete:", tasks.traverse())
    print("Size:", len(tasks))
