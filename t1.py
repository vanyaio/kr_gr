class Graph:
    def __init__(self):
        self.v = {}
        self.used = {}

        self.comps = {}
        self.v_c = {}
        self.cc = {}
        self.order = []

        self.tin = {}
        self.fup = {}

        self.cut_pnts = set()
        self.br = set()

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

        for v in self.get_all_v():
            self.tin[v] = None
        self.timer = 1


    def make_bidirectional(self):
        self.fill()
        for v in list(gr.v):
            for to in list(gr.v[v]):
                if to not in gr.v:
                    gr.v[to] = []
                if v not in gr.v[to]:
                    gr.v[to].append(v)


def dfs1(gr, v):
    if gr.used[v]:
        return
    gr.used[v] = True

    for u in gr.v[v]:
        dfs1(gr, u)

    gr.order.append(v)

def dfs2(gr_t, v, c_num):
    if gr_t.used[v]:
        return False
    gr_t.used[v] = True
    gr_t.comps[c_num].append(v)
    gr_t.v_c[v] = c_num

    for u in gr_t.v[v]:
        if not dfs2(gr_t, u, c_num):
            gr_t.cc[c_num].add(gr_t.v_c[u])

    return True

def comp_main(gr):
    gr_t = Graph()

    for u in gr.get_all_v():
        gr.used[u] = False
        gr_t.used[u] = False

    for v in gr.get_all_v():
        if (not gr.used[v]):
            dfs1(gr, v)
            print('dfs1 from ', v)
            print(gr.order)

    gr.order.reverse()
    print('true (reversed) order ', gr.order)
    for v in gr.v:
        for u in gr.v[v]:
            gr_t.v[u] = v

    c_num = 0
    for v in gr.order:
        if (not gr_t.used[v]):
            c_num += 1
            gr_t.comps[c_num] = []
            gr_t.cc[c_num] = set()
            dfs2(gr_t, v, c_num)

            print('dfs2 from ', v)
            print('got component ', c_num)
            print("it's vertexes ", gr_t.comps[c_num])
            print("it's c->c ", c_num, ' -> ', gr_t.cc[c_num])

    print('comps')
    for c in gr_t.comps:
        print(c, gr_t.comps[c])

    for c in gr_t.cc:
        for cs in gr_t.cc[c]:
            if cs not in gr.cc:
                gr.cc[cs] = set()
            gr.cc[cs].add(c)


    print('c -> c', gr.cc)

#cut points
def dfs_ptr(gr, v, p=None):
    gr.used[v] = True
    gr.tin[v] = gr.timer
    gr.fup[v] = gr.timer
    gr.timer += 1
    kids = 0

    for to in gr.v[v]:
        if (to == p):
            continue
        if gr.used[to]:
            gr.fup[v] = min(gr.fup[v], gr.tin[to])
        else:
            dfs_ptr(gr, to, v)
            gr.fup[v] = min(gr.fup[v], gr.fup[to])
            if (gr.fup[to] >= gr.tin[v] and p is not None):
               gr.cut_pnts.add(v)
            kids += 1

    if (p is None and kids > 1):
       gr.cut_pnts.add(v)

def dfs_br(gr, v, p=None):
    gr.used[v] = True
    gr.tin[v] = gr.timer
    gr.fup[v] = gr.timer
    gr.timer += 1

    for to in gr.v[v]:
        if (to == p):
            continue
        if gr.used[to]:
            gr.fup[v] = min(gr.fup[v], gr.tin[to])
        else:
            dfs_br(gr, to, v)
            gr.fup[v] = min(gr.fup[v], gr.fup[to])
            if (gr.fup[to] > gr.tin[v]):
               gr.br.add((v,to))

def second_main(gr):
    #cut points:
    for u in gr.get_all_v():
        gr.used[u] = False

    for u in gr.get_all_v():
        if not gr.used[u]:
            dfs_ptr(gr, u)

    print('cut points are')
    for v in gr.cut_pnts:
        print(v)

    #bridges
    for v in gr.get_all_v():
        gr.tin[v] = None
    gr.fup = {}

    for u in gr.get_all_v():
        gr.used[u] = False

    for u in gr.get_all_v():
        if not gr.used[u]:
            dfs_br(gr, u)

    print('bridges are')
    for e in gr.br:
        print(e)

    #block part
    b_gr = Graph()
    for v in gr.get_all_v():
        if v in gr.cut_pnts:
            continue
        b_gr.v[v] = []
        for u in gr.v[v]:
            if u in gr.cut_pnts:
                continue
            b_gr.v[v].append(u)
    b_gr.make_bidirectional()
    print("graphy without cut points", b_gr.v)

if __name__ == '__main__':
    #  gr = Graph()
    #  gr.v = { 'a' : ['b', 'c'], 'b' : ['a'], 'c' : ['x'], }
    #  gr.fill()
    #  comp_main(gr)

    #  gr = Graph()
    #  gr.v = { 'a' : ['b', 'c'], 'b' : ['a'], 'c' : ['x'], 'x' : [] }

    gr = Graph()
    #  gr.v = { 'a' : ['c', 'b'], 'b' : ['x', 'a'], 'c' : ['d', 'b'], \
            #  #  'a1' : ['c1'], 'b1' : ['c1'], 'c1' : ['d1'], \
            #  }  #'x' : [] }
    gr.v = { 'a' : ['c', 'b', 'd', 'f'], 'b' : ['c'], 'd' : ['f'] \
            #  'a1' : ['c1'], 'b1' : ['c1'], 'c1' : ['d1'], \
            }  #'x' : [] }
    gr.make_bidirectional()
    second_main(gr)
