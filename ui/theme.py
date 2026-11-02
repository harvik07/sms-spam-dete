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
</style>
"""
