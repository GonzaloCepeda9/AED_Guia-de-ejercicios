from typing import Any, Optional

class List(list):

    # Opcional: Esta función sirve para mostrar los elementos sin un método, separados por coma.
    # def __str__(self):
    #     return ', '.join(str(item) for item in self)
                    
    CRITERION_FUNCTION = {}

    def add_criterion(self, key_criterion: str, function):
        self.CRITERION_FUNCTION[key_criterion] = function

    def show(self) -> None:
        for element in self:
            print(element)

    def delete_value(self, value, key_value: str = None) -> Optional[Any]:
        index = self.search(value, key_value)
        if index is not None:
            return self.pop(index)
        else:
            return print(f'El elemento {index} no se encuentra en la lista.')

    def sort_by_criterion(self, criterion_key: str = None) -> None:

        criterion = self.CRITERION_FUNCTION.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):    # Si self tiene elementos y son simples...
            self.sort()
        else:
            return print('Criterio de orden no encontrado.')

    def search(self, value, key_value: str = None) -> int:

        self.sort_by_criterion(key_value)

        start = 0
        end = len(self) - 1
        middle = (start + end) // 2

        criterion = self.CRITERION_FUNCTION.get(key_value)

        while start <= end:

            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None
            elif criterion:
                middle_value = criterion(self[middle])
            else:
                middle_value = self[middle]    # Si no hay criterio porque en la lista hay datos simples, asigna directamente el valor especificado a "middle".

            if value == middle_value:
                return middle
            elif value < middle_value:
                end = middle - 1
            else:
                start = middle + 1
            middle = (start + end) // 2