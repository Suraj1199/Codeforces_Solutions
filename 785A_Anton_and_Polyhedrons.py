h = {'Tetrahedron': 4, 'Cube' : 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
n = int(input())
s = 0
for _ in range(n):
    s += h[input()]
print(s)