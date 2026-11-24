#!/usr/bin/env python3
"""Render the public academic CV in the same typography and layout as the supplied reference."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "ibrahim-badawi-platform" / "Ibrahem_Badawi_CV.pdf"
FONT_SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/crosextra/Carlito-Bold.ttf"
pdfmetrics.registerFont(TTFont("NotoSerifCV", FONT_SERIF))
pdfmetrics.registerFont(TTFont("CarlitoBoldCV", FONT_BOLD))
WIDTH, HEIGHT = 595.276, 841.89

# Position measurements (A4, upper-left origin) preserve the original 1-page CV.
# Tuple: x, y, font size, serif / bold, text, color.
rows = [
 (226.18,32,8,"s","Ibrahem J. Badawi  |  Management Information Systems and Digital Innovation","#606873"),
 (421.35,806.89,8,"s","Ibrahem J. Badawi  |  Page 1","#606873"),
 (72,90,19,"b","Ibrahem J. Badawi","#111111"),
 (72,109,10,"s","Management Information Systems | Digital Innovation | Digital Product Development","#4b5058"),
 (72,128,10,"s","Gaza, Palestine | Personal portfolio | GitHub | LinkedIn","#4b5058"),
 (72,152,12,"b","Professional Profile","#111111"),
 (72,169,10,"s","Management Information Systems specialist and founder of TechMood Technology, focused on","#20252b"),
 (72,183,10,"s","requirements analysis, digital product development, organisational processes and","#20252b"),
 (72,197,10,"s","technology-enabled innovation.","#20252b"),
 (72,221,12,"b","Education","#111111"),
 (72,238,10,"s","Al-Aqsa University, Gaza, Palestine | Management Information Systems and Contemporary","#20252b"),
 (72,252,10,"s","Business. Bachelor's studies completed. Cumulative average: 79.82% (145","#20252b"),
 (72,266,10,"s","credit hours). Graduation project: 93/100; field training: 89/100.","#20252b"),
 (72,290,12,"b","Academic Research","#111111"),
 (72,307,10,"s","The Role of Organizational Culture in Enabling the Application of E-Management —","#20252b"),
 (72,321,10,"s","collaborative undergraduate research examining organisational factors influencing electronic","#20252b"),
 (72,335,10,"s","management adoption.","#20252b"),
 (72,359,12,"b","Professional Experience","#111111"),
 (72,376,10,"s","TechMood Technology | Founder and Product Lead | Ongoing","#20252b"),
 (72,395,10,"s","Analyse user requirements, structure product workflows, plan features and review user","#20252b"),
 (72,409,10,"s","experiences across digital initiatives. Coordinate TechMood Community, connecting","#20252b"),
 (72,423,10,"s","professionals interested in management, information systems and technology.","#20252b"),
 (72,442,10,"s","Qiba Quran Center | Educational and Administrative Coordination | July 2019 – July 2022","#20252b"),
 (72,461,10,"s","Supported educational activities, operational follow-up, staff coordination and","#20252b"),
 (72,475,10,"s","communication.","#20252b"),
 (72,499,12,"b","Selected Digital Projects","#111111"),
 (72,516,10,"s","MentorMood — learning and professional mentoring; GrowthMood — training-centre","#20252b"),
 (72,530,10,"s","management; CodeMood — coding education; ImpactMood — volunteer and community","#20252b"),
 (72,544,10,"s","coordination.","#20252b"),
 (72,563,10,"s","TechMood Technology — project portfolio","#20252b"),
 (72,587,12,"b","Professional Credentials","#111111"),
 (72,604,10,"s","MBA in AI Graduate — professional certificate in business and artificial intelligence.","#20252b"),
 (72,628,12,"b","Skills and Languages","#111111"),
 (72,645,10,"s","Requirements analysis, product planning, UX design, business processes, digital","#20252b"),
 (72,659,10,"s","transformation and stakeholder coordination. Arabic: native; English: intermediate.","#20252b"),
]
c=canvas.Canvas(str(OUTPUT),pagesize=(WIDTH,HEIGHT),pageCompression=1)
for x,y,size,face,text,color in rows:
    c.setFillColor(color)
    c.setFont("CarlitoBoldCV" if face=="b" else "NotoSerifCV",size)
    c.drawString(x,HEIGHT-y,text)

# Hyperlinks are invisible, keeping the reference styling.
links=[
 ("Personal portfolio",109,128,"https://ibrahem-badawi-platform.vercel.app/"),
 ("GitHub",109,128,"https://github.com/IbrahemJBadawi"),
 ("LinkedIn",109,128,"https://www.linkedin.com/in/ibrahemjbadawi/"),
 ("TechMood Community",409,423,"https://t.me/techmoodcom"),
]
for term,baseline_low,baseline_high,url in links:
    for x,y,size,face,text,color in rows:
        if term in text and baseline_low <= y <= baseline_high:
            font="CarlitoBoldCV" if face=="b" else "NotoSerifCV"
            preceding=text.split(term,1)[0]
            x1=x+pdfmetrics.stringWidth(preceding,font,size)
            x2=x1+pdfmetrics.stringWidth(term,font,size)
            c.linkURL(url,(x1,HEIGHT-y-3,x2,HEIGHT-y+11),relative=0,thickness=0)
c.save()
if OUTPUT.stat().st_size < 8000:
    raise RuntimeError("Generated CV is unexpectedly small")
print(f"Generated {OUTPUT}: {OUTPUT.stat().st_size} bytes")
