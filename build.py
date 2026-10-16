"""Regenerate the static pages with: python build.py"""
from pathlib import Path
import re
import markdown

ROOT = Path(__file__).parent

def page(title, body, active=''):
    nav = ''.join(f'<a href="{key}.html" '+('aria-current="page"' if key == active else '')+f'>{label}</a>' for key,label in [('privacy','Privacy Policy'),('terms','Terms of Service')])
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · ToggyBot</title><meta name="description" content="ToggyBot privacy policy and terms of service.">
<link rel="icon" href="data:,"><link rel="stylesheet" href="assets/lenis.css"><link rel="stylesheet" href="assets/style.css?v=1">
<script defer src="assets/lenis.min.js"></script><script defer src="assets/site.js?v=1"></script></head>
<body id="top"><a class="skip" href="#content">Skip to content</a>
<header><nav aria-label="Documents">{nav}</nav></header>
<main id="content">{body}</main>
<footer><span>ToggyBot</span><a href="#top">Back to top</a></footer>
</body></html>'''

for key, title in [('privacy','Privacy Policy'),('terms','Terms of Service')]:
    source = (ROOT/f'{key}.md').read_text(encoding='utf-8-sig')
    source = re.sub(r'^---\s*\n---\s*\n', '', source)
    source = re.sub(r'^# .*\n', '', source, count=1).strip()
    source = re.sub(r'^\*\*Last updated:\*\*.*\n', '', source, count=1).strip()
    html = markdown.markdown(source, extensions=['toc'])
    body = f'<h1>{title}</h1><p class="date">Last updated October 16, 2026</p><article>{html}</article>'
    (ROOT/f'{key}.html').write_text(page(title,body,active=key),encoding='utf-8')

body = '''<h1>ToggyBot</h1><p class="date">Legal documents</p><ul class="documents"><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms of Service</a></li></ul>'''
(ROOT/'index.html').write_text(page('Legal',body),encoding='utf-8')
print('Built index.html, privacy.html, terms.html')

