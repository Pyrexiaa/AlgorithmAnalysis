def binary_search(arr, target):
   count = 0;
   left = 0
   right = len(arr) - 1

   while left <= right:
        middle = (left+right)//2

        if arr[middle] == target:
            return count
        elif arr[middle] < target:
            count += 1
            left = middle+1
        else:
            count +=1
            right = middle-1

   return -1 

# Example usage:
arr = [str(num).zfill(3) for num in range(1000)]
password = '500'
index = binary_search(arr, password)
if index != -1:
   print("Target found after "+ str(index)+" trials")
else:
   print("Target not found")
