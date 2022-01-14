import random as rand

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


def fill_rect_rand_colors(
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


def draw_rect_rand_colors(
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