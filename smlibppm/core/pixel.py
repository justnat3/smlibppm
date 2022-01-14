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