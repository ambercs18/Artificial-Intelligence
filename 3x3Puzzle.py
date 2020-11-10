
class Node:
    def __init__(self, state, action, depth):
        self.state = state
        self.action = action
        self.depth = depth


class Position:
    def __init__(self, i, j):
        self.j = j
        self.i = i

found = False
selected_depth = 0
Max_Depth = 50
puzzle_size = 3
print("Enter goal state")
GoalState=[]
for i in range(3):
    a=[]
    for j in range(3):
        a.append(int(input()))
    GoalState.append(a)

print("Enter present state")
StartState=[]
for i in range(3):
    a=[]
    for j in range(3):
        a.append(int(input()))
    StartState.append(a)
    # StartState.append(map(int,input().split()))

print(GoalState)
# GoalState = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 0]
# ]
#
# StartState = [
#     [4, 1, 2],
#     [0, 6, 3],
#     [7, 5, 8]
# ]

# for j in range(puzzle_size):
#    row = input().split()
#    for i in range(puzzle_size):
#        StartState[j][i] = int(row[i])


def print_state(state):
    result = ""
    for j in range(puzzle_size):
        for i in range(puzzle_size):
            result += str(state[j][i])
        result += "\n"
    print(result)


def copy_array(state):
    st = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for j in range(puzzle_size):
        for i in range(puzzle_size):
            st[j][i] = state[j][i]
    return st


def zero_position(state):
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            if state[j][i] == 0:
                return Position(i, j)
    return None


def can_right(position):
    if position.i == puzzle_size - 1:
        return False
    return True


def can_left(position):
    if position.i == 0:
        return False
    return True


def can_up(position):
    if position.j == 0:
        return False
    return True


def can_down(position):
    if position.j == puzzle_size - 1:
        return False
    return True


def right(state):
    st = copy_array(state)
    zero_pos = zero_position(state)
    if can_right(zero_pos):
        st[zero_pos.j][zero_pos.i + 1], st[zero_pos.j][zero_pos.i] = state[zero_pos.j][zero_pos.i], state[zero_pos.j][zero_pos.i + 1]
        return st
    return st


def left(state):
    st = copy_array(state)
    zero_pos = zero_position(state)
    if can_left(zero_pos):
        st[zero_pos.j][zero_pos.i - 1], st[zero_pos.j][zero_pos.i] = state[zero_pos.j][zero_pos.i], state[zero_pos.j][zero_pos.i - 1]
        return st
    return st


def up(state):
    st = copy_array(state)
    zero_pos = zero_position(state)
    if can_up(zero_pos):
        st[zero_pos.j - 1][zero_pos.i], st[zero_pos.j][zero_pos.i] = state[zero_pos.j][zero_pos.i], state[zero_pos.j - 1][zero_pos.i]
        return st
    return st


def down(state):
    st = copy_array(state)
    zero_pos = zero_position(state)
    if can_down(zero_pos):
        st[zero_pos.j + 1][zero_pos.i], st[zero_pos.j][zero_pos.i] = state[zero_pos.j][zero_pos.i], state[zero_pos.j + 1][zero_pos.i]
        return st
    return st


def checked(state):
    for node in frontHere:
        if node.state == state:
            return True
    return False


def get_action(state):
    for node in checked_states:
        if node.state == state:
            return node.action
    return None


def h(state):
    match = 0
    for j in range(puzzle_size):
        for i in range(puzzle_size):
            if state[j][i] == GoalState[j][i]:
                match += 1
    return 9 - match


def print_path():
    state = copy_array(GoalState)
    while state != StartState:
        action = get_action(state)

        if action == "right":
            actions.append("right")
            state = left(state)

        elif action == "left":
            actions.append("left")
            state = right(state)

        elif action == "up":
            actions.append("up")
            state = down(state)

        elif action == "down":
            actions.append("down")
            state = up(state)

    actions.reverse()

    print(len(actions), "Steps:\n")
    print_state(StartState)

    for action in actions:
        if action == "right":
            state = right(state)

        elif action == "left":
            state = left(state)

        elif action == "up":
            state = up(state)

        elif action == "down":
            state = down(state)
        print_state(state)


def get_state():
    selected_node = Node(None, None, None)
    index = 0
    selected_index = 0
    min_f = Max_Depth + 9
    for i in range(0, len(frontHere)):
        node = frontHere[i]
        if node.depth + h(node.state) < min_f:
            min_f = node.depth + h(node.state)
            selected_node.state = node.state
            selected_node.depth = node.depth
            selected_node.action = node.action
            selected_index = index
    frontHere.remove(frontHere[selected_index])
    return selected_node


frontHere = [Node(StartState, None, 0)]
checked_states = []
actions = []

while len(frontHere) != 0 and not found and selected_depth <= Max_Depth:
    best_result = get_state()
    left_state = left(best_result.state)
    right_state = right(best_result.state)
    up_state = up(best_result.state)
    down_state = down(best_result.state)

    if best_result.state == GoalState:
        found = True
    if not checked(right(best_result.state)):
        frontHere.append(Node(right(best_result.state), "right", selected_depth + 1))

    if not checked(left(best_result.state)):
        frontHere.append(Node(left(best_result.state), "left", selected_depth + 1))

    if not checked(up(best_result.state)):
        frontHere.append(Node(up(best_result.state), "up", selected_depth + 1))

    if not checked(down(best_result.state)):
        frontHere.append(Node(down(best_result.state), "down", selected_depth + 1))

    selected_depth = best_result.depth
    checked_states.append(best_result)

if found:
    print_path()
else:
    print("Can't Solve!")