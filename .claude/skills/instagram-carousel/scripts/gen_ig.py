#!/usr/bin/env python3
import base64
from pathlib import Path

BASE = Path(r"c:\Users\Admin\Desktop\⠀\'\Proyectos\Office-Control")
OUT  = BASE / "workspace/carousels/2026-03-26-claude-code-skills"
OUT.mkdir(parents=True, exist_ok=True)

# ── Assets ─────────────────────────────────────────────────────────────────────
with open(BASE / "AIGrowth/headshot.png", "rb") as f:
    HS = "data:image/png;base64," + base64.b64encode(f.read()).decode()

# ── Colors ─────────────────────────────────────────────────────────────────────
P   = "#D97757"
PL  = "#E8A080"
PD  = "#B85D3A"
LBG = "#EAE8DE"
LBO = "#D8D5CB"
DBG = "#141413"
GRD = f"linear-gradient(165deg, {PD} 0%, {P} 50%, {PL} 100%)"
N   = 7

# ── Claude logo path ────────────────────────────────────────────────────────────
CP = "M4.709 15.955l4.72-2.647.08-.23-.08-.128H9.2l-.79-.048-2.698-.073-2.339-.097-2.266-.122-.571-.121L0 11.784l.055-.352.48-.321.686.06 1.52.103 2.278.158 1.652.097 2.449.255h.389l.055-.157-.134-.098-.103-.097-2.358-1.596-2.552-1.688-1.336-.972-.724-.491-.364-.462-.158-1.008.656-.722.881.06.225.061.893.686 1.908 1.476 2.491 1.833.365.304.145-.103.019-.073-.164-.274-1.355-2.446-1.446-2.49-.644-1.032-.17-.619a2.97 2.97 0 01-.104-.729L6.283.134 6.696 0l.996.134.42.364.62 1.414 1.002 2.229 1.555 3.03.456.898.243.832.091.255h.158V9.01l.128-1.706.237-2.095.23-2.695.08-.76.376-.91.747-.492.584.28.48.685-.067.444-.286 1.851-.559 2.903-.364 1.942h.212l.243-.242.985-1.306 1.652-2.064.73-.82.85-.904.547-.431h1.033l.76 1.129-.34 1.166-1.064 1.347-.881 1.142-1.264 1.7-.79 1.36.073.11.188-.02 2.856-.606 1.543-.28 1.841-.315.833.388.091.395-.328.807-1.969.486-2.309.462-3.439.813-.042.03.049.061 1.549.146.662.036h1.622l3.02.225.79.522.474.638-.079.485-1.215.62-1.64-.389-3.829-.91-1.312-.329h-.182v.11l1.093 1.068 2.006 1.81 2.509 2.33.127.578-.322.455-.34-.049-2.205-1.657-.851-.747-1.926-1.62h-.128v.17l.444.649 2.345 3.521.122 1.08-.17.353-.608.213-.668-.122-1.374-1.925-1.415-2.167-1.143-1.943-.14.08-.674 7.254-.316.37-.729.28-.607-.461-.322-.747.322-1.476.389-1.924.315-1.53.286-1.9.17-.632-.012-.042-.14.018-1.434 1.967-2.18 2.945-1.726 1.845-.414.164-.717-.37.067-.662.401-.589 2.388-3.036 1.44-1.882.93-1.086-.006-.158h-.055L4.132 18.56l-1.13.146-.487-.456.061-.746.231-.243 1.908-1.312-.006.006z"

def svg(size=24, color="#fff"):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="{CP}" fill="{color}" fill-rule="nonzero"/></svg>'

# ── UI helpers ──────────────────────────────────────────────────────────────────
def pb(i, light):
    pct = f"{(i+1)/N*100:.1f}"
    tr  = "rgba(0,0,0,0.08)" if light else "rgba(255,255,255,0.12)"
    fi  = P if light else "#fff"
    lc  = "rgba(0,0,0,0.3)" if light else "rgba(255,255,255,0.4)"
    return (
        '<div style="position:absolute;bottom:0;left:0;right:0;padding:16px 28px 20px;'
        'z-index:10;display:flex;align-items:center;gap:10px;">'
        f'<div style="flex:1;height:3px;background:{tr};border-radius:2px;overflow:hidden;">'
        f'<div style="height:100%;width:{pct}%;background:{fi};border-radius:2px;"></div></div>'
        f'<span style="font-size:11px;color:{lc};font-weight:500;">{i+1}/{N}</span>'
        '</div>'
    )

