from lab3 import BinaryTree
import unittest

class Test(unittest.TestCase):
    def test_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        print(f"Збалансованість дерева - {root.balanced_tree()}")

    def test_postorder_build(self):
            
        postorder_tree = BinaryTree.build_from_postorder_file("tree.txt")
        print(f" {postorder_tree.print_tree()}")
        print(f"Збалансованість дерева - {postorder_tree.balanced_tree()}")

if __name__ == "__main__":
    unittest.main()