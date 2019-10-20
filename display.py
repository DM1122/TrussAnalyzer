# truss visualizer using turtle graphics

tim = turtle.Turtle()

def setup(speed=5):
    tim.shape('classic')
    tim.color('black')
    tim.pensize(3)
    tim.speed(speed)
    
    screen = turtle.Screen()
    screen.setup(width=disp_size[0], height=disp_size[1], startx=None, starty=None)
    screen.title('Truss Analysis')


def draw_axes():
    tim.penup()
    tim.home()
    
    axes_length_x = max([joints[i]['pos'][0] for i in joints])
    axes_length_y = max([joints[i]['pos'][1] for i in joints])

    tim.pendown()
    tim.backward(1*disp_scl)
    tim.forward(1*disp_scl)
    tim.forward(axes_length_x*disp_scl)
    tim.home()

    tim.setheading(90)
    tim.backward(1*disp_scl)
    tim.forward(1*disp_scl)
    tim.forward(axes_length_y*disp_scl)
    tim.home()

    tim.penup()


def draw_joints():
    for joint in joints:
        tim.penup()
        tim.goto(veclib.scal(joints[joint]['pos'],disp_scl))
        
        tim.pendown()
        if joints[joint]['support'] is not None:
            tim.setheading(90)
            tim.backward(10)
            tim.shape('triangle')
            tim.stamp()
            tim.shape('classic')
            tim.forward(10)
            tim.setheading(0)

        tim.dot(10,'red')


def draw_members():
    tim.color('blue')
    for member in members:
        tim.penup()
        tim.goto(veclib.scal(members[member]['start'], disp_scl))
        tim.pendown()
        tim.goto(veclib.scal(members[member]['end'], disp_scl))
    
    tim.color('black')


def draw_forces():
    for f in forces:
        tim.penup()
        tim.goto(veclib.scal(forces[f]['pos'],disp_scl))
        tim.setheading(forces[f]['ang'])
        tim.backward(10)
        tim.color('green')
        tim.shape('arrow')
        tim.stamp()
        tim.shape('classic')
        tim.color('black')

