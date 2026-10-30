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