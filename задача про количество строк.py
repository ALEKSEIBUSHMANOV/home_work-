
with open("1.txt", 'r', encoding='utf-8') as f1:
    count_1 = 0
    for i in f1:
        count_1 = count_1+1
    f1.seek(0)
    a = f1.read()

with open("2.txt", 'r', encoding='utf-8') as f2:
    count_2 = 0
    for i in f2:
        count_2 = count_2 + 1
    f2.seek(0)
    b = f2.read()

with open("3.txt", 'r', encoding='utf-8') as f3:
    count_3 = 0
    for i in f3:
        count_3 = count_3 + 1
    f3.seek(0)
    c = f3.read()

with open("file.txt", 'w', encoding='utf-8') as f:
    if count_2 < count_1 < count_3:
        f.write(f'2.txt\n {count_2}\n')
        f.write(b)
        f.write(f'1.txt\n {count_1}\n')
        f.write(a)
        f.write(f'3.txt\n {count_3}\n')
        f.write(c)
    elif count_1 < count_2 < count_3:
        f.write(f'1.txt\n {count_1}\n')
        f.write(a)
        f.write(f'2.txt\n {count_2}\n')
        f.write(b)
        f.write(f'3.txt\n {count_3}\n')
        f.write(c)
    elif count_1 < count_3 < count_2:
        f.write(f'1.txt\n {count_1}\n')
        f.write(a)
        f.write(f'3.txt\n {count_3}\n')
        f.write(c)
        f.write(f'2.txt\n {count_2}\n')
        f.write(b)
    elif count_2 < count_3 < count_1:
        f.write(f'2.txt\n {count_2}\n')
        f.write(b)
        f.write(f'3.txt\n {count_3}\n')
        f.write(c)
        f.write(f'1.txt\n {count_1}\n')
        f.write(a)
    elif count_3 < count_1 < count_2:
        f.write(f'3.txt\n {count_3}\n')
        f.write(c)
        f.write(f'1.txt\n {count_1}\n')
        f.write(a)
        f.write(f'2.txt\n {count_2}\n')
        f.write(b)
    elif count_3 < count_2 < count_1:
        f.write(f'3.txt\n {count_3}\n')
        f.write(c)
        f.write(f'2.txt\n {count_2}\n')
        f.write(b)
        f.write(f'1.txt\n {count_1}\n')
        f.write(a)




