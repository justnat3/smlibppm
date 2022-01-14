from smlibppm import *
import sys

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

    if not save_as_ppm("./examples/colorful_rect.ppm", pixels, w, h):
        print("writing file failed")
        exit(1)

    print("Success!")
    return 0


if __name__ == "__main__":
    if "--test" in sys.argv:
        test()
