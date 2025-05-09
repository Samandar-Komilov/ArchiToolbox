import cProfile
import sys

# NOT FINISHED!

im = [
    list('..########################...........'),
    list('..#......................#...#####...'),
    list('..#..........########....#####...#...'),
    list('..#..........#......#............#...'),
    list('..#..........########.........####...'),
    list('..######......................#......'),
    list('.......#..#####.....###########......'),
    list('.......####...#######................')
]

HEIGHT = len(im)
WIDTH = len(im[0])

def floodFill(image: list, x: int, y: int, newChar: str, oldChar: str = None) -> None:
    if oldChar == newChar or im[y][x] != oldChar:
        return 
    
    printImage(im)
    # Change the neighboring characters.
    if y + 1 < HEIGHT and im[y + 1][x] == oldChar:
        floodFill(im, x, y + 1, newChar, oldChar)
    if y - 1 >= 0 and im[y - 1][x] == oldChar:
        floodFill(im, x, y - 1, newChar, oldChar)
    if x + 1 < WIDTH and im[y][x + 1] == oldChar:
        floodFill(im, x + 1, y, newChar, oldChar)
    if x - 1 >= 0 and im[y][x - 1] == oldChar:
        floodFill(im, x - 1, y, newChar, oldChar)
        return

def printImage(image):
    for y in range(HEIGHT):
    # Print each row.
        for x in range(WIDTH):
            # Print each column.
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')


printImage(im)
floodFill(im, 1, 1, 'o')