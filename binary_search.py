def binarySearch(books, target):
    left = 0
    right = len(books) - 1

    while left <= right:
        middle = (left+right)//2

        if books[middle] == target:
            return middle
        elif books[middle] < target:
            left = middle+1
        else:
            right = middle-1

    return -1

books = sorted(['apple_book', 'orange_book', 'durian_book', 'mango_book'])
target = 'orange_book'
result = binarySearch(books, target)
if result == -1:
    print("No such book in the list!")
else:
    print('Book found at index {0}'.format(result))
    print('The book name is {0}'.format(books[result]))