import pydot
from node import Node
import numpy as np
from DrawLegend import draw_legend


def bfs(initial_state, mode="BFS"):
    graph = pydot.Dot(graph_type='digraph', label="Missionaries and Cannibals (BFS)", fontsize="30", color="red",
                      fontcolor="black", fontname='Arsenal', fillcolor="black")
    start_node = Node(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_solution()

    frontier = [start_node]
    explored = []
    killed = []

    print("The Starting node is \nDepth = %d" % start_node.depth)
    print(str(start_node.state))

    while frontier:
        node = frontier.pop(0)
        print("\nThe node selected to expand is\nDepth = " + str(node.depth) + "\n" + str(node.state) + "\n")

        explored.append(node.state)
        graph.add_node(node.graph_node)

        if node.parent:
            diff = np.subtract(node.parent.state, node.state)
            if node.parent.state[2] == 0:
                diff[0], diff[1] = -diff[0], -diff[1]
            graph.add_edge(
                pydot.Edge(node.parent.graph_node, node.graph_node, label=str(diff[0]) + "M  " + str(diff[1]) + "C",
                           fontsize='10', fontcolor='#cc0099'))
        children = node.generate_child()

        if not node.is_killed():
            print("The children nodes of this node are", end="")

            for child in children:
                if child.state not in explored:
                    print("\nDepth=%d" % child.depth)
                    print(str(child.state))
                    if child.goal_test():
                        print("Which is the goal state\n")
                        graph.add_node(child.graph_node)
                        diff = np.subtract(child.parent.state, child.state)
                        if child.parent.state[2] == 0:
                            diff[0], diff[1] = -diff[0], -diff[1]

                        graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node, fontsize='10',
                                                  label=str(diff[0]) + "M  " + str(diff[1]) + "C", fontcolor="#cc0099"))

                        # colour all leaves blue
                        leafs = {n.get_name(): True for n in graph.get_nodes()}
                        for e in graph.get_edge_list():
                            leafs[e.get_source()] = False
                        for leaf in leafs:
                            if leafs[leaf] and str(leaf) not in killed and str(leaf) != "\"[0, 0, 0]\"":
                                node = pydot.Node(leaf, style="filled", fillcolor="blue")
                                graph.add_node(node)

                        draw_legend(graph)
                        graph.write_png('MC_BFS.png')

                        return child.find_solution()
                    if child.is_valid():
                        frontier.append(child)
                        explored.append(child.state)

        else:
            print("This node is killed")
            killed.append("\"" + str(node.state) + "\"")

    return



