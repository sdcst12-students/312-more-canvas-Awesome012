import tkinter as tk
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map1.txt')
q = f.readlines()
q = list(q)
walls =[]

rec = c.create_rectangle(10,40,20,50,fill="#aa0000")
p = c.bbox(rec)
#print(p)
coll = c.find_overlapping(p[0], p[1], p[2], p[3])

def create():
    x1 = 0
    x2 = 30
    y1 = 0
    y2 = 30
    for i in q:
        for e in i:
            if e == "*":
                walls.append( c.create_rectangle(x1,y1,x2,y2,fill='#888888' ) )
                x1 = x1 + 30
                x2 = x2 + 30
            else:
                x1 = x1 + 30
                x2 = x2 + 30
        x1 = 0
        x2 = 30
        y1 = y1 + 30
        y2 = y2 + 30


# def collsionDetection():
    # check every single wall
    # for i in walls:

# every time you move,
# if collision
#   move back

def leftKey(e):
    x=-5
    y=0
    try:
        assert isCollision() != "1" 
        assert isCollision() != "4"
        c.move(rec,x,y)
    except:
        None
    

def rightKey(e):
    x=5
    y=0
    try:
        assert isCollision() != "2"
        assert isCollision() != "3"
        c.move(rec,x,y)
    except:
        None

def upKey(e):
    x=0
    y=-5
    try:
        assert isCollision() != "1"
        assert isCollision() != "3"
        c.move(rec,x,y)
    except:
        None

def downKey(e):
    x=0
    y=5
    try:
        assert isCollision() != "2"
        assert isCollision() != "4"
        c.move(rec,x,y)
    except:
        None

w.bind("<Left>",leftKey)
w.bind("<Right>",rightKey)
w.bind("<Up>",upKey)
w.bind("<Down>",downKey)
create()

def isCollision():
    awesome = ""
    for i in walls:
        q = c.bbox(i)
        x = c.bbox(rec)
        q = c.bbox(i)
        q = list(q)
        x = list(x)
        if q[1] <= x[1] <= q[3] and q[0] <= x[0] <= q[2]:
            awesome = "1"
            print(awesome)
            return awesome
        elif q[3] >= x[3] >= q[1] and q[2] >= x[2] >= q[0]:
            awesome = "2"
            print(awesome)
            return awesome
        elif q[2] >= x[2] >= q[0] and q[1] <= x[1] <= q[3]:
            awesome = "3"
            print(awesome)
            return awesome
        elif q[0] <= x[0] <= q[2] and q[3] >= x[3] >= q[1]:
            awesome = "4"
            print(awesome)
            return awesome
        #check to see if collision with rectangle
        # if collision return True
w.mainloop()