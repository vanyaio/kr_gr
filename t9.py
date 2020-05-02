import match

def main(gr):
    d_gr = match.Graph()
    for v in gr.get_all_v():
        vr = v + '_R'
        vl = v + '_L'
        d_gr.v[vr] = []
        d_gr.v[vl] = []

    for v in gr.get_all_v():

        if (not v in gr.v):
            continue

        vl = v + '_L'
        for u in gr.v[v]:
            ur = u + '_R'
            ul = u + '_L'

            d_gr.v[vl].append(ur)
            #  d_gr.v[vl].append(ur)

            #  d_gr.v[ul].append(vr)
            #  d_gr.v[ul].append(vr)


    #  for v in list(d_gr.v):
        #  for to in list(d_gr.v[v]):
            #  if to not in d_gr.v:
                #  d_gr.v[to] = []
            #  d_gr.v[to].append(v)
    print(d_gr.v)

    match.main(d_gr)
    for v in d_gr.get_all_v():
        if v[-1] == 'R':
            d_gr.r.add(v)
        else:
            d_gr.l.add(v)

    c_s = match.contr_set(d_gr)
    print("contr set is ", c_s)

if __name__ == "__main__":
    gr = match.Graph()

    gr.v = {'a' : ['e', 'b', 'g', 'f'], \
            'f' : ['c'], \
            'e' : ['d', 'c'], \
            'g' : ['d', 'f', 'h'], \
            'd' : ['f'], \
            }

    main(gr)
