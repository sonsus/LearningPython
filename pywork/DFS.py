#DFS in python
'''
Dunno whats going on inside, but it exceeds a limit in number of recursion
'''


def Visit(n_vertice, visited_list):
    visited_list.append(n_vertice)

def Unvisited_N(current_vertice, G_mat, visited_list):
    for i in range(len(G_mat[0])):
        if G_mat[current_vertice][i] and (i not in visited_list): 
            return i
    return 0 
def DFS(n_start, current, G_mat, visited_list):
    while 1:
        if Unvisited_N(current, G_mat, visited_list):
            Visit(current,visited_list)
            current=Unvisited_N(current, G_mat, visited_list)
        elif Unvisited_N(current, G_mat, visited_list)==0 and (0 not in visited_list):
            Visit(0,visited_list)
            current=0
        elif current == n_start: 
            print(visited_list)
        else:
            current==visited_list[-2]
            DFS(n_start, current,G_mat,visited_list)



if __name__=="__main__":

    G_adj=[
            [0,0,1,1,0,],
            [0,0,1,0,0,],
            [1,1,0,1,0,],
            [1,0,1,0,1,],
            [0,0,0,1,0,],
        ]
    visited = [-1,]
    n_start=int(input("among 0~4 choose an vertice# to start from: "))
    current=n_start
    DFS(n_start, current, G_adj, visited)