def arrow(light):
    bg = "rgba(0,0,0,0.06)" if light else "rgba(255,255,255,0.08)"
    st = "rgba(0,0,0,0.25)" if light else "rgba(255,255,255,0.35)"
    return (
        f'<div style="position:absolute;right:0;top:0;bottom:0;width:48px;z-index:9;'
        f'display:flex;align-items:center;justify-content:center;'
        f'background:linear-gradient(to right,transparent,{bg});">'
        f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none">'
        f'<path d="M9 6l6 6-6 6" stroke="{st}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg></div>'
    )

def tag(text, mode):
    if mode == "light":   c = P
    elif mode == "dark":  c = PL
    else:                 c = "rgba(255,255,255,0.6)"
    return (
        f'<span class="sans" style="display:inline-block;font-size:10px;font-weight:600;'
        f'letter-spacing:2px;color:{c};margin-bottom:16px;">{text}</span>'
    )

# ── Slides ──────────────────────────────────────────────────────────────────────

# Slide 1 — Hero (LIGHT_BG)
s1 = (
    f'<div class="slide" style="background:{LBG};position:relative;width:420px;height:525px;'
    'flex-shrink:0;display:flex;flex-direction:column;overflow:hidden;">'

    f'<div style="padding:44px 36px 52px;display:flex;flex-direction:column;flex:1;">'
    # Logo lockup
    '<div style="display:flex;align-items:center;gap:10px;margin-bottom:auto;">'
    f'<div style="width:42px;height:42px;background:{P};border-radius:12px;'
    'display:flex;align-items:center;justify-content:center;">'
    f'{svg(26, "#fff")}</div>'
    f'<span class="sans" style="font-size:13px;font-weight:600;color:{DBG};letter-spacing:0.3px;">Claude Code</span>'
    '</div>'
    # Main copy
    '<div>'
    f'{tag("CLAUDE CODE", "light")}'
    f'<h1 class="serif" style="font-size:36px;font-weight:700;color:{DBG};'
    'line-height:1.06;letter-spacing:-0.6px;margin:0 0 16px;">'
    'Skills:<br>el superpoder<br>que nadie usa</h1>'
    f'<p class="sans" style="font-size:14px;color:{DBG};opacity:0.55;line-height:1.55;margin:0;">'
    'Transforma a Claude Code en un experto especializado para cada tarea.'
    '</p></div>'
    '</div>'
    + pb(0, True) + arrow(True) +
    '</div>'
)

# Slide 2 — Problem (DARK_BG)
s2 = (
    f'<div class="slide" style="background:{DBG};position:relative;width:420px;height:525px;'
    'flex-shrink:0;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden;">'

    '<div style="padding:0 36px 52px;">'
    f'{tag("EL PROBLEMA", "dark")}'
    '<h2 class="serif" style="font-size:30px;font-weight:700;color:#fff;'
    'line-height:1.1;letter-spacing:-0.4px;margin:0 0 20px;">'
    '&iquest;Repet&iacute;s las<br>mismas instrucciones<br>en cada sesi&oacute;n?</h2>'
    '<div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px;">'
    '<span style="font-size:11px;padding:5px 12px;border:1px solid rgba(255,255,255,0.1);'
    'border-radius:20px;color:#6B6560;text-decoration:line-through;">Copiar prompts</span>'
    '<span style="font-size:11px;padding:5px 12px;border:1px solid rgba(255,255,255,0.1);'
    'border-radius:20px;color:#6B6560;text-decoration:line-through;">Explicar contexto</span>'
    '<span style="font-size:11px;padding:5px 12px;border:1px solid rgba(255,255,255,0.1);'
    'border-radius:20px;color:#6B6560;text-decoration:line-through;">Reconfigurar todo</span>'
    '</div>'
    '<p class="sans" style="font-size:14px;color:rgba(255,255,255,0.45);line-height:1.55;margin:0;">'
    'Cada sesi&oacute;n empieza de cero. El conocimiento se pierde.'
    '</p></div>'
    + pb(1, False) + arrow(False) +
    '</div>'
)

# Slide 3 — Solution (Gradient)
s3 = (
    f'<div class="slide" style="background:{GRD};position:relative;width:420px;height:525px;'
    'flex-shrink:0;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden;">'

    '<div style="padding:0 36px 52px;">'
    f'{tag("LA SOLUCIÓN", "grad")}'
    '<h2 class="serif" style="font-size:30px;font-weight:700;color:#fff;'
    'line-height:1.1;letter-spacing:-0.4px;margin:0 0 20px;">'
    'Skills: m&oacute;dulos<br>de conocimiento<br>portables</h2>'
    '<div style="padding:16px;background:rgba(0,0,0,0.15);border-radius:12px;'
    'border:1px solid rgba(255,255,255,0.12);">'
    '<p class="sans" style="font-size:11px;color:rgba(255,255,255,0.45);'
    'margin:0 0 8px;letter-spacing:1px;font-weight:600;">DEFINICI&Oacute;N</p>'
    '<p class="sans" style="font-size:13px;color:rgba(255,255,255,0.88);'
    'line-height:1.5;margin:0;font-style:italic;">'
    '&ldquo;Un skill es un paquete que Claude activa autom&aacute;ticamente &mdash; '
    'con contexto, scripts y assets listos para usar.&rdquo;'
    '</p></div></div>'
    + pb(2, False) + arrow(False) +
    '</div>'
)

