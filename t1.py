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
        return
    gr_t.used[v] = True
    gr_t.comps[c_num].append(v)
    gr_t.v_c[v] = c_num

    for u in gr_t.v[v]:
        dfs2(gr_t, u, c_num)

def comp_main(gr):
    gr_t = Graph()

    for u in gr.get_all_v():
        gr.used[u] = False
        gr_t.used[u] = False

    for v in gr.get_all_v():
        if (not gr.used[v]):
            dfs1(gr, v)
            print('dfs1 из', v)
            #  print('current order', gr.order)
            print('порядок:', gr.order)

    gr.order.reverse()
    #  print('true (reversed) order ', gr.order)
    print('обратный порядок', gr.order)

    for v in gr.get_all_v():
        gr_t.v[v] = []
    for v in gr.v:
        for u in gr.v[v]:
            gr_t.v[u].append(v)

    c_num = 0
    print('dfs2')
    for v in gr.order:
        if (not gr_t.used[v]):
            c_num += 1
            gr_t.comps[c_num] = []
            gr_t.cc[c_num] = set()
            dfs2(gr_t, v, c_num)

            print('->', v, end=", ")
            #  print('dfs2 из', v)
            #  print('got component ', c_num)
            #  print("it's vertexes ", gr_t.comps[c_num])
            print('новая компонента',c_num,'с вершинами',gr_t.comps[c_num])
            #  print("её вершины", gr_t.comps[c_num])
            #  print("it's c->c ", c_num, ' -> ', gr_t.cc[c_num])

    for v in gr_t.get_all_v():
        for u in gr_t.v[v]:
            v_num = gr_t.v_c[v]
            u_num = gr_t.v_c[u]
            gr_t.cc[v_num].add(u_num)


    print('комноненты')
    #  print('comps')
    for c in gr_t.comps:
        print(c, gr_t.comps[c], end= ", ")
    print()

    for c in gr_t.cc:
        for cs in gr_t.cc[c]:
            if cs not in gr.cc:
                gr.cc[cs] = set()
            gr.cc[cs].add(c)

    #  print('c -> c', gr.cc)
    print('метаграф', gr.cc)

#cut points
def dfs_ptr(gr, v, p=None):
    gr.used[v] = True
    gr.tin[v] = gr.timer
    gr.fup[v] = gr.timer
    print('dfs_ptr из', v, ', родитель', p, ', tin', gr.timer)
    #  print('dfs_ptr from', v, 'parent', p, 'tin', gr.timer, 'fup', gr.timer)
    gr.timer += 1
    kids = 0

    for to in gr.v[v]:
        if (to == p):
            continue
        if gr.used[to]:
            #  print('now v is', v)
            #  print('back edge', to, 'fup:', gr.fup[v])
            #  print('текущая вершина', v)
            old_fup = gr.fup[v]
            print('->', v)
            #  print('обр. ребро до', to, 'старый fup:', gr.fup[v], end=" ")
            gr.fup[v] = min(gr.fup[v], gr.tin[to])
            #  print('новый fup:', gr.fup[v])
            if gr.fup[v] != old_fup:
                print('обратное ребро до',to,'c новым fup:',gr.fup[v])

    for to in gr.v[v]:
        if (to == p):
            continue
        if not gr.used[to]:
            dfs_ptr(gr, to, v)
            old_fup = gr.fup[v]
            gr.fup[v] = min(gr.fup[v], gr.fup[to])
            #  print('now v is', v)
            #  print('forward edge',to,'old fup:',old_fup,'new fup:', gr.fup[v])
            #  print('текущая вершина', v)
            print('->', v)
            if gr.fup[v] != old_fup:
                print('прямое ребро до',to,'c новым fup:', gr.fup[v])
            if (gr.fup[to] >= gr.tin[v] and p is not None):
                print('to',to,'fup[to]:', gr.fup[to], '>= tin[v]', gr.tin[v])
                print(v, 'точка сочл.')
                #  print(v, 'is cut point')
                gr.cut_pnts.add(v)
            kids += 1

    if (p is None and kids > 1):
        print(v, 'точка сочл. как корень дфс с несколькими детьми')
        #  print(v, 'is cut point as root with several kids')
        gr.cut_pnts.add(v)

