from maya import *
locations=set()
location_layers={}
 
maxLength=8
settings=[4,2,2,1]
pieces_layers={}
 
for i in range(1,maxLength+1):
    pieces_layers[i]=[]
    location_layers[i]=set()
firstpass=True
def deletion(): 
    global pieces_layers
    for i in pieces_layers[1]:
        cmds.delete(i)
    pieces_layers[1]=[]
    for i in location_layers[1]:
        locations.remove(i)
    location_layers[1]=set()


  
def creation():
     global firstpass
     global pieces_layers
     global locations
     global location_layers
     global settings
     #get current values
     xLen=cmds.intSlider('xSlider',q=True,value=True)
     yLen=cmds.intSlider('ySlider',q=True,value=True)
     zLen=cmds.intSlider('zSlider',q=True,value=True)
     
     layers=cmds.intSlider('layerSlider',q=True,value=True)
     if xLen<settings[0] or yLen<settings[1] or zLen<settings[2] or xLen>settings[0] or yLen>settings[1] or zLen>settings[2]:
        delete_all()
       
      
         
        create_cuboid(xLen,yLen,zLen)
        if layers>1:
           for i in range(2,layers+1):
               create_layer(i) 
        
   
     
     
                  
     if layers>settings[3]:
         
         for i in range(settings[3]+1,layers+1):
             create_layer(i)
     if layers<settings[3]:
          
         for i in range(settings[3],layers,-1):
             delete_layer(i)
             
     settings=[xLen,yLen,zLen,layers]

     if firstpass:
        create_cuboid(xLen,yLen,zLen)
        firstpass=False
      
def create_cuboid(xLen,yLen,zLen):
    global pieces_layers
    global locations
    global location_layers
    for x in range(xLen):
           for y in range(yLen):
               for z in range(zLen):
                 a=cmds.polyCube() 
                 cmds.polyBevel( offset=0.1276 ,offsetAsFraction=1, autoFit= 1, segments= 1 ,worldSpace =1,uvAssignment=0, fillNgons= 1, mergeVertices =1, mergeVertexTolerance =0.0001 ,smoothingAngle=30 ,miteringAngle=180 ,angleTolerance =180 ,ch =1)             
                 pieces_layers[1].append(a)
                 cmds.move(x,y,z)
                 position =tuple([x,y,z])
                 locations.add(position)
                 location_layers[1].add(position)
    cmds.select(clear=True)
    r=cmds.intSlider('layerSlider',q=True,value=True)
    r=len(location_layers[r])
    cmds.textField('LValue',e=True,text=r)
  
          
      
def delete_all():
    global pieces_layers
    global locations
    global location_layers
    for i in pieces_layers:
        for j in pieces_layers[i]:
            cmds.delete(j)
        pieces_layers[i]=[]
    for i in location_layers:
        location_layers[i]=set()
    locations=set()         
      
           
    
 
def delete_layer(layer):
    global pieces_layers
    global locations
    global location_layers
     
    for i in location_layers[layer]:
      
       locations.remove(i)
    location_layers[layer]=set()  
    for i in pieces_layers[layer]:
        cmds.delete(i) 
    pieces_layers[layer]=[] 
    r=cmds.intSlider('layerSlider',q=True,value=True)
    r=len(location_layers[r])
    cmds.textField('LValue',e=True,text=r)
    
 
 
