from graphics import *
import math
def MTG():
    clist=[0,0,0,0,0,0,0,0] # counter for each cmc
    perli=[0,0,0,0,0,0,0,0] # percents for each cmc (as decimal value)
    landl=[0,0,0,0,0,0,0,0] # percents including lands (as deimal values)
    plist=[0,0,0,0,0,0,0,0] # used for determining bar height (psuedo percent value)
    rlist=[0,0,0,0,0,0,0,0] # list of bars for bar graph
    tlist=[0,0,0,0,0,0,0,0] # I have no clue but everything breaks without it
    xlist=[0,0,0,0,0,0,0,0] # list of text items for displaying percents
    xclis=[0,0,0,0,0,0,0,0] # list of text items for displaying count on graph
    blist=[]                # list of buttons
    z=0                     # all purpose counter
    landscore=100           # used for determining the amount of lands
    cmc=['cmc 1','cmc 2','cmc 3','cmc 4','cmc 5','cmc 6','cmc 7+','Lands']
    win=GraphWin("mtg",400,400)
# button set up
    reset=button(win,20,380,20,'red')
    resetT=Text(Point(200,380),"<- reset                press ' / ' and click to close")
    resetT.setFill('black')
    resetT.draw(win)
    for c in range(7):
        x=button(win,20,40+(25*c),15,'green')
        blist.append(x)
    for x in range(7):
         x=Text(Point(60,40+(25*x)),cmc[x])
         x.setFill('black')
         x.draw(win)
# graph set up
    graph=Rectangle(Point(115,220),Point(370,30))
    graph.setFill('white')
    graph.draw(win)
    for c in range(7):
        if c+1<7:
            x=Text(Point(135+(35*c),230),(c+1))
            x.setFill('black')
            x.draw(win)
        if c+1>=7:
            x=Text(Point(135+(35*c),230),'7+')
            x.setFill('black')
            x.draw(win)
    while True:
# determining the percent cmc (and a number of lands to add)
        for x in range(4):
            percent=round(perli[x]*100,1)
            text=cmc[x]+": "+str(percent)
            xlist[x]=Text(Point(50+(100*x),330),text)
            xlist[x].setFill('black')
            xlist[x].draw(win)
        for x in range(4,7):
            percent=round(perli[x]*100,1)
            text=cmc[x]+": "+str(percent)
            xlist[x]=Text(Point(50+(100*z),350),text)
            xlist[x].setFill('black')
            xlist[x].draw(win)
            z=z+1
        # land math
        try:
            landsT.undraw()
        except:
            gaba='gol'
        lands=round((landscore+(30*perli[1])+(60*perli[2])+(90*perli[3])+(120*perli[4])+(150*perli[5])+(180*perli[6]))/(6.666),0)
        text="lands: "+str(lands)
        landsT=Text(Point(350,350),text)
        landsT.setFill('black')
        landsT.draw(win)
        z=0 # resets the counter for the next time it is used
# displays real count on top of graph
        for x in range(7):
        # attemptes to undraw them (needs try except because xclis is initialized to an integer, not an object)
            try:
                xclis[x].undraw()
            except:
                pass
        for x in range(7):
            xclis[x]=Text(Point(135+(35*x),40),clist[x])
            xclis[x].setFill('black')
            xclis[x].draw(win)
# detects click and does the thing
        c=win.getMouse()
        for x in range(7):
            if blist[x].contains(c)==True:
                clist[x]=clist[x]+1
                blist[x].press()
        # things for reset button
            elif reset.contains(c)==True: #resets all counters and graph
                for x in range(7):
                    #attempts to undraw all the bars and the text on the graph 
                    try:
                        rlist[x].undraw()
                        xclis[x].undraw()
                    except:
                        pass
                clist=[0,0,0,0,0,0,0,0]
                plist=[0,0,0,0,0,0,0,0]
                rlist=[0,0,0,0,0,0,0,0]
                tlist=[0,0,0,0,0,0,0,0]
                xclis=[0,0,0,0,0,0,0,0]
                z=0
            else:
                pass
    # updating bar graphs after a button is pressed
        for x in range(7):
            try:
                rlist[x].undraw()
            except:
                pass
        for x in range(7):
            # sometimes (if the first thing clicked is not a valid button) it will try to divide by zero
            try:
                perli[x]=clist[x]/sum(clist)
            except:
                genericvariable=17 # for some reason just having pass was giving problems so here is "bootleg pass"
            plist[x]=(180*perli[x])
            x1=120+(x*35)
            y1=220
            x2=150+(x*35)
            y2=220-plist[x]
            bar=Rectangle(Point(x1,y1),Point(x2,y2))
            rlist[x]=bar
            bar.setFill('cyan')
            bar.draw(win)
    # at the end of each loop, the percents text is undrawn to start up again at the top
        for x in range(8):
            try:
                xlist[x].undraw()
            except:
                the_fitness_gram_pacer_test="a multistage aerobic capacity test that progressively gets more difficult as it continues." #bootleg pass
    # checks the last key pressed, currently only one command, if the key is slash, the next click closes the program
        cmd=win.checkKey()
        if cmd=='slash':
            win.close()
            break

#button class:
class button:
    def __init__(self, win, x, y, diameter, color):
        centerPoint = Point(x, y)
        radius=diameter/2
        circle=Circle(centerPoint,radius)
        circle.setFill(color)
        circle.draw(win)
        self.x=x
        self.y=y
        self.radius=radius
        self.obj=circle
        self.color=color
    def contains(self,point):
            pointX=point.getX()
            pointY=point.getY()
            distance=math.sqrt((pointX-self.x)**2+(pointY-self.y)**2)
            if distance<=self.radius:
                return True
            else:
                return False
    def press(self):
        self.obj.setFill("red")
        time.sleep(0.2)
        self.obj.setFill(self.color)
        
