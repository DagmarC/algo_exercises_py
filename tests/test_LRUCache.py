import unittest
from coding_interview.linked_list.LRU_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)  # kapacita 2 pre väčšinu testov

    def test_basic_functionality(self):
        self.cache.put(1, 100)
        self.assertEqual(self.cache.get(1), 100)
        self.assertEqual(self.cache.get(2), -1)  # neexistujúci kľúč

    def test_capacity_limit(self):
        self.cache.put(1, 100)
        self.cache.put(2, 200)
        self.cache.put(3, 300)  # toto by malo vyhodiť kľúč 1
        self.assertEqual(self.cache.get(1), -1)
        self.assertEqual(self.cache.get(2), 200)
        self.assertEqual(self.cache.get(3), 300)

    def test_update_existing_key(self):
        self.cache.put(1, 100)
        self.cache.put(1, 200)  # aktualizácia hodnoty
        self.assertEqual(self.cache.get(1), 200)

    def test_lru_eviction_order(self):
        self.cache.put(1, 100)
        self.cache.put(2, 200)
        self.cache.get(1)  # používame 1, takže 2 by malo byť ďalšie na vyhodenie
        self.cache.put(3, 300)
        self.assertEqual(self.cache.get(2), -1)
        self.assertEqual(self.cache.get(1), 100)
        self.assertEqual(self.cache.get(3), 300)

    def test_zero_capacity(self):
        cache = LRUCache(0)
        cache.put(1, 100)
        self.assertEqual(cache.get(1), -1)

    def test_large_operations(self):
        cache = LRUCache(3)
        operations = [
            (1, 100), (2, 200), (3, 300),  # naplnenie cache
            (4, 400),  # vyhodí 1
            (2, None),  # get 2
            (5, 500),  # vyhodí 3
        ]
        
        for key, value in operations:
            if value is None:
                cache.get(key)
            else:
                cache.put(key, value)
                
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 200)
        self.assertEqual(cache.get(3), -1)
        self.assertEqual(cache.get(4), 400)
        self.assertEqual(cache.get(5), 500)


if __name__ == '__main__':
    unittest.main()