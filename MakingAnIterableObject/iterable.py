from errors import ItError, FilterError

class It:
    def __init__(self, l, start=0):
        self.__list = l
        self.__contor = start

    def add(self, object):
        self.__list.append(object)

    def size(self):
        return len(self.__list)

    def __iter__(self):
        return self

    def __next__(self):
        contor = self.__contor

        try:
            self.__list[contor]
        except Exception:
            self.__contor = 0
            raise StopIteration
            return

        self.__contor += 1
        return self.__list[contor]

    def __getitem__(self, contor):
        return self.__list[contor]

    def __setitem__(self, contor, newitem):
        self.__list[contor] = newitem

    def __delitem__(self, object):
        if object not in self.__list:
            raise ItError("your It data structure does not contain the element you want to remove!")
        self.__list.remove(object)

    def __str__(self):
        n = len(self.__list)
        print_string = ''
        for i in range(n):
            print_string += str(self.__list[i]) + " "
        return print_string

    def __len__(self):
        return len(self.__list)

    @staticmethod
    def compare(x, y, order):
        if order == 'ascending':
            if x >= y:
                return True
            return False
        elif order == 'descending':
            if x < y:
                return True
            return False

    def gnomeSort(self, order):
        index = 0
        n = len(self.__list)
        arr = self.__list
        while(index < n):
            if index == 0:
                index += 1
            statement = self.compare(arr[index], arr[index-1], order)
            if statement:
                index += 1
            else:
                arr[index], arr[index-1] = arr[index-1], arr[index]
                index -= 1


class GnomeSort:
    def __init__(self, l, compare):
        self.__list = l
        self.compare = compare

    def gnomeSort(self):
        index = 0
        n = len(self.__list)
        arr = self.__list
        while(index < n):
            if index == 0:
                index += 1
            statement = self.compare(arr[index], arr[index-1])
            if statement:
                index += 1
            else:
                arr[index], arr[index-1] = arr[index-1], arr[index]
                index -= 1


class Filter:
    def __init__(self, l, accf):
        self.__l = l
        self.__accf = accf

    def filter(self):
        n = len(self.__l)
        i = 0
        while i < n:
            if not self.__accf(self.__l[i]):
                self.__l.remove(self.__l[i])
                n = n - 1
                i = i - 1
            i = i + 1
