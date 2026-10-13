"""Two detailed interpretations with unchanged original Turtle starter marks."""
from pathlib import Path
import math,json,argparse,turtle
from turtle_engine import ExportTurtle,BASE,path,rect,circle,arc,text,dash,base,export,GREEN
ROOT=Path(__file__).resolve().parent
def heading(p,title,sub):
 text(p,35,34,'MANY MAYBES / CHALLENGE 01',11,GREEN,True)
 text(p,35,73,title,25,GREEN,True);text(p,35,104,sub,12,'#658379')
def footer(p,title,sub):
 path(p,[(35,643),(765,643)],'#D1DCD6',1)
 text(p,35,675,title,16,GREEN,True);text(p,35,705,sub,11,'#586B62')
 text(p,35,738,'Original marks stay dark green. Our illustrative interpretation, drawn with Python Turtle.',10,'#658379')
def extra_bubble(p,x,y,r):
 circle(p,x,y,r,'#89B7BD',None,.6);arc(p,x,y,r*.7,205,275,'#EFFCFA',1)
def underwater(p):
 heading(p,'ONE BUBBLE, TWO MOMENTS','What if separate circles show the same thing at different times and depths?')
 stages=[]
 def st(n):stages.append({'name':n,'action_end':len(getattr(p,'actions',[]))})
 # Water column: lighter near surface, darker near bottom, flat illustrative bands.
 colors=['#D7F1ED','#D0EBE7','#C9E5E2','#C2DFDD','#BBD9D9','#B4D2D4','#AECBCD']
 for j,c in enumerate(colors):rect(p,100,195+j*53,600,54,c,c,.1)
 rect(p,100,195,600,371,'#89ADB0',None,1)
 # Rippled surface and shafts of light.
 for k in range(4):
  pts=[(105+i*10,205+k*9+2*math.sin(i*.6+k)) for i in range(60)]
  path(p,pts,'#F5FFFC',1)
 for pts in [[(180,198),(209,198),(401,529),(356,500)],[(260,198),(287,198),(472,465),(436,440)],[(409,198),(425,198),(599,520),(571,491)]]:path(p,pts,'#DDF2E9',.1,'#DDF2E9')
 st('Water depth, surface ripples and light')
 # Sand and rock habitat.
 path(p,[(100,545),(163,539),(246,552),(320,540),(398,553),(502,540),(587,548),(700,538),(700,592),(100,592)],'#C4BDA2',.8,'#E5DEC1')
 for x,y,w,h in [(136,536,26,12),(617,535,43,18),(449,549,24,10),(223,541,17,9)]:
  pts=[(x,y),(x+w*.25,y-h),(x+w*.78,y-h*.65),(x+w,y),(x+w*.7,y+4),(x+4,y+3)]
  path(p,pts,'#8FA7A0',.7,'#ABC0B1')
 for j in range(65):circle(p,111+(j*83)%577,560+(j*13)%26,.8,'#C4B48D','#C4B48D',.2)
 # The fixed arc becomes the outer edge of a kelp leaf.
 outer=[q for seg in BASE[8:10] for q in seg]
 inner=[(340.5+(x-340.5)*.87,345.5+(y+70-345.5)*.87) for x,y in outer]
 leaf=[(x,y+70) for x,y in outer]+inner[::-1]
 path(p,leaf,'#5D8D77',.7,'#86B89A')
 path(p,[(340.5,460.5),(333,506),(344,552)],'#568C75',2)
 for pts in [[(338,512),(308,475),(310,453),(327,480),(338,512)],[(340,541),(370,505),(379,488),(373,519),(340,541)]]:path(p,pts,'#63967B',.7,'#95C3A0')
 for x in [175,196,568,589]:
  path(p,[(x,554),(x-7,516),(x+5,487)],'#739B83',1.5)
  path(p,[(x-5,529),(x-18,509),(x-16,497)],'#739B83',1)
 st('Seabed, rocks and kelp around the unchanged arc')
 # Small diagonal belongs to the outline of a ray viewed from above.
 a=(490.5,285.5);b=(538.0108185687617,252.23256669163925)
 path(p,[a,b,(558,259),(598,282),(573,310),(546,318),(519,301),a],'#6C949C',1,'#91B5B6')
 path(p,[(546,316),(557,341),(563,359),(555,377)],'#6C949C',1.5)
 circle(p,552,278,1.3,'#517D84','#517D84',.3);circle(p,566,279,1.3,'#517D84','#517D84',.3)
 for y in [288,293,298]:path(p,[(550,y),(560,y+1)],'#70989D',.65)
 for x,y,r in [(153,382,7),(171,363,3),(650,388,4),(661,362,2),(413,270,3),(430,251,2),(212,461,4),(223,432,2)]:extra_bubble(p,x,y,r)
 st('A ray and environmental depth cues')
 # Fixed circles show an overlaid history of one bubble. No circle outline edits.
 for cx,cy,r in [(285.5,310.5,54),(510.5,445.5,29)]:
  circle(p,cx,cy,r,'#9BBFC0','#DFF3EE',.5)
  arc(p,cx,cy,r-5,198,280,'#F9FFFC',3)
  arc(p,cx,cy,r-9,8,95,'#A8CED0',1)
  arc(p,cx,cy,r-13,208,249,'#F8FFFC',1.5)
 # A dotted temporal link is a diagram overlay, not the kelp or a measured trajectory.
 pts=[(478,431),(451,426),(414,410),(380,385),(349,362)]
 for a,b in zip(pts,pts[1:]):dash(p,a,b,'#79A3A5',.8,9)
 path(p,[(350,370),(349,362),(357,364)],'#79A3A5',1)
 base(p)
 st('Two moments of one bubble, with original marks overlaid')
 text(p,203,387,'LATER / NEARER THE VIEWER',9,'#426F70',True)
 text(p,473,491,'EARLIER / DEEPER',9,'#426F70',True)
 text(p,103,622,'Two moments overlaid for comparison; not two bubbles at the same instant.',11,'#586B62')
 footer(p,'Thinking move: change time, then use depth to explain size.','The arc becomes kelp; the diagonal becomes a ray. Context supports the time interpretation.')
 return stages

