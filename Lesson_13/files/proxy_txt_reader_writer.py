# 2 - Implement writer for proxy pattern from the lesson.
from interfaces.iread import Read
from txt_reader import TxtReader
from interfaces.iwrite import Write
from txt_writer import TxtWriter


class ProxyTxtRW(Read, Write):

    def __init__(self, real_reader: Read, real_writer: Write):
        self.__result = ''
        self.__is_actual = None
        self.__real_reader = real_reader
        self.__real_writer = real_writer

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__real_reader.read()
            self.__is_actual = True
            return self.__result

    def write(self, new_data):
        if self.__result == new_data:
            return "This data already exists!"
        else:
            self.__real_writer.write(new_data)
            self.__result = new_data
            self.__is_actual = True
            return self.__result


if __name__ == '__main__':
    try:
        my_reader = TxtReader('my_file.txt')
        my_writer = TxtWriter("my_file.txt")
        my_proxy = ProxyTxtRW(my_reader, my_writer)

        print(my_proxy.read())
        print(my_proxy.write("This is a beautiful day!"))
        print(my_proxy.read())
    except Exception as error:
        print(error)


