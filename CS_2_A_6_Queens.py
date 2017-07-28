import unittest
#When running unittests set to True
testing = False
counter = [1]
'''
    This method assumes the solution is a list of tuples such as:
    [(0, 1), (1, 3), (2, 0), (3, 2)]
'''
def print_board(solution):
    length = len(solution)
    print("for:", length)
    print('-' * length)

    if solution == []:
        print("no solution found")
    else:
        for i in range(length):
            for j in range(length):
                if (i, j) in solution:
                    print("Q", end="")
                else:
                    print(".", end="")
            print()

    print('-' * length)
    print('Solution #:', counter)
    counter[0]+=1

'''
    Given the location of two queens, find if they are safe
    from each other.
'''

def safe(one, two):
    one_x, one_y = one
    two_x, two_y = two
    return not (one_x == two_x or one_y == two_y or \
        abs(two_x - one_x) == abs(two_y - one_y))

def solve_queens(row, placed, size):

    if row == size:
        print_board(placed)
        if testing: return placed

    for column in range(size):
        good = True
        new_queen = (row, column)

        for saff in placed:
            good &= safe(saff, new_queen)
        if good:
            placed.append(new_queen)
            if not solve_queens(row+1, placed, size):
                placed.pop(-1)
            else: return True
    #return False


class test_queens (unittest.TestCase):

    #def test_solve(self):
        #self.assertEqual(solve_queens(0, [], 4), ([(0, 1), (1, 3), (2, 0), (3, 2)]))
    def test_solve_queens_2x2(self):
        self.assertFalse(solve_queens(0, [], 2))
    def test_print_board_3X3(self):
        self.assertFalse(solve_queens(0, [],3))
    def test_print_board_4x4(self):
        self.assertTrue(solve_queens(0, [], 4))
    def test_safe(self):
        self.assertTrue(safe((0, 1), (1, 3)))
    def test_safe_again(self):
        self.assertTrue(safe((0, 1), (3, 2)))

if '__main__' == __name__:
    """
    solution = [(0, 1), (1, 3), (2, 0), (3, 2)]
    print_board(solution)
    """

    if not testing: solve_queens(0, [], 20)
