import unittest
from LinkedListClass import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_head(self):
        self.assertEqual(self.ll.insert_at_head(10), 'Узел с данными 10 добавлен в начало списка')
        self.assertEqual(self.ll.get(10)[1].data, 10)

    def test_insert_at_end(self):
        self.ll.insert_at_head(10)
        self.assertEqual(self.ll.insert_at_end(13), 'Узел с данными 13 добавлен в конец списка')

    def test_remove_node_position(self):
        self.ll.insert_at_end(10)
        self.ll.insert_at_end(22)
        self.ll.insert_at_end(33)
        self.assertEqual(self.ll.remove_node_position(1), 'Удален узел с данными 10 позиции 1')
        self.assertEqual(self.ll.remove_node_position(10), 'Ничего не удалено')
        self.assertEqual(self.ll.remove_node_position(2), 'Удален узел с данными 33 позиции 2')

    def test_insert_at_position(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_end(11)
        self.ll.insert_at_end(12)
        self.assertEqual(self.ll.insert_at_position(5, 2), 'Узел с данными 5 добавлен на позицию 2')
        self.assertEqual(self.ll.insert_at_position(5, 10), None)

    def test_print_ll(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_head(11)
        self.ll.insert_at_head(12)
        self.assertEqual(self.ll.print_ll(), 'Данные списка выведены')

    def test_get(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_head(11)
        self.ll.insert_at_head(12)
        self.assertEqual(self.ll.get(11)[1].data, 11)
        self.assertEqual(self.ll.get(15)[1], None)

    def test_change_data(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_head(11)
        self.ll.insert_at_head(12)
        self.assertEqual(self.ll.change_data(10, 150), 'Заменены данные в узле № 3')
        self.assertEqual(self.ll.change_data(18, 150), 'Данные не обнаружены')

