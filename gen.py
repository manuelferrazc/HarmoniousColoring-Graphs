import random

sizes = [10, 20, 30, 40, 50]
edges = {
    0.01:'0.01',
    0.03:'0.03',
    0.05:'0.05',
    0.1 :'0.10',
    0.2 :'0.20',
    0.3 :'0.30'
}

def genGraph(n,e):
    x = []

    for i in range(n):
        for j in range(i+1,n):
            x.append((i+1,j+1))

    mx = n*(n-1)/2
    qtd = 0

    g = []

    while qtd/mx<e:
        i = random.randint(0,len(x)-1)
        g.append(x[i])

        x[i] = x[len(x)-1]
        x.pop()
        
        qtd+=1
    
    g.sort()
    
    return g


def printGraph(n,edges,filename):
    with open(filename,'w') as file:
        file.write(f'p edge {n} {len(edges)}\n')

        for a,b in edges:
            file.write(f'e {a} {b}\n')


def main():
    for n in sizes:
        for e in edges:
            for i in range(1,5):
                l = genGraph(n,e)

                printGraph(n,l,f'graphs/RAND{i}/{n}_{edges[e]}.txt')


if __name__=='__main__':
    main()