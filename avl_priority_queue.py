class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, value, priority):
        self.root = self.insert_recursive(self.root, value, priority)

    def insert_recursive(self, node, value, priority):
        if not node:
            return Node(value, priority)
        
        if priority >= node.priority:
            node.left = self.insert_recursive(node.left, value, priority)
        else:
            node.right = self.insert_recursive(node.right, value, priority)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        
        if balance > 1 and priority >= node.left.priority:
            return self.rotate_right(node)
        if balance < -1 and priority < node.right.priority:
            return self.rotate_left(node)
        if balance > 1 and priority < node.left.priority:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and priority >= node.right.priority:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def peek(self):
        if not self.root:
            return None
        
        current = self.root
        while current.left:
            current = current.left
            
        print(f"Найлівіший елемент вузла \"{self.root.value}\" - {current.value}")
        return (current.value, current.priority)

    def pop(self):
        if not self.root:
            return None
        
        highest_node = self.root
        while highest_node.left:
            highest_node = highest_node.left
        
        result = (highest_node.value, highest_node.priority)
        self.root = self.delete_recursive(self.root, highest_node.priority, highest_node.value)
        return result

    def delete_recursive(self, root, priority, value=None):
        if not root:
            return root

        if priority > root.priority:
            root.left = self.delete_recursive(root.left, priority, value)
        elif priority < root.priority:
            root.right = self.delete_recursive(root.right, priority, value)
        else:
            if value is not None and root.value != value:
                root.left = self.delete_recursive(root.left, priority, value)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                temp = self.get_min_value_node(root.right)
                root.priority = temp.priority
                root.value = temp.value
                root.right = self.delete_recursive(root.right, temp.priority, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def display(self):
        if not self.root:
            print(f"Черга порожня ")
            return

        elements = []
        def in_order(node):
            if node:
                in_order(node.left)
                elements.append(node)
                in_order(node.right)
        
        in_order(self.root)
        
        print(f"\n Всього елементів: {len(elements)})")
        for i, node in enumerate(elements, 1):
            print(f"{i}. Пріоритет: {node.priority} Значення: {node.value}")
        print("------------------------------------------")