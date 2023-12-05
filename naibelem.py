spisok = list(map(int, input().split()))
max = spisok[0], 0
for dex, el in enumerate(spisok, start = 0):
    if el > max[0]:
        max = el, dex
print(' '.join(map(str, max)))