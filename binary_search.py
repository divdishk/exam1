# Divdish Kaur
# Algorithm Homework 1


def binary_search(file_name, target):
    lines_array = [] 

    try:
        with open("number.txt", "r") as file:
            lines_array = file.readlines()

        left = 0
        right = len(lines_array) - 1

        while left <= right:
            mid = (left + right ) // 2
            current = int(lines_array[mid].strip())

            if current == int(target):
                return target
            elif int(target) < current:
                right = mid - 1
            else:
                left = mid + 1

        return "{target} not found in the file."
    
    except:
        print ("File Not Found.")

target_value = '51216352'
file_name = "number.txt"
result = binary_search(file_name,target_value)
print(result)