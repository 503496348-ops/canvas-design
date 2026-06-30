/*
 * presenter-runtime.js — lightweight presenter mode for Canvas Design decks.
 * Contract:
 *   - Slides: .slide or section[data-title]
 *   - Speaker notes: <aside class="notes">...</aside> inside each slide
 *   - Press S to open presenter window
 *   - Arrow keys sync between audience and presenter
 */
(function () {
  const slides = Array.from(document.querySelectorAll('.slide, section[data-title]'));
  if (!slides.length) return;

  let current = Math.max(0, slides.findIndex(s => s.classList.contains('active') || s.classList.contains('is-active')));
  let presenter = null;
  const channel = ('BroadcastChannel' in window) ? new BroadcastChannel('canvas-design-presenter') : null;
  const startTime = Date.now();

  function titleOf(slide, idx) {
    return slide.dataset.title || slide.querySelector('h1,h2')?.textContent?.trim() || `Slide ${idx + 1}`;
  }

  function notesOf(slide) {
    return slide.querySelector('aside.notes')?.innerHTML?.trim() || '<em>本页暂无讲者备注。</em>';
  }

  function activate(idx, broadcast = true) {
    current = Math.max(0, Math.min(idx, slides.length - 1));
    slides.forEach((s, i) => {
      s.classList.toggle('active', i === current);
      s.classList.toggle('is-active', i === current);
      s.style.display = i === current ? '' : 'none';
    });
    if (broadcast) channel?.postMessage({ type: 'goto', idx: current });
    renderPresenter();
  }

  function elapsed() {
    const sec = Math.floor((Date.now() - startTime) / 1000);
    const m = String(Math.floor(sec / 60)).padStart(2, '0');
    const s = String(sec % 60).padStart(2, '0');
    return `${m}:${s}`;
  }

  function presenterHtml() {
    const slide = slides[current];
    const next = slides[Math.min(current + 1, slides.length - 1)];
    const noteHtml = notesOf(slide);
    const css = `
      body{margin:0;background:#101114;color:#f5f5f0;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Noto Sans SC',system-ui,sans-serif;}
      .grid{display:grid;grid-template-columns:1.2fr .8fr;grid-template-rows:1fr 1fr;gap:14px;height:100vh;padding:14px;box-sizing:border-box;}
      .card{background:#1b1d22;border:1px solid #333842;border-radius:14px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.28);}
      .head{height:38px;display:flex;align-items:center;justify-content:space-between;padding:0 14px;background:#242832;color:#aeb6c5;font-size:12px;text-transform:uppercase;letter-spacing:.08em;}
      .body{padding:18px;font-size:20px;line-height:1.6;}
      .preview{display:flex;align-items:center;justify-content:center;height:calc(100% - 38px);font-size:28px;text-align:center;padding:24px;box-sizing:border-box;background:#f7f3ea;color:#151515;}
      .notes{grid-row:1/3;grid-column:2;}
      .notes .body{font-size:26px;line-height:1.65;overflow:auto;height:calc(100% - 74px);}
      .timer{font-size:54px;font-variant-numeric:tabular-nums;font-weight:800;}
      button{background:#f5c84b;border:0;border-radius:8px;padding:8px 12px;font-weight:700;cursor:pointer;}
    `;
    return `<!doctype html><html><head><meta charset="utf-8"><title>Presenter</title><style>${css}</style></head><body>
      <div class="grid">
        <section class="card"><div class="head"><span>Current ${current + 1}/${slides.length}</span><button onclick="opener.postMessage({type:'presenter-prev'}, '*')">Prev</button></div><div class="preview">${titleOf(slide, current)}</div></section>
        <section class="card"><div class="head"><span>Next</span><button onclick="opener.postMessage({type:'presenter-next'}, '*')">Next</button></div><div class="preview">${titleOf(next, Math.min(current + 1, slides.length - 1))}</div></section>
        <section class="card notes"><div class="head"><span>Speaker Script</span><span class="timer">${elapsed()}</span></div><div class="body">${noteHtml}</div></section>
      </div>
      <script>setInterval(()=>{ if (opener) opener.postMessage({type:'presenter-refresh'}, '*') }, 1000); document.addEventListener('keydown',e=>{ if(e.key==='ArrowRight') opener.postMessage({type:'presenter-next'}, '*'); if(e.key==='ArrowLeft') opener.postMessage({type:'presenter-prev'}, '*'); if(e.key==='Escape') close(); });</script>
    </body></html>`;
  }

  function openPresenter() {
    if (presenter && !presenter.closed) { presenter.focus(); renderPresenter(); return; }
    presenter = window.open('', 'canvas-design-presenter', 'width=1280,height=800');
    renderPresenter();
  }

  function renderPresenter() {
    if (!presenter || presenter.closed) return;
    presenter.document.open();
    presenter.document.write(presenterHtml());
    presenter.document.close();
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') activate(current + 1);
    if (e.key === 'ArrowLeft') activate(current - 1);
    if (e.key.toLowerCase() === 's') openPresenter();
  });

  window.addEventListener('message', (e) => {
    if (e.data?.type === 'presenter-next') activate(current + 1);
    if (e.data?.type === 'presenter-prev') activate(current - 1);
    if (e.data?.type === 'presenter-refresh') renderPresenter();
  });

  channel?.addEventListener('message', (e) => {
    if (e.data?.type === 'goto' && typeof e.data.idx === 'number') activate(e.data.idx, false);
  });

  activate(current, false);
})();
