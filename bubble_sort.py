# This is Bubble Sort function
def bubble_sort2(ls):
    swapped = True
    for r1 in range(len(ls)-1, 0, -1):
        # print(i)
        if swapped==False:
            break
        swapped = False
        for r2 in range(r1):
            if ls[r2] > ls[r2+1]:
                ls[r2], ls[r2 + 1] = ls[r2 + 1], ls[r2]
                # Set the flag to True so we'll loop again
                swapped = True


# Test function
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort2(random_list_of_nums)
print(random_list_of_nums)