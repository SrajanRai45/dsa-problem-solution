#def merge_srot(a,b):
#    for i in a:
#        b.append(i)
#    b.sort()
#    return b.copy()
lista = [1,2,3,4,5,6,7,8,9]
#listb = [32,354,878,89,342]
#print(merge_srot(lista,listb))
listb = [11,12,13,14,15]

def merge_sorted(a, b):
    i, j = 0, 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # Append remaining elements if any
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
print(merge_sorted(lista,listb))