def create_layer(layer):
    global pieces_layers
    global locations
    global location_layers
    
 
    
  
    
    finalAdditions=[]
    for x,y,z in location_layers[layer-1]:
      #print x,y,z
      possibleAdditions=[(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]
      newAdditions=[] 
      for cube in possibleAdditions:
          if cube not in locations:
                 aa,bb,cc=cube
                 #print a,b,c
                 a=cmds.polyCube() 
                 cmds.move(aa,bb,cc) 
                 cmds.polyBevel( offset=0.1276 ,offsetAsFraction=1, autoFit= 1, segments= 1 ,worldSpace =1,uvAssignment=0, fillNgons= 1, mergeVertices =1, mergeVertexTolerance =0.0001 ,smoothingAngle=30 ,miteringAngle=180 ,angleTolerance =180 ,ch =1)             
                 pieces_layers[layer].append(a)
                  
                  
                 newAdditions.append(cube)
      cmds.select(clear=True)
      for i in newAdditions:
          locations.add(i)
          finalAdditions.append(i)
    for i in finalAdditions:
          location_layers[layer].add(i)
    r=cmds.intSlider('layerSlider',q=True,value=True)
    r=len(location_layers[r])
    cmds.textField('LValue',e=True,text=r)
          
    
    
      
                 
     
     #create 
     
 

def setXText():
    f=cmds.intSlider('xSlider',q=True,value=True)
    cmds.textField('xValue',e=True,text=f)
    creation()

def setYText():
    f=cmds.intSlider('ySlider',q=True,value=True)
    cmds.textField('yValue',e=True,text=f)
    creation()

def setZText():
    f=cmds.intSlider('zSlider',q=True,value=True)
    cmds.textField('zValue',e=True,text=f)
    creation()
    
def setLayerText():
    f=cmds.intSlider('layerSlider',q=True,value=True)
    cmds.textField('layerValue',e=True,text=f)
    creation()
  
def setXSlider():
    global maxLength
    f=cmds.textField('xValue',q=True,text=True)
    f=int(f)
    if f<1:
       cmds.textField('xValue',e=True,text="1")
       f=1
    if f>maxLength:
       cmds.textField('xValue',e=True,text=str(maxLength))
       f=maxLength
    cmds.intSlider('xSlider',e=True,value=f)
    creation()
    
def setYSlider():
    f=int(cmds.textField('yValue',q=True,text=True))
    cmds.intSlider('ySlider',e=True,value=f)
    creation()
    
def setZSlider():
    f=int(cmds.textField('zValue',q=True,text=True))
    cmds.intSlider('zSlider',e=True,value=f)
    creation()
    
def setLayerSlider():
    f=int(cmds.textField('layerValue',q=True,text=True))
    cmds.intSlider('layerSlider',e=True,value=f)
    creation()

window= cmds.window( width=400, height =400 , title="Cuboid", iconName='Cuboid', rtf=True, bgc=[1,1,.8] , toolbox=True)
Lay= cmds.rowColumnLayout(p=window, width=450,height=400, numberOfColumns=3, columnWidth=[(1, 80), (2, 80), (3, 80)] ,columnSpacing=[[1,50],[2,50],[3,50],[4,50]],rowSpacing=[1,10]  )

blank1=cmds.text(label="",height=40)
blank1=cmds.text(label="")
blank1=cmds.text(label="")
xButton=cmds.button( label='X',c="creation()")
yButton=cmds.button( label='Y' )
zButton=cmds.button( label='Z' )
blank1=cmds.text(label="",height=5)
blank1=cmds.text(label="")
blank1=cmds.text(label="")
xValue=cmds.textField('xValue',tx="4" ,cc="setXSlider()") 
yValue =cmds.textField('yValue', tx="2" ,cc="setYSlider()") 
zValue=cmds.textField('zValue', tx="2",cc="setZSlider()" ) 
blank1=cmds.text(label="",height=10)
blank1=cmds.text(label="")
blank1=cmds.text(label="")
XScroll=cmds.intSlider('xSlider',min=1,max=maxLength,step=1,value=4,cc="setXText()")
yScroll=cmds.intSlider('ySlider',min=1,max=maxLength,step=1,value=2,cc="setYText()")
zScroll=cmds.intSlider('zSlider',min=1,max=maxLength,step=1,value=2,cc="setZText()")
blank1=cmds.text(label="",height=40)
blank1=cmds.text(label="")
blank1=cmds.text(label="")
blank1=cmds.text(label="")
layersButton=cmds.button( label='Layers' )
layersButton=cmds.button( label='# in Layer' )
blank1=cmds.text(label="")
blank1=cmds.text(label="")
blank1=cmds.text(label="")
blank1=cmds.text(label="")
layersValue=cmds.textField('layerValue',tx="1",cc="setLayerSlider()")
LValue=cmds.textField('LValue',tx="")
blank1=cmds.text(label="")
blank1=cmds.text(label="")
blank1=cmds.text(label="")
blank1=cmds.text(label="")
zScroll=cmds.intSlider('layerSlider',min=1,max=maxLength,step=1,value=1,cc="setLayerText()")
#cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.setParent( '..' )
cmds.window( window, edit=True, widthHeight=(450, 400) )
creation()
cmds.showWindow( window )
cmds.window( window, edit=True, widthHeight=(450, 400) )