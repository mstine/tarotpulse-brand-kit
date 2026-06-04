#!/usr/bin/env python3
"""Render the kit's markdown docs into on-brand, mobile-friendly HTML pages
so they open and read in the browser (no raw .md downloads). Re-runnable."""
import markdown, pathlib
KIT = pathlib.Path(__file__).resolve().parent

DOCS = [
    ("downloads/site-migration-guide.md", "migration-guide.html", "Site Migration Guide", "Making mytarotpulse.com uniform — in GoHighLevel"),
    ("downloads/brand-unification-spec.md", "brand-spec.html", "Brand Spec", "The Pattern-Hunter's Journal — unified system"),
]

TPL = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>{title} · TarotPulse</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Space+Mono:wght@400;700&display=swap');
:root{{--navy:#16204a;--obsidian:#0f1330;--gold:#c8a44d;--gold-deep:#b98f3c;--gold-soft:#e2cf98;--lav:#b9a3e3;--ink:#ece7d8;--mut:#9a93b4;}}
*{{box-sizing:border-box;}}
body{{margin:0;background:var(--navy);color:var(--ink);font-family:'Cormorant Garamond',Georgia,serif;line-height:1.6;}}
.bar{{position:sticky;top:0;background:rgba(15,19,48,.92);backdrop-filter:blur(6px);border-bottom:1px solid rgba(200,164,77,.3);padding:13px 20px;font-family:'Space Mono',monospace;font-size:13px;letter-spacing:1px;z-index:10;}}
.bar a{{color:var(--gold-soft);text-decoration:none;}}
.bar a:hover{{color:#fff;}}
.doc{{max-width:760px;margin:0 auto;padding:30px 22px 70px;}}
h1{{font-family:'Cinzel',serif;font-weight:700;color:var(--gold-soft);font-size:clamp(28px,6vw,40px);line-height:1.12;letter-spacing:.5px;margin:.4em 0 .1em;}}
h2{{font-family:'Cinzel',serif;font-weight:600;color:var(--gold);font-size:clamp(21px,4.5vw,27px);margin:1.3em 0 .3em;padding-top:.4em;border-top:1px solid rgba(200,164,77,.2);}}
h3{{font-family:'Cinzel',serif;font-weight:600;color:var(--gold-soft);font-size:19px;margin:1.1em 0 .2em;}}
p,li{{font-size:18px;color:#ddd8ea;}}
a{{color:var(--gold-soft);}}
strong,b{{color:var(--gold-soft);font-weight:600;}}
em{{color:#cfc8e6;}}
code{{font-family:'Space Mono',monospace;font-size:.85em;background:rgba(200,164,77,.12);color:var(--gold-soft);padding:1px 6px;border-radius:4px;}}
pre{{background:#0b0f26;border:1px solid rgba(200,164,77,.25);border-radius:8px;padding:16px;overflow-x:auto;-webkit-overflow-scrolling:touch;}}
pre code{{background:none;color:#d9e0ff;padding:0;font-size:13px;line-height:1.55;}}
hr{{border:none;border-top:1px solid rgba(200,164,77,.25);margin:1.6em 0;}}
blockquote{{border-left:3px solid var(--lav);background:rgba(185,163,227,.08);margin:1em 0;padding:.5em 16px;border-radius:0 6px 6px 0;font-style:italic;}}
.tablewrap{{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:1em 0;border:1px solid rgba(200,164,77,.22);border-radius:8px;}}
table{{border-collapse:collapse;width:100%;min-width:480px;font-size:16px;}}
th,td{{text-align:left;padding:10px 14px;border-bottom:1px solid rgba(200,164,77,.18);}}
th{{font-family:'Space Mono',monospace;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:var(--gold);background:rgba(13,19,48,.6);}}
ul,ol{{padding-left:22px;}}
li{{margin:.4em 0;}}
li input[type=checkbox]{{accent-color:var(--gold);margin-right:6px;}}
.foot{{text-align:center;color:var(--mut);font-family:'Space Mono',monospace;font-size:12px;letter-spacing:1px;margin-top:50px;}}
</style></head>
<body>
<div class="bar"><a href="index.html">← TarotPulse Brand Kit</a></div>
<div class="doc">
{body}
<div class="foot">✦ TAROTPULSE · part of the brand kit</div>
</div>
</body></html>"""

def main():
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    for src, out, title, _sub in DOCS:
        text = (KIT / src).read_text()
        md.reset()
        body = md.convert(text)
        # wrap tables for horizontal scroll on phones
        body = body.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
        (KIT / out).write_text(TPL.format(title=title, body=body))
        print("wrote", out)

main()
