import argparse

parser = argparse.ArgumentParser()
parser.add_argument("graph_file", help="name of input graph file")
parser.add_argument("size_of_truss", help="choose size of truss",
                    type=int)

args = parser.parse_args()
f = open(args.graph_file)
k = args.size_of_truss

#Create graph-adjacency lists with dictionary
graph={}
for line in f:
    l = line.rstrip()
    parts = l.split(' ')
    key=int(parts[0])
    value=int(parts[1])
    if key not in graph:
        graph[key] = []
    if value not in graph:
        graph[value] = []
    if value not in graph[key]:
        graph[key].append(value)
    if key not in graph[value]:
        graph[value].append(key)
f.close()

#Algorithm to reduce graph to k-truss
def intersection(a, b):
    combs=[]
    for x in a:
        for y in b:
            if x==y:
                combs.append(x)
    return combs

def reduce(graph, k):
    newgraph=graph
    change = 'true'
    while (change=='true'):
        change='false'
        for node in graph:
            for edge in graph[node]:
                intlist=intersection(graph[node], graph[edge])
                length=len(intlist)
                if length < k-2:
                    newgraph[node].remove(edge)
                    newgraph[edge].remove(node)
                    change='true'
    create_output(newgraph)
    return newgraph

#Create the final output, so that each k-truss is printed only once and all k-trusses are sorted and printed with the requested format.
def create_output(g):
    sg={}
    for node in g:
        sg[node]=[node]
        for edge in g[node]:
            if len(g[node])!= 0:
                sg[node].append(edge)
        sg[node].sort(key=None, reverse=False)
    sg=sorted(sg.values())
    for node in range(len(sg)):
        if len(sg[node])>1:
            if  node>0:
                if sg[node]!=sg[node-1]:
                    print('(', end='')
                    print(", ".join(map(str, sg[node])), end='')
                    print(')')

            else:
                    print('(', end='')
                    print(", ".join(map(str, sg[node])), end='')
                    print(')')

    return sg

reduce(graph, k)
