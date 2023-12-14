from collections import defaultdict, deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traversal(root):
    if not root:
        return []

    order = defaultdict(list)

    queue = deque()
    queue.append((root, 0))

    while queue:
        node, distance = queue.popleft()

        order[distance].append(str(node.val))

        if node.left:
            queue.append((node.left, distance + 1))

        if node.right:
            queue.append((node.right, distance - 1))

    for level in order.values():
        if len(level) > 1:
            level.reverse()

    result = []
    for distance in sorted(order.keys()):
        result.extend(order[distance])

    final_result = " ".join(result)

    return final_result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

final_exam = traversal(root)

print(f"Output:\n{final_exam }")
