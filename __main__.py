from smlibppm import *
import sys

def main() -> int:

    file = "./examples/colorful_rect.ppm"
    # init ppm
    ppm = PPM(256, 256)

    # generate color
    color = generate_rand_color()

    # draw 
    ppm.draw_circle(color, 20, (100,100), 20.2)
    
    # save the ppm and catch potential errors passed up
    if not ppm.save_as_ppm(file):
        eprint("ERROR: Writing file %s failed" % file)
        exit(1)

    # success!
    print("Success! Built %s" % file)
    return 0

if __name__ == "__main__":
    main()