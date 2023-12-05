spisok = list(map(int, input().split()))
count = 0
for el in spisok:
    if el > 0:
        count += 1
print(count)   