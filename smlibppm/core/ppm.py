from smlibppm.core.rect import draw_rect_rand_colors as _draw_rect_rand_colors
from smlibppm.core.rect import fill_rect_rand_colors as _fill_rect_rand_colors
from smlibppm.core.noise import generate_color_noise as _generate_color_noise
from smlibppm.core.line import draw_line_rand_colors as _draw_line_rand_colors
from smlibppm.core.circle import draw_circle as _draw_circle
from smlibppm.core.pixel import put_pixel as _put_pixel
from smlibppm.core.rect import draw_rect as _draw_rect
from smlibppm.core.rect import fill_rect as _fill_rect
from smlibppm.core.line import draw_line as _draw_line
import random as rand
import os

# TODO:
# impl rect thickness
# this is a library we should make it
#   user friendly with class for people to use
# some sizes of rects go out of bounds
# cant fill entire ppm with a color from a rect
# no bounds checking
# specifying all the possible userspace functions avaliable
# this also simplifies some of the logic with the pixel map


class PPM(object):
    """
    specifying all the possible userspace functions avaliable
    this also simplifies some of the logic with the pixel map
    """

    def __init__(self, width: int, height: int):
        # break code if not the right type
        if not isinstance(width, int):
            raise ValueError(
                f"width Expected int but found -> {type(width)}")

        # break code if not the right type
        if not isinstance(height, int):
            raise ValueError(
                f"height Expected int but found -> {type(height)}")

        self.width = width
        self.height = height
        self.pixels = [["255", " 255", " 255 "] for i in range(0, width * height)]

    def pixel_to_grayscale(self, color: list) -> list:
        """[converts pixel to grayscale]

        Args:
            color (list): [original color]

        Returns:
            [list]: [grayscale pixel]
        """
        color[0] = str(int(color[0]) / 3)
        color[1] = str(int(color[1]) / 3)
        color[2] = str(int(color[2]) / 3)
        return color

    def init_buffer(self, width: int, height: int):
        """[enabling people to create multiple pixel maps,
            this will not keep state of the old print map however]

        Args:
            width (int): [width of the image]
            height (int): [height of the image]

        Raises:
            ValueError: [width assertion]
            ValueError: [height assertion]
        """
        # break code if not the right type
        if not isinstance(width, int):
            raise ValueError(
                f"width Expected int but found -> {type(width)}")

        # break code if not the right type
        if not isinstance(height, int):
            raise ValueError(
                f"height Expected int but found -> {type(height)}")

        self.width = width
        self.height = height
        self.pixels = [
            ["255", " 255", " 255 "] for i in range(0, self.width * self.height)
        ]

    def draw_circle(self, color: list, radius: int, center: tuple, e: float):
        """[draw circle]

        Args:
            color (list): [color of circle]
            center (tuple): [center of circle]
            radius (int): [radius of circle]
        """
        _draw_circle(color, self.pixels, self.width, self.height, center, radius, e)

    def fill_rect(self, color: list, wb: int, hb: int, roi: list):
        """
            Draws Rectangle of a specified color

        Args:
            color (list): [color fo the rect]
            wb (int): [width of the box]
            hb (int): [height of the box]
            roi (list): [region of interest]
        """
        # break code if not the right type
        if not isinstance(wb, int):
            raise ValueError(
                f"widthbox Expected int but found -> {type(hb)}")

        if not isinstance(hb, int):
            raise ValueError(
                f"heightbox Expected int but found -> {type(wb)}")

        if not isinstance(roi, list):
            raise ValueError(
                f"roi Expected list but found -> {type(wb)}")

        if len(roi) > 2 or len(roi) < 1:
            raise ValueError(
                f"invalid length: roi- Expected 2 but found -> {len(roi)}")

        _fill_rect(color, self.pixels, self.width, self.height, wb, hb, roi)

    def fill_rect_rand_colors(self, wb: int, hb: int, roi: list):
        """
            Draws Rectangle of a specified color

        Args:
            wb (int): [width of the box]
            hb (int): [height of the box]
            roi (list): [region of interest]
        """
        # break code if not the right type
        if not isinstance(wb, int):
            raise ValueError(
                f"widthbox Expected int but found -> {type(hb)}")

        if not isinstance(hb, int):
            raise ValueError(
                f"heightbox Expected int but found -> {type(wb)}")

        if not isinstance(roi, list):
            raise ValueError(
                f"roi Expected list but found -> {type(wb)}")

        if len(roi) > 2 or len(roi) < 1:
            raise ValueError(
                f"invalid length: roi- Expected 2 but found -> {len(roi)}")
        _fill_rect_rand_colors(self.pixels, self.width, self.height, wb, hb, roi)

    def draw_rect(self, color: list, wb: int, hb: int, roi: list):
        """
            Draws Rectangle of a specified color

        Args:
            color (list): [color fo the rect]
            wb (int): [width of the box]
            hb (int): [height of the box]
            roi (list): [region of interest]
        """
        # break code if not the right type
        if not isinstance(wb, int):
            raise ValueError(
                f"widthbox Expected int but found -> {type(hb)}")

        if not isinstance(hb, int):
            raise ValueError(
                f"heightbox Expected int but found -> {type(wb)}")

        if not isinstance(roi, list):
            raise ValueError(
                f"roi Expected list but found -> {type(wb)}")

        if len(roi) > 2 or len(roi) < 1:
            raise ValueError(
                f"invalid length: roi- Expected 2 but found -> {len(roi)}")
        _draw_rect(color, self.pixels, self.width, self.height, wb, hb, roi)

    def draw_rect_rand_colors(self, wb: int, hb: int, roi: list):
        """
            Draws Rectangle of a specified color

        Args:
            wb (int): [width of the box]
            hb (int): [height of the box]
            roi (list): [region of interest]
        """
        # break code if not the right type
        if not isinstance(wb, int):
            raise ValueError(
                f"widthbox Expected int but found -> {type(hb)}")

        if not isinstance(hb, int):
            raise ValueError(
                f"heightbox Expected int but found -> {type(wb)}")

        if not isinstance(roi, list):
            raise ValueError(
                f"roi Expected list but found -> {type(wb)}")

        if len(roi) > 2 or len(roi) < 1:
            raise ValueError(
                f"invalid length: roi- Expected 2 but found -> {len(roi)}")

        _draw_rect_rand_colors(self.pixels, self.width, self.height, wb, hb, roi)

    def put_pixel(self, color: list, x: int, y: int) -> bool:
        """
            Draws pixel of a specified color in a specified position

        Args:
            color: color of pixel
        """

        if not isinstance(color, list):
            raise ValueError(
                f"color: Expected list but found -> {type(color)}")

        if not isinstance(x, list):
            raise ValueError(
                f"color: Expected list but found -> {type(x)}")

        if not isinstance(y, list):
            raise ValueError(
                f"invalid length: roi- Expected 2 but found -> {type(y)}")

        _put_pixel(color, x, y)

    def draw_line(self, color: list, start: tuple, end: tuple) -> bool:
        """
            Draws line of a specified color in a specified position

        Args:
            color: color of pixel
            start: tuple of x,y
            end:   tuple of x,y
        """
        _draw_line(color, self.pixels, self.width, start, end)

    def draw_line_rand_colors(self, start: tuple, end: tuple) -> bool:
        """
            Draws line of a specified color in a specified position

        Args:
            color: color of pixel
            start: tuple of x,y
            end:   tuple of x,y
        """
        _draw_line_rand_colors(self.pixels, self.width, start, end)

    def generate_color_noise(self):
        _generate_color_noise(self.pixels)

    def save_as_ppm(self, fd: str) -> bool:
        """[Saves ppm file]

        Args:
            fd: path to ppm

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
            fd.write(f"P3\n{self.width} {self.height}\n255\n")

            ptr = 0
            try:
                # write each pixel to the file
                for i in self.pixels:
                    if ptr == self.width:
                        ptr = 0
                        fd.write("\n")

                    # Should just be an array of str of len 3 RGB
                    fd.write("".join(i))
                    ptr += 1

            except Exception as err:
                raise err
                print(f"FAILED: {err}")
                return False
        return True


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
