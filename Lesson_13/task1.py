# 1 - Implement adapter patter from_txt_to_html
#
# for example, we have a such structure in txt:
#
# name,last_name,age,salary
# John,Malkovich,28,1000
# I want to see:
#
# <name>John</name>
# <last_name>Malkovich</last_name>
# .............
# It should work with any file with such a structure

class TxtToHtmlAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def txt_to_html(self):
        with open(self.__file_path, "r") as file:
            lines = file.readlines()

        header = lines[0].replace("\n", "").split(",")
        user_info = [user.replace("\n", "").split(",") for user in lines[1:]]
        html_result = []

        for user in user_info:
            for i in range(len(header)):
                html_result.append(f"<{header[i]}>{user[i]}</{header[i]}>")
        return "\n".join(html_result)


if __name__ == '__main__':
    try:
        my_file = TxtToHtmlAdapter("user_info.txt")
        print(my_file.txt_to_html())

    except Exception as error:
        print(error)
