import random as rand
import sys
import os

# TODO:
# impl rect thickness
# this is a library we should make it user friendly with class for people to use
# some sizes of rects go out of bounds
# cant fill entire ppm with a color from a rect
# no bounds checking


def generate_color_noise(pixels: list) -> list:
    """[given a pixel array]

    Args:
        pixels (list): [list of pixels]

    Returns:
        list: [list of modified pixels]
    """
    stack = []

    # for all pixels
    for i in range(0, len(pixels)):
        # generate a random pixel - custom rgb value
        pixel = [
            f"{rand.randint(0,255)} ",
            f"{rand.randint(0,255)} ",
            f" {rand.randint(0,255)} ",
        ]
        # replace that pixel in the array
        pixels[i] = pixel

    return pixels


def generate_rand_color() -> list:
    """[generates a random colored pixel]

    Returns:
        list: [a random colored pixel]
    """
    pixel = [
        f"{rand.randint(0,255)} ",
        f"{rand.randint(0,255)} ",
        f" {rand.randint(0,255)} ",
    ]
    return pixel


def fill_rect(
    color: list, pixels: list, w: int, h: int, wb: int, hb: int, roi: list
) -> list:
    """[fills a rectangle full of a colors]

    Args:
        color  (list): [list of rgb values representing a pixel]
        pixels (list): [list of pixels]
        w      (int):  [width of image]
        h      (int):  [height of image]
        wb     (int):  [width of box]
        hb     (int):  [height of box]
        roi    (list): [region of interest generated from top_left corner of rect]

    Returns:
        list: [list of pixel (modified)]
    """

    # get roi of rect
    t_lft = (roi[0] * w) + roi[1] + 1

    # row & col pointer
    r_ptr = 0
    w_ptr = 0

    # Render Col
    while True:

        # break if we are at the correct height
        if r_ptr == hb:
            break

        # get first pixel of column and draw it
        pixels[t_lft + r_ptr * w] = color
        # store column to paint
        tmp = t_lft + r_ptr * w
        # increment row pointer
        r_ptr += 1

        # render row
        for i in range(0, wb):
            # take first pixel and offset it by the with of the rect
            pixels[tmp + w_ptr] = color
            # increment width pointer
            w_ptr += 1

            # reset the ptr if we are at the correct width
            if w_ptr == wb:
                w_ptr = 0

    return pixels


def fill_rect_of_random_colors(
    pixels: list, w: int, h: int, wb: int, hb: int, roi: list
) -> list:
    """[fills a rectangle full of a random colors]

    Args:
        pixels (list): [list of pixels]
        w      (int):  [width of image]
        h      (int):  [height of image]
        wb     (int):  [width of box]
        hb     (int):  [height of box]
        roi    (list): [region of interest generated from top_left corner of rect]

    Returns:
        list: [list of pixel (modified)]
    """

    # get roi of rect
    t_lft = (roi[0] * w) + roi[1] + 1

    # row & col pointer
    r_ptr = 0
    w_ptr = 0

    # Render Col
    while True:

        # break if we are at the correct height
        if r_ptr == hb:
            break

        # get first pixel of column and draw it
        pixels[t_lft + r_ptr * w] = [
            f"{rand.randint(0,255)} ",
            f"{rand.randint(0,255)} ",
            f" {rand.randint(0,255)} ",
        ]
        # store column to paint
        tmp = t_lft + r_ptr * w
        # increment row pointer
        r_ptr += 1

        # render row
        for i in range(0, wb):
            # take first pixel and offset it by the with of the rect
            pixels[tmp + w_ptr] = [
                f"{rand.randint(0,255)} ",
                f"{rand.randint(0,255)} ",
                f" {rand.randint(0,255)} ",
            ]
            # increment width pointer
            w_ptr += 1

            # reset the ptr if we are at the correct width
            if w_ptr == wb:
                w_ptr = 0

    return pixels


def draw_rect(
    color: list, pixels: list, w: int, h: int, wb: int, hb: int, roi: list
) -> list:
    """[draw a (border)rectangle full of a specifed color]

    Args:
        color  (list): [list of rgb values representing a pixel]
        pixels (list): [list of pixels]
        w      (int):  [width of image]
        h      (int):  [height of image]
        wb     (int):  [width of box]
        hb     (int):  [height of box]
        roi    (list): [region of interest generated from top_left corner of rect]

    Returns:
        list: [list of pixel (modified)]
    """

    # get roi of rect
    t_lft = (roi[0] * w) + roi[1] + 1

    # row & col pointer
    r_ptr = 0
    w_ptr = 0

    # Render Col
    while True:

        # break if we are at the correct height
        if r_ptr == hb:
            break

        # get first pixel of column and draw it
        pixels[t_lft + r_ptr * w] = color
        tmp = t_lft + r_ptr * w
        # increment row pointer
        r_ptr += 1

        # render row
        for i in range(0, wb):
            # if we are at the end of the rect draw a pixel
            if w_ptr == wb - 1:
                # take first pixel and offset it by the with of the rect
                pixels[tmp + w_ptr] = color
                # increment width pointer

            if r_ptr == 1 or r_ptr == hb:
                # take first pixel and offset it by the with of the rect
                pixels[tmp + w_ptr] = color
                # increment width pointer

            w_ptr += 1

            # reset the ptr if we are at the correct width
            if w_ptr == wb:
                w_ptr = 0
    return pixels


