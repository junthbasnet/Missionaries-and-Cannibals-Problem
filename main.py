from time import time
from SearchAlgorithm import bfs
from SearchAlgorithm import dfs
from node import Node

initial_state= [3,3,1]

Node.num_of_instances=0
t0=time()
solution=bfs(initial_state)
t1=time()-t0
print('Solution:', solution)
print('space:',Node.num_of_instances)
print('time for bfs :',t1,'seconds')


print("Now DFS TIME!!!")

t2=time()
solution=dfs(initial_state)
t3=time()-t2
print('Solution:', solution)
print('space:',Node.num_of_instances)
print('time for dfs :',t3,'seconds')

print("THE TIME TAKEN BY DFS IS {} and BFS is {} ".format(t3,t1))
