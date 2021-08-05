#!/usr/bin/env python
# coding: utf-8

# In[6]:



# In[26]:




graph = {
  'a' : ['b','c'],
  'b' : [ 'd', 'e'],
  'c' : ['f'],
  'd' : [],
  'e' : ['f'],
  'f':[]
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'd')    # function calling


# In[ ]:




