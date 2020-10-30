# Donovan Stark(drs474@nau.edu) and James Zanetti(jaz239@nau.edu)
import turtle

def getdata():
    data = []
    star_data = open('stars.txt')
    star_data = star_data
    for line in star_data:
        line = line.rstrip('\n')
        data += [line]
    star_data.close()
    return data
    

def cnvrtdata(point):
    x = float(point[0])
    y = float(point[1])
    x = x*250
    y = y*250
    m = (10/(float(point[4])+2)) 
    if len(point) !=6:
        n = point[6:]
        cur = [x,y,m,n]
        return cur
    else:
        cur = [x,y,m]
        return cur
def drawstar(loops,stars):
    for i in range(loops):
        turtle.color('white')
        turtle.penup()
        turtle.goto(stars[i][0],stars[i][1])
        turtle.seth(0)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(stars[2])
            turtle.right(90)
def connectstars():
    pass

def main():
    turtle.bgcolor('black')
    turtle.screensize(500, 500)
    data = getdata()
    loops = len(data)
    stars = []
    for i in range(len(data)):
        point = data[i].split()
        stars += [cnvrtdata(point)]
    drawstar(loops,stars)

main()
