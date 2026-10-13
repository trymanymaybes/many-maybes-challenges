"""Detailed overhead park. Original starter geometry stays unchanged.
Run: python source/draw_cultural_park.py; optional --gui for Python Turtle window.
"""
from pathlib import Path
import math,json,argparse,turtle
from turtle_engine import ExportTurtle, BASE, path,rect,circle,arc,text,dash,base,export,GREEN
ROOT=Path(__file__).resolve().parent
LAWN='#DDE8CE';TREE='#A6BF8B';DARKTREE='#718D63';WALK='#F9F2DF';EDGE='#8E9E88';ROAD='#BBC3C5';ROOF='#E6DCC9';SHADOW='#B0BBA8';BLUE='#7395A1';BROWN='#A89173'
def polar(cx,cy,r,a):return(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))
def tree(p,x,y,r=9):
 circle(p,x-3,y+4,r,'#B0BEA1','#C0CDB1',.3)
 circle(p,x,y,r,DARKTREE,TREE,.8)
 arc(p,x,y,r*.6,20,145,'#88A874',.8)
 path(p,[(x-2,y+2),(x+2,y-3)],DARKTREE,.8)
def bench(p,x,y,angle=0):
 a=math.radians(angle);u=(math.cos(a),math.sin(a));v=(-u[1],u[0])
 pts=[(x+u[0]*s+v[0]*t,y+u[1]*s+v[1]*t) for s,t in [(-7,-2),(7,-2),(7,2),(-7,2)]]
 path(p,pts+[pts[0]],BROWN,.8,'#E4CDA4')
 path(p,[(x-7*u[0],y-7*u[1]),(x+7*u[0],y+7*u[1])],BROWN,.6)
def person(p,x,y,col='#657E8C'):
 circle(p,x,y,1.6,col,col,.5);path(p,[(x,y+2),(x,y+6)],col,1.5);path(p,[(x-2,y+4),(x+2,y+4)],col,.7)
def building(p,x,y,w,h,style=0):
 rect(p,x-5,y+6,w,h,'#CFD3CE','#CFD3CE',.1)
 rect(p,x,y,w,h,'#9CABA9',ROOF,1.1);rect(p,x+3,y+3,w-6,h-6,'#C6BAA5',None,.5)
 rect(p,x+w*.13,y+h*.18,w*.29,h*.24,'#8B9FA4','#B9D0D5',.6)
 # Roof ventilation units and solar rows, not facade windows.
 rect(p,x+w*.6,y+h*.18,w*.21,h*.17,'#A4ADA6','#CCD1C9',.6)
 for i in range(3):path(p,[(x+w*.62,y+h*.2+i*2),(x+w*.79,y+h*.2+i*2)],'#A4ADA6',.4)
 for j in range(3):rect(p,x+6+j*6,y+h-13,4,7,'#6F8A99','#91ADBB',.4)
 if style:rect(p,x+w-12,y+h-14,7,8,'#AB9D88','#F0E7D7',.5)
def sector(p,cx,cy,r1,r2,a,b,fill):
 pts=[polar(cx,cy,r2,a+(b-a)*i/90) for i in range(91)]
 pts+=[polar(cx,cy,r1,b-(b-a)*i/90) for i in range(91)]
 path(p,pts,EDGE,.5,fill)
