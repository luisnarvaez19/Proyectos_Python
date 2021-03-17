# El elemento más grande presente en una lista de números
def max_recursive(listElements):
    if len(listElements) == 1:
        return listElements.pop()
    else:
        elem = listElements.pop()
        return max_2_numbers(max_recursive(listElements), elem)



def max_2_numbers(number1, number2):
    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        raise TypeError("TypeError. max_2_numbers receives 2 numbers")
    elif number1 < number2:
        return number2
    else:
        return number1


def main():
    my_list = [1, 11, 19, 13, 17, 2]
    maximo = max_recursive(my_list)
    print(maximo)  # maximo debe ser 19


if __name__ == "__main__":
    main()

'''
[1, 11, 19, 13, 17, 2]

[1, 11, 19, 13, 17]
        
[1, 11,  19, 13]

.
.
.

[1 ]


50 20 8 4 13 2 2 16 8 9 85

20 8 4 13 2 2 16 8 9 50 85
8 4 13 2 2 16 8 9 20 50 85
4 8 2 2 13 8 9 16 20 50 85
4 2 2 8 8 9 13 16 20 50 85
2 2 4 8 8 9 13 16 20 50 85
2 2 4 8 8 9 13 16 20 50 85

50 20 8 4 13 2 2 16 8 9 85
2 20 8 4 13 50 2 16 8 9 85
2 2  8 4 13 50 20 16 8 9 85
2 2 4 8 13 50 20 16 8 9 85
2 2 4 8 8 50 20 16 13 9 85
2 2 4 8 8 9 20 16 13 50 85
2 2 4 8 8 9 13 16 20 50 85
2 2 4 8 8 9 13 16 20 50 85


'''
