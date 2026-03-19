
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def balanced_tree(self) -> bool:
        def check_height(current_node):
            if current_node is None:
                return 0
            
            left_height = check_height(current_node.left)
            right_height = check_height(current_node.right)

            if left_height == -1:
                return -1
            
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return check_height(self) != -1
    
    @classmethod
    def build_from_postorder_file(cls, filename: str):
        try:
            with open(filename, 'r') as file:
                content = file.read().replace(',', ' ').split()
                postorder_list = [int(x) for x in content]
        except FileNotFoundError:
            print(f"Помилка: Файл {filename} не знайдено.")
            return None

        def construct(lower_bound=float('-inf'), upper_bound=float('inf')):
            if not postorder_list or postorder_list[-1] < lower_bound or postorder_list[-1] > upper_bound:
                return None
            
            val = postorder_list.pop()
            node = cls(val)
            
            node.right = construct(val, upper_bound)
            
            node.left = construct(lower_bound, val)

            return node
            
        return construct()
    
    def print_tree(self):
        if not self: return
        canvas = {}

        def add_to_canvas(x, y, text):
            start_x = x - len(text) // 2
            for i, char in enumerate(text):
                canvas[(start_x + i, y)] = char

        def draw(node, x, y, is_left, step_y):
            if not node: return
            
            add_to_canvas(x, y, str(node.value))

            if node == self:
                if node.left:
                    add_to_canvas(x - 3, y, "---")
                    draw(node.left, x - 6, y, True, 2)
                if node.right:
                    add_to_canvas(x + 3, y, "---")
                    draw(node.right, x + 6, y, False, 2)
            else:
                dir_x = -5 if is_left else 5
                
                if node.left:
                    char = "/" if is_left else "\\"
                    add_to_canvas(x + dir_x // 2, y + step_y, char)
                    draw(node.left, x + dir_x, y + step_y * 2, is_left, max(1, step_y - 1))
                    
                if node.right:
                    char = "\\" if is_left else "/"
                    add_to_canvas(x + dir_x // 2, y - step_y, char)
                    draw(node.right, x + dir_x, y - step_y * 2, is_left, max(1, step_y - 1))

        draw(self, 0, 0, True, 2)

        min_x = min(x for x, y in canvas.keys())
        max_x = max(x for x, y in canvas.keys())
        min_y = min(y for x, y in canvas.keys())
        max_y = max(y for x, y in canvas.keys())

        print("\nВид дерева зверху:")
        for y in range(min_y, max_y + 1):
            row = "".join(canvas.get((x, y), " ") for x in range(min_x, max_x + 1))
            print(row.rstrip())