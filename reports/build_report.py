#!/usr/bin/env python3
"""Build the cited research PDF from the AI-assisted project research notes.

Dependencies: reportlab, mistune, pypdf. No dataset responses are embedded.
Run: python3 reports/build_report.py
"""
from pathlib import Path
import collections
import html
import json
import re
from urllib.parse import urljoin, urlparse, unquote

import mistune
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, HRFlowable, CondPageBreak,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / 'skill-data-atlas-complete-research-report.pdf'
DATE = '29 October 2026'
REVISION_DATE = '30 October 2026'
REPO = 'https://github.com/AndersH3/skill-data-atlas/'
NAVY = colors.HexColor('#122D45')
TEAL = colors.HexColor('#087F8C')
INK = colors.HexColor('#223747')
MUTED = colors.HexColor('#596D7A')
PALE = colors.HexColor('#EDF4F6')
RULE = colors.HexColor('#CDD9DF')

for name, filename in [('Research','DejaVuSans.ttf'),('Research-Bold','DejaVuSans-Bold.ttf'),
                       ('Research-Italic','DejaVuSans-Oblique.ttf'),('Research-BoldItalic','DejaVuSans-BoldOblique.ttf'),
                       ('ResearchMono','DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/' + filename))
pdfmetrics.registerFontFamily('Research', normal='Research', bold='Research-Bold',
                              italic='Research-Italic', boldItalic='Research-BoldItalic')

S = {}
S['body'] = ParagraphStyle('ResearchBody', fontName='Research', fontSize=9.2, leading=14,
    textColor=INK, spaceAfter=6, allowWidows=0, allowOrphans=0, splitLongWords=1)
S['h1'] = ParagraphStyle('Chapter', parent=S['body'], fontName='Research-Bold', fontSize=21,
    leading=27, textColor=NAVY, spaceBefore=4, spaceAfter=17, keepWithNext=1)
S['h2'] = ParagraphStyle('Section', parent=S['body'], fontName='Research-Bold', fontSize=13,
    leading=18, textColor=TEAL, spaceBefore=15, spaceAfter=9, keepWithNext=1)
S['h3'] = ParagraphStyle('Subsection', parent=S['body'], fontName='Research-Bold', fontSize=10.5,
    leading=15, textColor=NAVY, spaceBefore=11, spaceAfter=7, keepWithNext=1)
S['small'] = ParagraphStyle('Small', parent=S['body'], fontSize=8, leading=11.5, textColor=MUTED, spaceAfter=4)
S['table'] = ParagraphStyle('Cell', parent=S['body'], fontSize=7.4, leading=10.7, spaceAfter=0)
S['th'] = ParagraphStyle('TableHeading', parent=S['table'], fontName='Research-Bold', textColor=colors.white)
S['quote'] = ParagraphStyle('Callout', parent=S['body'], leftIndent=12, rightIndent=12,
    borderPadding=10, backColor=PALE, spaceBefore=5, spaceAfter=12)
S['code'] = ParagraphStyle('Code', parent=S['small'], fontName='ResearchMono', fontSize=7.3,
    leading=10.5, backColor=PALE, borderPadding=8, spaceAfter=10)
S['bullet'] = ParagraphStyle('BulletBody', parent=S['body'], leftIndent=13, firstLineIndent=-10)
S['cover_title'] = ParagraphStyle('CoverTitle', fontName='Research-Bold', fontSize=34,
    leading=43, textColor=NAVY, spaceAfter=20)
S['cover_sub'] = ParagraphStyle('CoverSubtitle', parent=S['body'], fontSize=15, leading=23,
    textColor=MUTED, spaceAfter=21)

def clean(s):
    return s.replace('\u2011','-').replace('\u2013','-').replace('\u2014',' - ').replace('\u2212','-')

sources = collections.OrderedDict()
source_names={}
def citation(url, title):
    title=clean(title or '')
    if not title or title.startswith(('https://','http://')) or re.match(r'^(source\s*\d*|primary evidence|download/landing)$',title,re.I):
        title=source_names.get(url) or (urlparse(url).netloc+' - '+unquote(urlparse(url).path.rstrip('/').split('/')[-1]).replace('_',' '))
    if url not in sources:
        sources[url] = {'number':len(sources)+1,'title':title or url}
    n = sources[url]['number']
    return f'<link href="{html.escape(url,quote=True)}" color="#087F8C">[{n}]</link>'

