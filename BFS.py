# Author : Junth Basnet
# Missionaries and Cannibals Problem (COMP 472 Artificial Intelligence Assignment 2)

from anytree import Node, RenderTree


class State:
    def __init__(self, cl, ml, boat_pos, cr, mr):
        self.cl = cl
        self.ml = ml
        self.boat_pos = boat_pos
        self.cr = cr
        self.mr = mr
        self.parent = None

    def goal_state(self):
        if self.cl == 0 and self.ml == 0:
            return True
        else:
            return False

    def is_valid_state(self):
        if (self.ml >= 0 and self.mr >= 0) \
                and (self.cl >= 0 and self.cr >= 0) \
                and (self.ml == 0 or self.ml >= self.cl) \
                and (self.mr == 0 or self.mr >= self.cr):

            return True
        else:
            return False

    def __eq__(self, other):
        return self.cl == other.cl and self.ml == other.ml \
               and self.boat_pos == other.boat_pos and self.cr == other.cr \
               and self.mr == other.mr

    def __hash__(self):
        return hash((self.cl, self.ml, self.boat_pos, self.cr, self.mr))


def successors(current_state):
    children = []

    if current_state.boat_pos == 'Left':
        """There are 5 Possibilities for next state"""

        # First Possibility : 2 Cannibals crossing river from left to right
        next_state = State(current_state.cl - 2, current_state.ml, 'Right', current_state.cr + 2, current_state.mr)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

        # Second Possibility : 2 Missionaries crossing river from left to right
        next_state = State(current_state.cl, current_state.ml - 2, 'Right', current_state.cr, current_state.mr + 2)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

        # Third Possibility : 1 Missionary crossing river from left to right
        next_state = State(current_state.cl, current_state.ml - 1, 'Right', current_state.cr, current_state.mr + 1)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

        # Fourth Possibility : 1 Cannibal crossing river from left to right
        next_state = State(current_state.cl - 1, current_state.ml, 'Right', current_state.cr + 1, current_state.mr)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

        # Fifth Possibility : 1 Missionary and 1 Cannibal crossing river from left to right
        next_state = State(current_state.cl - 1, current_state.ml - 1, 'Right', current_state.cr + 1,
                           current_state.mr + 1)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

    else:
        """Similarly there are 5 possibilities while crossing river from Right to Left"""

        # First Possibility : 2 Cannibals crossing river from Right to left
        next_state = State(current_state.cl + 2, current_state.ml, 'Left', current_state.cr - 2, current_state.mr)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

        # Second Possibility : 2 Missionaries crossing river from Right to Left
        next_state = State(current_state.cl, current_state.ml + 2, 'Left', current_state.cr, current_state.mr - 2)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

        # Third Possibility : 1 Missionary crossing river from Right to Left
        next_state = State(current_state.cl, current_state.ml + 1, 'Left', current_state.cr, current_state.mr - 1)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

        # Fourth Possibility : 1 Cannibal crossing river from Right to Left
        next_state = State(current_state.cl + 1, current_state.ml, 'Left', current_state.cr - 1, current_state.mr)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

        # Fifth Possibility : 1 Missionary and 1 Cannibal crossing river from Right to Left
        next_state = State(current_state.cl + 1, current_state.ml + 1, 'Left', current_state.cr - 1,
                           current_state.mr - 1)
        if next_state.is_valid_state():
            next_state.parent = current_state
            children.append(next_state)

    return children


def breadth_first_search():
    initial_state = State(3, 3, 'Left', 0, 0)

    if initial_state.goal_state():
        return initial_state

    queue = []
    explored = []

    queue.append(initial_state)
    while (queue):
        state = queue.pop(0)
        if state.goal_state():
            return state

        explored.append(state)
        children = successors(state)
        for child in children:
            if child not in explored:
                explored.append(child)
                queue.append(child)


def print_solution(solution):
    path = []
    final = []
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        final.append("(" + str(state.cl) + "," + str(state.ml) \
                     + "," + state.boat_pos + "," + str(state.cr) + "," + \
                     str(state.mr) + ")")
    return final


returned_final = print_solution(breadth_first_search())


def draw_tree(returned_final):
    a = Node(returned_final[0])
    b = Node(returned_final[1], parent=a)
    c = Node(returned_final[2], parent=b)
    d = Node(returned_final[3], parent=c)
    e = Node(returned_final[4], parent=d)
    f = Node(returned_final[5], parent=e)
    g = Node(returned_final[6], parent=f)
    h = Node(returned_final[7], parent=g)
    i = Node(returned_final[8], parent=h)
    j = Node(returned_final[9], parent=i)
    k = Node(returned_final[10], parent=j)
    l = Node(returned_final[11], parent=k)
    n = Node("(2,2,Right,1,1)", parent=a)
    c = Node(returned_final[2], parent=n)
    d = Node(returned_final[3], parent=c)
    e = Node(returned_final[4], parent=d)
    f = Node(returned_final[5], parent=e)
    g = Node(returned_final[6], parent=f)
    h = Node(returned_final[7], parent=g)
    i = Node(returned_final[8], parent=h)
    j = Node(returned_final[9], parent=i)
    k = Node(returned_final[10], parent=j)
    l = Node(returned_final[11], parent=k)

    for pre, fill, node in RenderTree(a):
        print("%s%s" % (pre, node.name))


def main():
    print("State Space Tree")
    print("(Cannibal Left, Missionary Left, Boat Position, Cannibal Right, Missionary Right)")
    breadth_first_search()
    draw_tree(returned_final)


if __name__ == "__main__":
    main()
