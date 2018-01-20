from unittest import TestCase
from popular_game import pick_optimal_color, connected_tiles_of_tile, tile_is_on_the_board, neighbouring_tiles_of_tiles


class Test_popular_game(TestCase):
    def test_pick_optimal_color_if_there_is_just_one_color(self):
        board = ["ORRRRR",
                 "RRRRRR",
                 "RRRRRR",
                 "RRRRRR",
                 "RRRRRR",
                 "RRRRRR"]
        color = pick_optimal_color(board)
        self.assertIs(color, "R")

    def test_pick_blue_as_first_from_example(self):
        board = ["RORBRO",
                 "BRBOBO",
                 "BBOBBB",
                 "BORBRO",
                 "BOROOO",
                 "RBROBR"]
        color = pick_optimal_color(board)
        self.assertIs(color, "B")

    def test_pick_orange_as_second_from_example(self):
        board = ["BORBRO",
                 "BRBOBO",
                 "BBOBBB",
                 "BORBRO",
                 "BOROOO",
                 "RBROBR"]
        color = pick_optimal_color(board)
        self.assertIs(color, "O")

    def test_pick_red_as_third_from_example(self):
        board = ["OORBRO",
                 "ORBOBO",
                 "OOOBBB",
                 "OORBRO",
                 "OOROOO",
                 "RBROBR"]
        color = pick_optimal_color(board)
        self.assertIs(color, "R")

    def test_pick_blue_as_fourth_from_example(self):
        board = ["RRRBRO",
                 "RRBOBO",
                 "RRRBBB",
                 "RRRBRO",
                 "RRROOO",
                 "RBROBR"]
        color = pick_optimal_color(board)
        self.assertIs(color, "B")

    def test_number_of_connected_tiles_is_one(self):
        board = ["RORBRO",
                 "BRBOBO",
                 "BBOBBB",
                 "BORBRO",
                 "BOROOO",
                 "RBROBR"]
        self.assertIs(len(connected_tiles_of_tile(board, row=1, column=1)), 1)

    def test_number_of_connected_tiles_is_two(self):
        board = ["RORBRO",
                 "BRBOBO",
                 "BBOBBB",
                 "BORBRO",
                 "BOROOO",
                 "RBROBR"]
        self.assertIs(len(connected_tiles_of_tile(board, 0, 5)), 2)

    def test_number_of_connected_tiles_is_three(self):
        board = ["RORBRO",
                 "BRBOBO",
                 "BBOBBB",
                 "BORBRO",
                 "BOROOO",
                 "RBROBR"]
        self.assertIs(len(connected_tiles_of_tile(board, 3, 2)), 3)

    def test_number_of_connected_tiles_is_five(self):
        board = ["RORBRO",
                 "BRBOBO",
                 "BBOBBB",
                 "BORBRO",
                 "BOROOO",
                 "RBROBR"]
        self.assertIs(len(connected_tiles_of_tile(board, 2, 1)), 5)

    def test_tile_is_on_the_board(self):
        board = ["R"]
        self.assertTrue(tile_is_on_the_board(board, 0, 0))

    def test_tile_is_not_on_the_board(self):
        board = ["R"]
        self.assertFalse(tile_is_on_the_board(board, 1, 0))

    def test_neighbouring_tiles_of_tiles_has_two_neighbours(self):
        board = ["RORBRO",
                 "BRBOBO",
                 "BBOBBB",
                 "BORBRO",
                 "BOROOO",
                 "RBROBR"]
        self.assertSetEqual(neighbouring_tiles_of_tiles(board, [(0, 0)]), {(0, 1), (1, 0)})

    def test_neighbouring_tiles_of_group_of_five_tiles_has_seven_neighbours(self):
        board = ["RORBRO",
                 "BRBOBO",
                 "BBOBBB",
                 "BORBRO",
                 "BOROOO",
                 "RBROBR"]
        self.assertSetEqual(neighbouring_tiles_of_tiles(board, [(4, 3), (4, 4), (4, 5), (5, 3), (3, 5)]),
                            {(2, 5), (3, 4), (3, 3), (4, 2), (5, 2), (5, 4), (5, 5)})

# Todos:
#   * Add testcase for 'if there is a tie, break ties by choosing the color that has the lowest rank among the colors.'
#   * Add testcase for smaller grids
#   * If needed, asymmetric boards?
#   * Maybe refactor board-variable in testcases a bit
#   * Maybe refactor a bit more (Got tired for now an need a break :_) , we can continue this in an on-site interview)
