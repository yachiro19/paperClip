import unittest

from dfs import dfs


class DfsTests(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(dfs({}, "a"), ["a"])

    def test_single_vertex(self):
        self.assertEqual(dfs({"a": []}, "a"), ["a"])

    def test_simple_path(self):
        graph = {"a": ["b"], "b": ["c"], "c": []}
        self.assertEqual(dfs(graph, "a"), ["a", "b", "c"])

    def test_disconnected_graph_stays_in_component(self):
        graph = {"a": ["b"], "b": [], "c": ["d"], "d": []}
        self.assertEqual(set(dfs(graph, "a")), {"a", "b"})
        self.assertEqual(set(dfs(graph, "c")), {"c", "d"})

    def test_graph_with_cycle_terminates(self):
        graph = {"a": ["b"], "b": ["c"], "c": ["a"]}
        self.assertEqual(set(dfs(graph, "a")), {"a", "b", "c"})

    def test_missing_start_vertex_is_not_in_graph(self):
        graph = {"b": []}
        self.assertEqual(dfs(graph, "z"), ["z"])


if __name__ == "__main__":
    unittest.main()
