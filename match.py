class Graph:
    def __init__(self):
        self.v = {}
        self.l = set()
        self.r = set()
        self.used = {}
        self.match = {}

    def get_all_v(self):
        res = set()
        for v in self.v:
            res.add(v)
            for u in self.v[v]:
                res.add(u)
        return res

    def fill(self):
        for v in self.get_all_v():
            if v not in gr.v:
                gr.v[v] = []

    def make_bidirectional(self):
        self.fill()
        for v in list(gr.v):
            for to in list(gr.v[v]):
                if to not in gr.v:
                    gr.v[to] = []
                if v not in gr.v[to]:
                    gr.v[to].append(v)

def dfs(gr, v, q):
    if gr.used[v]:
        return False
    q.append(v)
    gr.used[v] = True

    if gr.match[v] is not None:
        u = gr.match[v]
        if gr.used[u]:
            for to in gr.v[v]:
                if (gr.match[to] is None):
                    gr.match[to] = v
                    gr.match[v] = to
                    q.append(to)
                    return True
                elif dfs(gr, to, q):
                    gr.match[v] = to
                    gr.match[to] = v
                    return True
        else:
            if dfs(gr, u, q):
                gr.match[v] = None
                return True
    else:
        for to in gr.v[v]:
            if gr.match[to] is None:
                gr.match[v] = to
                gr.match[to] = v
                q.append(to)
                return True
            elif dfs(gr, to, q):
                gr.match[v] = to
                gr.match[to] = v
                return True

    q.pop()
    return False

def main(gr):
    #  for v in gr.v:
        #  gr.match[v] = None
        #  for u in gr.v[v]:
            #  gr.match[u] = None
    for v in gr.get_all_v():
        gr.match[v] = None 


    for v in gr.v:
        if gr.match[v] is not None:
            continue
        for u in gr.v[v]:
            if gr.match[u] is None:
                gr.match[u] = v
                gr.match[v] = u
                break

    print('curr gr:')
    print_gr(gr)
    print('________________')
    for v in gr.v:
        #  for u in gr.v:
        for u in gr.get_all_v():
            gr.used[u] = False
        q = []
        if gr.match[v] is not None:
            continue
        if dfs(gr, v, q):
            print('dfs from ', v, 'and q is')
            print(q)
            print('curr gr:')
            print_gr(gr)
            print('________________')


def contr_set(gr):
    newgr = {}
    for v in gr.v:
        newgr[v] = []

    for l in gr.l:
        for r in gr.v[l]:
            if gr.match[l] is not None and gr.match[l] == r:
                newgr[r].append(l)
            else:
                newgr[l].append(r)
    used = {}
    for u in gr.v:
        used[u] = False

    for l in gr.l:
        if gr.match[l] is None:
            q = []
            dfs_contr_set(l, newgr, used, q)
            print('contr set: start dfs from', l)
            print('added vertexes ', q)
            print('*********')

    lp = set()
    rp = set()
    lm = set()
    rm = set()
    for v in used:
        if used[v] and v in gr.l:
            lp.add(v)
        if used[v] and v in gr.r:
            rp.add(v)
        if (not used[v]) and v in gr.l:
            lm.add(v)
        if (not used[v]) and v in gr.r:
            rm.add(v)

    print('l- is ', lm)
    print('r+ is ', rp)
    return lm.union(rp)


def dfs_contr_set(v, newgr, used, q):
    if used[v]:
        return False
    used[v] = True
    q.append(v)

    for u in newgr[v]:
        dfs_contr_set(u, newgr, used, q)

def print_gr(gr):
    for v in gr.v:
        if (gr.match[v] is not None):
            print(v, gr.match[v])


if __name__ == "__main__":
    gr = Graph()

    #  gr.v = {'A' : ['g', 'h'], \
            #  'B' : ['a', 'c', 'f', 'h', 'j'], \
            #  'C' : ['g'], \
            #  'D' : ['a', 'g', 'h', 'i'], \
            #  'E' : ['d', 'g'], \
            #  'F' : ['d', 'f', 'h'], \
            #  'G' : ['d'], \
            #  'H' : ['b', 'j'], \
            #  'I' : ['a', 'c', 'e', 'h'], \
            #  'J' : ['d', 'e'] \
           #  }

    #  gr.l = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    #  gr.r = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

    gr.v = { \
            'x1' : ['y3', 'y5', 'y10'], \
            'x2' : ['y3'], \
            'x3' : ['y5', 'y7', 'y10'], \
            'x4' : ['y1'], \
            'x5' : ['y10'], \
            'x6' : ['y6', 'y7'], \
            'x7' : ['y3', 'y5'], \
            'x8' : ['y4', 'y5', 'y6', 'y8'], \
            'x9' : ['y2', 'y4', 'y8'], \
            'x10' : ['y4', 'y7', 'y10'], \
           }

    gr.l = set(['x1','x2', 'x3','x4','x5','x6','x7','x8','x9','x10'])
    gr.r = set(['y1','y2', 'y3','y4','y5','y6','y7','y8','y9','y10'])

    #  make bidirecional
    #  for v in list(gr.v):
        #  for to in list(gr.v[v]):
            #  if to not in gr.v:
                #  gr.v[to] = []
            #  gr.v[to].append(v)

    gr.make_bidirectional()
    main(gr)
    c_s = contr_set(gr)
    print("contr set is ", c_s)
