def binary_search(list, item): # prerequisite: `list` must be a sorted array
    low = 0
    high = len(list) - 1

    while low <= high: # narrow from the left and the right of the list until the item is found or the last element, which is in (low = high)th element in the list
        mid = (low + high) // 2 # `//` -> means floor division (or integer division???)
        guess = list[mid]
        if guess == item: # the guess matches the searched item, return the position
            return mid
        if guess > item: # the guess is high, drop away the right side of the array
            high = mid - 1
        else:
            low = mid + 1 # the guess is low, drop away the left side of the array
        
    return None # item does not exist in the list
    

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # -> must return 1, which is index of 3