def text_only(tokens):
    return ''.join(t.get('raw',text_only(t.get('children',[]))) for t in tokens)

def inlines(tokens, context='README.md'):
    out=[]
    for t in tokens:
        typ=t['type']; children=t.get('children',[])
        if typ=='text':out.append(html.escape(clean(t['raw'])))
        elif typ=='strong':out.append('<b>'+inlines(children,context)+'</b>')
        elif typ=='emphasis':out.append('<i>'+inlines(children,context)+'</i>')
        elif typ=='codespan':out.append('<font name="ResearchMono" size="8">'+html.escape(clean(t['raw']))+'</font>')
        elif typ=='link':
            url=t['attrs']['url']
            if not url.startswith(('http://','https://')):
                url=urljoin(REPO+'blob/main/'+context,url)
            label=text_only(children)
            shown=inlines(children,context)
            if label.startswith(('http://','https://')):shown='Source'
            out.append(shown+' '+citation(url,label))
        elif typ in ('softbreak','linebreak'):out.append(' ' if typ=='softbreak' else '<br/>')
        elif typ in ('inline_html','block_html'):out.append(html.escape(clean(t.get('raw',''))))
        else:out.append(inlines(children,context) if children else html.escape(clean(t.get('raw',''))))
    return ''.join(out)

heading_count=0
def heading(text,level=1):
    global heading_count
    heading_count+=1
    p=Paragraph(html.escape(clean(text)),S['h1' if level==1 else 'h2' if level==2 else 'h3'])
    p.bookmark='section-'+str(heading_count)
    p.toc_level=0 if level==1 else 1 if level==2 else None
    p.plain_heading=clean(text)
    return p

WIDTH=A4[0]-102
def render_blocks(tokens, context, skip_first_heading=True):
    flow=[];first=True
    for t in tokens:
        typ=t['type']
        if typ=='heading':
            if first and skip_first_heading:first=False;continue
            first=False
            level=min(t['attrs']['level']+1,3)
            flow.append(heading(text_only(t.get('children',[])),level))
        elif typ in ('paragraph','block_text'):
            flow.append(Paragraph(inlines(t.get('children',[]),context),S['body']))
        elif typ=='list':
            ordered=t.get('attrs',{}).get('ordered',False)
            start=t.get('attrs',{}).get('start',1)
            for i,item in enumerate(t['children']):
                first_item=True
                for child in item.get('children',[]):
                    if child['type'] in ('block_text','paragraph'):
                        prefix=f'{start+i}. ' if ordered else '\u2022 '
                        flow.append(Paragraph((prefix if first_item else '')+inlines(child.get('children',[]),context),S['bullet']))
                        first_item=False
                    else:flow+=render_blocks([child],context,False)
        elif typ=='table':
            # Keep a heading with the first table row without moving a whole
            # otherwise-splittable table to a fresh page.
            if flow and getattr(flow[-1],'bookmark',None):
                lead=flow.pop();lead.keepWithNext=0
                flow.extend([CondPageBreak(135),lead])
            matrix=[]
            for chunk in t['children']:
                rows=[chunk] if chunk['type']=='table_head' else chunk['children']
                for row in rows:
                    matrix.append([Paragraph(inlines(cell.get('children',[]),context),S['th' if not matrix else 'table']) for cell in row['children']])
            n=len(matrix[0]); weights=([.24,.76] if n==2 else [.2,.26,.54] if n==3 else [.19,.27,.27,.27] if n==4 else [1/n]*n)
            if n==3 and matrix[0][0].getPlainText()=='Payload':
                weights=[.58,.17,.25]
            if n==3 and matrix[0][0].getPlainText()=='Work area':
                weights=[.18,.44,.38]
            if n==4 and matrix[0][0].getPlainText()=='Archive' and 'SHA-256' in matrix[0][-1].getPlainText():
                weights=[.23,.14,.12,.51]
            table=Table(matrix,colWidths=[WIDTH*x for x in weights],repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),
                ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
                ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),.6,TEAL),
                ('LINEBELOW',(0,-1),(-1,-1),.4,RULE)]))
            flow += [table,Spacer(1,12)]
        elif typ=='block_code':
            for line in t.get('raw','').splitlines():flow.append(Paragraph(html.escape(clean(line)) or ' ',S['code']))
        elif typ=='block_quote':
            for c in t.get('children',[]):
                if c['type']=='paragraph':flow.append(Paragraph(inlines(c.get('children',[]),context),S['quote']))
                else:flow+=render_blocks([c],context,False)
        elif typ=='thematic_break':flow.append(HRFlowable(width=WIDTH,color=RULE,spaceBefore=8,spaceAfter=8))
    return flow

