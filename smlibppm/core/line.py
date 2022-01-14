import random as rand 

def draw_line_rand_colors(pixels: list, w: int, start: tuple, end: tuple) -> list:
    """[draw a line between two points random color sequence]

    Args:
        color (list): [rgb value of the line]
        pixels (list): [list of pixels]
        w (int): [width of image]
        start (tuple): [start coordinates]
        end (tuple): [end coordinates]

    Returns:
        list: [list of modified pixels]
    """

    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = x2 - x1
    dy = y2 - y1

    stp = dx if dx > dy else dy
    xnc = int(dx / stp)
    ync = int(dy / stp)

    x = x1
    y = y1

    for i in range(0, stp):
        print(w, (x, y))
        put_pixel(generate_rand_color(), pixels, w, (x, y))
        x += xnc
        y += ync


def draw_line(color: list, pixels: list, w: int, start: tuple, end: tuple) -> list:
    """[draw a line between two points]

    Args:
        color (list): [rgb value of the line]
        pixels (list): [list of pixels]
        w (int): [width of image]
        start (tuple): [start coordinates]
        end (tuple): [end coordinates]

    Returns:
        list: [list of modified pixels]
    """

    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = x2 - x1
    dy = y2 - y1

    stp = dx if dx > dy else dy
    xnc = int(dx / stp)
    ync = int(dy / stp)

    x = x1
    y = y1

    for i in range(0, stp):
        print(w, (x, y))
        put_pixel(color, pixels, w, (x, y))
        x += xnc
        y += ync