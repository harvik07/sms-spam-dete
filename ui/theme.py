"""Page styling for the Streamlit app."""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

:root {
  --paper: #f6f1e7;
  --card: #fffdf8;
  --ink: #1f2a37;
  --muted: #6b6558;
  --line: #d9d1c0;
  --spam: #b91c1c;
  --spam-soft: #fde2d8;
  --safe: #166534;
  --safe-soft: #dcefdc;
  --accent: #c2410c;
}

html, body, [class*="st-"], .stApp { font-family: 'IBM Plex Sans', sans-serif; }
.stApp { background: var(--paper); color: var(--ink); }
.block-container { max-width: 880px; padding-top: 2.5rem; }

.masthead { border-bottom: 3px double var(--ink); padding-bottom: 1rem; margin-bottom: 1.5rem; }
.kicker {
  font-family: 'IBM Plex Mono', monospace; font-size: .75rem;
  letter-spacing: .14em; text-transform: uppercase; color: var(--accent);
}
.masthead h1 {
  font-family: 'Fraunces', serif; font-weight: 800; font-size: 3rem;
  line-height: 1.05; margin: .25rem 0 .5rem; padding: 0; color: var(--ink);
}
.masthead p { color: var(--muted); margin: 0; }

.result {
  position: relative; background: var(--card); border: 1px solid var(--line);
  border-radius: 6px; padding: 1.5rem; margin-top: 1rem; overflow: hidden;
}
.stamp {
  position: absolute; top: 1.1rem; right: 1.25rem; transform: rotate(-6deg);
  font-family: 'IBM Plex Mono', monospace; font-weight: 600; font-size: 1.15rem;
  letter-spacing: .12em; padding: .25rem .7rem; border: 3px solid currentColor; border-radius: 4px;
}
.stamp.spam { color: var(--spam); }
.stamp.safe { color: var(--safe); }

.score-label { font-family: 'IBM Plex Mono', monospace; font-size: .75rem; color: var(--muted); }
.score-value { font-family: 'Fraunces', serif; font-size: 2.6rem; font-weight: 800; line-height: 1.1; }
.track { height: 8px; background: var(--line); border-radius: 4px; margin: .75rem 0 1.25rem; }
.fill { height: 100%; border-radius: 4px; }
.fill.spam { background: var(--spam); }
.fill.safe { background: var(--safe); }

.bubble {
  background: var(--paper); border-radius: 14px 14px 14px 2px;
  padding: .85rem 1rem; line-height: 1.7; overflow-wrap: anywhere;
}
mark.up { background: var(--spam-soft); color: var(--spam); padding: .05rem .2rem; border-radius: 3px; }
mark.down { background: var(--safe-soft); color: var(--safe); padding: .05rem .2rem; border-radius: 3px; }
.legend { font-size: .8rem; color: var(--muted); margin-top: .6rem; }

.stat-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: .75rem; margin-bottom: 1.25rem; }
.stat { background: var(--card); border: 1px solid var(--line); border-radius: 6px; padding: .85rem 1rem; }
.stat b { display: block; font-family: 'Fraunces', serif; font-size: 1.6rem; }
.stat span { font-size: .8rem; color: var(--muted); }

.footer {
  margin-top: 3rem; padding-top: .75rem; border-top: 1px solid var(--line);
  font-size: .8rem; color: var(--muted);
}
.footer a { color: var(--accent); }

@media (max-width: 640px) {
  .masthead h1 { font-size: 2.2rem; }
  .stat-row { grid-template-columns: repeat(2, 1fr); }
}
</style>
"""
