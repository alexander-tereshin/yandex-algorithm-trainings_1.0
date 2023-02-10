# Бригада скорой помощи выехала по вызову в один из отделенных районов. 
# К сожалению, когда диспетчер получил вызов, он успел записать только адрес дома и номер квартиры K1, а затем связь прервалась. 
# Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь выезжала в квартиру K2, которая расположена в подъезда P2 на этаже N2. 
# Известно, что в доме M этажей и количество квартир на каждой лестничной площадке одинаково. 
# Напишите программу, которая вычилсяет номер подъезда P1 и номер этажа N1 квартиры K1.



import math

k1, m, k2, p2, n2 = list(map(int, input().split()))

if k1 != k2:

    # list with all possible options of number of flats per floor
    ls = []

    for i in range(1, 1001):
        if math.ceil(math.ceil(k2 / i) / m) == p2 and math.ceil((k2 - (i * m) * (p2 - 1)) / i) == n2:
            ls.append(i)

    if len(ls) == 0:
        print(-1, -1)

    elif len(ls) == 1:
        x = ls[0]
        p1 = math.ceil(math.ceil(k1 / x) / m)
        n1 = math.ceil((k1 - (x * m) * (p1 - 1)) / x)
        print(p1, n1)

    else:
        p1_vals = set()
        n1_vals = set()

        for i in ls:
            p1 = math.ceil(math.ceil(k1 / i) / m)
            n1 = math.ceil((k1 - (i * m) * (p1 - 1)) / i)
            p1_vals.add(p1)
            n1_vals.add(n1)

        if len(p1_vals) > 1 and len(n1_vals) > 1:
            print(0, 0)

        elif len(p1_vals) == 1 and len(n1_vals) > 1:
            print(*p1_vals, 0)

        elif len(p1_vals) > 1 and len(n1_vals) == 1:
            print(0, *n1_vals)
        else:
            print(*p1_vals, *n1_vals)

else:
    ls = []
    for i in range(1, 1001):
        if math.ceil(math.ceil(k2 / i) / m) == p2 and math.ceil((k2 - (i * m) * (p2 - 1)) / i) == n2:
            ls.append(i)

    if len(ls) == 0:
        print(-1, -1)
    else:
        print(p2, n2)
