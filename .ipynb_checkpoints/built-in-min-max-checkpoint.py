# use 12, 37, 36 for maximum numbers when running

def maximum(value1, value2, value3):
    """Return the maximum value of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return print(max_value)

if __name__ == "__main__":
    import sys
    maximum(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))


print('The min value is', min([15, 9, 27, 14]))

print('The max value is', max([12, 27, 36]))


#Loni Wood
    