def dfs_br(gr, v, p=None):
    gr.used[v] = True
    gr.tin[v] = gr.timer
    gr.fup[v] = gr.timer
    #  print('dfs_br from', v,'parent',p,'tin', gr.timer, 'fup', gr.timer)
    print('dfs_br из', v,', родитель',p,', tin', gr.timer)
    gr.timer += 1

    for to in gr.v[v]:
        if (to == p):
            continue
        if gr.used[to]:
            #  print('now v is', v)
            #  print('back edge', to, 'fup:', gr.fup[v])
            #  print('текущая вершина', v)
            print('->', v)
            old_fup = gr.fup[v]
            #  print('обратное ребро до', to, 'старый fup:', old_fup, end=" ")
            gr.fup[v] = min(gr.fup[v], gr.tin[to])
            #  print('новый fup:', gr.fup[v])
            if gr.fup[v] != old_fup:
                print('обратное ребро до',to,'c новым fup:',gr.fup[v])
            #  print('new fup:', gr.fup[v])
    for to in gr.v[v]:
        if not gr.used[to]:
            dfs_br(gr, to, v)
            old_fup = gr.fup[v]
            gr.fup[v] = min(gr.fup[v], gr.fup[to])
            #  print('now v is', v)
            #  print('forward edge',to,'old fup:',old_fup,'new fup:',gr.fup[v])
            #  print('текущая вершина', v)
            print('->', v)
            if gr.fup[v] != old_fup:
                print('прямое ребро до',to,'c новым fup:',gr.fup[v])
            if (gr.fup[to] > gr.tin[v]):
                print('to',to,'fup[to]:', gr.fup[to], '>= tin[v]', gr.tin[v])
                #  print((v,to), 'is bridge')
                print((v,to), '- мост')
                gr.br.add((v,to))

def second_main(gr):
    print('cut points')
    for u in gr.get_all_v():
        gr.used[u] = False

    for u in gr.get_all_v():
        if not gr.used[u]:
            dfs_ptr(gr, u)

    print('cut points are')
    for v in gr.cut_pnts:
        print(v)

    print('bridges')
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

    print('block part')
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
    print("graph without cut points", b_gr.v)

    print('*' * 8)
    comp_main(b_gr)

if __name__ == '__main__':
#  E={AK, BC, BD, CA, CB, CK, DC, EA, EL, GA, GH, HA, JB, JI, LE, LJ}.

    gr = Graph()
    gr.v = { 'a' : ['k'], \
             'b' : ['c', 'd' ], \
             'c' : ['a', 'b', 'k'], \
             'd' : ['c', ], \
             'e' : ['a', 'l'], \
             'g' : ['a', 'h', ], \
             'h' : ['a', ], \
             'j' : ['b', 'i'], \
             #  'k' : ['g'], \
             'l' : ['e', 'j'], \
             #  'c' : [], \
           }
    gr.fill()
    comp_main(gr)

    gr = Graph()
    gr.v = { 'a' : ['k'], \
             'b' : ['c', 'd' ], \
             'c' : ['a', 'b', 'k'], \
             'd' : ['c', ], \
             'e' : ['a', 'l'], \
             'g' : ['a', 'h', ], \
             'h' : ['a', ], \
             'j' : ['b', 'i'], \
             #  'k' : ['g'], \
             'l' : ['e', 'j'], \
             #  'c' : [], \
           }
    gr.make_bidirectional()
    second_main(gr)

    #  gr = Graph()
    #  gr.v = { 'a' : ['f', 'j', 'k'], \
             #  'b' : ['l', ], \
             #  'd' : ['e'], \
             #  'g' : ['a', 'b'], \
             #  'h' : ['d', 'i'], \
             #  'i' : ['a', 'e', 'g'], \
             #  'j' : ['b', 'i'], \
             #  'k' : ['g'], \
             #  'l' : ['e'], \
             #  'c' : [], \
           #  }
    #  gr.fill()
    #  comp_main(gr)

    #  gr = Graph()
    #  gr.v = { 'a' : ['f', 'j', 'k'], \
             #  'b' : ['l', ], \
             #  'd' : ['e'], \
             #  'g' : ['a', 'b'], \
             #  'h' : ['d', 'i'], \
             #  'i' : ['a', 'e', 'g'], \
             #  'j' : ['b', 'i'], \
             #  'k' : ['g'], \
             #  'l' : ['e'], \
             #  'c' : [], \
           #  }
    #  gr.make_bidirectional()
    #  second_main(gr)
