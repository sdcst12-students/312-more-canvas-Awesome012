import tkinter as tk
"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map2.txt')
q = f.readlines()
q = list(q)
walls  =[]
wallImg0 = tk.PhotoImage(file="assets/map.water.png")
wallImg1 = tk.PhotoImage(file="assets/map.plains.png")
wallImg2 = tk.PhotoImage(file="assets/map.forest.png")
wallImg3 = tk.PhotoImage(file="assets/map.hills.png")
wallImg4 = tk.PhotoImage(file="assets/map.mountain.png")
wallImg5 = tk.PhotoImage(file="assets/map.swamp.png")
wallImg6 = tk.PhotoImage(file="assets/map.city.png")
def create():
    x = 20
    y = 20
    for i in q:
        for e in i:
            if e == "0":
                walls.append( c.create_image(x,y,image=wallImg0))
                x = x + 30
            if e == "1":
                walls.append( c.create_image(x,y,image=wallImg1))
                x = x + 30
            if e == "2":
                walls.append( c.create_image(x,y,image=wallImg2))
                x = x + 30
            if e == "3":
                walls.append( c.create_image(x,y,image=wallImg3))
                x = x + 30
            if e == "4":
                walls.append( c.create_image(x,y,image=wallImg4))
                x = x + 30
            if e == "5":
                walls.append( c.create_image(x,y,image=wallImg5))
                x = x + 30
            if e == "6":
                walls.append( c.create_image(x,y,image=wallImg6))
                x = x + 30
            else:
                None
        x = 20
        y = y + 30


create()
w.mainloop()