import match

def main_while(mat):
    n = len(mat)
    m = len(mat[0])

    #  print('stepped in while')
    #  for i in range(n):
        #  print(mat[i])

    gr = match.Graph()

    for i in range(n):
        v = 'l_' + str(i + 1)
        gr.l.add(v)
        gr.v[v] = []
    for j in range(m):
        v = 'r_' + str(j + 1)
        gr.r.add(v)
        gr.v[v] = []

    for i in range(n):
        v = 'l_' + str(i + 1)
        for j in range(m):
            u = 'r_' + str(j + 1)
            if mat[i][j] == 0:
                gr.v[v].append(u)
                gr.v[u].append(v)
    #  print(gr.v)

    match.main(gr)
    c_s = match.contr_set(gr)
    print("contr set is ", c_s)
    if len(c_s) == n:
        return False

    mn = 10000000000
    for i in range(n):
        for j in range(m):
            v = 'l_' + str(i + 1)
            u = 'r_' + str(j + 1)
            if (v not in c_s) and (u not in c_s):
                if mat[i][j] < mn:
                    mn = mat[i][j]
    for i in range(n):
        for j in range(m):
            v = 'l_' + str(i + 1)
            u = 'r_' + str(j + 1)
            if (v not in c_s) and (u not in c_s):
                mat[i][j] = mat[i][j] - mn
            if (v in c_s) and (u in c_s):
                mat[i][j] = mat[i][j] + mn

    #  print('stepped out while')
    #  for i in range(n):
        #  print(mat[i])

    return True

def main(mat):
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        mn = 100000000000
        for j in range(m):
            if mat[i][j] < mn:
                mn = mat[i][j]
        for j in range(m):
            mat[i][j] = mat[i][j] - mn

    while (main_while(mat)):
        continue

    for i in range(n):
        print(mat[i])

if __name__ == "__main__":
    #  mat = [
            #  [24, 10, 21, 11], \
            #  [14, 22, 10, 15], \
            #  [15, 17, 20, 19], \
            #  [11, 19, 14, 13], \
        #  ]
    mat = [
            [32, 11, 19, 18, 44, 65, 23, 18], \
            [41, 54, 23, 19, 87, 16, 25, 33], \
            [47, 34, 41, 26, 15, 47, 29, 52], \
            [73, 14, 10, 0, 12, 29, 33, 50], \
            [37, 33, 18, 29, 26, 26, 26, 41, 84], \
            [72, 61, 38, 96, 26, 14, 55, 47], \
            [38, 17, 26, 49, 28, 91, 97, 24], \
            [32, 52, 67, 71, 33, 56, 54, 22], \
        ]

    main(mat)
