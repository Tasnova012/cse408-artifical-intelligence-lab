#!/usr/bin/env python
# coding: utf-8

# In[26]:




graph = {
  'e' : ['b','g'],
  'b' : ['i', 'd', 'f'],
  'f' : [],
  'd' : ['a','c','g'],
  'i' : ['a'],
  'a' : ['c']
    'c':['g']
    'g':[]
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





# In[18]:


dic={}
fn='cgpa_list.txt'
print("\n")
f1=open(fn,"r")
for l in f1:
    (name,dept,cgpa)=l.split()
    dic[name]=[dept,cgpa]
    f1.close
    for key,value in dic.items():
     name,dept,cgpa=key,value[0],value[1]
    print'(name,"\t",dept,"\t",cgpa)
    print("\n")
    while true:
        name=
        input("enter the new of whose cgpa you want to change:")
        cgpa=str(input(enter the new cgpa:))
        cgpa=cgpa+"\n"
        dic[name][1]=cgpa
        ans=input("do you want more change(y/n):")
        if ans=='n'
        break
        
f1=open(fn, "w")
print("\n")
forkey,value in dic.items()
name,dept,cgpa=key,value[0]

for i in range(ln):
 name=str(input("Enter the name:"))
 dept=str(input("Enter the department:"))
 cgpa=str(input("Enter the cgpa:"))
 std=name+"\t"+dept+"\t"+cgpa
 print(std, end="\n", file=f1)
 print("\n")
f1.close
f1=open(fn, "r")
for l in f1:
 name, dept, cgpa =l.split("\t")
 print(name, dept, float(cgpa), end="\n")
f1.close


# In[19]:


get_ipython().run_line_magic('Including', 'data files')
:-use_module(inputGraph).
-----------
get_ipython().run_line_magic('Declaration', 'of dynamic data')
:-dynamic(t_node/2).
:-dynamic(pq/1).
:-dynamic(pp/1).
    get_ipython().run_line_magic('Search', 'begins')
search:-write('Enter start node:'),read(S),h_fn(S,HV),
assert(t_node(S, 'nil')),assert(pq([node(S,HV)])),
assert(pp([])),generate,find_path_length(L), display_result(L).
get_ipython().run_line_magic('Generating', 'the solution')
generate:-pq([H|_]),H=node(N,_),N=g, add_to_pp(g),!.
generate:-pq([H|_]),H=node(N,_),update_with(N), generate.
    get_ipython().run_line_magic('Adding', 'a node to possible path')
add_to_pp(N):-pp(Lst), append(Lst,[N],Lst1), retract(pp(_)),
assert(pp(Lst1)).
---------
get_ipython().run_line_magic('Updating', 'data according to selected node.')
update_with(N):-update_pq_tr(N), update_pp(N).
    get_ipython().run_line_magic('Updating', 'Priority Queue and Tree')
update_pq_tr(N):-pq(Lst), delete_1st_element(Lst,Lst1), retract(pq(_)),
assert(pq(Lst1)), add_children(N).
delete_1st_element(Lst,Lst1):-Lst = [_|Lst1].
add_children(N):- neighbor(N,X,_), not(t_node(X,_)),insrt_to_pq(X),
assert(t_node(X,N)),fail.
add_children(_).
---------
get_ipython().run_line_magic('Updating', 'Priority Queue and Tree')
update_pq_tr(N):-pq(Lst), delete_1st_element(Lst,Lst1), retract(pq(_)),
assert(pq(Lst1)), add_children(N).
delete_1st_element(Lst,Lst1):-Lst = [_|Lst1].
add_children(N):- neighbor(N,X,_), not(t_node(X,_)),insrt_to_pq(X),
assert(t_node(X,N)),fail.
add_children(_).
---------
get_ipython().run_line_magic('Updating', 'Possible Path')
update_pp(N):- retract(pp(_)), assert(pp([])), renew_pp(N).
renew_pp(N):-t_node(N,nil), pp(X), append([N],X,X1),
retract(pp(_)), assert(pp(X1)), !.
renew_pp(N):- pp(X), append([N],X,X1), retract(pp(_)), assert(pp(X1)),
t_node(N,N1), renew_pp(N1).
---------
get_ipython().run_line_magic('Finding', "'shortest' path length")
find_path_length(L):-pp(Lst),path_sum(Lst,L).
path_sum(Lst,0):- Lst=[g|_],!.
path_sum(Lst,L):-Lst=[N|T],T=[N1|_], neighbor(N,N1,D), path_sum(T,L1),L is L1+D.
---------
get_ipython().run_line_magic('Displaying', "'shortest' path and its length")
display_result(L):- pp(Lst), write('Solution:'), write(Lst),nl,
write('Length:'), write(L).
---------


# In[ ]:




