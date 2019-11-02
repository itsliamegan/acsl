from typing import Union, List, Sequence


class Node:
    value: Union[str, int]
    children: List["Node"]

    def __init__(self, value: Union[str, int], children: List["Node"] = None):
        self.value = value

        if children is None:
            self.children = []

        else:
            self.children = children

    def size(self) -> int:
        size = 1

        for child in self.children:
            size += child.size()

        return size

    def evaluate(self) -> int:
        if isinstance(self.value, int):
            return self.value

        evaluated_children = [child.evaluate() for child in self.children]
        return evaluate_expression(self.value, *evaluated_children)

    def __repr__(self) -> str:
        value = str(self.value)

        for child in self.children:
            value += "\n"
            value += str(child)

        return value


def evaluate_expression(operator: str, x: int, y: int, z: int = 0) -> int:
    if operator == "+":
        return x + y

    if operator == "-":
        return x - y

    if operator == "*":
        return x * y

    if operator == "@":
        return y if x >= 0 else z

    if operator == ">":
        return max(x, y, z)

    raise ValueError("Operator must be one of +, -, *, or @")


def create_expression_tree(expression: str) -> Node:
    atoms = expression.split(" ")
    binary_operators = ["+", "-", "*"]
    trinary_operators = ["@", ">"]

    def create_expression_tree_helper(atoms: Sequence[Union[str, int]], position: int):
        position += 1
        atom = atoms[position]

        if atom in binary_operators:
            left_tree = create_expression_tree_helper(atoms, position)
            increment = left_tree.size()
            right_tree = create_expression_tree_helper(
                atoms, position + increment)

            return Node(atom, [left_tree, right_tree])

        elif atom in trinary_operators:
            left_tree = create_expression_tree_helper(atoms, position)
            first_increment = left_tree.size()
            middle_tree = create_expression_tree_helper(
                atoms, position + first_increment)
            second_increment = middle_tree.size()
            right_tree = create_expression_tree_helper(
                atoms, position + first_increment + second_increment)

            return Node(atom, [left_tree, middle_tree, right_tree])

        else:
            return Node(int(atom))

    return create_expression_tree_helper(atoms, -1)


for _ in range(5):
    tree = create_expression_tree(input())
    print(tree.evaluate())
