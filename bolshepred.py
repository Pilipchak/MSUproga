spisok = list(map(int, input().split()))
for i in range(1, len(spisok)):
    if spisok[i - 1] < spisok[i]:
        print(spisok[i], end = " ")
