from functools import reduce

import main
from binary_tree import BinaryTree


def test_binary_tree_get_leaves_1():
    tree = BinaryTree(10)
    assert tree.get_leaves() == [10]


def test_binary_tree_get_leaves_2():
    tree = BinaryTree(10)
    tree2 = BinaryTree(20, tree)
    assert tree2.get_leaves() == [10]


def test_binary_tree_get_leaves_3():
    tree = BinaryTree(10)
    tree2 = BinaryTree(20, tree)
    tree3 = BinaryTree(30, tree2, tree)
    assert tree3.get_leaves() == [10, 10]


def test_duple_factoring_1():
    r = main.duple_factoring(150)
    assert r == (2, 75)


def test_duple_factoring_2():
    r = main.duple_factoring(75)
    assert r == (3, 25)


def test_duple_factoring_3():
    r = main.duple_factoring(25)
    assert r == (5, 5)


def test_duple_factoring_4():
    r = main.duple_factoring(5)
    assert r == (5, 1)


def test_prime_factor_1():
    number = 150
    tree = main.prime_factor(BinaryTree(number))
    assert tree.get_leaves() == [2, 3, 5, 5]
    assert reduce(lambda x, y: x*y, tree.get_leaves()) == number


def test_prime_factor_2():
    number = 56
    tree = main.prime_factor(BinaryTree(number))
    assert tree.get_leaves() == [2, 2, 2, 7]
    assert reduce(lambda x, y: x*y, tree.get_leaves()) == number


def test_prime_factor_3():
    number = 2569
    tree = main.prime_factor(BinaryTree(number))
    assert tree.get_leaves() == [7, 367]
    assert reduce(lambda x, y: x*y, tree.get_leaves()) == number