# Slide 4 — Anatomy (LIGHT_BG)
def feat(label, desc, border=True):
    bd = f"border-bottom:1px solid {LBO};" if border else ""
    return (
        f'<div style="display:flex;align-items:flex-start;gap:14px;padding:11px 0;{bd}">'
        f'<span style="color:{P};font-size:13px;width:18px;text-align:center;'
        'margin-top:2px;flex-shrink:0;">&#10086;</span>'
        f'<div><span class="sans" style="font-size:13px;font-weight:600;color:{DBG};">'
        f'{label}</span>'
        f'<span class="sans" style="font-size:12px;color:#8A8580;"> &mdash; {desc}</span>'
        '</div></div>'
    )

s4 = (
    f'<div class="slide" style="background:{LBG};position:relative;width:420px;height:525px;'
    'flex-shrink:0;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden;">'

    '<div style="padding:0 36px 52px;">'
    f'{tag("ANATOMÍA", "light")}'
    f'<h2 class="serif" style="font-size:30px;font-weight:700;color:{DBG};'
    'line-height:1.1;letter-spacing:-0.4px;margin:0 0 18px;">'
    '&iquest;Qu&eacute; tiene<br>un skill?</h2>'
    '<div>'
    + feat("SKILL.md", "El cerebro: trigger y workflow completo")
    + feat("scripts/", "Python o Bash que Claude ejecuta")
    + feat("references/", "Docs, schemas y ejemplos de contexto")
    + feat("assets/", "Im&aacute;genes, fonts y archivos est&aacute;ticos", False)
    + '</div></div>'
    + pb(3, True) + arrow(True) +
    '</div>'
)

# Slide 5 — How it works (DARK_BG)
def step_dark(num, title, sub):
    return (
        '<div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">'
        f'<div style="width:28px;height:28px;border-radius:8px;'
        'background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.08);'
        'display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
        f'<span class="sans" style="font-size:12px;color:{PL};font-weight:700;">{num}</span>'
        '</div>'
        f'<div><span class="sans" style="font-size:13px;font-weight:600;color:#fff;">{title}</span>'
        f'<span class="sans" style="font-size:12px;color:rgba(255,255,255,0.35);"> &mdash; {sub}</span>'
        '</div></div>'
    )

s5 = (
    f'<div class="slide" style="background:{DBG};position:relative;width:420px;height:525px;'
    'flex-shrink:0;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden;">'

    '<div style="padding:0 36px 52px;">'
    f'{tag("CÓMO FUNCIONA", "dark")}'
    '<h2 class="serif" style="font-size:30px;font-weight:700;color:#fff;'
    'line-height:1.1;letter-spacing:-0.4px;margin:0 0 20px;">'
    'Del trigger<br>a la acci&oacute;n</h2>'
    '<div>'
    + step_dark("1", "Escrib&iacute;s la palabra clave", "ej: &ldquo;carousel&rdquo;")
    + step_dark("2", "Claude detecta el trigger", "carga el SKILL.md autom&aacute;tico")
    + step_dark("3", "Ejecuta el workflow", "scripts, assets y contexto listos")
    + (
        '<div style="display:flex;align-items:center;gap:12px;">'
        f'<div style="width:28px;height:28px;background:{P};border-radius:8px;'
        'display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
        '<span style="font-size:14px;color:#fff;font-weight:700;">&#10003;</span></div>'
        f'<div><span class="sans" style="font-size:13px;font-weight:600;color:{PL};">'
        'Output generado</span>'
        '<span class="sans" style="font-size:12px;color:rgba(255,255,255,0.35);"> &mdash; cero configuraci&oacute;n manual</span>'
        '</div></div>'
    )
    + '</div></div>'
    + pb(4, False) + arrow(False) +
    '</div>'
)

