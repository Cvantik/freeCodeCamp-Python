def selection_sort(list_of_items:list):
    for i in range(len(list_of_items)):
        min_index = i
        for j in range(i + 1 ,len(list_of_items)):
            if list_of_items[j] < list_of_items[min_index]:
                min_index = j
        if min_index != i:
            list_of_items[i], list_of_items[min_index] = list_of_items[min_index], list_of_items[i]
    return list_of_items