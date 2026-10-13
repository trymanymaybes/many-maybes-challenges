"""Revised Turtle previews: visual evidence rather than explanatory labels."""
from pathlib import Path
import math,json
from turtle_engine import ExportTurtle,BASE,path,rect,circle,arc,text,base,export,GREEN
from previous_scenes import underwater,desk,heading,footer
ROOT=Path(__file__).resolve().parent

def ellipse(p,x,y,rx,ry,col,fill=None,width=1):
 pts=[(x+rx*math.cos(i*math.pi/72),y+ry*math.sin(i*math.pi/72)) for i in range(145)]
 path(p,pts,col,width,fill)

def fish(p,x,y,s,col='#438C96',direction=1):
 def pts(arr):return [(x+direction*a*s,y+b*s) for a,b in arr]
 path(p,pts([(-12,0),(-22,-10),(-21,9),(-12,0)]),col,.6,col)
 path(p,pts([(-13,0),(-7,-6),(4,-7),(14,-1),(15,1),(4,7),(-7,6),(-13,0)]),col,.8,'#ACCCD0')
 path(p,pts([(-2,-6),(2,-12),(7,-6)]),col,.7,'#75ABB1')
 path(p,pts([(-3,5),(2,10),(6,6)]),col,.6)
 path(p,pts([(6,-4),(4,0),(6,4)]),col,.7)
 circle(p,x+direction*10*s,y-1*s,1.2*s,'#335B63','#335B63',.4)
 path(p,pts([(-9,0),(1,1)]),'#D7EBE9',.65)

def clean(p):
 # Remove semantic labels, temporal arrows and original overlay before adding detail.
 p.actions=[a for a in p.actions if not(a[0]=='text' and a[2]!='PAUSE')
  and not(a[0]=='line' and a[2]==GREEN and a[3]==3)
  and not(a[0]=='line' and a[2]=='#79A3A5')]

