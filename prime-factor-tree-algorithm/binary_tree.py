from __future__ import annotations
from typing import List


class BinaryTree():
    def __init__(self, value: int,
                 left: 'BinaryTree' = None,
                 right: 'BinaryTree' = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def get_leaves(self) -> List[int]:
        leaves: List[int] = list()

        if self.left is not None:
            leaves.extend(self.left.get_leaves())

        if self.right is not None:
            leaves.extend(self.right.get_leaves())

        if not self.right and not self.left:
            leaves.append(self.value)

        return sorted(leaves)
