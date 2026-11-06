from typing import Any

class HeapMax:

    def __init__(self):
        self.elements = []

    def size(self) -> int:
        return len(self.elements)

    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def add(self, value: Any) -> None:
        self.element.append(value)
        self.float(self.size()-1)

    def float(self, index: int) -> None:
        father = (index - 1) // 2
        
        while index > 0 and self.elements[index] > self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def remove(self) -> Any:
        last = self.size() - 1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            mayor = left_son
            if right_son < self.size():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            if self.elements[index] < self.elements[mayor]:
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False

    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive():
        pass

    def attention():
        pass