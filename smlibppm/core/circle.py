from smlibppm.core.pixel import put_pixel

# yikes this solution is weird thanks to / 
# https://stackoverflow.com/questions/22777049/how-can-i-draw-a-circle-in-a-data-array-map-in-python
def draw_circle(color: list, pixels: list, width: int, height: int, center: tuple, radius: int, elispon: float):
    """[draw a circle]

    Args:
        color (list): [color of the circle]
        pixels (list): [pixel map]
        width (int): [width of the image]
        height (int): [height of the image]
        center (tuple): [center of the circle]
        radius (int): [raidus of the circle]
        elispon (float): [not sure what this is]
    """
    for y in range(height):
        for x in range(width):
            if abs((x-center[0])**2 + (y-center[1])**2 - radius**2) < elispon**2:
                put_pixel(color, pixels, width, (x,y))