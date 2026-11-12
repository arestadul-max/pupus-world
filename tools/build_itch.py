# Builds the itch.io version of Pupu's World from the development game, without touching the development file.
#   python3 build_itch.py <game index.html> <out dir>
# itch.io version: the Prologue and Chapters 1-3 (no Chapter 4 yet) · main menu: Continue / New Game / Language (no Select Mission)
# · saves the chapter the player has reached (Chapter 2's three parts count as one chapter) · fonts built in (works offline).
import sys, os, base64
SRC, OUT = sys.argv[1], sys.argv[2]
g = open(SRC).read()
def rep(a, b, n=1):
    global g
    c = g.count(a)
    if c != n: sys.exit('build_itch: expected %d of %r, found %d' % (n, a[:70], c))
    g = g.replace(a, b)
# 1. main menu: [Continue], New Game, Language
rep("const pg = G.menuPage || 'main', n = pg === 'main' ? 3 : MISSIONS.length + 1; let pick = -1;",
    "const pg = 'main', n = itchItems().length; let pick = -1;")
rep("      if (pg === 'main') { if (pick === 0) startGame(); else if (pick === 2) setLang(LANG === 'bn' ? 'en' : 'bn'); else { G.menuPage = 'missions'; G.menuSel = 0; } }",
    "      if (pg === 'main') { const it = itchItems()[pick]; if (it === 'cont') itchContinue(); else if (it === 'new') startGame(); else if (it === 'lang') setLang(LANG === 'bn' ? 'en' : 'bn'); }")
rep("    else if (edges.ch3) { audioInit(); startMission(3); }\n    else if (edges.ch2) { audioInit(); startMission(2); }\n    else if (edges.ch1) { audioInit(); startMission(1); }\n", "")
rep("  if ((G.menuPage || 'main') === 'main') return [0, 1, 2].map(i => ({x: MENU_MAIN.x, y: MENU_MAIN.y + i * (MENU_MAIN.h + MENU_MAIN.gap), w: MENU_MAIN.w, h: MENU_MAIN.h}));",
    "  if (true) return itchItems().map((_, i) => ({x: MENU_MAIN.x, y: MENU_MAIN.y + i * (MENU_MAIN.h + MENU_MAIN.gap), w: MENU_MAIN.w, h: MENU_MAIN.h}));")
rep("  const pg = G.menuPage || 'main', sel = G.menuSel || 0, rs = menuRects(), bob = Math.sin(G.t * 3) * 2;",
    "  const pg = 'main', sel = G.menuSel || 0, rs = menuRects(), bob = Math.sin(G.t * 3) * 2;")
rep("    [['▶  Start Game', 'Begin with the Prologue'], ['Select Mission', 'Play any part of the demo'], [L2('ভাষা: বাংলা', 'Language: English'), L2('ইংরেজিতে বদলাতে চাপো', 'Press to switch to বাংলা')]].forEach(([t, sub], i) => {",
    "    itchItems().map(it => it === 'cont' ? [L2('▶  চালিয়ে যাও', '▶  Continue'), itchSaveLabel()] : it === 'new' ? [itchSave() ? L2('নতুন খেলা', 'New Game') : L2('▶  নতুন খেলা', '▶  New Game'), L2('প্রস্তাবনা থেকে শুরু', 'Begin with the Prologue')] : [L2('ভাষা: বাংলা', 'Language: English'), L2('ইংরেজিতে বদলাতে চাপো', 'Press to switch to বাংলা')]).forEach(([t, sub], i) => {")
rep("const MENU_MAIN = {x: W / 2 - 170, y: 290, w: 340, h: 54, gap: 10};", "const MENU_MAIN = {x: W / 2 - 170, y: 290, w: 340, h: 54, gap: 10};   // (itch.io build)")
# 2. no Chapter 4 yet: Chapter 3's card ends the demo and goes back to the menu
rep("  if (G.state === 'l3end') { G.endT += dt; if (G.endT > 1 && (edges.tap || edges.use || edges.jump)) startLib(); return; }",
    "  if (G.state === 'l3end') { G.endT += dt; if (G.endT > 1 && (edges.tap || edges.use || edges.jump)) { SURF = PRO_SURF; WW = PRO_WW; WH = 840; resetAll(); stopRiver(); } return; }")
rep("""  text('Next  ·  CHAPTER 4: The Library of Unfinished Stories', W / 2, 330, 18, CREAM, 700, 'center');
  text('চতুর্থ অধ্যায়: অসমাপ্ত গল্পের পাঠাগার  ·  a first look, still being built', W / 2, 356, 14, 'rgba(243,230,200,.8)', 600, 'center');
  if (G.endT > 1) { ctx.globalAlpha = 0.6 + Math.sin(G.t * 3) * 0.4; text(isTouch ? 'Tap to continue' : 'Press Enter to continue', W / 2, 432, 18, TURMERIC, 700, 'center'); }""",
"""  demoBadge(W / 2, 318, -0.04, 16);
  text('This is the end of the demo  ·  ডেমো এখানেই শেষ', W / 2, 356, 16, CREAM, 700, 'center');
  text('More chapters are coming. Thank you for playing!', W / 2, 380, 14, 'rgba(243,230,200,.8)', 600, 'center');
  if (G.endT > 1) { ctx.globalAlpha = 0.6 + Math.sin(G.t * 3) * 0.4; text(isTouch ? 'Tap to return to the menu' : 'Press Enter to return to the menu', W / 2, 432, 18, TURMERIC, 700, 'center'); }""")
