import unittest

from queue import Queue
from tests.test_LinkedListClass import TestLinkedList
from tests.test_Queue import TestQueue


action_list = ['Тест класса LinkedList', 'Тест класса Queue']

print('Выберите ваши действия:')
for number, name in enumerate(action_list):
    print(f'{number + 1}. {name}')

if int(input('-> ')) == 1:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLinkedList)
    unittest.TextTestRunner(verbosity=2).run(suite)

else:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueue)
    unittest.TextTestRunner(verbosity=2).run(suite)

    queue_main = Queue(4)
    queue_main.add_queue(11, index=0)
    queue_main.add_queue(9, index=3)
    queue_main.add_queue(10)
    queue_main.add_queue(12)
    queue_main.add_queue(15)
    print(f'Список пустой = {queue_main.is_empty()}')
    print(f'Список полный = {queue_main.is_full()}')
    print(f'Удаление позиции = {queue_main.del_queue(3)}') # Не стал менять ваш код, поэтому индекс здесь начинается с 1
    print('Наша очередь:')
    queue_main.show()

print('Приложение завершило свою работу...')
