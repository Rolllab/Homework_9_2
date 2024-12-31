from LinkedListClass import LinkedList

class Queue(LinkedList):
    def __init__(self, size:int=None):
        super().__init__()
        self.size = size


    @staticmethod
    def is_empty():
        """ Проверяет очередь на пустоту """
        return True if not LinkedList.List else False


    def is_full(self):
        """ Проверяет очередь на заполнение """
        return True if len(LinkedList.List) == self.size else False


    def add_queue(self, elem, index:int=None):
        """ Добавляет элемент в очередь """
        if not self.is_full():
            if index == 0:      # Если указано, что вставить в начало списка - вставляем в начало списка
                self.insert_at_head(elem)
                return True
            # Если есть индекс и его значение меньше длины списка минус 1 - вставляем по индексу, иначе - вставляем в конец списка
            if index and index < len(LinkedList.List) - 1:
                self.insert_at_position(elem, index)
                return True
            self.insert_at_end(elem)    # Вставляем в конец списка, если нет индекса или его значение указано не верно
            return True
        return False                    # Вернем False, если очередь заполнена или ошибка в данных
    
    def del_queue(self, index):            # удаление элемента из очереди
        if self.remove_node_position(index) == 'Ничего не удалено':
            return False
        return True
    
    def show(self):                 # отображение всех элементов очереди на экран
        self.print_ll()
