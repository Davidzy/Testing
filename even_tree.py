n, m = [int(x) for x in raw_input().strip().split()]
nodes = []
edges = []
tree = {}
for i in xrange(m):
    cnode, pnode = [int(x) for x in raw_input().strip().split()]
    cnode = cnode - 1
    pnode = pnode - 1
    if not cnode in nodes: nodes.append(cnode)
    if not pnode in nodes: nodes.append(pnode)
    if not [cnode, pnode] in edges: edges.append([cnode, pnode])
    if not pnode in tree:
        tree[pnode] = [cnode]
    else: 
        tree[pnode].append(cnode)
nodes.sort()

def child_num(v, tree):
    num = 1
    if not v in tree:
        return num
    else:
        for vc in tree[v]:
            num += child_num(vc, tree)
        return num
asroot = [child_num(i, tree) for i in nodes]

num_cut = 0
for edge in edges:
    if asroot[edge[0]] % 2 == 0:
        num_cut += 1
        
print num_cut

