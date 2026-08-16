import unittest

from mergesort import merge_sort


class MergeSortTests(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_duplicates_are_stable(self):
        items = [(3, "a"), (1, "x"), (3, "b"), (2, "y"), (1, "z")]
        self.assertEqual(
            merge_sort(items),
            [(1, "x"), (1, "z"), (2, "y"), (3, "a"), (3, "b")],
        )

    def test_does_not_mutate_input(self):
        original = [3, 1, 2]
        merge_sort(original)
        self.assertEqual(original, [3, 1, 2])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-3, 0, -1, 2, -2]), [-3, -2, -1, 0, 2])


if __name__ == "__main__":
    unittest.main()