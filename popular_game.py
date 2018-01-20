#!/usr/bin/env python3
from collections import Counter


def pick_optimal_color(board):
    neighbouring_colors = Counter()
    connected_starting_tiles = connected_tiles_of_tile(board, 0, 0)
    for neighbouring_tile in neighbouring_tiles_of_tiles(board, connected_starting_tiles):
        tile_color = color_of_tile(board, *neighbouring_tile)
        neighbouring_colors[tile_color] += len(connected_tiles_of_tile(board, *neighbouring_tile))
    return neighbouring_colors.most_common(1)[0][0]


def color_of_tile(board, row, column):
    return board[row][column]


def tile_is_on_the_board(board, row, column):
    # Assume board is symmetric for now
    nr_rows = nr_columns = len(board)
    return 0 <= row < nr_rows and 0 <= column < nr_columns


def neighbouring_tiles_of_tile(board, row, column):
    left = (row, column - 1)
    right = (row, column + 1)
    upper = (row - 1, column)
    lower = (row + 1, column)
    return [tile for tile in [left, right, upper, lower] if tile_is_on_the_board(board, *tile)]


def neighbouring_tiles_of_tiles(board, tiles):
    neighbours = set()
    color = color_of_tile(board, *list(tiles)[0])
    for tile in tiles:
        for neighbour in neighbouring_tiles_of_tile(board, *tile):
            if not tile_has_correct_color(board, color, *neighbour):
                neighbours.add(neighbour)
    return neighbours


def tile_has_correct_color(board, color, row, column):
    return board[row][column] == color


def connected_tiles_of_tile(board, row, column):
    color = board[row][column]
    connected_tiles = set()
    connected_tiles.add((row, column))
    last_round_nr_connected_tiles = 0
    while last_round_nr_connected_tiles != len(connected_tiles):
        last_round_nr_connected_tiles = len(connected_tiles)
        for connected_tile in connected_tiles.copy():
            for tile in neighbouring_tiles_of_tile(board, *connected_tile):
                if tile_has_correct_color(board, color, *tile):
                    connected_tiles.add(tile)
    return connected_tiles
