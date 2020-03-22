import unittest
from challenges.queue_two_stacks import Queue

class TestQueue(unittest.TestCase):

    def test_queue(self):
        tmp_queue: Queue = Queue()
        actual_size: int = tmp_queue.size
        expected_size: int = 0
        self.assertEqual(expected_size, actual_size)

        actual_outcome: None = tmp_queue.dequeue()
        expected_outcome: None = None
        self.assertEqual(expected_outcome, actual_outcome)

        tmp_queue.enqueue(1)
        tmp_queue.enqueue(2)
        tmp_queue.enqueue(3)
        tmp_queue.enqueue(4)
        tmp_queue.enqueue(5)

        actual_size: int = tmp_queue.size
        expected_size: int = 5
        self.assertEqual(expected_size, actual_size)

        expected_item: int = 1
        actual_item: int = tmp_queue.dequeue()
        self.assertEqual(expected_item, actual_item)
        actual_size: int = tmp_queue.size
        expected_size: int = 4
        self.assertEqual(expected_size, actual_size)

        expected_item: int = 2
        actual_item: int = tmp_queue.dequeue()
        self.assertEqual(expected_item, actual_item)
        actual_size: int = tmp_queue.size
        expected_size: int = 3
        self.assertEqual(expected_size, actual_size)

        tmp_queue.enqueue(6)

        actual_size: int = tmp_queue.size
        expected_size: int = 4
        self.assertEqual(expected_size, actual_size)

        expected_item: int = 3
        actual_item: int = tmp_queue.dequeue()
        self.assertEqual(expected_item, actual_item)

        actual_size: int = tmp_queue.size
        expected_size: int = 3
        self.assertEqual(expected_size, actual_size)


if __name__ == "__main__":
    unittest.main()