from typing import Tuple

from binary_tree import BinaryTree


def duple_factoring(number: int) -> Tuple[int, int]:
    for n in range(2, number):
        if number % n == 0:
            return (n, int(number/n))

    return (number, 1)


def is_prime(number: int) -> bool:
    for n in range(2, int(number/2)):
        if number % n == 0:
            return False

    return True


def prime_factor(tree: BinaryTree) -> BinaryTree:
    if tree.value == 1:
        return tree

    if is_prime(tree.value):
        return tree

    n, m = duple_factoring(tree.value)

    tree.right = prime_factor(BinaryTree(n))
    tree.left = prime_factor(BinaryTree(m))

    return tree
