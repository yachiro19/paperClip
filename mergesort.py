def merge_sort(items):
    if len(items) <= 1:
        return list(items)

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return _merge(left, right)


def _merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if right[j] < left[i]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged