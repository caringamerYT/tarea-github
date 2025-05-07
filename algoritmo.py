n = 1203

for i in range(0, len(n)):
    num = n[i]
    num_str = str(num)

    digits = []
    for d in num_str:
        digits.append(int(d))
        print (d, digits)