# Slide 6 — How-to steps (LIGHT_BG)
def step_light(num, title, desc, border=True):
    bd = f"border-bottom:1px solid {LBO};" if border else ""
    return (
        f'<div style="display:flex;align-items:flex-start;gap:16px;padding:12px 0;{bd}">'
        f'<span class="serif" style="font-size:24px;font-weight:300;color:{P};'
        'min-width:32px;line-height:1;">{num}</span>'
        f'<div><span class="sans" style="font-size:13px;font-weight:600;color:{DBG};">'
        f'{title}</span>'
        f'<span class="sans" style="font-size:12px;color:#8A8580;"> &mdash; {desc}</span>'
        '</div></div>'
    )

s6 = (
    f'<div class="slide" style="background:{LBG};position:relative;width:420px;height:525px;'
    'flex-shrink:0;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden;">'

    '<div style="padding:0 36px 52px;">'
    f'{tag("PASO A PASO", "light")}'
    f'<h2 class="serif" style="font-size:30px;font-weight:700;color:{DBG};'
    'line-height:1.1;letter-spacing:-0.4px;margin:0 0 18px;">'
    'Cre&aacute; tu<br>primer skill</h2>'
    '<div>'
    + step_light("01", "Cre&aacute; SKILL.md", "Define triggers y el workflow a seguir")
    + step_light("02", "Agreg&aacute; scripts/", "Python o Bash que Claude puede ejecutar")
    + step_light("03", "Inclu&iacute; references/", "Docs y schemas de contexto adicional")
    + step_light("04", "Install&aacute;lo", "Copi&aacute; en .claude/skills/ y prob&aacute;lo", False)
    + '</div></div>'
    + pb(5, True) + arrow(True) +
    '</div>'
)

# Slide 7 — CTA (Gradient, no arrow)
s7 = (
    f'<div class="slide" style="background:{GRD};position:relative;width:420px;height:525px;'
    'flex-shrink:0;display:flex;flex-direction:column;justify-content:center;'
    'align-items:center;text-align:center;overflow:hidden;">'

    '<div style="padding:0 36px 52px;display:flex;flex-direction:column;align-items:center;">'
    '<div style="width:72px;height:72px;border-radius:50%;overflow:hidden;'
    'border:2px solid rgba(255,255,255,0.35);margin-bottom:20px;">'
    f'<img src="{HS}" style="width:100%;height:100%;object-fit:cover;" alt="thiagostefano">'
    '</div>'
    f'{tag("SEGUIME", "grad")}'
    '<h2 class="serif" style="font-size:32px;font-weight:700;color:#fff;'
    'line-height:1.1;letter-spacing:-0.5px;margin:0 0 10px;">@thiagostefano</h2>'
    '<p class="sans" style="font-size:14px;color:rgba(255,255,255,0.72);'
    'line-height:1.5;margin:0 0 28px;">'
    'Automatizaci&oacute;n, IA y<br>productividad con Claude Code</p>'
    f'<div style="display:inline-flex;align-items:center;padding:12px 28px;'
    f'background:{LBG};color:{PD};font-family:\'Space Grotesk\',sans-serif;'
    'font-weight:600;font-size:14px;border-radius:28px;">'
    'Seguir en Instagram &#8599;'
    '</div></div>'
    + pb(6, False) +
    '</div>'
)

# ── Assemble ────────────────────────────────────────────────────────────────────
slides_html = s1 + s2 + s3 + s4 + s5 + s6 + s7
dots_html   = "".join(
    ('<span class="active"></span>' if i == 0 else '<span></span>')
    for i in range(N)
)

CSS = (
    "*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}"
    "body{background:#f0ede6;min-height:100vh;display:flex;align-items:center;"
    "justify-content:center;font-family:'Space Grotesk',sans-serif;padding:32px 16px;}"
    ".serif,.sans{font-family:'Space Grotesk',sans-serif;}"
    ".ig-frame{width:420px;background:#fff;border-radius:12px;overflow:hidden;"
    "box-shadow:0 8px 40px rgba(0,0,0,0.18);}"
    ".ig-header{display:flex;align-items:center;gap:10px;padding:12px 14px;"
    "border-bottom:1px solid #efefef;}"
    ".ig-header .avatar{width:36px;height:36px;border-radius:50%;overflow:hidden;flex-shrink:0;}"
    ".ig-header .avatar img{width:100%;height:100%;object-fit:cover;}"
    ".ig-header .info .name{font-size:13px;font-weight:600;color:#141413;line-height:1.2;}"
    ".ig-header .info .sub{font-size:11px;color:#8A8580;}"
    ".ig-header .more{margin-left:auto;color:#8A8580;font-size:20px;line-height:1;}"
    ".carousel-viewport{width:420px;height:525px;overflow:hidden;position:relative;"
    "cursor:grab;user-select:none;}"
    ".carousel-viewport:active{cursor:grabbing;}"
    ".carousel-track{display:flex;width:100%;height:100%;"
    "transition:transform 0.35s cubic-bezier(.25,.46,.45,.94);will-change:transform;}"
    ".ig-dots{display:flex;justify-content:center;gap:5px;padding:10px 0 8px;}"
    ".ig-dots span{width:6px;height:6px;border-radius:50%;background:#dbdbdb;"
    "transition:background 0.2s,width 0.2s;}"
    ".ig-dots span.active{background:BRAND_P;width:16px;border-radius:3px;}"
    ".ig-actions{display:flex;align-items:center;padding:4px 14px 8px;gap:16px;}"
    ".ig-actions svg{width:24px;height:24px;}"
    ".ig-actions .bookmark{margin-left:auto;}"
    ".ig-caption{padding:0 14px 14px;}"
    ".ig-caption .cap-user{font-size:13px;font-weight:600;color:#141413;}"
    ".ig-caption .cap-text{font-size:13px;color:#141413;}"
    ".ig-caption .cap-time{font-size:11px;color:#8A8580;margin-top:4px;}"
).replace("BRAND_P", P)

