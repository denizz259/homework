# my_list = range(0, 10)
# try:
#     request_item = int(input("What list element do you need?\n"))
# except ValueError:
#     request_item = 1
# try:
#     print(f"This list value is {my_list[request_item]}")
# except IndexError as e:
#     print(e)

# number_1 = input("Enter first number\n")
# number_2 = input("Enter second number\n")
#
# try:
#     number_1 = int(number_1)
# except ValueError:
#     print("First number value is not a number")
# try:
#     number_2 = int(number_2)
# except ValueError:
#     print("Second number value is not a number")

# doc_name = input('Enter doc name\n')+'.txt'
# try:
#     f = open(doc_name, 'r+')
# except FileNotFoundError:
#     print(f"File with this name doesn't exist. Please check spelling for {doc_name}")


# def divider(a: int, b: int):
#     result = int
#     try:
#         result = a/b
#
#     except ZeroDivisionError:
#         return print("Can't divide by 0, please change the second number")
#
#     except TypeError:
#         return print('Both numbers you enter must be NUMBERS')
#     else:
#         return print(result)
#
#
# divider(8, 0)
# divider(8, 2)
# divider('t', 4)
# divider('t', 0)
# divider(0, 5)

#
# f = open('exam.txt', "r")
# text_whole = f.read()
# text_list = text_whole.split()
# f.close()
#
# while True:
#     try:
#         text_list.remove(".")
#     except ValueError:
#         break
# while True:
#     try:
#         text_list.remove("-")
#     except ValueError:
#         break
# while True:
#     try:
#         text_list.remove(",")
#     except ValueError:
#         break
#
# print(text_list)
# print(len(text_list))

# def input_file(a: str):
#
#     try:
#         f = open(a+".txt", 'r')
#     except FileNotFoundError:
#         return print('File not found')
#     else:
#         f.close()
#         f = open(a+'.txt', 'a')
#         user_text = input('Enter your text:\n') + '\n'
#         f.write(user_text)
#         f.close()
#         return print('Sucess')
#
#
# input_file('random')

def text_migration(a: str, b: str):

    try:
        file_1 = open(a+".txt", "r")
    except FileNotFoundError:
        return print(f'File not found, please check typing{a}')
    try:
        file_2 = open(b+".txt", "r")
    except FileNotFoundError:
        return print(f'File not found, please check typing{b}')
    else:
        file_2.close()

        file_2 = open(b+".txt", "a+")
        file_1.seek(0)
        file_2.writelines(file_1.readlines())
    file_2.seek(0)
    file_1.close()

    return print(file_2.read()), file_2.close()


text_migration("exam5", "test")



