def water_v2(p):
 underwater(p);clean(p)
 heading(p,'BENEATH THE SURFACE','What do light, reflections and living surroundings make possible?')
 # Fine intersecting caustic ribbons on the seabed.
 for j in range(8):
  y=551+j*4
  path(p,[(106+i*7,y+2.3*math.sin(i*.45+j*.6)) for i in range(84)],'#F4EDCB',.8)
 for j in range(9):
  x=113+j*67
  path(p,[(x+9*math.sin(i*.5+j),546+i*3) for i in range(15)],'#F7EED0',.7)
 # Branching coral, blades and tiny shell details create an inhabited foreground.
 for x,y,h,col in [(122,552,48,'#BB8C86'),(649,547,44,'#B99088'),(455,559,37,'#AB9D88')]:
  path(p,[(x,y),(x+2,y-h)],col,3)
  for k in range(1,5):
   yy=y-k*h/5
   for sign in [-1,1]:
    path(p,[(x+2,yy),(x+sign*(9+k),yy-6),(x+sign*(12+k),yy-13)],col,2)
    path(p,[(x+sign*(9+k),yy-6),(x+sign*(16+k),yy-5)],col,1.4)
 for x,y in [(390,574),(574,568),(191,579),(325,560)]:
  ellipse(p,x+2,y+2,9,3,'#C0B69A','#C0B69A',.3)
  path(p,[(x-8,y),(x-6,y-5),(x,y-8),(x+6,y-5),(x+8,y),(x-8,y)],'#B9A385',.7,'#F2DFC0')
  for off in [-5,-2,2,5]:path(p,[(x,y),(x+off,y-5)],'#C3AE8B',.5)
 for x in [204,219,593,605]:
  path(p,[(x,554),(x-6,532),(x+1,508),(x-2,481)],'#5D937E',1.4)
  for yy in [495,513,532]:path(p,[(x-2,yy+6),(x-10,yy),(x-8,yy-8)],'#82B09B',.9)
 for x,y,s,d in [(196,419,1.05,1),(616,427,.95,-1),(620,318,.7,-1),(174,288,.6,1),(588,456,.65,-1)]:fish(p,x,y,s,direction=d)
 # Distant school: small silhouettes help separate foreground and background.
 for j in range(7):fish(p,396+j*19,222+(j%3)*7,.28,'#82B0B4',1)
 # Ribs and reflected glints on the ray and kelp.
 for j in range(7):path(p,[(535+j*4,286),(548+j*4,304)],'#ACCBC7',.55)
 path(p,[(535,263),(551,268),(569,276)],'#CCE0D7',1)
 for a in range(24,84,10):
  x=340.5+110*math.cos(math.radians(a));y=345.5+110*math.sin(math.radians(a))
  path(p,[(x,y),(x-5,y-6)],'#ADC8A1',.7)
 # Reflective circular forms: tonal depth, reflected habitat and curved highlights.
 for cx,cy,r in [(285.5,310.5,54),(510.5,445.5,29)]:
  for j in range(10):
   colors=['#80B1B5','#8DBBC0','#9AC5C8','#A7CED0','#B3D6D6','#BDDCDC','#C7E3E0','#D0E9E4','#D7EDE7','#DEF1EB']
   circle(p,cx-j*.6,cy-j*.7,r-j*1.5,colors[j],colors[j],.1)
  # A curved, compressed reflection of the surface and aquatic vegetation.
  for j in range(3):
   yy=cy-r*.35+j*r*.12
   path(p,[(cx-r*.65+i*r*.065,yy+math.sin(i*.45+j)*r*.05) for i in range(21)],'#B0D2CF',.7)
  path(p,[(cx+r*.3,cy+r*.51),(cx+r*.23,cy+r*.22),(cx+r*.35,cy-r*.02)],'#86B5AE',1.2)
  path(p,[(cx+r*.25,cy+r*.28),(cx+r*.1,cy+r*.1)],'#99C4B9',1)
  arc(p,cx,cy,r-4,195,271,'#F5FFFB',3)
  arc(p,cx,cy,r-9,201,245,'#E3FAF2',1.3)
  arc(p,cx,cy,r-5,13,87,'#65999F',1.3)
  ellipse(p,cx-r*.37,cy-r*.47,r*.12,r*.06,'#FFFFFF','#FFFFFF',.2)
  circle(p,cx+r*.45,cy+r*.18,r*.035,'#E8FBF6','#E8FBF6',.2)
 # Suspended particles imply water rather than empty paper.
 for j in range(53):
  x=108+(j*97)%576;y=239+(j*41)%286
  if math.hypot(x-285.5,y-310.5)>64 and math.hypot(x-510.5,y-445.5)>37:
   circle(p,x,y,.55+j%3*.25,'#E0F3EC','#E0F3EC',.1)
 base(p)
 text(p,103,622,'Let the scene suggest an interpretation before giving it a name.',11,'#586B62')
 footer(p,'Thinking move: add material, light and a living context.','Reflective forms, kelp, fish and the seabed turn the same marks into an underwater world.')

