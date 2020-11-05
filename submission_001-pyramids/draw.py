def get_shape():
    shape = input("Shape?: ").lower()
    while shape != "pyramid" and shape != "square" and shape != "triangle" and shape != "rectangle" and shape != "diamond" and shape !="flag":
        shape = input("Shape?: ").lower()
    return shape

# TODO: Step 1 - get height (it must be int!)
def get_height():
    
    height = (input("Height?: "))
    while height.isdigit() == False or int(height) > 80 :
        height = input("Height?: ")
    return int(height)


# TODO: Step 2
def draw_pyramid(height, outline):
    if(outline == True):
        for i in range(1, height+1):
            for j in range(1, 2*height):
                if i == height or i + j == height+1 or  j - i == height-1:
                    print("*", end = "")
                elif j - i > height - 1:
                    pass
                else:
                    print(" ", end="")
            print()
    else:
        for i in range(1,height+1):
                print(" " *(height-i) + "*" *(2*i-1))



# TODO: Step 3
def draw_square(height, outline):
    if(outline == True):
        for i in range(height):
            for j in range(height):
                if i == 0 or i == height-1 or j == 0 or j == height-1:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print("")
    else:
        for i in range(1,height+1):
            print("*" *height)


# TODO: Step 4
def draw_triangle(height, outline):
    if(outline == True):
        for i in range(height):
            for j in range(i+1):
                if j == 0 or i == (height-1) or i == j:
                    print("*" ,end = "")
                else:
                    print(end = " ")
            print()
    else:    
        for i in range(1, height+1):
            print("*" *i)


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    if shape == "square":
        draw_square(height, outline)
    if shape == "triangle":
        draw_triangle(height, outline)
    if shape == "rectangle":
        draw_rectangle(height, outline)
    if shape == "diamond":
        draw_diamond(height, outline)
    if shape == "flag":
        draw_flag(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline only? (y/N): ")
    if outline == "y":
        return True
    else:
        return False

#   Step 6 - Other shapes
def draw_rectangle(height, outline):
    if (outline == True):
        for i in range(1,height):
            for j in range(1,height*2):
                if i == 1 or i == (height-1) or j == 1 or j == ((height*2 -1)):
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
            print()
    else:
        for i in range(1,height):
            for j in range(1,height*2):
                print("*", end = " ")
            print()

def draw_diamond(height, outline):
    
    if(outline == True):
        for i in range(1, height+1):
            for j in range(1, height-i+1):
                print(" ", end = "")
            for j in range(1, 2*i):
                if j == 1 or j == 2*i -1:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print()

        for i in range(height-1, 0, -1):
            for j in range(1, height-i+1):
                print(" ", end = "")
            for j in range(1, 2*i):
                if j == 1 or j == 2*i -1:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print("")
    else:
        for i in range(height):
            print(" " *(height-i-1) + "* " *(i+1))
        for j in range(height-1, 0, -1):
            print(" "*(height-j) + "* " *(j))

def draw_flag(height, outline):
    if(outline == True):
        for i in range(1,height):
            for j in range(1,height*2):
                if i == 1 or i == (height-1) or j == 1 or j == ((height*2 -1)):
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
            print()

        for i in range(height):
            print("*")
    else:
        for i in range(1,height):
            for j in range(1,height*2):
                print("*", end = " ")
            print("")

        for i in range(height):
            print("*")
        

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)