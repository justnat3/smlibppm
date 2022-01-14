import random as rand
import sys
import os

# TODO:
# impl rect thickness
# this is a library we should make it user friendly with class for people to use
# some sizes of rects go out of bounds
# cant fill entire ppm with a color from a rect
# no bounds checking

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

def save_as_ppm(fd: str, pixels: list, w: int, h: int) -> bool:
    """[Saves ppm file]

    Args:
        fd     (str):  [file path]
        pixels (list): [list of pixels]
        w      (int):  [width of the image]
        h      (int):  [height of the image]

    Returns:
        bool: [if the image was saved]
    """
    # this is handled in main
    # if fd == "" or fd is None:
    #     eprint("ERROR: No file specified")

    if os.path.isfile(fd):
        os.remove(fd)

    with open(fd, "a") as fd:
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



