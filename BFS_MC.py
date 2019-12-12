import pydot
from node import Node
import numpy as np
from DrawLegend import draw_legend


def bfs(initial_state, mode="BFS"):
    graph = pydot.Dot(graph_type='digraph', label="Missionaries and Cannibals (BFS)", fontsize="30", color="red",
                      fontcolor="black", fontname='Arsenal', fillcolor="black")
    start_node = Node(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_action_sequence()

    frontier = [start_node]
    explored = []
    killed = []

    print("\nInitial State: {0}    |   Depth: {1}".format(start_node.state, start_node.depth))

    while frontier:

        node = frontier.pop(0)
        print("-------------------------------------------------------------------")
        print("Exploring State: {0}    |    Depth: {1}".format(node.state, node.depth))

        explored.append(node.state)
        graph.add_node(node.graph_node)

        if node.parent:
            diff = np.subtract(node.parent.state, node.state)
            if node.parent.state[2] == 0:
                diff[0], diff[1] = -diff[0], -diff[1]
            graph.add_edge(
                pydot.Edge(node.parent.graph_node, node.graph_node, label=str(diff[0]) + "M  " + str(diff[1]) + "C",
                           fontsize='10', fontcolor='#cc0099'))

        if not node.is_killed():
            children = node.generate_child()
            print("Children States of {0} are as follows: ".format(node.state))

            for child in children:

                if child.state not in explored:
                    print("{0}      |       Depth: {1}".format(child.state, child.depth))
                    if child.goal_test():
                        print("************************** Goal State Found! ****************************")
                        graph.add_node(child.graph_node)
                        diff = np.subtract(child.parent.state, child.state)
                        if child.parent.state[2] == 0:
                            diff[0], diff[1] = -diff[0], -diff[1]

                        graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node, fontsize='10',
                                                  label=str(diff[0]) + "M  " + str(diff[1]) + "C", fontcolor="#cc0099"))

                        leafs = {n.get_name(): True for n in graph.get_nodes()}
                        for e in graph.get_edge_list():
                            leafs[e.get_source()] = False
                        for leaf in leafs:
                            if leafs[leaf] and str(leaf) not in killed and str(leaf) != "\"[0, 0, 0]\"":
                                node = pydot.Node(leaf, style="filled", fillcolor="gray")
                                graph.add_node(node)

                        draw_legend(graph)
                        graph.write_png('MC_BFS.png')

                        return child.find_action_sequence()
                    if child.is_valid():
                        frontier.append(child)
                        explored.append(child.state)

        else:
            print("{} is killed! (Missionaries > Cannibals)".format(node.state))
            killed.append("\"" + str(node.state) + "\"")

    return



