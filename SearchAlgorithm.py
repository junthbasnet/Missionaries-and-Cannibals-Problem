from queue import Queue
from node import Node
import pydot
import numpy as np
from collections import deque

def bfs(initial_state,mode="bfs"):
    graph = pydot.Dot(graph_type='digraph',label="Missionaries and Cannibals (BFS)  ",fontsize="30", color="red",
                                                    fontcolor="black",fontname='Impact', fillcolor="black")
    start_node = Node(initial_state, None, None,0)
    if start_node.goal_test():
        return start_node.find_solution()

    q = Queue()
    q.put(start_node)
    explored=[]
    killed=[]
    print("The starting node is \ndepth=%d" % start_node.depth)
    print(str(start_node.state))
    while not(q.empty()):
        node=q.get()
        print("\nthe node selected to expand is\ndepth="+str(node.depth)+"\n"+str(node.state)+"\n")
        explored.append(node.state)
        graph.add_node(node.graph_node)
        if node.parent:
            diff=np.subtract(node.parent.state,node.state)
            if node.parent.state[2]==0:
                diff[0],diff[1]=-diff[0],-diff[1]
            graph.add_edge(pydot.Edge(node.parent.graph_node, node.graph_node,label=str(diff)))
        children=node.generate_child()
        if not node.is_killed():
            print("the children nodes of this node are",end="")
            for child in children:
                if child.state not in explored:
                    print("\ndepth=%d" % child.depth)
                    print(str(child.state))
                    if child.goal_test():
                        print("which is the goal state\n")
                        graph.add_node(child.graph_node)
                        diff = np.subtract(node.parent.state, node.state)
                        if node.parent.state[2] == 0:
                            diff[0], diff[1] = -diff[0], -diff[1]

                        graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node,label=str(diff)))

                        # colour all leaves blue
                        leafs = {n.get_name(): True for n in graph.get_nodes()}
                        for e in graph.get_edge_list():
                            leafs[e.get_source()] = False
                        for leaf in leafs:
                            if leafs[leaf] and str(leaf) not in killed and str(leaf)!="\"[0, 0, 0]\"":
                                node = pydot.Node(leaf, style="filled", fillcolor="blue")
                                graph.add_node(node)

                        draw_legend(graph)
                        graph.write_png('MC_BFS.png')

                        return child.find_solution()
                    if child.is_valid():
                        q.put(child)
                        explored.append(child.state)

        else:
            print("This node is killed")
            killed.append("\""+str(node.state)+"\"")

    return


def draw_legend(graph):
    graphlegend = pydot.Cluster(graph_name="legend", label="Labels", fontsize="20", color="red",
                                fontcolor="blue", style="filled", fillcolor="white",fontname='Impact')

    legend1 = pydot.Node('Processed', shape="plaintext",fontname='Impact')
    graphlegend.add_node(legend1)
    legend2 = pydot.Node("Killed ", shape="plaintext",fontname='Impact')
    graphlegend.add_node(legend2)
    legend3 = pydot.Node('Impossible', shape="plaintext",fontname='Impact')
    graphlegend.add_node(legend3)
    legend4 = pydot.Node('Goal', shape="plaintext",fontname='Impact')
    graphlegend.add_node(legend4)

    node1 = pydot.Node("1", style="filled", fillcolor="green", label="")
    graphlegend.add_node(node1)
    node2 = pydot.Node("2", style="filled", fillcolor="red", label="")
    graphlegend.add_node(node2)
    node3 = pydot.Node("3", style="filled", fillcolor="blue", label="")
    graphlegend.add_node(node3)
    node4 = pydot.Node("4", style="filled", fillcolor="gold", label="")
    graphlegend.add_node(node4)

    graph.add_subgraph(graphlegend)
    graph.add_edge(pydot.Edge(legend1, legend2, style="invis"))
    graph.add_edge(pydot.Edge(legend2, legend3, style="invis"))
    graph.add_edge(pydot.Edge(legend3, legend4, style="invis"))
    # graph.add_edge(pydot.Edge(legend4, legend5, style="invis"))
    graph.add_edge(pydot.Edge(node1, node2, style="invis"))
    graph.add_edge(pydot.Edge(node2, node3, style="invis"))
    graph.add_edge(pydot.Edge(node3, node4, style="invis"))

def dfs(initial_state):
	graph = pydot.Dot(graph_type='digraph',label=" Missionaries and Cannibals (DFS) ", color="yellow",
													fontcolor="black", style="filled", fillcolor="blue")
	start_node = Node(initial_state, None, None,0)
	if start_node.goal_test():
		return start_node.find_solution()

	q = deque()
	q.append(start_node)
	explored=[]
	killed=[]
	print("The starting node is \ndepth=%d" % start_node.depth)
	print(str(start_node.state))
	while (q.__len__()>0):
		node=q.pop()
		print("\nthe node selected to expand is\ndepth="+str(node.depth)+"\n"+str(node.state)+"\n")
		explored.append(node.state)
		graph.add_node(node.graph_node)
		if node.parent:
			diff=np.subtract(node.parent.state,node.state)
			if node.parent.state[2]==0:
				diff[0],diff[1]=-diff[0],-diff[1]
			graph.add_edge(pydot.Edge(node.parent.graph_node, node.graph_node,label=str(diff)))
		children=node.generate_child()
		if not node.is_killed():
			print("the children nodes of this node are",end="")
			for child in children:
				if child.state not in explored:
					print("\ndepth=%d" % child.depth)
					print(str(child.state))
					if child.goal_test():
						print("which is the goal state\n")
						graph.add_node(child.graph_node)
						diff = np.subtract(node.parent.state, node.state)
						if node.parent.state[2] == 0:
							diff[0], diff[1] = -diff[0], -diff[1]

						graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node,label=str(diff)))

						# colour all leaves blue
						leafs = {n.get_name(): True for n in graph.get_nodes()}
						for e in graph.get_edge_list():
							leafs[e.get_source()] = False
						for leaf in leafs:
							if leafs[leaf] and str(leaf) not in killed and str(leaf)!="\"[0, 0, 0]\"":
								node = pydot.Node(leaf, style="filled", fillcolor="blue")
								graph.add_node(node)

						draw_legend(graph)
						graph.write_png('MC_DFS.png')

						return child.find_solution()
					if child.is_valid():
						q.append(child)
						explored.append(child.state)

		else:
			print("This node is killed")
			killed.append("\""+str(node.state)+"\"")
	return



