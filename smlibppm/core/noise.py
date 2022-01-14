import random as rand 

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

