def quick_sort(integers: list[int]) -> list[int]:
    if len(integers) <= 1:
        return integers
    pivot = integers[0]
    left = [x for x in integers[1:] if x < pivot]
    right = [x for x in integers[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