def desk_v2(p):
 desk(p);clean(p)
 heading(p,'IN THE MIDDLE OF MAKING','What do objects, shadows and traces reveal about this moment?')
 # Extended cast shadow first, then the cup. Large starter circle is its exact rim.
 ellipse(p,309,335,68,51,'#D5BE9B','#D5BE9B',.1)
 ellipse(p,304,330,60,46,'#C9B08D','#C9B08D',.1)
 # Ceramic handle with open middle and an interior contact edge.
 ellipse(p,350,314,27,19,'#8B948B','#E8E7DA',1)
 ellipse(p,351,314,17,11,'#B5AA92','#EDDEC5',.8)
 arc(p,350,314,19,-70,75,'#FBF9EC',1.5)
 circle(p,285.5,310.5,54,'#C1C1AD','#F6F0DB',.7)
 circle(p,285.5,310.5,47,'#A49881','#B49C77',1)
 circle(p,284.5,309,43,'#655146','#745647',.5)
 # Coffee shading and reflections show a filled cup, not a labelled ring.
 arc(p,284.5,309,39,25,151,'#5B453A',3)
 arc(p,284.5,309,38,202,276,'#D9B98C',2)
 arc(p,284.5,309,35,209,261,'#E8CE9D',.9)
 ellipse(p,270,288,12,4,'#EFE1BD','#EFE1BD',.3)
 ellipse(p,280,292,6,2,'#D0B48F','#D0B48F',.2)
 for x,y,r in [(307,319,1.6),(301,330,1),(306,331,.7),(270,335,1.1)]:circle(p,x,y,r,'#BD9A6E','#BD9A6E',.3)
 arc(p,285.5,310.5,51,199,276,'#FFFCED',2)
 arc(p,285.5,310.5,49,20,108,'#C0BAA3',1)
 # The smaller circle remains an exposed wet print, with uneven residue and glint.
 for rr,a,b,col,w in [(33,13,165,'#C0B795',2.2),(31,193,310,'#A3B4A1',2),(27,22,112,'#B4C4AE',1.5),(25,194,267,'#D7D9BE',1)]:arc(p,510.5,445.5,rr,a,b,col,w)
 ellipse(p,503,439,20,16,'#D4D5B9','#D4D5B9',.2)
 ellipse(p,504,437,17,13,'#E3E4CC','#E3E4CC',.2)
 path(p,[(493,434),(501,431),(508,432)],'#FBF9E9',1.4)
 for x,y,rx,ry in [(549,455,3,2),(540,475,2,3),(483,480,2,1),(525,488,3,1.5)]:
  ellipse(p,x+1,y+1,rx+1,ry+1,'#C3BC9E','#C3BC9E',.3)
  ellipse(p,x,y,rx,ry,'#C0D1C0','#D5E1CD',.3)
  path(p,[(x-rx*.3,y-ry*.3),(x+rx*.3,y-ry*.5)],'#FFFCEE',.5)
 # Contact shadows along existing objects, staying outside their silhouettes.
 path(p,[(111,423),(207,427),(207,245)],'#C7B695',2)
 path(p,[(622,434),(672,434),(672,346)],'#C3B191',2.2)
 path(p,[(434,328),(456,321),(478,302)],'#C9BCA0',1.6)
 # Pencil shavings and eraser crumbs add evidence of work, not decorative noise.
 for x,y in [(405,495),(388,510),(418,512)]:
  path(p,[(x-9,y),(x-4,y-7),(x+7,y-4),(x+10,y+3),(x+2,y+8),(x-9,y)],'#B88E64',.7,'#E8C18C')
  path(p,[(x-5,y),(x-1,y-3),(x+5,y),(x+2,y+4),(x-5,y)],'#C79E71',.6,'#F6E0AC')
  path(p,[(x-4,y-6),(x+7,y-4)],'#637773',1)
 for j in range(15):
  x=364+(j*19)%60;y=461+(j*11)%23
  path(p,[(x,y),(x+2,y-1),(x+3,y+1)],'#B9AE94',.5)
 # Swatches and graphite crosshatching make the sketchbook look actively used.
 for y,col in [(328,'#B7C4A5'),(340,'#C7AF93'),(352,'#B0C1C5')]:
  for j in range(5):path(p,[(110+j*3,y),(114+j*3,y+8)],col,1)
 for j in range(5):path(p,[(109+j*4,299),(111+j*4,288)],'#A2AAA0',.5)
 # Small color smears and palette mixing streaks.
 for pts,col in [([(629,510),(642,512),(649,510)],'#B0BCB0'),([(615,509),(620,514),(626,515)],'#D2BA95'),([(395,366),(401,368),(405,367)],'#A9B6A0')]:path(p,pts,col,1.2)
 base(p)
 text(p,103,625,'A cup is present. A second ring and scattered materials leave the story open.',11,'#586B62')
 footer(p,'Thinking move: combine visible objects with traces of use.','Light, ceramic, coffee, wet residue and drawing materials give the starter a believable setting.')

if __name__=='__main__':
 data={}
 for name,fn in [('challenge-01-underwater-rich-v2',water_v2),('challenge-01-desk-rich-v2',desk_v2)]:
  p=ExportTurtle();fn(p)
  expected=[('line',[(a[0],a[1]+70),(b[0],b[1]+70)],GREEN,3) for pts in BASE for a,b in zip(pts,pts[1:])]
  assert [a for a in p.actions if a[0]=='line' and a[2]==GREEN and a[3]==3]==expected
  export(p,name);data[name]=p.actions
 (ROOT/'images'/'drawing-actions-v2.json').write_text(json.dumps(data))
 print('Revised scenes exported; all original strokes verified unchanged.')
