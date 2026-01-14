import turtle

def indent_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
        return 
    segment = length / 3
    indent_edge(segment, depth - 1)
    turtle.left(60)
    indent_edge(segment, depth - 1)
    turtle.right(120)
    indent_edge(segment, depth - 1)
    turtle.left(60)
    indent_edge(segment, depth - 1)

def draw_recursive_polygon(sides, side_length, depth):
    angle = 360 / sides
    for _ in range(sides):
        indent_edge(side_length, depth)
        turtle.left(angle)

def main():
    sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))
 
    if sides < 3:
        print("Number of sides must be at least 3.")
        return
    if side_length <= 0:
        print("Side length must be positive.")
        return
    if depth < 0:
        print("Recursion depth cannot be negative.")
        
        return

    turtle.title("Recursive Geometric Pattern (Inward Indentation)")
    turtle.speed(0)            
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-side_length / 2, side_length / 3)
    turtle.pendown()
    turtle.tracer(False)
    draw_recursive_polygon(sides, side_length, depth)
    turtle.update()
    turtle.done()
    
if __name__ == "__main__":
    main()