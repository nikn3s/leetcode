# You are given a list if numbers
# Your task is to move the zeros to the end of the list
# Catch: You must not duplicate the list 

def moveZeros(arr: list):
    for i in arr:
        if i == 0:
            arr.append(i)
            arr.remove(i)
    return arr

move = moveZeros([0,1,0,3,12])
print(move)
