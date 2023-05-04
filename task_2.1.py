# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


arr = [[4,6,2,1,9,63,-134,566], [-52, 56, 30, 29, -54, 0, -110], [42, 54, 65, 87, 0], [5]]

def insertion(arr):
  for i in range(len(arr)):
    j = i - 1
    key = arr[i]
    while arr[j] > key and j >= 0:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr

def minimum(arr):
  for arr in arr:
    print('В списке', arr, 'min =', insertion(arr)[0])

def maximum(arr):
  for arr in arr:
    print('В списке', arr, 'max =', insertion(arr)[len(arr)-1])

def main():
  print(maximum(arr))
  print(minimum(arr))

print(main())