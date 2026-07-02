import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from modules.presentation_density_evaluator import evaluate_slide_text

def test_density_detects_thin_slide():
    r=evaluate_slide_text('标题\n- 一个点\n- 两个点')
    assert r.score < 70 and r.issues

def test_density_accepts_structured_slide():
    text='增长飞轮\n导语：围绕获客、转化、复购三段建立闭环\n1. 获客模块\n- 入口统一\n- 线索分层\n- 7日回访\n2. 转化模块\n- 话术A/B\n- 成交率18%\n- 样板案例\n3. 复购模块\n- 30天触达\n- 2类权益\n- 复盘面板\n底部总结：先做闭环，再扩规模'
    assert evaluate_slide_text(text).score >= 70
