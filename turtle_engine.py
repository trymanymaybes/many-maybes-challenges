"""Three interpretations, using Python Turtle's standard navigation engine.

Headless export: Turtle TNavigator records the same pen movements to SVG/PNG.
Exports recorded Turtle movements without opening a display.
No AI-generated imagery. Starter coordinates are preserved exactly.
"""
from pathlib import Path
import turtle, math, xml.etree.ElementTree as ET, html, argparse
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'images';OUT.mkdir(exist_ok=True)
GREEN='#233F36';BLUE='#547D91';PALE='#EAF1F2';TAN='#C1A682';INK='#263C35';RED='#B55C49';CREAM='#FAF8F1'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def load_font(size,bold=False):
 candidates=[BOLD if bold else FONT,'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf','Arial.ttf']
 for candidate in candidates:
  try:return ImageFont.truetype(candidate,size)
  except OSError:pass
 return ImageFont.load_default(size=size)
BASE=[]
for e in ET.parse(Path(__file__).with_name('challenge-01-turtle-starter.svg')).getroot().iter():
 if 'points' in e.attrib:BASE.append([tuple(map(float,p.split(','))) for p in e.attrib['points'].split()])
class ExportTurtle(turtle.TNavigator):
 def __init__(self):
  super().__init__();self.actions=[];self.down=False;self.color=INK;self.width=2;self.fill=None;self.fillpoints=None
 def _goto(self,end):
  start=self._position
  if self.down:self.actions.append(('line',[(start[0],-start[1]),(end[0],-end[1])],self.color,self.width))
  if self.fillpoints is not None:self.fillpoints.append((end[0],-end[1]))
  self._position=end
 def penup(self):self.down=False
 def pendown(self):self.down=True
 def pencolor(self,c):self.color=c
 def pensize(self,w):self.width=w
 def fillcolor(self,c):self.fill=c
 def begin_fill(self):self.fillpoints=[(self._position[0],-self._position[1])];self.fillstart=len(self.actions)
 def end_fill(self):
  self.actions.insert(self.fillstart,('fill',self.fillpoints,self.fill,0));self.fillpoints=None
 def speed(self,*a):return 0
 def _tracer(self,*a):return 0
 def _delay(self,*a):return 0
 def write(self,s,font=('DejaVu Sans',12,'normal'),align='left'):
  self.actions.append(('text',(self._position[0],-self._position[1]),s,font[1],font[2],self.color,align))

def go(p,x,y):p.goto(x,-y)
def path(p,pts,col=BLUE,width=2,fill=None):
 p.penup();p.pencolor(col);p.pensize(width);go(p,*pts[0]);p.pendown()
 if fill:p.fillcolor(fill);p.begin_fill()
 for a in pts[1:]:go(p,*a)
 if fill:go(p,*pts[0]);p.end_fill()
 p.penup()
def rect(p,x,y,w,h,col=BLUE,fill=None,width=2):path(p,[(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y)],col,width,fill)
def circle(p,x,y,r,col=BLUE,fill=None,width=2):
 p.penup();go(p,x,y+r);p.setheading(0);p.pencolor(col);p.pensize(width);p.pendown()
 if fill:p.fillcolor(fill);p.begin_fill()
 p.circle(r,steps=144)
 if fill:p.end_fill()
 p.penup()
def arc(p,cx,cy,r,a,b,col=BLUE,width=2):
 pts=[(cx+r*math.cos(math.radians(v)),cy+r*math.sin(math.radians(v))) for v in [a+(b-a)*j/80 for j in range(81)]]
 path(p,pts,col,width)
def text(p,x,y,s,size=12,col=INK,bold=False):
 p.penup();go(p,x,y);p.pencolor(col);p.write(s,font=('DejaVu Sans',size,'bold' if bold else 'normal'))
def dash(p,a,b,col=BLUE,width=1.5,step=12):
 dx=b[0]-a[0];dy=b[1]-a[1];L=math.hypot(dx,dy)
 for s in range(0,int(L),step):
  aa=s/L;bb=min(s+step*.55,L)/L;path(p,[(a[0]+dx*aa,a[1]+dy*aa),(a[0]+dx*bb,a[1]+dy*bb)],col,width)
def base(p):
 # Added graphics never edit these arrays. The starter is redrawn on top.
 for pts in BASE:path(p,[(x,y+70) for x,y in pts],GREEN,3)
def header(p,n,title,sub):
 text(p,35,34,'MANY MAYBES / CHALLENGE 01',11,GREEN,True)
 text(p,35,73,title,27,GREEN,True);text(p,35,105,sub,13,BLUE)
def footer(p,move,explain):
 path(p,[(35,640),(765,640)],'#D1DCD6',1)
 text(p,35,674,move,18,GREEN,True)
 text(p,35,704,explain,12,INK)
 text(p,35,735,'Dark green = original marks. Added illustration = one possible interpretation.',10,BLUE)

def export(p,name):
 scale=2;im=Image.new('RGB',(1600,1540),CREAM);d=ImageDraw.Draw(im)
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="770" viewBox="0 0 800 770"><rect width="800" height="770" fill="{CREAM}"/>']
 for a in p.actions:
  if a[0]=='line':
   _,pts,c,w=a;d.line([(x*scale,y*scale) for x,y in pts],fill=c,width=max(1,round(w*scale)))
   coords=' '.join(f'{x:.4f},{y:.4f}' for x,y in pts);parts.append(f'<polyline points="{coords}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>')
  elif a[0]=='fill':
   _,pts,c,_=a;d.polygon([(x*scale,y*scale) for x,y in pts],fill=c);coords=' '.join(f'{x:.4f},{y:.4f}' for x,y in pts);parts.append(f'<polygon points="{coords}" fill="{c}"/>')
  elif a[0]=='text':
   _,(x,y),s,sz,style,c,align=a;ff=load_font(sz*scale,style=='bold')
   d.text((x*scale,y*scale),s,font=ff,fill=c,anchor='ls')
   parts.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,sans-serif" font-size="{sz}" font-weight="{"bold" if style=="bold" else "normal"}" fill="{c}">{html.escape(s)}</text>')
 parts.append('</svg>');im.save(OUT/f'{name}.png');(OUT/f'{name}.svg').write_text('\n'.join(parts))
 return im

