from math import pi
t = [20.88,
19.42,
18.55,
17.95,
17.65,
16.81,
15.77]
T = []
for i in t:
    T.append(i / 15)
g = []
for i in T:
    print(i**2)

print('lf')
print()

for i in t:
    print(0.1/i)

print('fl')
print()

I = [0.05874486999999999,
0.029029720000000002,
0.02373167]
for i in I:
    print(i * 0.008)

print()
print('fl')
print()


g = ((2 * pi) ** 2) / 3.932
print(g)

print('sdf')
print()

E = [0.010, 0.010, 0.010, 0.012, 0.012, 0.012, 0.012]
for i in range(len(T)):
    print(T[i] ** 2 * E[i])