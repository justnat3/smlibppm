import random as rand
import sys 
import os 

# TODO:
# impl rect thickness
# this is a library we should make it user friendly with class for people to use
# some sizes of rects go out of bounds
# cant fill entire ppm with a color from a rect
# no bounds checking
# can only modify clean pixel map - can't add onto it 

def generate_color_noise(pixels: list) -> list:
    """
        Generates random noise

        returns
        -------
            list of pixels

        Params
        ------
            pixels : list
                list of pixel information [r,g,b]
    """
    stack = []

    # for all pixels
    for i in range(0, len(pixels)):
        # generate a random pixel - custom rgb value
        pixel = [f"{rand.randint(0,255)} ", f"{rand.randint(0,255)} ", f" {rand.randint(0,255)} "]
        # replace that pixel in the array
        pixels[i] = pixel

    return pixels


def generate_rand_color() -> list:
    """ returns a random color """
    pixel = [f"{rand.randint(0,255)} ", f"{rand.randint(0,255)} ", f" {rand.randint(0,255)} "]
    return pixel 


def fill_rect(color: list, pixels: list, w: int, h: int, wb: int, hb: int, roi: list) -> list:
    """
        fill a Rectange with color 

        returns
        -------
            list
                colored pixels in a rectangle

        params
        ------

            pixels : list
                list of pixels [r,g,b]

            w : int
                height of pixel map 

            h : int
                width of pixel map 

            wb : int
                width of the rect

            hb : int
                height of the rect

            roi : tuple
                region of interest, ordered from top left

        """
    # get roi of rect
    t_lft = (roi[0]*w) + roi[1] + 1

    # row & col pointer
    r_ptr = 0
    w_ptr = 0

    # Render Col
    while(True):

        # break if we are at the correct height
        if r_ptr == hb:
            break

        # get first pixel of column and draw it 
        pixels[t_lft + r_ptr*w] = color
        # store column to paint
        tmp = t_lft + r_ptr*w
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



def fill_rect_of_random_colors(pixels: list, w: int, h: int, wb: int, hb: int, roi: list) -> list:
    """
        Fill a Rectange with random colors 

        returns
        -------
            list
                random colored pixels in a rectangle

        params
        ------
            pixels : list
                list of pixels [r,g,b]

            w : int
                height of pixel map 

            h : int
                width of pixel map 

            wb : int
                width of the rect

            hb : int
                height of the rect

            roi : tuple
                region of interest, ordered from top left

        """

    # get roi of rect
    t_lft = (roi[0]*w) + roi[1] + 1

    # row & col pointer
    r_ptr = 0
    w_ptr = 0

    # Render Col
    while(True):

        # break if we are at the correct height
        if r_ptr == hb:
            break

        # get first pixel of column and draw it 
        pixels[t_lft + r_ptr*w] = [f"{rand.randint(0,255)} ", f"{rand.randint(0,255)} ", f" {rand.randint(0,255)} "]
        # store column to paint
        tmp = t_lft + r_ptr*w
        # increment row pointer
        r_ptr += 1

        # render row
        for i in range(0, wb):
            # take first pixel and offset it by the with of the rect
            pixels[tmp + w_ptr] = [f"{rand.randint(0,255)} ", f"{rand.randint(0,255)} ", f" {rand.randint(0,255)} "]
            # increment width pointer
            w_ptr += 1

            # reset the ptr if we are at the correct width
            if w_ptr == wb:
                w_ptr = 0

    return pixels 


def draw_rect(color: list, pixels: list, w: int, h: int, wb: int, hb: int, roi: list) -> list:
    """
        draw a Rectange with color 

        returns
        -------
            list
                random colored pixels in a rectangle

        params
        ------
            color: list
                pixel color information 

            pixels : list
                list of pixels [r,g,b]

            w : int
                height of pixel map 

            h : int
                width of pixel map 

            wb : int
                width of the rect

            hb : int
                height of the rect

            roi : tuple
                region of interest, ordered from top left

        """
    # get roi of rect
    t_lft = (roi[0]*w) + roi[1] + 1

    # row & col pointer
    r_ptr = 0
    w_ptr = 0

    # Render Col
    while(True):

        # break if we are at the correct height
        if r_ptr == hb:
            break

        # get first pixel of column and draw it 
        pixels[t_lft + r_ptr*w] = color
        tmp = t_lft + r_ptr*w
        # increment row pointer
        r_ptr += 1

        # render row
        for i in range(0, wb):
            # if we are at the end of the rect draw a pixel
            if w_ptr == wb-1:
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


def draw_rect_rand_color(color: list, pixels: list, w: int, h: int, wb: int, hb: int, roi: list) -> list:
    """
        fill a Rectange with color 

        returns
        -------
            list
                colored pixels in a rectangle

        params
        ------

            pixels : list
                list of pixels [r,g,b]

            w : int
                height of pixel map 

            h : int
                width of pixel map 

            wb : int
                width of the rect

            hb : int
                height of the rect

            roi : tuple
                region of interest, ordered from top left

        """
    # get roi of rect
    t_lft = (roi[0]*w) + roi[1] + 1

    # row & col pointer
    r_ptr = 0
    w_ptr = 0

    # Render Col
    while(True):

        # break if we are at the correct height
        if r_ptr == hb:
            break

        # get first pixel of column and draw it 
        pixels[t_lft + r_ptr*w] = [f"{rand.randint(0,255)} ", f"{rand.randint(0,255)} ", f" {rand.randint(0,255)} "]
        tmp = t_lft + r_ptr*w
        # increment row pointer
        r_ptr += 1

        # render row
        for i in range(0, wb):
            # if we are at the end of the rect draw a pixel
            if w_ptr == wb-1:
                # take first pixel and offset it by the with of the rect
                pixels[tmp + w_ptr] = [f"{rand.randint(0,255)} ", f"{rand.randint(0,255)} ", f" {rand.randint(0,255)} "]
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


def save_as_ppm(pixels: list, w: int, h: int) -> bool:
    """
        Returns
        -------
            bool
                was the operation successful

        Params
        ------
            pixels : list
                pixel map in the form of a list

            w : list
                width of the pixel map

            h : list
                height of the pixel map
    """
    if os.path.isfile('./pog.ppm'):
        os.remove('./pog.ppm')

    with open('./pog.ppm', 'a') as fd:
        # writing ppm header
        fd.write(f"P3\n{w} {h}\n255\n")

        ptr = 0
        try:
            # write each pixel to the file
            for i in pixels:
                if ptr == w:
                    ptr = 0
                    fd.write('\n')

                # Should just be an array of str of len 3 RGB
                fd.write("".join(i))
                ptr += 1

        except Exceptiona as err:
            print(f"FAILED: {err}")
            return False
    return True


def test() -> int:
    w, h = 32,16
    pixels = [['255',' 255',' 255 '] for i in range(0, w*h)]

    # draw_rect(generate_rand_color(), pixels, w, h, 17, 12, [1,1])
    # draw_rect_of_random_colors(pixels, w, h, 17, 12, [1,1])
    # draw_rect(generate_rand_color(), pixels, w, h, 17, 12, [1,1])
    # draw_rect(generate_rand_color(), pixels, w, h, 3, 3, [3,3])
    # fill_rect(generate_rand_color(), pixels, w, h, 3, 3, [3,3])
    draw_rect(generate_rand_color(), pixels, w, h, 3, 3, [1,1])

    # pixels = generate_color_noise(pixels)

    if not save_as_ppm(pixels, w, h):
        print("writing file failed")
        exit(1)

    print("Success!")
    return 0 

if __name__ == "__main__":
    if "--test" in sys.argv:
        test()