class ResearchDoc(BaseDocTemplate):
    def __init__(self,path):
        super().__init__(str(path),pagesize=A4,leftMargin=51,rightMargin=51,topMargin=55,bottomMargin=49,
            title='Skill Data Atlas: Complete Research and Redistribution Report',
            author='Skill Data Atlas project; AI-assisted with OpenAI Codex',subject='Human skill-response datasets, access, licensing and scoring research')
        frame=Frame(self.leftMargin,self.bottomMargin,self.width,self.height,id='normal',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates(PageTemplate(id='pages',frames=[frame],onPage=self.decorate))
    def decorate(self,c,doc):
        if doc.page==1:
            c.setFillColor(TEAL);c.rect(0,A4[1]-17,A4[0],17,fill=1,stroke=0);return
        c.setStrokeColor(RULE);c.setLineWidth(.5);c.line(51,A4[1]-34,A4[0]-51,A4[1]-34)
        c.setFont('Research',7.3);c.setFillColor(MUTED)
        c.drawString(51,A4[1]-25,'SKILL DATA ATLAS  /  RESEARCH & REDISTRIBUTION REVIEW')
        c.drawString(51,28,'Research: '+DATE+'  |  Report revision: '+REVISION_DATE)
        c.drawRightString(A4[0]-51,28,str(doc.page))
    def afterFlowable(self,f):
        if getattr(f,'bookmark',None):
            self.canv.bookmarkPage(f.bookmark)
            if f.toc_level is not None:
                self.notify('TOCEntry',(f.toc_level,f.plain_heading,self.page,f.bookmark))
                self.canv.addOutlineEntry(f.plain_heading,f.bookmark,level=f.toc_level,closed=False)
            else:
                self.canv.addOutlineEntry(f.plain_heading,f.bookmark,level=1,closed=True)

def main():
    catalogue=json.loads((ROOT/'data/catalogue.json').read_text())
    for row in catalogue:
        for url in row['source_urls']:source_names.setdefault(url,row['name']+' - source documentation')
    source_names.update({
        'https://cran.r-project.org/doc/manuals/r-release/R-exts.html#Licensing':'R Core Team - Writing R Extensions: Licensing',
        'https://cran.r-project.org/web/packages/policies.html':'CRAN Repository Policy - source formats and licensing',
    })
    audit_path=ROOT/'data/redistribution-audit.json'
    audit=json.loads(audit_path.read_text()) if audit_path.exists() else {'decisions':[],'summary':'Acquisition audit in progress; rebuild after completion.'}
    sources.clear()
    md=mistune.create_markdown(renderer='ast',plugins=['table','url'])
    short_ai=(ROOT/'reports/ai-disclosure-short.md').read_text()
    short_ai=re.sub(r'^# [^\n]+\n','',short_ai,count=1).strip()
    short_ai=html.escape(clean(short_ai)).replace('Appendix A','<link href="#ai-disclosure" color="#087F8C">Appendix A</link>')
    story=[Spacer(1,75),Paragraph('Skill Data Atlas',S['cover_title']),
           Paragraph('A complete review of human skill-response datasets and their redistribution conditions',S['cover_sub']),
           HRFlowable(width=75,thickness=4,color=TEAL,hAlign='LEFT'),Spacer(1,24),
           Paragraph('37 source profiles across cognitive ability, educational and adult assessments, subject learning, language and short-answer performance.',S['body']),
           Spacer(1,18),Paragraph('<b>Research and acquisition date</b><br/>'+DATE,S['body']),
           Paragraph('<b>Document revision</b><br/>'+REVISION_DATE+' (project branding and AI disclosure)',S['body']),
           Paragraph('<b>Prepared for</b><br/>AndersH3 / Skill Data Atlas',S['body']),
           Spacer(1,15),Paragraph('<b>AI disclosure</b><br/>'+short_ai,S['quote']),
           Paragraph('<link href="'+REPO+'" color="#087F8C">github.com/AndersH3/skill-data-atlas</link>',S['small']),PageBreak(),
           heading('Contents')]
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC0',fontName='Research-Bold',fontSize=10,leading=17,textColor=NAVY,leftIndent=0,firstLineIndent=0,spaceBefore=8),
       ParagraphStyle('TOC1',fontName='Research',fontSize=8.3,leading=12,textColor=MUTED,leftIndent=15,firstLineIndent=0)]
    story += [toc,PageBreak()]
    sections=[('1. Executive findings','reports/executive-summary.md'),('2. Research method and analysis guidance','research/methodology.md'),
              ('3. Redistribution decisions and downloaded collection','reports/acquisition-review.md'),
              ('4. Cognitive ability and performance','research/cognitive-ability.md'),
              ('5. Large educational and adult assessments','research/large-scale-assessments.md'),
              ('6. Subject tests and learning-response data','research/subject-tests-and-learning.md'),
              ('7. Language assessment and constructed responses','research/language-and-short-answers.md'),
              ('8. Discovery resources and exclusions','research/discovery-and-exclusions.md'),
              ('9. Verification, limitations and reproducibility','reports/verification-summary.md')]
    source_parts=[]
    for title,file in sections:
        path=ROOT/file
        if not path.exists():continue
        text=path.read_text();source_parts.append('# '+title+'\n\n'+re.sub(r'^# [^\n]+\n','',text,count=1))
        story.append(heading(title))
        story+=render_blocks(md(clean(text)),file)
        story.append(PageBreak())
    # Parse the appendix before building the bibliography so its evidence links
    # receive reference entries, while keeping the appendix at the report end.
    appendix_path='reports/ai-disclosure.md'
    appendix_text=(ROOT/appendix_path).read_text()
    appendix_heading=heading('Appendix A. AI disclosure')
    appendix_heading.bookmark='ai-disclosure'
    appendix_flow=[appendix_heading]+render_blocks(md(clean(appendix_text)),appendix_path)
    story.append(heading('10. Sources and references'))
    story.append(Paragraph('Numbered references correspond to clickable citations throughout the report. Source terms and dataset versions were checked on 29 October 2026 unless a profile states a narrower evidence scope. Links are supplied for verification; repository copies do not imply that external content inherits the project licence.',S['body']))
    for url,item in list(sources.items()):
        n=item['number'];title=html.escape(item['title']);safe=html.escape(url,quote=True)
        story.append(Paragraph(f'<b>[{n}] {title}</b><br/><link href="{safe}" color="#087F8C">{html.escape(url)}</link>',S['small']))
    story.extend([PageBreak(),*appendix_flow])
    ResearchDoc(PDF).multiBuild(story)
    appendix_source=re.sub(r'^# [^\n]+\n','',appendix_text,count=1)
    (ROOT/'reports/complete-report-source.md').write_text('# Front-report AI disclosure\n\n'+re.sub(r'^# [^\n]+\n','',(ROOT/'reports/ai-disclosure-short.md').read_text(),count=1).strip()+'\n\n'+'\n\n'.join(source_parts)+'\n\n# Sources\n\n'+'\n'.join(f"[{v['number']}] {v['title']} - {u}" for u,v in sources.items())+'\n\n# Appendix A. AI disclosure\n\n'+appendix_source.rstrip()+'\n')
    from pypdf import PdfReader
    reader=PdfReader(PDF)
    text='\n'.join(p.extract_text() or '' for p in reader.pages)
    assert len(reader.pages)>20,'Incomplete report'
    compact=re.sub(r'\s+','',text)
    assert all(r['id'] in compact for r in catalogue),'A catalogue profile is missing from the report audit'
    assert 'Acquisition audit in progress' not in text,'Acquisition report is incomplete'
    assert 'AI disclosure' in (reader.pages[0].extract_text() or ''),'Front disclosure missing'
    assert 'Appendix A. AI disclosure' in text,'Disclosure appendix missing'
    assert 'Rebuilding the PDF is distinct' in text,'Full disclosure text missing'
    metrics={'pages':len(reader.pages),'references':len(sources),'text_characters':len(text),'bytes':PDF.stat().st_size,
             'catalogue_profiles':len(catalogue),'output':PDF.relative_to(ROOT).as_posix(),
             'research_snapshot':'2026-10-29','document_revision':'2026-10-30',
             'front_ai_disclosure':True,'full_ai_disclosure_appendix':True}
    (OUT/'report-quality-check.json').write_text(json.dumps(metrics,indent=2)+'\n')
    print(json.dumps(metrics,indent=2))

if __name__=='__main__':main()
