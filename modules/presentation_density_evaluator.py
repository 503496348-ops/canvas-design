from __future__ import annotations
from dataclasses import dataclass
import re
@dataclass
class DensityReport:
    score:int; level:str; issues:list[str]; suggestions:list[str]
def evaluate_slide_text(text:str)->DensityReport:
    lines=[x.strip() for x in text.splitlines() if x.strip()]
    bullets=[x for x in lines if re.match(r'^[-*•\d]+[.)、\s]', x)]
    numbers=re.findall(r'\d+(?:\.\d+)?%?|[一二三四五六七八九十]+', text)
    headings=[x for x in lines if len(x)<=24 and not x.endswith('。')]
    issues=[]; suggestions=[]; score=100
    if len(lines)<10: issues.append('content too thin for a premium infographic slide'); suggestions.append('add 3-4 modules with title, points, and callouts'); score-=25
    if len(bullets)<6: issues.append('not enough structured bullet/cell content'); score-=15
    if len(numbers)<3: issues.append('few visible metrics or numbered anchors'); suggestions.append('add real counts, dates, percentages, or ranked labels without fabricating data'); score-=15
    if len(headings)<3: issues.append('weak modular hierarchy'); score-=15
    if re.search(r'lorem|ipsum|placeholder|占位|待填写', text, re.I): issues.append('placeholder text detected'); score-=40
    score=max(0,min(100,score)); level='excellent' if score>=85 else 'usable' if score>=70 else 'thin' if score>=50 else 'fail'
    return DensityReport(score, level, issues, suggestions)
