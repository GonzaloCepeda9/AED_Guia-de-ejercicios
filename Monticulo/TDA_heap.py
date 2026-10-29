class HeapMax:

    def __init__(self):
        self.elements = []

    def size(self) -> int:
        return len(self.elements)

    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    