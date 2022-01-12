from PIL import Image
import os

def main() -> int:
    # try:
    img = Image.open('./remoberry.png').convert('RGB')
    pixel = img.load()

    HEIGHT = img.size[1]-5
    WIDTH = img.size[0]-5
    x = 0 # x → 
    y = 0 # y ↑ 
    w_stack = []

    while(True):
        # next column
        if x == WIDTH: 
            x = 0
            if y != HEIGHT:
                y += 1 
            else: break
            print(w_stack)
            w_stack = []
        w_stack.append(pixel[x,y])
        x += 1
            
    # except Exception as err:
    #     print("EXCU_FAILURE:\n", err, '\n')
    #     print("DB_INFO", x, y)
    #     print('\t', "HEIGHT:", HEIGHT, '\n\tWIDTH:', WIDTH)
    #     exit()
    return 0 

if __name__ == "__main__":
    main()