import turtle 
import random as rd

def langton(): 
  
    window = turtle.Screen() 
    window.bgcolor('white')
    window.screensize(1280,720)
    window.setup(width=1280,height=720,startx=None,starty=None)
    
    
    maps = {}
    
    ant = turtle.Turtle()    
    ant.shape('square')     
    ant.shapesize(0.5) 
    ant.speed(1000000000)
    ant.penup()
    pos=(0,0)

    counter=turtle.Turtle(visible=False)
    cycle=0

    while True:
        
        counter.undo()
        counter.penup()
        counter.setposition(300,300)
        counter.write("Step="+str(cycle),font=("Arial",20,"normal"))
        cycle=cycle+1
        
        step = 10


            
        if  pos not in maps or maps[pos] == "white": 
              

            ant.fillcolor("blue")         
            ant.stamp()                               
            invert(maps, ant, "blue") 
            ant.right(60) 
            ant.forward(step)                          
            pos = coordinate(ant) 
              
        elif maps[pos] == "blue":
            
            ant.fillcolor("red")                            
            invert(maps, ant, "red")
            ant.stamp()
            ant.right(120)
            ant.forward(step) 
            pos = coordinate(ant)
            
        elif maps[pos] == "red":
            
            ant.fillcolor("orange")         
            ant.stamp()                               
            invert(maps, ant, "orange")
            ant.forward(step) 
            pos = coordinate(ant)

        elif maps[pos] == "orange":
            
            ant.fillcolor("green") 
            invert(maps, ant, "green") 
            ant.stamp() 
            ant.right(180) 
            ant.forward(step) 
            pos = coordinate(ant)
            
        elif maps[pos] == "green":
            
            ant.fillcolor("yellow")                                        
            invert(maps, ant, "yellow")
            ant.stamp()
            ant.right(120)
            ant.forward(step) 
            pos = coordinate(ant)
            
        elif maps[pos] == "yellow":
            
            ant.fillcolor("purple")                                       
            invert(maps, ant, "purple")
            ant.stamp() 
            ant.right(60)
            ant.forward(step) 
            pos = coordinate(ant)
            
        elif maps[pos] == "purple":
            
            ant.fillcolor("white")                                        
            invert(maps, ant, "white")
            ant.stamp()
            ant.left(120)
            ant.forward(step) 
            pos = coordinate(ant)
           

        if ant.xcor()<=-640 or ant.xcor()>=640 or ant.ycor()<=-360\
           or ant.ycor()>=360:
            break
    

        
def invert(graph, ant, color): 
    graph[coordinate(ant)] = color 
  
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))

#------------ΜΑΙΝ------------#  
if __name__=="__main__":
    langton()