from maya.cmds import *
import maya.mel as mel
 
n=15
import random
r="r"
l="l"
f=[r,r,l,r,r,l,r,r,l,r,r,l,r,r,l]
last="r"
#[r,l,l,l,r,l,l,r,l,l,r,l,l,l,r]
        
def draw(f):
     
    global last
    l="l"
    r="r"
    angle=0 
    n=len(f) 
    select(all=True)
    select("clock",d=True)
    select("counterclock",d=True)
    
    delete() 
     
    if f[0]=="r":
           select("clock",r=True)
           duplicate(n="arc1")
            
           showHidden(a=True)
           last="r"
            
       
           
            
           
          
    else:
           select("counterclock",r=True)
           duplicate(n="arc1")
           showHidden(a=True)
           last="l"
           
                   
           
    for i in range(1,n):
        
        if f[i]=="r":
            h=1
        else:
            h=0
        if h:
           #print "right", angle 
           lastone="arc"+str(i)
           if last=="r":
              angle-=72
              #print "right to right ",angle
           else:
               angle+=72
               #print "left to right ",angle
           last="r"
           select("clock",r=True)
           y="arc"+str(i+1)
           duplicate()
           rename(y)
           showHidden(a=True)
           
           
         
           select(lastone+"|loc2",r=True) 
           position=xform(  query=True, translation=True, worldSpace=True)
            
           PositionX=position[0]
           PositionZ=position[2]
         
           
           select(y,r=True) 
           move(PositionX,0,PositionZ)
           rotate(0,angle,0)
           
           
           
           
        else:
           #print "left", angle 
           lastone="arc"+str(i)
           if last=="r":
               
               angle-=72
               #print "right to left",angle
               
           else:
               angle+=72
               #print "left to left",angle
           last="l"
           select("counterclock",r=True)
           y="arc"+str(i+1)
           duplicate()
           rename(y)
           showHidden(a=True)
            
         
           select(lastone+"|loc2",r=True) 
           position=xform(  query=True, translation=True, worldSpace=True)
            
           PositionX=position[0]
           PositionZ=position[2]
         
           
           select(y,r=True) 
           move(PositionX,0,PositionZ)
           rotate(0,angle,0)
    #select(clear=True)
    select(y+"|loc2",r=True)
   
            
         
#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ 
def makeArcs():
    select(all=True)
    delete()
    circle(name="the",r=5)
  
    rotate(90,0,0)
    
    setAttr( "makeNurbCircle1.sections",5)
   
    duplicate()
    select(all=True)
    mel.eval('CutCurve')
     
    select(all=True)
    mel.eval('CutCurve')
    d=ls(sl=True)
     
    nm=d[1]
    #print nm
    
    select(all=True)
   
    select("detachedCurve3",r=True)
    rename("ccw")
    mel.eval("InvertSelection")
    
    delete()
    select("ccw.cv[3]",r=True)
    cluster()
    spaceLocator(name="loc1")
    select("cluster1Handle",r=True)
    select("loc1",add=True)
    parentConstraint(weight=1) 
    select("ccw",r=True)
    select("loc1",add=True)
    parent()
    select("loc1",r=True)
    delete("cluster1Handle")
    move(0,0,0,rpr=True)
    select("loc1|ccw",r=True)
    parent(w=True)
 
 
    select("ccw.cv[0]",r=True)
    cluster()
     
    spaceLocator(name="loc2")
     
    select("cluster1Handle",r=True)
    select("loc2",add=True)
    parentConstraint(weight=1)
    delete("cluster1Handle")
    
    
    
    select("loc1",r=True)
    select("loc2",add=True)
    select("ccw",add=True)
    group(name="counterclock")
     
     
     
     
    xform(pivots=[0,0,0])
    
    duplicate()
    scale(1,1,-1)
    rename("clock")
    select("clock|ccw")
    rename("cw")
    setAttr("counterclock.visibility",0) 
    setAttr("clock.visibility",0) 
def Go():
    global n
    global f
    f=[]
    
     
    for i in range(1,n+1):
        h=radioButtonGrp("arc"+str(i),q=True,select=True)
         
        if h==1:
            f.append("r")
        else:
            f.append("l")
    print f
    draw(f)
        
    
def changeNumbers():
   global n
   global f
   print "Changing Numbers"   
   n= intSliderGrp("Numbers",q=True,value=True)
   for i in range(1,n+1):
       radioButtonGrp("arc"+str(i),e=True,enable=True,bgc=[0.2,0.3,0.2])
   for i in range(n+1,71):
       radioButtonGrp("arc"+str(i),e=True,enable=False,bgc=[0.3,0.2,0.2])
   Go()
       

def createWindows():
    global f
    dd=0
    
    if window("RobotWindow",exists=True):
        deleteUI("RobotWindow");
       
        
        
    window("RobotWindow",sizeable=True)
     
     
     
    rowColumnLayout( numberOfRows=71,height=1450,rowHeight=[(1,65)] )
    intSliderGrp(  "Numbers", field=True, label='   Number of Arcs (1-70)        ', minValue=1, maxValue=70, fieldMinValue=1, fieldMaxValue=70, value=15,cc="changeNumbers()" )
    scrollLayout(verticalScrollBarThickness=16,width=460)
    for i in range(15):
        ss=f[i]
        
        if ss=="r":
            dd=1
        else:
            dd=2
        k="Arc  "+str(i+1)+"          "
        m="arc"+str(i+1)
        radioButtonGrp( m,label=k, labelArray2=[' Clockwise', ' Counterclockwise               ' ], numberOfRadioButtons=2 ,enable=True,cc="Go()",select=dd,bgc=[0.2,0.3,0.2])    
    for i in range(16,71):   
        k="Arc "+str(i)  +"          "
        m="arc"+str(i)
        radioButtonGrp(m, label=k, labelArray2=[' Clockwise', ' Counterclockwise               ' ], numberOfRadioButtons=2 ,enable=False,cc="Go()",select=1,bgc=[0.3,0.2,0.2])
    
    
     
    showWindow()
    window("RobotWindow",e=True,widthHeight=[460,450])
    



             
makeArcs()         
r="r"
l="l"
createWindows()

f=[r,r,l,r,r,l,r,r,l,r,r,l,r,r,l]
draw(f)