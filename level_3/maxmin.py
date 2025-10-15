def maxmin(arr):
    max=arr[0]
    min=arr[0]
    for num in arr:
        if num>max:
            max=num
        if num<min:
            min=num
    
    return [min, max]


print('enter a list of numbers separated by commas e.g. 1,2,3')
s=input()
arr= [int(x) for x in s.split(",")]
print(f'the minimum and maximum numbers in your list are: {maxmin(arr)}')