JS = (
    "const track=document.getElementById('track');"
    "const dots=document.querySelectorAll('#dots span');"
    "const TOTAL=N_SLIDES,WIDTH=420;"
    "let current=0,startX=0,startT=0,dragging=false;"
    "function goTo(idx){"
    "  current=Math.max(0,Math.min(TOTAL-1,idx));"
    "  track.style.transform='translateX('+((-current)*WIDTH)+'px)';"
    "  dots.forEach((d,i)=>d.classList.toggle('active',i===current));"
    "}"
    "track.addEventListener('pointerdown',e=>{"
    "  dragging=true;startX=e.clientX;startT=-current*WIDTH;"
    "  track.style.transition='none';track.setPointerCapture(e.pointerId);"
    "});"
    "track.addEventListener('pointermove',e=>{"
    "  if(!dragging)return;"
    "  track.style.transform='translateX('+(startT+e.clientX-startX)+'px)';"
    "});"
    "track.addEventListener('pointerup',e=>{"
    "  if(!dragging)return;dragging=false;"
    "  track.style.transition='transform 0.35s cubic-bezier(.25,.46,.45,.94)';"
    "  const dx=e.clientX-startX;"
    "  if(dx<-40)goTo(current+1);"
    "  else if(dx>40)goTo(current-1);"
    "  else goTo(current);"
    "});"
).replace("N_SLIDES", str(N))

html = (
    '<!DOCTYPE html>\n<html lang="es">\n<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
    '<title>Claude Code Skills &mdash; @thiagostefano</title>\n'
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n'
    '<style>' + CSS + '</style>\n'
    '</head>\n<body>\n'
    '<div class="ig-frame">\n'
    '  <div class="ig-header">\n'
    f'    <div class="avatar"><img src="{HS}" alt="thiagostefano"></div>\n'
    '    <div class="info"><div class="name">thiagostefano</div>'
    '<div class="sub">Claude Code &middot; Skills</div></div>\n'
    '    <div class="more">&middot;&middot;&middot;</div>\n'
    '  </div>\n'
    '  <div class="carousel-viewport">\n'
    '    <div class="carousel-track" id="track">\n'
    + slides_html + '\n'
    '    </div>\n  </div>\n'
    '  <div class="ig-dots" id="dots">' + dots_html + '</div>\n'
    '  <div class="ig-actions">\n'
    '    <svg viewBox="0 0 24 24" fill="none" stroke="#141413" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>\n'
    '    <svg viewBox="0 0 24 24" fill="none" stroke="#141413" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>\n'
    '    <svg viewBox="0 0 24 24" fill="none" stroke="#141413" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/>'
    '<line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>\n'
    '    <svg class="bookmark" viewBox="0 0 24 24" fill="none" stroke="#141413" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/></svg>\n'
    '  </div>\n'
    '  <div class="ig-caption">\n'
    '    <span class="cap-user">thiagostefano </span>\n'
    '    <span class="cap-text">Claude Code Skills: m&oacute;dulos de conocimiento portables 🧩</span>\n'
    '    <div class="cap-time">hace 2 horas</div>\n'
    '  </div>\n'
    '</div>\n'
    '<script>' + JS + '</script>\n'
    '</body>\n</html>'
)

out = OUT / "carousel.html"
out.write_text(html, encoding="utf-8")
print(f"OK  {out}")
print(f"Tamano: {out.stat().st_size // 1024} KB")