rep("Demo: the Prologue, Chapters 1 to 3 and a first look at Chapter 4", "Demo version: the Prologue and Chapters 1 to 3", 2)
rep('"ডেমো: প্রস্তাবনা, ১ থেকে ৩ অধ্যায় আর চতুর্থ অধ্যায়ের এক ঝলক"', '"ডেমো সংস্করণ: প্রস্তাবনা আর ১ থেকে ৩ অধ্যায়"')
# 3. saving: the chapter he has reached (Chapter 2's parts are one chapter)
save = r"""
// ---- (itch.io build) saving: the chapter the player has reached; Continue starts that chapter again ----
const ITCH_SAVE = 'pupusworld.itch.save.v1';
const ITCH_CH = {pro: ['প্রস্তাবনা · মাঝরাতের টিভি', 'Prologue · Midnight TV'], ch1: ['অধ্যায় ১ · ঘাট', 'Chapter 1 · The Ghat'], ch2: ['অধ্যায় ২ · অঙ্ক স্যারের ক্লাস', 'Chapter 2 · Anko Sir\'s Class'], ch3: ['অধ্যায় ৩ · কালো-বিজলির ল্যাব', 'Chapter 3 · Kalo-Bijli\'s Lab']};
function itchSave() { try { const v = localStorage.getItem(ITCH_SAVE); return v && ITCH_CH[v] ? v : null; } catch (e) { return null; } }
function itchSaveSet(ch) { try { localStorage.setItem(ITCH_SAVE, ch); } catch (e) {} }
function itchItems() { return itchSave() ? ['cont', 'new', 'lang'] : ['new', 'lang']; }
function itchSaveLabel() { const c = ITCH_CH[itchSave()]; return c ? L2(c[0], c[1]) : ''; }
function itchContinue() { const c = itchSave(); setRun(false); if (c === 'ch1') startGhat(); else if (c === 'ch2') startAnko(true); else if (c === 'ch3') startLab(); else startGame(); }
{ const wrap = (f, ch) => function () { const r = f.apply(this, arguments); itchSaveSet(ch); return r; };
  startGame = wrap(startGame, 'pro'); startGhat = wrap(startGhat, 'ch1'); startAnko = wrap(startAnko, 'ch2'); startLab = wrap(startLab, 'ch3'); }
"""
rep("langUI();\nrequestAnimationFrame(frame);\ncanvas.focus();\n})();", save + "langUI();\nrequestAnimationFrame(frame);\ncanvas.focus();\n})();")
# 4. a standalone page with the fonts built in (works offline and inside itch.io's frame)
F = '/home/claude/fonts/node_modules/@fontsource/'
BN = 'U+0951-0952, U+0964-0965, U+0980-09FE, U+1CD0, U+1CD2, U+1CD5-1CD6, U+1CD8, U+1CE1, U+1CEA, U+1CED, U+1CF2, U+1CF5-1CF7, U+200C-200D, U+20B9, U+25CC, U+A8F1'
def face(fam, w, path, rng=None):
    b = base64.b64encode(open(F + path, 'rb').read()).decode()
    return "@font-face{font-family:'%s';font-style:normal;font-weight:%d;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2');%s}\n" % (fam, w, b, ('unicode-range:' + rng + ';') if rng else '')
css = face('Rozha One', 400, 'rozha-one/files/rozha-one-latin-400-normal.woff2')
for w in (400, 600, 700):
    css += face('Hind Siliguri', w, 'hind-siliguri/files/hind-siliguri-latin-%d-normal.woff2' % w)
    css += face('Hind Siliguri', w, 'hind-siliguri/files/hind-siliguri-bengali-%d-normal.woff2' % w, BN)
for o in ['<link rel="preconnect" href="https://fonts.googleapis.com">\n', '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n',
          '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;600;700&family=Rozha+One&display=swap">\n', '<meta name="claude:viewport-fit-sides" content="cover">\n']:
    rep(o, '')
head = ('<!doctype html>\n<html lang="bn"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="description" content="Pupu\'s World (পুপুর জগৎ): a hand-drawn Bengali folk-art (Rongpat) platformer about a boy, his cat and the memories of his Dadu.">\n'
        '<style>/* fonts built in, so the game works offline (Rozha One and Hind Siliguri, SIL Open Font License) */\n' + css + '</style>\n')
out = head + g.rstrip() + '\n</html>\n'
os.makedirs(OUT + '/browser', exist_ok=True); os.makedirs(OUT + '/download/PupusWorld', exist_ok=True)
open(OUT + '/browser/index.html', 'w').write(out)
open(OUT + '/download/PupusWorld/Play Pupus World.html', 'w').write(out)
print('built', len(out) // 1024, 'KB')
