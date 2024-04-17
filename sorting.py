import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    data = dict()
    with open(file_name) as file:
        reader = csv.reader(file)
        for row_num , row in enumerate(reader):
            #print(row)
            if row_num == 0:
                row1 = row
                for value in row:
                    data[value] = []
            else:
                for key, value in zip(row1, row):
                    data[key].append(int(value))
    #print(data)
    return data


numbers = read_data("numbers.csv")

# def selection_sort(data):
#     #print(numbers)
#     j = 0
#
#     for k in range(len(numbers.keys())):
#
#         for value2 in numbers.values():
#             for i in range(len(value2)):
#                 if value2[i] > value2[0 + j]:
#                     pomocna = value2[i]
#                     value2[i] = value2[0+j]
#                     value2[0+j] = pomocna
#                 j = j + 1
#                 print(value2)
#
#
# sorted = selection_sort(numbers)
hod = [2 , 5 , 1 , 8 , 3 , 9 , 1 , 6 ]
# def buuble_sort(data):
#     n = len(data)
#     for i in range(n):
#         for j in range( n - i -1):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#
#     print(data)
# buuble_sort(hod)
# def insertion_sort(data):
#     for i in range(len(data)):
#         for j in range(len(data)-1):
#             while data[j +1] < data[j]:
#                 data[j +1], data[j] = data[j], data[j + 1]
#     print(data)
#
#
# insertion_sort(hod)
def merge_sort(data):


merge_sort(hod)
def main():
    pass


if __name__ == '__main__':
    main()


