"""
Exercise 1: Inventory Management System
----------------------------------------
Data structures & algorithms are essential for large inventories because
lookups, insertions, updates and deletions must scale well as the number
of SKUs grows into the thousands/millions. A hash map (dict) gives O(1)
average-case add/update/delete/search by productId, which a plain list
cannot (O(n) search). An ArrayList/list would be better only if the
dominant access pattern is ordered iteration or index-based access.

Chosen structure: dict keyed by productId (HashMap equivalent).
"""

from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    product_name: str
    quantity: int
    price: float


class Inventory:
    """Inventory backed by a hash map (dict) keyed on product_id."""

    def __init__(self):
        self._products: dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        # O(1) average
        if product.product_id in self._products:
            raise ValueError(f"Product {product.product_id} already exists")
        self._products[product.product_id] = product

    def update_product(self, product_id: str, **fields) -> None:
        # O(1) average
        product = self._products.get(product_id)
        if product is None:
            raise KeyError(f"Product {product_id} not found")
        for key, value in fields.items():
            setattr(product, key, value)

    def delete_product(self, product_id: str) -> None:
        # O(1) average
        if product_id not in self._products:
            raise KeyError(f"Product {product_id} not found")
        del self._products[product_id]

    def get_product(self, product_id: str) -> Product | None:
        # O(1) average
        return self._products.get(product_id)

    def list_products(self) -> list[Product]:
        # O(n)
        return list(self._products.values())


"""
Time complexity summary (dict / HashMap):
    add_product     -> O(1) average, O(n) worst case (hash collisions/rehash)
    update_product  -> O(1) average
    delete_product  -> O(1) average
    get_product     -> O(1) average

Optimization notes:
    - A dict already gives near-optimal average complexity for point
      operations. Worst-case degrades to O(n) only under pathological
      hash collisions, which Python's hash randomization mitigates.
    - If frequent range queries by price are needed, maintain a secondary
      sorted index (e.g. a sorted list of (price, product_id) tuples, or
      a balanced BST) alongside the dict, trading memory for query speed.
"""


if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_product(Product("P001", "Wireless Mouse", 50, 19.99))
    inventory.add_product(Product("P002", "Mechanical Keyboard", 30, 49.99))

    inventory.update_product("P001", quantity=45)
    print("After update:", inventory.get_product("P001"))

    inventory.delete_product("P002")
    print("Remaining products:", inventory.list_products())