def draw_rect_rand_color(
    color: list, pixels: list, w: int, h: int, wb: int, hb: int, roi: list
) -> list:
    """[draws a rectangle full of a random colors]

    Args:
        pixels (list): [list of pixels]
        w      (int):  [width of image]
        h      (int):  [height of image]
        wb     (int):  [width of box]
        hb     (int):  [height of box]
        roi    (list): [region of interest generated from top_left corner of rect]

    Returns:
        list: [list of pixel (modified)]
    """
    # get roi of rect
    t_lft = (roi[0] * w) + roi[1] + 1

    # row & col pointer
    r_ptr = 0
    w_ptr = 0

    # Render Col
    while True:

        # break if we are at the correct height
        if r_ptr == hb:
            break

        try:
            # get first pixel of column and draw it
            pixels[t_lft + r_ptr * w] = [
                f"{rand.randint(0,255)} ",
                f"{rand.randint(0,255)} ",
                f" {rand.randint(0,255)} ",
            ]
            tmp = t_lft + r_ptr * w
            # increment row pointer
            r_ptr += 1

            # render row
            for i in range(0, wb):
                # if we are at the end of the rect draw a pixel
                if w_ptr == wb - 1:
                    # take first pixel and offset it by the with of the rect
                    pixels[tmp + w_ptr] = [
                        f"{rand.randint(0,255)} ",
                        f"{rand.randint(0,255)} ",
                        f" {rand.randint(0,255)} ",
                    ]
                    # increment width pointer

                if r_ptr == 1 or r_ptr == hb:
                    # take first pixel and offset it by the with of the rect
                    pixels[tmp + w_ptr] = color
                    # increment width pointer

                w_ptr += 1

                # reset the ptr if we are at the correct width
                if w_ptr == wb:
                    w_ptr = 0

        except IndexError:
            pass

    return pixels


def save_as_ppm(pixels: list, w: int, h: int) -> bool:
    """[Saves ppm file]

    Args:
        pixels (list): [list of pixels]
        w      (int):  [width of the image]
        h      (int):  [height of the image]

    Returns:
        bool: [if the image was saved]
    """
    if os.path.isfile("./pog.ppm"):
        os.remove("./pog.ppm")

    with open("./pog.ppm", "a") as fd:
        # writing ppm header
        fd.write(f"P3\n{w} {h}\n255\n")

        ptr = 0
        try:
            # write each pixel to the file
            for i in pixels:
                if ptr == w:
                    ptr = 0
                    fd.write("\n")

                # Should just be an array of str of len 3 RGB
                fd.write("".join(i))
                ptr += 1

        except Exceptiona as err:
            print(f"FAILED: {err}")
            return False
    return True


def draw_line_rand_color(pixels: list, w: int, start: tuple, end: tuple) -> list:
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


def put_pixel(color: list, pixels: list, w: int, cord: tuple) -> list:
    """[Put pixel at coordinate]

    Args:
        color  (list): [color of the pixel]
        pixels (list): [list of pixels]
        w      (int):  [width of the image]
        cord   (list): [tuple of x,y]

    Returns:
        list: [list of pixels]
    """

    x = cord[0]
    y = cord[1]
    # x+w*y put pixel at cord
    pixels[x + w * y] = color

    return pixels


def draw_circle() -> list:
    """[draw a circle]"""


def test() -> int:
    """[little test function]

    Returns:
        int: [if the program was successful]
    """
    w, h = 256, 256
    pixels = [["255", " 255", " 255 "] for i in range(0, w * h)]

    # draw_rect(generate_rand_color(), pixels, w, h, 17, 12, [1,1])
    fill_rect(generate_rand_color(), pixels, w, h, 50, 50, [1,1])
    # draw_rect(generate_rand_color(), pixels, w, h, 17, 12, [1,1])
    # draw_rect(generate_rand_color(), pixels, w, h, 3, 3, [3,3])
    # fill_rect(generate_rand_color(), pixels, w, h, 3, 3, [3,3])
    # draw_rect(generate_rand_color(), pixels, w, h, 3, 3, [1,1])
    # draw_rect_rand_color(generate_rand_color(), pixels, w, h, 16, 16, [0, 0])

    # pixels = generate_color_noise(pixels)
    # put_pixel(
    #         generate_rand_color(),
    #         pixels,
    #         w,
    #         (5,12)
    #     )
    # draw_line(generate_rand_color(), pixels, w, (1,1), (5,5))
    # draw_line_rand_color(pixels, w, (1,1), (5,5))

    if not save_as_ppm(pixels, w, h):
        print("writing file failed")
        exit(1)

    print("Success!")
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        test()
