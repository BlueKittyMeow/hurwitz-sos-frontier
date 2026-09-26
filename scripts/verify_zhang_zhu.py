"""Independent exact check of Zhang–Zhu arXiv:2605.00590v2 (2026), (3.2).
Transcribed from the public HTML and cross-checked against PDF p. 6.
Gaussian integers are pairs of Python integers. No floating-point arithmetic.
"""
from itertools import product
ARRAY = '''
A 2 3 4 5 6 7 8 9 10 11 12
-2 A -4 3 -6 5 8 -7 -10 9 -12 11
-3 4 A -2 -7 -8 5 6 11 -12 -9 10
-4 -3 2 A -8 7 -6 5 -12 -11 10 9
5 -6 -7 -8 B 2 3 4 13 14 15 16
6 5 -8 7 -2 B -4 3 -14 13 -16 15
7 8 5 -6 -3 4 B -2 15 -16 -13 14
8 -7 6 5 -4 -3 2 B -16 -15 14 13
-9 10 -11 12 -13 14 -15 16 C -2 3 -4
-10 -9 12 11 -14 -13 16 15 2 C -4 -3
-11 12 9 -10 -15 16 13 -14 -3 4 C -2
-12 -11 -10 -9 -16 -15 -14 -13 4 3 2 C
'''
def vec(token):
    v = [(0, 0)] * 18
    if token == 'A': v[0] = (1, 0)
    elif token == 'B': v[:3] = [(-1, 0), (1, 0), (0, 1)]
    elif token == 'C': v[:3] = [(1, 0), (1, 0), (0, -1)]
    else:
        t = int(token)
        v[abs(t)+1] = (1 if t > 0 else -1, 0)
    return v
V = [[vec(t) for t in line.split()] for line in ARRAY.strip().splitlines()]
assert len(V) == 12 and all(len(row) == 12 for row in V)
def dot(u, v):
    return (sum(a*c-b*d for (a,b),(c,d) in zip(u,v)),
            sum(a*d+b*c for (a,b),(c,d) in zip(u,v)))
def add(u,v): return (u[0]+v[0],u[1]+v[1])
checks = 0
for i,j,k,l in product(range(12),repeat=4):
    actual = add(dot(V[i][j],V[k][l]),dot(V[i][l],V[k][j]))
    expected = (2*int(i==k)*int(j==l),0)
    assert actual == expected, (i+1,j+1,k+1,l+1,actual,expected)
    checks += 1
print(f'PASS: {checks} exact Gaussian-integer coefficient equations for [12,12,18].')
print('The first 11 rows and columns also satisfy the equations, proving the stated restriction [11,11,18].')
