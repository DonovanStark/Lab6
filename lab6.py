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
    if m > 2:
        m = 2
    elif m < 1:
        m = 1
    if len(point) !=6:
        n = point[6:]
        if len(n) > 1:
            n = ' '.join(n)
        cur = [x,y,m,n]
        return cur
    
    else:
        cur = [x,y,m]
        return cur

def drawstars(loops,stars):
    for i in range(loops):
        turtle.color('white')
        turtle.penup()
        turtle.goto(stars[i][0],stars[i][1])
        turtle.seth(0)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(stars[i][2])
            turtle.right(90)
        turtle.end_fill()

def getconst(i):
    i = str(i)
    constellations = {'0':'BigDipper_lines.txt','1':'Cas_lines.txt','2':'Gemini_lines.txt','3':'UrsaMajor_lines.txt',
            '4':'Bootes_lines.txt','5':'Cyg_lines.txt','6':'Hydra_lines.txt','7':'UrsaMinor_lines.txt'}
    cont = []
    constellation = open(constellations[i])
    for line in constellation:
        line = line.rstrip('\n')
        cont += [line.split(',')]
    constellation.close()
    return cont
def mark1(star,stars):
    for i in range(len(stars)):
        if len(stars[i]) > 3:
            if 'DENEB KAITOS' in stars[i][3]:
                pass
            else:    
                if star in stars[i][3]:
                    return stars[i]
def mark2(star,stars):
    for i in range(len(stars)):
        if len(stars[i]) > 3:
                
            if 'DENEB KAITOS' in stars[i][3]:
                pass
            else:    
                if star in stars[i][3]:
                    return stars[i]


def drawline(star1,star2):
    turtle.penup()
    turtle.goto(star1[0],star1[1])
    turtle.pencolor('yellow')
    turtle.pendown()
    turtle.goto(star2[0],star2[1])
def main():
    turtle.bgcolor('black')
    turtle.screensize(500, 500)
    turtle.speed(0)
    turtle.tracer(1,0)
    data = getdata()
    loops = len(data)
    stars = []
    for i in range(len(data)):
        point = data[i].split()
        stars += [cnvrtdata(point)]
    drawstars(loops,stars)
    for i in range(8):
        cur = getconst(i)
        for n in range(len(cur)):
            star1 = mark1(cur[n][0],stars)
            star2 = mark2(cur[n][1],stars)
            drawline(star1,star2)

    turtle.exitonclick()
main()
