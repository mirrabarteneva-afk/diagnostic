def has_pair(items, target):
    for i in range(len(items) - 1):
        if (items[i] + items[-i-1] == target) and items[i] != items[-i]:
            return True
    return False

print(has_pair([3, 1, 4, 2], 5))
print(has_pair([1, 2, 3], 10))
print(has_pair([4, 4, 1], 8))