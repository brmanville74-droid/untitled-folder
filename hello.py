import turtle
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Geometric Pattern Generator")

# Setup the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(2)
turtle.tracer(0, 0)  # Turns off animation for instant drawing

def draw_pattern():
    num_circles = 36  # How many shapes to draw in the rotation
    hue = 0
    
    for i in range(200):
        # Generate vibrant colors using HSV to RGB conversion
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(color)
        hue += 0.005
        
        # Drawing the geometric shape
        t.forward(i * 2)
        t.left(59)  # Changing this angle changes the entire pattern
        
        # Create a secondary recursive-looking effect
        for j in range(2):
            t.forward(i)
            t.left(120)

    turtle.update()  # Refresh the screen once drawing is done

draw_pattern()
t.hideturtle()
screen.exitonclick()