def draw(p):
 stages=[]
 def stage(name):
  if hasattr(p,'actions'):stages.append({'name':name,'action_end':len(p.actions)})
 text(p,35,34,'MANY MAYBES / CHALLENGE 01',11,GREEN,True)
 text(p,35,73,'A CULTURAL PARK, SEEN FROM ABOVE',25,GREEN,True)
 text(p,35,104,'The same four marks become a place with height, purpose and connections.',12,'#658379')
 # Urban block, continuous perimeter street and landscaped parcel.
 rect(p,27,154,746,470,'#E0E3DB','#F0F1E9',.5)
 rect(p,94,172,576,422,'#AEB8BC',ROAD,1)
 rect(p,133,210,499,346,'#D9DDD3','#EBEEE4',.6)
 rect(p,165,219,440,329,EDGE,LAWN,1.4)
 # Two-way lanes, breaks at crossings.
 for a,b in [((112,205),(112,554)),((652,210),(652,550)),((139,190),(625,190)),((145,576),(625,576))]:dash(p,a,b,'#F8F7EF',1,17)
 # Surrounding buildings, roofs and rooftop infrastructure.
 for j,b in enumerate([(36,216,41,71),(36,318,40,70),(35,425,41,106),(692,213,58,89),(692,337,58,91),(692,468,57,69),(178,605,97,29),(306,605,84,29),(424,605,94,29),(550,605,58,29)]):building(p,*b,j%2)
 # small top-edge buildings tucked beyond street.
 for b in [(160,141,83,24),(280,141,75,24),(399,141,107,24),(545,141,62,24)]:building(p,*b)
 stage('Surrounding streets and building roofs')
 # Cars, lane islands, crossings and drains.
 for x,y,w,h in [(102,253,8,17),(116,458,8,17),(642,426,8,17),(653,230,8,17),(218,178,18,8),(431,192,18,8),(255,564,18,8),(542,579,18,8)]:
  rect(p,x,y,w,h,'#7C8D91','#F8FAF7',.7);rect(p,x+1.5,y+2,w-3,h-4,'#9CB4BB','#B6C8CC',.4)
 for y in [299,307,315,323]:path(p,[(632,y),(669,y)],'#FCFAF2',4)
 for x in [358,367,376,385]:path(p,[(x,556),(x,594)],'#FCFAF2',4)
 rect(p,159,218,11,330,EDGE,'#C5D9B2',.7)
 for y in range(233,537,27):tree(p,165,y,5)
 for x,y in [(588,234),(582,266),(588,356),(585,503),(208,511),(252,518),(300,520),(424,510),(475,511),(536,519)]:tree(p,x,y,8)
 stage('Trees, crossings and urban scale')
 # Circulation deliberately drawn before architecture.
 for pts in [[(600,312),(550,310),(474,314),(349,310)],[(473,314),(474,346),(454,350)],[(550,310),(570,371),(556,415),(553,445)],[(374,549),(375,499),(469,489),(550,470)],[(198,500),(374,499)],[(224,274),(203,305),(202,460),(232,490)]]:
  path(p,pts,'#C7BAA0',15);path(p,pts,WALK,12)
 # Arrival plaza and gate.
 rect(p,577,292,27,39,'#D1C1A5',WALK,.6)
 for y in [297,309,321]:path(p,[(578,y),(601,y)],'#D8CBB3',.5)
 path(p,[(605,292),(616,292)],EDGE,2);path(p,[(605,331),(616,331)],EDGE,2)
 # short original diagonal becomes the long edge of a canopy.
 a=(490.5,285.5);b=(538.0108185687617,252.23256669163925)
 path(p,[(a[0]-5,a[1]+9),(b[0]-5,b[1]+9),(b[0]+1,b[1]+17),(a[0]+1,a[1]+17)],SHADOW,.4,SHADOW)
 path(p,[a,b,(b[0]+7,b[1]+10),(a[0]+7,a[1]+10),a],'#AB9272',1,'#E7CFA6')
 for k in [.2,.4,.6,.8]:
  xx=a[0]+(b[0]-a[0])*k;yy=a[1]+(b[1]-a[1])*k;path(p,[(xx,yy),(xx+7,yy+10)],'#C0A987',.6)
 path(p,[(524,280),(551,310)],WALK,10)
 stage('Paths, arrival plaza and entrance canopy')
 # Tower: concentric stepped terraces; directional ground shadow.
 cx,cy=285.5,310.5
 circle(p,cx-13,cy+18,57,SHADOW,SHADOW,.3)
 circle(p,cx,cy,65,'#C6BAA0',WALK,.7)
 for rr,fc in [(54,'#DFCCAC'),(44,'#EADCC4'),(34,'#F3E9D6'),(24,'#E3DEC8'),(14,'#F5EFE0')]:
  circle(p,cx-1.3,cy+2.5,rr,'#C3B18F','#C3B18F',.4)
  circle(p,cx,cy,rr,'#A39173',fc,.9)
 # planted terrace strip, radial railing posts and terrace stair flight.
 for ang in range(0,360,20):
  path(p,[polar(cx,cy,51,ang),polar(cx,cy,54,ang)],'#A99577',.65)
 for ang in [35,80,135,175,215,260,300]:
  x,y=polar(cx,cy,49,ang);circle(p,x,y,2.6,'#8DAB75','#ABC393',.5)
 for rr in range(17,50,4):
  aa=polar(cx,cy,rr,-47);bb=polar(cx,cy,rr,-36);path(p,[aa,bb],'#A69A80',.7)
 # Roof fixtures: solar panels, lift/stair enclosure and water tank.
 rect(p,cx-9,cy-8,9,12,'#708D99','#9EBBC9',.5)
 path(p,[(cx-4.5,cy-8),(cx-4.5,cy+4)],'#D4E0E3',.4)
 rect(p,cx+3,cy-2,7,6,'#9A9785','#D8D3C0',.5)
 circle(p,cx+3,cy-9,3,'#8B9DA0','#B6CCD0',.5)
 stage('Tower: stepped roof terraces and rooftop fixtures')
 # Fan-shaped amphitheatre: starter arc is part of the outer retaining wall.
 ax,ay=340.5,345.5
 sector(p,ax,ay,50,115,0,125,'#E5D9C0')
 for rr in [58,68,78,88,98,108,115]:arc(p,ax,ay,rr,0,125,'#A59070',.85)
 # radial aisles cut through rows, with stair treads.
 for ang in [23,63,104]:
  path(p,[polar(ax,ay,53,ang),polar(ax,ay,114,ang)],WALK,7)
  for rr in range(58,113,8):path(p,[polar(ax,ay,rr,ang-2.5),polar(ax,ay,rr,ang+2.5)],'#B4A484',.5)
 # Stage points towards the fan. Back wall and equipment are visible from above.
 sector(p,ax,ay,28,47,0,125,'#CDB391')
 arc(p,ax,ay,28,0,125,'#947E64',1.2)
 rect(p,370,352,10,7,'#7E867B','#A0A798',.6)
 for rr in [73,93,108]:
  for ang in range(5,124,9):
   if min(abs(ang-z) for z in [23,63,104])>5:
    x,y=polar(ax,ay,rr,ang);path(p,[(x-1,y),(x+1,y)],'#BAA78B',1.3)
 stage('Amphitheatre: concentric seating, aisles and stage')
 # Round garden pavilion: a roof seen overhead, with eight ribs and a skylight.
 px,py=510.5,445.5
 circle(p,px-6,py+9,30,SHADOW,SHADOW,.4)
 circle(p,px,py,44,'#C3B998',WALK,.7)
 for a1,a2 in [(10,75),(105,165),(195,250),(280,335)]:sector(p,px,py,35,42,a1,a2,'#B8CFA0')
 circle(p,px,py,29,'#A89476','#EDD6AF',.7)
 for ang in range(0,360,45):path(p,[polar(px,py,6,ang),polar(px,py,28,ang)],'#B8A080',.7)
 circle(p,px,py,7,'#819FA7','#BED4D9',.7)
 for x,y in [(565,443),(550,483),(461,441),(505,392)]:bench(p,x,y,90 if x>550 else 0)
 for x,y in [(564,475),(457,480),(552,399),(470,406)]:tree(p,x,y,6)
 # Service block and public furniture.
 building(p,205,430,27,39,1)
 for x,y in [(245,493),(430,491),(580,376),(203,382)]:bench(p,x,y)
 for x,y in [(535,309),(486,314),(356,313),(472,348),(549,415),(550,467),(381,492),(375,530),(218,300)]:person(p,x,y)
 # Lighting, bicycle stand and bollards.
 for x,y in [(574,296),(580,330),(240,490),(447,494),(200,411)]:circle(p,x,y,1.4,'#8D9F96','#8D9F96',.5)
 for x in [578,583,588,593]:arc(p,x,286,2.2,180,360,'#8A9A94',.7)
 stage('Garden pavilion, planting, benches and people')
 # All original starter segments go back on top, unchanged.
 base(p);stage('Preserved dark-green starter overlay')
 # Labels outside important geometry; avoid using labels as a substitute for drawing.
 text(p,225,235,'TERRACED TOWER',8,'#536D5E',True)
 text(p,309,480,'OPEN-AIR THEATRE',8,'#536D5E',True)
 text(p,468,542,'GARDEN PAVILION',8,'#536D5E',True)
 text(p,469,238,'ENTRY CANOPY',8,'#536D5E',True)
 text(p,35,659,'A viewpoint becomes an imagined world through connected details.',16,GREEN,True)
 text(p,35,688,'Tower terraces suggest height; roofs carry fixtures; paths connect the garden and theatre.',11,'#586B62')
 text(p,35,711,'Straight-down view: roof lights and equipment are visible, rather than facade windows.',11,'#586B62')
 text(p,35,740,'Original marks stay dark green. One illustrative interpretation, drawn with Python Turtle.',10,'#658379')
 # compass, so the view is explicit rather than a generic labelled rectangle.
 path(p,[(744,144),(744,122)],'#718B7C',1.2);path(p,[(739,129),(744,122),(749,129)],'#718B7C',1.2);text(p,740,115,'N',8,GREEN,True)
 return stages
if __name__=='__main__':
 ag=argparse.ArgumentParser();ag.add_argument('--gui',action='store_true');args=ag.parse_args()
 if args.gui:
  sc=turtle.Screen();sc.setup(1000,970);sc.setworldcoordinates(0,-770,800,0);sc.bgcolor('#FAF8F1');sc.tracer(0)
  p=turtle.Turtle();p.hideturtle();draw(p);sc.update();turtle.done()
 else:
  p=ExportTurtle();stages=draw(p)
  expected=[('line',[(a[0],a[1]+70),(b[0],b[1]+70)],GREEN,3) for pts in BASE for a,b in zip(pts,pts[1:])]
  actual=[a for a in p.actions if a[0]=='line' and a[2]==GREEN and a[3]==3]
  assert actual==expected,'Starter geometry changed'
  export(p,'challenge-01-cultural-park')
  (ROOT/'images'/'cultural-park-drawing-stages.json').write_text(json.dumps({'stages':stages,'actions':p.actions},indent=2))
  print('Detailed park exported. Original geometry verified. Drawing stages recorded.')
