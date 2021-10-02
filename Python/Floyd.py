def main():
    n=eval(input('Enter number of vertices\n'))
    weight=[]
    for i in range(n):
        weight.append([])
        for j in range(n):
            print('Enter weight between vertex',i+1,'and',j+1)
            w=eval(input())
            weight[i].append(w)
    path_length=floyd(weight)
    print('Shortest path length is',path_length)

def floyd(weight):
    n=len(weight)
    d=weight
    for k in range(n):
        for i in range(n):
            for j in range (n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

main()

