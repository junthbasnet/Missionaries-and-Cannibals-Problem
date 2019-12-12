from time import time
from BFS_MC import bfs
from DFS_MC import dfs
from node import Node

initial_state = [3, 3, 1]

star = "**************************************************************"
dashed = "----------------------------------------------------------------"

print(star)
print("                 BFS Search Space and Solution")
print(star)

Node.num_of_instances = 0

t0 = time()
solution = bfs(initial_state)
t1 = time()
bfs_time = t1 - t0

print("\nAction Sequence Leading to Goal State:\n ")
for i in range(9):
    m = solution[i][0]
    c = solution[i][1]
    print(str(i + 1) + ". " + str(m) + " Missionary " + ", " + str(c) + " Cannibal")

bfs_search_space = Node.num_of_instances

print('')
print(dashed)
print('Search Space (BFS):', bfs_search_space)
print('Time for BFS: ', bfs_time, 'seconds')
print(dashed)

print('\n')
print(star)
print("                 DFS Search Space and Solution")
print(star)


Node.num_of_instances = 0

t2 = time()
solution = dfs(initial_state)
t3 = time()
dfs_time = t3 - t2

print("\nAction Sequence Leading to Goal State:\n ")
for i in range(9):
    m = solution[i][0]
    c = solution[i][1]
    print(str(i + 1) + ". " + str(m) + " Missionary " + ", " + str(c) + " Cannibal")

dfs_search_space = Node.num_of_instances

print('')
print(dashed)
print('Search Space (DFS):', dfs_search_space)
print('Time for DFS: ', dfs_time, 'seconds')
print(dashed)

print("\n" + star)

print("                 Comparision between BFS and DFS")

print(star + "\n")

long_dashed = "------------------------------------------------------------------------------------------------------------ "
print(long_dashed)
print("  Search Strategy employed                         Time(Seconds)                          Search Space")
print(long_dashed)
print("1. Breadth First Search (BFS)                   {0}                          {1}   ".format(bfs_time, bfs_search_space))
print("2. Depth First Search (DFS)                     {0}                          {1}   ".format(dfs_time, dfs_search_space))

