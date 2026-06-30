 print(list(range(1, 100)))

total = 0
for e in range(1, 100):
    if e % 3 == 0 or e % 5 == 0:
        total += e
print(total)