class Graph:
    def __init__(self):
        self.v = {}
        self.used = {}
        self.comps = {}
        self.v_c = {}
        self.cc = {}
        self.order = []

    def get_all_v(self):
        res = set()
        for v in self.v:
            res.add(v)
            for u in self.v[v]:
                res.add(u)
        return res

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

def main(gr):
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

if __name__ == '__main__':
    gr = Graph()
    gr.v = { 'a' : ['b', 'c'], 'b' : ['a'], 'c' : ['x'], 'x' : [] }
    main(gr)
