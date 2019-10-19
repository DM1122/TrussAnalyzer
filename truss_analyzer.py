# A script designed to analyze trusses (all of them)
# David Maranto

import turtle
import veclib

disp_size = [1000,500]
disp_scl = 25       # every meter represents disp_scl pixels
disp_speed = 10


# joints = [      # [x-coord, y-coord, support?]
#     [0,0,1],
#     [5,0,0],
#     [11,0,1],
#     [2.5,3,0],
#     [7.5,3,0],
# ]


joints = {
    'A':{
        'pos':[0,0],
        'support?':True
    },

    'B':{
        'pos':[5,0],
        'support?':True
    },

    'C':{
        'pos':[2.5,3],
        'support?':False
    }
}


members = {
    'AB':{
        'start':joints['A']['pos'],
        'end':joints['B']['pos'],
        'dir':None,
        'length':None,
        'force':None
    },

    'AC':{
        'start':joints['A']['pos'],
        'end':joints['C']['pos'],
        'dir':None,
        'length':None,
        'force':None
    },

    'CB':{
        'start':joints['C']['pos'],
        'end':joints['B']['pos'],
        'dir':None,
        'length':None,
        'force':None
    }

}


#should be automatically generated and populated
# angles = {}




def disp_setup():
    tim.shape('classic')
    tim.color('black')
    tim.pensize(3)
    tim.speed(disp_speed)
    
    screen = turtle.Screen()
    screen.setup(width=disp_size[0], height=disp_size[1], startx=None, starty=None)
    screen.title('Truss Analysis')


def disp_draw_axes():
    tim.penup()
    tim.home()
    
    axes_length_x = max([joints[i]['pos'][0] for i in joints])

    # axes_length_y = max([joints[i][1] for i in range(len(joints))])
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


def disp_draw_joints():
    for joint in joints:
        tim.penup()
        tim.goto(veclib.scal(joints[joint]['pos'],disp_scl))
        
        tim.pendown()
        if joints[joint]['support?']:
            tim.setheading(90)
            tim.backward(10)
            tim.shape('triangle')
            tim.stamp()
            tim.shape('classic')
            tim.forward(10)
            tim.setheading(0)

        tim.dot(10,'red')


def disp_draw_members():
    tim.color('blue')
    for member in members:
        tim.penup()
        tim.goto(veclib.scal(members[member]['start'], disp_scl))
        tim.pendown()
        tim.goto(veclib.scal(members[member]['end'], disp_scl))
    
    tim.color('black')


def calc_dirs():
    for member in members:
        dir = veclib.sub(members[member]['start'], members[member]['end'])
        members[member]['dir'] = dir


def calc_lengths():
    for member in members:
        leng = veclib.mag(members[member]['dir'])
        members[member]['length'] = leng
    

def calc_angs():
    angs = {}


    # find all member pairs and add them to pair array (excluding pairs bisected by a member)
    pairs = []
    for joint in joints:

        joined_members = []
        for member in members:
            if (members[member]['start'] == joints[joint]['pos']) or (members[member]['end'] == joints[joint]['pos']):      # check if a member is connected to this joint
                joined_members.append(member)

        joint_angs = []
        for joined_member in joined_members:
            others = joined_members.copy()
            others.remove(joined_member)

            for e in others:
                ang = veclib.ang(members[joined_member]['dir'], members[e]['dir'])
                joint_angs.append(ang)
            

        joint_angs.sort()
        print(joint_angs)
        joint_angs = joint_angs[:len(joined_members)-1]
        print(joint_angs)





if __name__ == '__main__':
    tim = turtle.Turtle()

    disp_setup()
    disp_draw_axes()
    disp_draw_joints()
    disp_draw_members()

    calc_dirs()
    calc_lengths()
    calc_angs()


    input("Press Enter to continue...")


    #turtle.bye()

