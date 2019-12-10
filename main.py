from time import time
from BFS_MC import bfs
from DFS_MC import dfs
from node import Node

initial_state = [3, 3, 1]

Node.num_of_instances = 0
t0 = time()
solution = bfs(initial_state)
t1 = time() - t0
print('Solution:', solution)
print('Search Space:', Node.num_of_instances)
print('Time for BFS :', t1, 'seconds')


print("**************************************************************")
print("**************************************************************")

print("DFS Search Space and Solution")

print("**************************************************************")
print("**************************************************************")

t2 = time()
solution = dfs(initial_state)
t3 = time() - t2
print('Solution:', solution)
print('Search Space:', Node.num_of_instances)
print('Time for DFS :', t3, 'seconds')

print("The time taken by DFS is {} and BFS is {} ".format(t3, t1))
