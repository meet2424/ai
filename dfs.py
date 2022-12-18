# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }
 
# visited = []
# queue = []
 
# closed_list=[]
 
 
# def dfs(visited, graph, node,goal):
#     path={}
#     path[node]=node
#     root=[]
#     visited.append(node)
   
#     queue.append(node)
#     print(f"Open List: {queue}\nClosed list: {closed_list} ")
#     print(queue)
 
#     while queue:        
#         m = queue.pop()
#         closed_list.append(m)
#         print(f"Open List: {queue}\nClosed list: {closed_list} \n")
   
#         if m==goal:
#           while path[m]!=m:
#             root.append(m)
#             m=path[m]
#           root.append(m)
#           root.reverse()
#           print(f'Path:{root}')
#           return     
 
#         for neighbour in graph[m]:
#             if neighbour not in visited: 
#               queue.append(neighbour)
#               path[neighbour]=m
           
       
#     print('Path does not exist')
 
# print("Following is the Depth-First Search")
 
# dfs(visited, graph, '5','4')


graph={
  '5':['3','7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': [],
}

visited=[]
queue=[]

closed_list=[]

def dfs(visited, graph,node,goal):
  path={}
  path[node]=node
  root=[]
  queue.append(node)
  print(f'Open List: {queue}\nClosed List: {closed_list}\n')

  while queue:
    m=queue.pop()
    closed_list.append(m)
    print(f'Open List: {queue}\nClosed List: {closed_list}\n')

    if(m==goal):
      while path[m]!=m:
        root.append(m)
        m=path[m]
      root.append(m)
      root.reverse()
      print(f"\nPath: {root}")  
      return

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        path[neighbour]=m
    print(f'Open List: {queue}\nClosed List: {closed_list}\n')

  print("Path does not found")

dfs(visited,graph,'5','4')