def desk(p):
 heading(p,'AFTER A SKETCHING SESSION','What if the marks are clues about what is missing?')
 stages=[]
 def st(n):stages.append({'name':n,'action_end':len(getattr(p,'actions',[]))})
 rect(p,83,195,637,407,'#B9A286','#EDDEC5',1.4)
 rect(p,89,200,625,396,'#D9C3A2',None,.5)
 # Wood grain is continuous across empty spaces, not a blank symbol background.
 for j,y in enumerate(range(214,595,21)):
  pts=[(92+i*12,y+2*math.sin(i*.32+j)+math.sin(i*.91)*.8) for i in range(52)]
  path(p,pts,'#DDC7A4',.65)
  if j%4==0:path(p,[(270,y+3),(308,y+4),(338,y+3)],'#D1B893',.6)
 st('Desk surface and wood grain')
 # Open sketchbook, clip and spine: surrounding objects give the traces a setting.
 path(p,[(97,224),(201,230),(209,424),(109,419)],'#CBBFA8',.5,'#D6CBB7')
 path(p,[(93,219),(192,226),(202,416),(100,409)],'#AEAB97',.8,'#FFFCF1')
 path(p,[(141,222),(151,413)],'#D0CAB7',1)
 for y in [248,267,287,307,327,347,367,388]:path(p,[(153,y),(190,y+3)],'#D6D0BD',.6)
 # Rough house sketch instead of actual private written content.
 path(p,[(104,272),(121,255),(135,277)],'#90A7A8',.8)
 path(p,[(108,273),(112,300),(134,302),(133,278)],'#90A7A8',.8)
 rect(p,120,287,6,12,'#90A7A8',None,.6)
 rect(p,158,231,12,6,'#8FA2A0','#B3C3BE',.7)
 st('Sketchbook, rough drawing and desk context')
 # Paper tear incorporates the original diagonal exactly.
 a=(490.5,285.5);b=(538.0108185687617,252.23256669163925)
 path(p,[(428,226),(582,226),(582,242),(550,246),b,a,(477,300),(467,296),(450,319),(428,326)],'#C2B397',.8,'#FFFEF5')
 for y in [247,260,274]:path(p,[(438,y),(484,y)],'#C5C1AF',.65)
 path(p,[(556,231),(573,231),(573,241)],'#D4C7AD',.6)
 # Dotted cut-out scrap shape nearby, with no claim of a true reconstruction.
 path(p,[(565,299),(587,295),(596,312),(574,321),(565,299)],'#CAB89C',.6,'#FAF2DF')
 # Phone and watercolor palette: explicitly mundane studio objects.
 rect(p,620,342,48,89,'#81979C','#C2D0CF',1)
 rect(p,625,348,38,72,'#98B0B2','#E0ECE7',.5)
 circle(p,644,425,1.8,'#91A6A7','#91A6A7',.3)
 text(p,631,372,'PAUSE',7,'#799291',True)
 for y in [386,394,402]:path(p,[(632,y),(655,y)],'#B2C8C1',1)
 palette=[(632+43*math.cos(j*math.pi/60),510+24*math.sin(j*math.pi/60)) for j in range(121)]
 path(p,palette,'#B6AA91',.8,'#FAF2DF')
 for x,y,co in [(608,501,'#A4B88B'),(628,496,'#E1B47D'),(649,502,'#A0BDC6'),(643,519,'#C69F9E'),(622,524,'#B8A3BD')]:circle(p,x,y,4,co,co,.5)
 circle(p,605,518,5,'#BAAF95','#EDDEC5',.6)
 st('Torn note, phone and remaining art materials')
 # Mug ring and smaller jar ring. Neither missing object is drawn.
 for cx,cy,r,col in [(285.5,310.5,54,'#BD9566'),(510.5,445.5,29,'#90AAA6')]:
  arc(p,cx,cy,r+4,9,151,col,1.5)
  arc(p,cx,cy,r-3,171,302,col,1.2)
  for j,ang in enumerate([22,45,167,203,252,319]):
   xx=cx+(r+8+j%3)*math.cos(math.radians(ang));yy=cy+(r+8+j%3)*math.sin(math.radians(ang));circle(p,xx,yy,1+j%2*.5,col,col,.4)
 # Arc becomes a scuff, with layered scratches and a little dust.
 for rr,a1,a2 in [(110,15,87),(119,20,78),(112,28,67),(122,40,81)]:arc(p,340.5,345.5,rr,a1,a2,'#B9A381',.65)
 for j in range(12):
  ang=20+j*5;x,y=(340.5+125*math.cos(math.radians(ang)),345.5+125*math.sin(math.radians(ang)));path(p,[(x,y),(x+2,y+1)],'#C7AE86',.7)
 # Pencil and paintbrush with ferrules and bristles.
 path(p,[(243,497),(344,554)],'#B69865',5);path(p,[(243,497),(344,554)],'#E9C97C',3)
 path(p,[(344,554),(352,561),(340,557)],'#7C8F93',.8,'#98A5A4')
 path(p,[(352,561),(348,558)],'#6D7B7A',1)
 path(p,[(408,532),(482,561)],'#A99A7F',3)
 path(p,[(477,559),(489,564)],'#90A4A3',5)
 path(p,[(489,564),(507,572),(503,562),(489,561)],'#7E8D80',.8,'#B0BE9F')
 # Keys and crumbs establish that the surface was used, not an abstract diagram.
 circle(p,554,563,6,'#91A3A0',None,1.2)
 path(p,[(559,564),(577,570),(577,574),(570,572),(571,568)],'#91A3A0',2)
 for x,y in [(367,276),(356,291),(381,288),(388,275),(366,307)]:path(p,[(x,y),(x+3,y-2),(x+4,y+2),(x,y)],'#BC9D74',.4,'#D4B98F')
 base(p);st('Stains, scuff, droplets and unchanged original marks')
 text(p,231,387,'A MUG WAS HERE?',9,'#846E51',True)
 text(p,473,496,'A SMALL JAR?',9,'#68887F',True)
 text(p,115,625,'The marks suggest a story. They do not establish one correct explanation.',11,'#586B62')
 footer(p,'Thinking move: infer what might have left a trace.','We changed objects into evidence, then added context that makes several stories plausible.')
 return stages

