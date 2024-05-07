def f(array):
    flag = 0
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            flag = 1
            break
    if flag == 0:
        print(array)
    else:
        return f(array)

a = [2, 3, 1, 6, 3, 2]
f(a)