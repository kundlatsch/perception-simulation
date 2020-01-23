class OrderedList():

    def __init__(self):
        self.__list = {}


    def get_top(self):
        first = True
        top = None
        for element in self.__list:
            if first:
                top = element
                first = False
            
            elif self.__list[element] > self.__list[element]:
                top = element

        self.__list.pop(top, None)
        return top
    
    def insert(self, element):
        if element in self.__list:
            old_value = self.__list[element]
            self.__list[element] = old_value + 1
        else:
            self.__list[element] = 1
