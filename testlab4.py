from avl_priority_queue import AVLPriorityQueue
import unittest

class TestAVLQueue(unittest.TestCase):
    
    def setUp(self):
        self.pq = AVLPriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("Task Low", 10)
        
        self.pq.insert("Task High", 50)
        self.pq.insert("Task Medium", 30)
        
        
        val, priority = self.pq.peek()
        self.assertEqual(val, "Task High")
        self.assertEqual(priority, 50)
        print(f"Найвищий пріоритет — {priority}")
        self.pq.display()

    def test_pop_order(self):
        tasks = [("A", 10), ("B", 100), ("C", 50), ("D", 75)]
        for val, prio in tasks:
            self.pq.insert(val, prio)
        self.pq.display()
            
        self.assertEqual(self.pq.pop(), ("B", 100))
        self.assertEqual(self.pq.pop(), ("D", 75))
        self.assertEqual(self.pq.pop(), ("C", 50))
        self.assertEqual(self.pq.pop(), ("A", 10))
        
        self.assertIsNone(self.pq.pop())
        self.pq.display()

    def test_same_priority(self):
        self.pq.insert("First", 20)
        self.pq.insert("Second", 20)
        
        val, prio = self.pq.pop()
        self.assertEqual(val, "Second") 
        self.assertEqual(prio, 20)
        self.pq.display()

    def test_empty_queue(self):
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.pop())
        self.pq.display()

if __name__ == "__main__":
    unittest.main()