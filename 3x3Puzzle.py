import random

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]


def index(item, sequence):
    if item in sequence:
        return sequence.index(item)
    else:
        return -1


def heuristic(puzzle, item_total_calc, total_calc):
    t = 0
    for row in range(3):
        for col in range(3):
            val = puzzle.peek(row, col) - 1
            target_col = val % 3
            target_row = val / 3

            if target_row < 0:
                target_row = 2
            t += item_total_calc(row, target_row, col, target_col)
    return total_calc(t)


def manhattan(puzzle):
    return heuristic(puzzle,
                     lambda r, tr, c, tc: abs(tr - r) + abs(tc - c),
                     lambda t: t)


class SlidePuzzle:
    def __init__(self):
        self.heurisitcvalue = 0
        self.depth = 0
        self.parent = None
        self.adj_matrix = []
        for i in range(3):
            self.adj_matrix.append(goal_state[i][:])

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        else:
            return self.adj_matrix == other.adj_matrix

    def __str__(self):
        res = ''
        for row in range(3):
            res += ' '.join(map(str, self.adj_matrix[row]))
            res += '\r\n'
        return res

    def clone(self):
        a = SlidePuzzle()
        for i in range(3):
            a.adj_matrix[i] = self.adj_matrix[i][:]
        return a

    def get_legal_moves(self):
        row, col = self.find(0)
        free = []

        if row > 0:
            free.append((row - 1, col))
        if col > 0:
            free.append((row, col - 1))
        if row < 2:
            free.append((row + 1, col))
        if col < 2:
            free.append((row, col + 1))
        return free

    def generate_moves(self):
        free = self.get_legal_moves()
        zero = self.find(0)

        def swap_and_clone(first, second):
            p = self.clone()
            p.swap(first, second)
            p.depth = self.depth + 1
            p.parent = self
            return p

        return map(lambda pair: swap_and_clone(zero, pair), free)

    def generate_solution_path(self, path):
        if self.parent == None:
            return path
        else:
            path.append(self)
            return self.parent.generate_solution_path(path)

    def solve(self, h):
        def is_solved(puzzle):
            return puzzle.adj_matrix == goal_state

        openlist = [self]
        closedlist = []
        move_count = 0
        while len(openlist) > 0:
            x = openlist.pop(0)
            move_count += 1
            if (is_solved(x)):
                if len(closedlist) > 0:
                    return x.generate_solution_path([]), move_count
                else:
                    return [x]

            successors = x.generate_moves()
            index_open = index_closed = -1
            for move in successors:
                index_open = index(move, openlist)
                index_closed = index(move, closedlist)
                heurisitcvalue = h(move)
                fval = heurisitcvalue + move.depth
                if index_closed == -1 and index_open == -1:
                    move.heurisitcvalue = heurisitcvalue
                    openlist.append(move)
                elif index_open > -1:
                    copy = openlist[index_open]
                    if fval < copy.heurisitcvalue + copy.depth:
                        copy.heurisitcvalue = heurisitcvalue
                        copy.parent = move.parent
                        copy.depth = move.depth
                elif index_closed > -1:
                    copy = closedlist[index_closed]
                    if fval < copy.heurisitcvalue + copy.depth:
                        move.heurisitcvalue = heurisitcvalue
                        closedlist.remove(copy)
                        openlist.append(move)
            closedlist.append(x)
            openlist = sorted(openlist, key=lambda p: p.heurisitcvalue + p.depth)
        return [], 0

    def shuffle(self, step_count):

        for i in range(step_count):
            row, col = self.find(0)
            free = self.get_legal_moves()
            target = random.choice(free)
            self.swap((row, col), target)
            row, col = target

    def find(self, value):
        if value < 0 or value > 8:
            raise Exception("Number out of range")

        for row in range(3):
            for col in range(3):
                if self.adj_matrix[row][col] == value:
                    return row, col

    def peek(self, row, col):
        return self.adj_matrix[row][col]

    def poke(self, row, col, value):
        self.adj_matrix[row][col] = value

    def swap(self, pos_first, pos_second):
        temp = self.peek(*pos_first)
        self.poke(pos_first[0], pos_first[1], self.peek(*pos_second))
        self.poke(pos_second[0], pos_second[1], temp)


def main():
    p = SlidePuzzle()
    p.shuffle(20)
    print(p)

    path, count = p.solve(manhattan)
    path.reverse()
    for i in path:
        print(i)
    print("Solved, exploring", count, "states")


if __name__ == "__main__":
    main()
