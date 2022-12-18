graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
 
visited = []
queue = []
 
closed_list=[]
path=[]
 
def bfs(visited, graph, node,goal):
   
    visited.append(node)
    path={}
    path[node]=node
    root=[]
    queue.append(node)
    print(f"Open List: {queue}\nClosed list: {closed_list} ")
 
    while queue:        
        m = queue.pop(0)
        closed_list.append(m)
   
       
   
        if m==goal:
           
            while path[m]!=m:
                root.append(m)
                m=path[m]
            root.append(m)
            root.reverse()
            print(f'Path:{root}')
            return
     
 
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                path[neighbour]=m
           
        print(f"Open List: {queue}\nClosed list: {closed_list} ")
    print(f'Path :{path}')
 
 
 
 
print("Following is the Breadth-First Search")
bfs(visited, graph, '5','4')  
