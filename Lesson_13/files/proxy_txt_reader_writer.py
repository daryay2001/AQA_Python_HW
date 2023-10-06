# 2 - Implement writer for proxy pattern from the lesson.
from interfaces.iread import Read
from txt_reader import TxtReader
from interfaces.iwrite import Write
from interfaces.txt_writer import TxtWriter


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

    def write(self, data: str):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__real_writer.write(data)
            self.__is_actual = True
            return self.__result


if __name__ == '__main__':
    try:
        reader_reader = TxtReader('my_file.txt')
        proxy = ProxyTxtRW(reader_reader)
        print(proxy.read())  # тут прочитали файл
        print(proxy.read())  # тут вже не читаємо, а забираємо текст файлу

        my_writer = TxtWriter("my_file.txt")
        my_proxy = ProxyTxtRW(my_writer)
        print(my_proxy.write("Hello"))
    except Exception as error:
        print(error)


