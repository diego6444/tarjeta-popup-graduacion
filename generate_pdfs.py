#!/usr/bin/env python3
"""
PDF Generator for Graduation Pop-up Card
Creates print-ready PDFs with all specifications from the requirements
"""

from reportlab.lib.pagesizes import A3, A4
from reportlab.lib.units import mm, cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white
import math
import os

# Color definitions
COLORS = {
    'rosa_suave': HexColor('#FFD6E8'),
    'lila_claro': HexColor('#E6D5F5'),
    'amarillo': HexColor('#FFF4CC'),
    'verde_agua': HexColor('#D5F5E3'),
    'azul_cielo': HexColor('#D6EAF8'),
    'rosa_fuerte': HexColor('#FF69B4'),
    'lila_fuerte': HexColor('#9B59B6'),
    'dorado': HexColor('#FFD700'),
    'negro': HexColor('#333333'),
    'gris': HexColor('#999999'),
    'gris_oscuro': HexColor('#666666'),
    'rojo': HexColor('#FF0000'),
}

# Page dimensions
PAGE_WIDTH = 12 * cm
PAGE_HEIGHT = 18 * cm
FULL_WIDTH = 60 * cm
FULL_HEIGHT = 18 * cm
BLEED = 3 * mm

def draw_banderines(c, x, y, width, colors, size=1.5*cm):
    """Draw triangular banners"""
    spacing = size * 0.6
    num_flags = int(width / spacing)
    
    for i in range(num_flags):
        color_idx = i % len(colors)
        c.setFillColor(colors[color_idx])
        c.setStrokeColor(colors[color_idx])
        
        x_pos = x + i * spacing
        # Draw triangle
        p = c.beginPath()
        p.moveTo(x_pos, y)
        p.lineTo(x_pos + spacing * 0.8, y)
        p.lineTo(x_pos + spacing * 0.4, y - size)
        p.close()
        c.drawPath(p, fill=1, stroke=1)

def draw_confetti(c, x, y, width, height, density=20, opacity=0.3):
    """Draw confetti decorations"""
    import random
    random.seed(42)  # Consistent random placement
    
    colors = [COLORS['rosa_fuerte'], COLORS['lila_fuerte'], COLORS['dorado'], 
              COLORS['amarillo'], COLORS['rosa_suave']]
    
    for i in range(density):
        cx = x + random.random() * width
        cy = y + random.random() * height
        size = random.uniform(0.2*cm, 0.5*cm)
        rotation = random.uniform(0, 360)
        color = random.choice(colors)
        
        c.saveState()
        c.setFillColorRGB(color.red, color.green, color.blue, alpha=opacity)
        c.translate(cx, cy)
        c.rotate(rotation)
        
        if random.random() > 0.5:
            # Rectangle
            c.rect(-size/2, -size/2, size, size, fill=1, stroke=0)
        else:
            # Circle
            c.circle(0, 0, size/2, fill=1, stroke=0)
        
        c.restoreState()

def draw_circles_background(c, x, y, width, height, opacity=0.25):
    """Draw pastel circles background"""
    import random
    random.seed(123)
    
    colors = [COLORS['rosa_suave'], COLORS['lila_claro'], COLORS['amarillo'], 
              COLORS['verde_agua'], COLORS['azul_cielo']]
    
    for i in range(8):
        cx = x + random.random() * width
        cy = y + random.random() * height
        radius = random.uniform(1*cm, 3*cm)
        color = random.choice(colors)
        
        c.saveState()
        c.setFillColorRGB(color.red, color.green, color.blue, alpha=opacity)
        c.circle(cx, cy, radius, fill=1, stroke=0)
        c.restoreState()

def draw_birrete(c, x, y, size=1.5*cm):
    """Draw graduation cap (birrete)"""
    # Base
    c.setFillColor(black)
    c.rect(x - size*0.6, y, size*1.2, size*0.15, fill=1, stroke=0)
    
    # Top square
    c.rect(x - size*0.5, y + size*0.15, size, size, fill=1, stroke=0)
    
    # Button
    c.setFillColor(COLORS['dorado'])
    c.circle(x, y + size*0.65, size*0.1, fill=1, stroke=0)
    
    # Tassel
    c.setStrokeColor(COLORS['dorado'])
    c.setLineWidth(2)
    c.line(x, y + size*0.65, x + size*0.4, y - size*0.2)
    c.circle(x + size*0.4, y - size*0.2, size*0.15, fill=1, stroke=0)

def draw_fireworks(c, x, y):
    """Draw fireworks decoration"""
    colors = [COLORS['dorado'], COLORS['rosa_fuerte']]
    
    for angle in range(0, 360, 30):
        c.setStrokeColor(colors[angle // 180])
        c.setLineWidth(2)
        rad = math.radians(angle)
        x2 = x + math.cos(rad) * 1.5*cm
        y2 = y + math.sin(rad) * 1.5*cm
        c.line(x, y, x2, y2)
        c.circle(x2, y2, 0.1*cm, fill=1, stroke=0)

def draw_serpentinas(c, x, y, width, height):
    """Draw serpentinas (streamers)"""
    import random
    random.seed(456)
    
    colors = [COLORS['rosa_fuerte'], COLORS['lila_fuerte']]
    
    for i in range(3):
        c.saveState()
        color = colors[i % 2]
        c.setStrokeColorRGB(color.red, color.green, color.blue, alpha=0.4)
        c.setLineWidth(4)
        
        start_x = x + random.random() * width
        start_y = y + height
        
        p = c.beginPath()
        p.moveTo(start_x, start_y)
        
        for j in range(10):
            next_x = start_x + math.sin(j * 0.5) * 2*cm
            next_y = start_y - j * height / 10
            p.lineTo(next_x, next_y)
        
        c.drawPath(p, stroke=1, fill=0)
        c.restoreState()

def draw_popup_space(c, x, y, width, height, label="[PERSONAJE POP-UP]"):
    """Draw space for pop-up character with dashed border"""
    c.setStrokeColor(COLORS['gris'])
    c.setLineWidth(0.5)
    c.setDash([3, 3])
    c.rect(x, y, width, height, fill=0, stroke=1)
    c.setDash([])
    
    # Label
    c.setFillColor(COLORS['gris'])
    c.setFont("Helvetica", 8)
    text_width = c.stringWidth(label, "Helvetica", 8)
    c.drawString(x + (width - text_width) / 2, y + height / 2, label)

def draw_portada(c, x_offset, y_offset):
    """Draw the cover page (PORTADA)"""
    # Background circles
    draw_circles_background(c, x_offset, y_offset, PAGE_WIDTH, PAGE_HEIGHT, opacity=0.3)
    
    # Banderines at top
    colors = [COLORS['rosa_fuerte'], COLORS['lila_fuerte'], COLORS['amarillo'], COLORS['verde_agua']]
    draw_banderines(c, x_offset, y_offset + PAGE_HEIGHT - 1*cm, PAGE_WIDTH, colors)
    
    # Main text
    c.setFillColor(COLORS['negro'])
    c.setFont("Helvetica-Bold", 28)
    text = "Llegó el"
    text_width = c.stringWidth(text, "Helvetica-Bold", 28)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 12*cm, text)
    
    c.setFont("Helvetica-Bold", 32)
    text = "gran día!!!"
    text_width = c.stringWidth(text, "Helvetica-Bold", 32)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 10*cm, text)
    
    # Year 2025 with colors
    year_colors = [COLORS['rosa_fuerte'], COLORS['lila_fuerte'], COLORS['amarillo'], COLORS['verde_agua']]
    year = "2025"
    c.setFont("Helvetica-Bold", 48)
    
    total_width = sum([c.stringWidth(d, "Helvetica-Bold", 48) for d in year])
    x_start = x_offset + (PAGE_WIDTH - total_width) / 2
    
    for i, digit in enumerate(year):
        c.setFillColor(year_colors[i])
        c.drawString(x_start, y_offset + 6*cm, digit)
        x_start += c.stringWidth(digit, "Helvetica-Bold", 48)
    
    # Birrete in top right corner
    draw_birrete(c, x_offset + PAGE_WIDTH - 2*cm, y_offset + PAGE_HEIGHT - 3*cm)
    
    # Confetti
    draw_confetti(c, x_offset, y_offset, PAGE_WIDTH, PAGE_HEIGHT, density=15, opacity=0.5)

def draw_pagina1(c, x_offset, y_offset):
    """Draw page 1"""
    # Top text
    c.setFillColor(COLORS['negro'])
    c.setFont("Helvetica", 18)
    
    text = "Nunca dudes de que"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 15*cm, text)
    
    text = "lo puedes todo en la vida"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 13.5*cm, text)
    
    # Pop-up space in center
    popup_width = 6*cm
    popup_height = 5*cm
    popup_x = x_offset + (PAGE_WIDTH - popup_width) / 2
    popup_y = y_offset + (PAGE_HEIGHT - popup_height) / 2
    draw_popup_space(c, popup_x, popup_y, popup_width, popup_height)
    
    # Fireworks in corners
    draw_fireworks(c, x_offset + 2*cm, y_offset + 15*cm)
    draw_fireworks(c, x_offset + PAGE_WIDTH - 2*cm, y_offset + 3*cm)
    
    # Confetti
    draw_confetti(c, x_offset, y_offset, PAGE_WIDTH, PAGE_HEIGHT, density=10, opacity=0.2)
    
    # Bottom text
    c.setFont("Helvetica", 16)
    text = "siempre voy a estar para"
    text_width = c.stringWidth(text, "Helvetica", 16)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 3*cm, text)
    
    text = "ayudarte!"
    text_width = c.stringWidth(text, "Helvetica", 16)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 1.5*cm, text)

def draw_pagina2(c, x_offset, y_offset):
    """Draw page 2"""
    # Banderines at top
    colors = [COLORS['rosa_fuerte'], COLORS['lila_fuerte'], COLORS['amarillo'], COLORS['verde_agua']]
    draw_banderines(c, x_offset, y_offset + PAGE_HEIGHT - 1*cm, PAGE_WIDTH, colors, size=1.2*cm)
    
    # Top text
    c.setFillColor(COLORS['lila_fuerte'])
    c.setFont("Helvetica-Bold", 24)
    text = "Quiero que sepas"
    text_width = c.stringWidth(text, "Helvetica-Bold", 24)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 14*cm, text)
    
    # Pop-up space
    popup_width = 6*cm
    popup_height = 5*cm
    popup_x = x_offset + (PAGE_WIDTH - popup_width) / 2
    popup_y = y_offset + (PAGE_HEIGHT - popup_height) / 2
    draw_popup_space(c, popup_x, popup_y, popup_width, popup_height)
    
    # Serpentinas
    draw_serpentinas(c, x_offset, y_offset, PAGE_WIDTH, PAGE_HEIGHT)
    
    # Bottom text
    c.setFillColor(COLORS['negro'])
    c.setFont("Helvetica", 18)
    text = "y que estamos muy"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 3*cm, text)
    
    text = "orgullosos de vos"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 1.5*cm, text)

def draw_pagina3(c, x_offset, y_offset):
    """Draw page 3"""
    # Background circles
    draw_circles_background(c, x_offset, y_offset, PAGE_WIDTH, PAGE_HEIGHT, opacity=0.25)
    
    # Small birretes in corners
    c.saveState()
    c.setFillColorRGB(0, 0, 0, alpha=0.5)
    draw_birrete(c, x_offset + 2*cm, y_offset + PAGE_HEIGHT - 2*cm, size=1*cm)
    draw_birrete(c, x_offset + PAGE_WIDTH - 2*cm, y_offset + PAGE_HEIGHT - 2*cm, size=1*cm)
    c.restoreState()
    
    # Top text
    c.setFillColor(COLORS['negro'])
    c.setFont("Helvetica", 18)
    
    text = "Hoy se termina"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 15*cm, text)
    
    text = "una etapa muy"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 13.5*cm, text)
    
    text = "importante en tu vida"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 12*cm, text)
    
    # Pop-up space
    popup_width = 6*cm
    popup_height = 5*cm
    popup_x = x_offset + (PAGE_WIDTH - popup_width) / 2
    popup_y = y_offset + (PAGE_HEIGHT - popup_height) / 2
    draw_popup_space(c, popup_x, popup_y, popup_width, popup_height)
    
    # Bottom text
    text = "y comienza otra"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 3*cm, text)
    
    text = "mucho mejor"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 1.5*cm, text)

def draw_pagina4(c, x_offset, y_offset):
    """Draw page 4 (final page)"""
    # Background circles
    draw_circles_background(c, x_offset, y_offset, PAGE_WIDTH, PAGE_HEIGHT, opacity=0.2)
    
    # Confetti
    draw_confetti(c, x_offset, y_offset, PAGE_WIDTH, PAGE_HEIGHT, density=15, opacity=0.5)
    
    # Top text
    c.setFillColor(COLORS['negro'])
    c.setFont("Helvetica", 18)
    
    text = "Tu esfuerzo y"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 15*cm, text)
    
    text = "dedicación dieron"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 13.5*cm, text)
    
    text = "fruto"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 12*cm, text)
    
    # Pop-up space
    popup_width = 6*cm
    popup_height = 5*cm
    popup_x = x_offset + (PAGE_WIDTH - popup_width) / 2
    popup_y = y_offset + (PAGE_HEIGHT - popup_height) / 2
    draw_popup_space(c, popup_x, popup_y, popup_width, popup_height)
    
    # Bottom text
    c.setFont("Helvetica", 18)
    text = "lo lograste"
    text_width = c.stringWidth(text, "Helvetica", 18)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 4*cm, text)
    
    # Name in pink
    c.setFillColor(COLORS['rosa_fuerte'])
    c.setFont("Helvetica-Bold", 24)
    text = "Augusto!!!"
    text_width = c.stringWidth(text, "Helvetica-Bold", 24)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 2.5*cm, text)
    
    # Final message
    c.setFillColor(COLORS['negro'])
    c.setFont("Helvetica", 16)
    text = "Te Amo hijo."
    text_width = c.stringWidth(text, "Helvetica", 16)
    c.drawString(x_offset + (PAGE_WIDTH - text_width) / 2, y_offset + 1*cm, text)

def draw_fold_guides(c, x_offset, y_offset):
    """Draw fold and cut guides"""
    # Cut guides (dashed, exterior)
    c.setStrokeColor(COLORS['gris'])
    c.setLineWidth(0.5)
    c.setDash([3, 3])
    c.rect(x_offset, y_offset, PAGE_WIDTH, PAGE_HEIGHT, fill=0, stroke=1)
    c.setDash([])

def draw_fold_line(c, x, y1, y2, label_top="", label_bottom=""):
    """Draw fold line between pages"""
    c.setStrokeColor(COLORS['gris_oscuro'])
    c.setLineWidth(0.3)
    c.line(x, y1, x, y2)
    
    # Labels
    if label_top:
        c.saveState()
        c.setFillColor(COLORS['gris'])
        c.setFont("Helvetica", 6)
        c.translate(x, y2 - 1*cm)
        c.rotate(90)
        c.drawString(0, 0, label_top)
        c.restoreState()
    
    if label_bottom:
        c.saveState()
        c.setFillColor(COLORS['gris'])
        c.setFont("Helvetica", 6)
        c.translate(x, y1 + 1*cm)
        c.rotate(90)
        c.drawString(0, 0, label_bottom)
        c.restoreState()

def create_a3_pdf():
    """Create the complete A3 PDF with all 5 pages"""
    filename = "imprimibles/tarjeta-completa-A3.pdf"
    
    # A3 landscape
    c = canvas.Canvas(filename, pagesize=(A3[1], A3[0]))
    c.setTitle("Tarjeta Pop-up Graduación - A3")
    
    # Calculate positioning to center the 60x18cm card on A3
    a3_width = A3[1]
    a3_height = A3[0]
    
    # Center the full card
    start_x = (a3_width - FULL_WIDTH) / 2
    start_y = (a3_height - FULL_HEIGHT) / 2
    
    # Draw each page
    pages = [draw_portada, draw_pagina1, draw_pagina2, draw_pagina3, draw_pagina4]
    
    for i, draw_func in enumerate(pages):
        x_offset = start_x + i * PAGE_WIDTH
        draw_func(c, x_offset, start_y)
        draw_fold_guides(c, x_offset, start_y)
        
        # Draw fold lines between pages
        if i < len(pages) - 1:
            fold_x = start_x + (i + 1) * PAGE_WIDTH
            label = "DOBLEZ " + ("MONTAÑA" if i % 2 == 0 else "VALLE")
            draw_fold_line(c, fold_x, start_y, start_y + PAGE_HEIGHT, label_top=label)
    
    c.save()
    print(f"Created {filename}")

def create_a4_part1_pdf():
    """Create first part for A4 printing (Portada + Página 1 + half of Página 2)"""
    filename = "imprimibles/tarjeta-completa-A4-parte1.pdf"
    
    # Use landscape A4
    c = canvas.Canvas(filename, pagesize=(A4[1], A4[0]))
    c.setTitle("Tarjeta Pop-up Graduación - A4 Parte 1")
    
    total_width = 2.5 * PAGE_WIDTH
    a4_width = A4[1]
    a4_height = A4[0]
    
    scale = min(a4_width / total_width, a4_height / PAGE_HEIGHT) * 0.95
    
    start_x = (a4_width - total_width * scale) / 2
    start_y = (a4_height - PAGE_HEIGHT * scale) / 2
    
    c.saveState()
    c.scale(scale, scale)
    
    # Draw portada
    draw_portada(c, start_x / scale, start_y / scale)
    draw_fold_guides(c, start_x / scale, start_y / scale)
    
    # Draw página 1
    x_offset = start_x / scale + PAGE_WIDTH
    draw_pagina1(c, x_offset, start_y / scale)
    draw_fold_guides(c, x_offset, start_y / scale)
    draw_fold_line(c, x_offset, start_y / scale, start_y / scale + PAGE_HEIGHT, label_top="DOBLEZ MONTAÑA")
    
    # Draw half of página 2
    x_offset = start_x / scale + 2 * PAGE_WIDTH
    c.saveState()
    c.rect(x_offset, start_y / scale, PAGE_WIDTH / 2, PAGE_HEIGHT, fill=0, stroke=0)
    draw_pagina2(c, x_offset, start_y / scale)
    c.restoreState()
    
    # Clip to show only half
    p = c.beginPath()
    p.rect(x_offset, start_y / scale, PAGE_WIDTH / 2, PAGE_HEIGHT)
    c.clipPath(p, stroke=0)
    
    draw_fold_line(c, x_offset, start_y / scale, start_y / scale + PAGE_HEIGHT, label_top="DOBLEZ VALLE")
    
    # Add junction mark
    c.setStrokeColor(COLORS['rojo'])
    c.setLineWidth(1)
    junction_x = x_offset + PAGE_WIDTH / 2
    c.line(junction_x, start_y / scale, junction_x, start_y / scale + PAGE_HEIGHT)
    
    c.restoreState()
    
    # Add instruction
    c.setFillColor(COLORS['negro'])
    c.setFont("Helvetica-Bold", 10)
    c.drawString(a4_width - 5*cm, a4_height - 1*cm, "Unir con Parte 2 →")
    
    c.save()
    print(f"Created {filename}")

def create_a4_part2_pdf():
    """Create second part for A4 printing (half of Página 2 + Página 3 + Página 4)"""
    filename = "imprimibles/tarjeta-completa-A4-parte2.pdf"
    
    c = canvas.Canvas(filename, pagesize=(A4[1], A4[0]))
    c.setTitle("Tarjeta Pop-up Graduación - A4 Parte 2")
    
    total_width = 2.5 * PAGE_WIDTH
    a4_width = A4[1]
    a4_height = A4[0]
    
    scale = min(a4_width / total_width, a4_height / PAGE_HEIGHT) * 0.95
    
    start_x = (a4_width - total_width * scale) / 2
    start_y = (a4_height - PAGE_HEIGHT * scale) / 2
    
    c.saveState()
    c.scale(scale, scale)
    
    # Draw half of página 2
    x_offset = start_x / scale
    c.saveState()
    p = c.beginPath()
    p.rect(x_offset, start_y / scale, PAGE_WIDTH / 2, PAGE_HEIGHT)
    c.clipPath(p, stroke=0)
    draw_pagina2(c, x_offset - PAGE_WIDTH / 2, start_y / scale)
    c.restoreState()
    
    # Junction mark
    c.setStrokeColor(COLORS['rojo'])
    c.setLineWidth(1)
    c.line(x_offset, start_y / scale, x_offset, start_y / scale + PAGE_HEIGHT)
    
    # Draw página 3
    x_offset = start_x / scale + PAGE_WIDTH / 2
    draw_pagina3(c, x_offset, start_y / scale)
    draw_fold_guides(c, x_offset, start_y / scale)
    draw_fold_line(c, x_offset, start_y / scale, start_y / scale + PAGE_HEIGHT, label_top="DOBLEZ VALLE")
    
    # Draw página 4
    x_offset = start_x / scale + 1.5 * PAGE_WIDTH
    draw_pagina4(c, x_offset, start_y / scale)
    draw_fold_guides(c, x_offset, start_y / scale)
    draw_fold_line(c, x_offset, start_y / scale, start_y / scale + PAGE_HEIGHT, label_top="DOBLEZ MONTAÑA")
    
    c.restoreState()
    
    # Add instruction
    c.setFillColor(COLORS['negro'])
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*cm, a4_height - 1*cm, "← Unir con Parte 1")
    
    c.save()
    print(f"Created {filename}")

def draw_stick_figure(c, x, y, width, height):
    """Draw basic stick figure body (without specific features)"""
    center_x = x + width / 2
    head_y = y + height - 1.5*cm
    
    # Head
    c.setStrokeColor(black)
    c.setLineWidth(3)
    c.circle(center_x, head_y, 0.8*cm, fill=0, stroke=1)
    
    # Body
    c.line(center_x, head_y - 0.8*cm, center_x, y + 3*cm)
    
    # Legs (in V)
    c.line(center_x, y + 3*cm, center_x - 0.8*cm, y + 0.5*cm)
    c.line(center_x, y + 3*cm, center_x + 0.8*cm, y + 0.5*cm)

def draw_personaje1(c, x, y, width, height):
    """Draw character 1 - with heart"""
    center_x = x + width / 2
    head_y = y + height - 1.5*cm
    
    # Floating heart above
    heart_y = head_y + 1.5*cm
    c.setFillColor(COLORS['rosa_fuerte'])
    c.setStrokeColor(COLORS['rosa_fuerte'])
    c.setLineWidth(2)
    
    # Simple heart shape
    p = c.beginPath()
    p.moveTo(center_x, heart_y - 0.4*cm)
    p.curveTo(center_x - 0.6*cm, heart_y + 0.4*cm, center_x - 0.6*cm, heart_y, center_x, heart_y - 0.2*cm)
    p.curveTo(center_x + 0.6*cm, heart_y, center_x + 0.6*cm, heart_y + 0.4*cm, center_x, heart_y - 0.4*cm)
    c.drawPath(p, fill=1, stroke=1)
    
    # Face - smile
    c.setStrokeColor(black)
    c.setLineWidth(3)
    c.circle(center_x, head_y, 0.8*cm, fill=0, stroke=1)
    
    # Eyes (dots)
    c.setFillColor(black)
    c.circle(center_x - 0.3*cm, head_y + 0.2*cm, 0.08*cm, fill=1, stroke=0)
    c.circle(center_x + 0.3*cm, head_y + 0.2*cm, 0.08*cm, fill=1, stroke=0)
    
    # Smile
    c.setStrokeColor(black)
    c.setLineWidth(2)
    p = c.beginPath()
    p.arc(center_x - 0.3*cm, head_y - 0.5*cm, center_x + 0.3*cm, head_y - 0.1*cm, 0, 180)
    c.drawPath(p, stroke=1, fill=0)
    
    # Body
    c.setLineWidth(3)
    c.line(center_x, head_y - 0.8*cm, center_x, y + 3*cm)
    
    # Arms extended horizontally
    c.line(center_x - 1.5*cm, head_y - 0.3*cm, center_x + 1.5*cm, head_y - 0.3*cm)
    
    # Legs
    c.line(center_x, y + 3*cm, center_x - 0.8*cm, y + 0.5*cm)
    c.line(center_x, y + 3*cm, center_x + 0.8*cm, y + 0.5*cm)

def draw_personaje2(c, x, y, width, height):
    """Draw character 2 - SOS INCREÍBLE with sign"""
    center_x = x + width / 2
    head_y = y + height - 1.5*cm
    
    # Face
    c.setStrokeColor(black)
    c.setLineWidth(3)
    c.circle(center_x, head_y, 0.8*cm, fill=0, stroke=1)
    
    # Eyes
    c.setFillColor(black)
    c.circle(center_x - 0.3*cm, head_y + 0.2*cm, 0.08*cm, fill=1, stroke=0)
    c.circle(center_x + 0.3*cm, head_y + 0.2*cm, 0.08*cm, fill=1, stroke=0)
    
    # Smile
    c.setStrokeColor(black)
    c.setLineWidth(2)
    p = c.beginPath()
    p.arc(center_x - 0.3*cm, head_y - 0.5*cm, center_x + 0.3*cm, head_y - 0.1*cm, 0, 180)
    c.drawPath(p, stroke=1, fill=0)
    
    # Body
    c.setLineWidth(3)
    c.line(center_x, head_y - 0.8*cm, center_x, y + 3*cm)
    
    # Sign
    sign_width = 3*cm
    sign_height = 1.5*cm
    sign_x = center_x - sign_width / 2
    sign_y = head_y - 2*cm
    
    c.setFillColor(white)
    c.setStrokeColor(black)
    c.setLineWidth(2)
    c.rect(sign_x, sign_y, sign_width, sign_height, fill=1, stroke=1)
    
    # Text on sign
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 14)
    text = "SOS"
    text_width = c.stringWidth(text, "Helvetica-Bold", 14)
    c.drawString(sign_x + (sign_width - text_width) / 2, sign_y + sign_height - 0.6*cm, text)
    
    c.setFont("Helvetica-Bold", 10)
    text = "INCREÍBLE"
    text_width = c.stringWidth(text, "Helvetica-Bold", 10)
    c.drawString(sign_x + (sign_width - text_width) / 2, sign_y + 0.3*cm, text)
    
    # Arms holding sign
    c.setStrokeColor(black)
    c.setLineWidth(3)
    c.line(center_x, head_y - 1*cm, sign_x, sign_y + sign_height / 2)
    c.line(center_x, head_y - 1*cm, sign_x + sign_width, sign_y + sign_height / 2)
    
    # Legs
    c.line(center_x, y + 3*cm, center_x - 0.8*cm, y + 0.5*cm)
    c.line(center_x, y + 3*cm, center_x + 0.8*cm, y + 0.5*cm)
    
    # Confetti around
    import random
    random.seed(789)
    colors = [COLORS['rosa_fuerte'], COLORS['lila_fuerte'], COLORS['dorado'], COLORS['amarillo']]
    for i in range(10):
        cx = x + random.random() * width
        cy = y + height / 2 + random.random() * height / 2
        size = 0.15*cm
        color = random.choice(colors)
        c.setFillColor(color)
        if random.random() > 0.5:
            c.circle(cx, cy, size, fill=1, stroke=0)
        else:
            c.rect(cx, cy, size, size, fill=1, stroke=0)

def draw_personaje3(c, x, y, width, height):
    """Draw character 3 - Celebrating with arms up"""
    center_x = x + width / 2
    head_y = y + height - 1.5*cm
    
    # Face
    c.setStrokeColor(black)
    c.setLineWidth(3)
    c.circle(center_x, head_y, 0.8*cm, fill=0, stroke=1)
    
    # Closed eyes (curved lines)
    c.setStrokeColor(black)
    c.setLineWidth(2)
    p = c.beginPath()
    p.arc(center_x - 0.5*cm, head_y + 0.1*cm, center_x - 0.1*cm, head_y + 0.3*cm, 180, 360)
    c.drawPath(p, stroke=1, fill=0)
    
    p = c.beginPath()
    p.arc(center_x + 0.1*cm, head_y + 0.1*cm, center_x + 0.5*cm, head_y + 0.3*cm, 180, 360)
    c.drawPath(p, stroke=1, fill=0)
    
    # Open mouth (circle)
    c.setFillColor(black)
    c.circle(center_x, head_y - 0.2*cm, 0.2*cm, fill=1, stroke=0)
    
    # Body
    c.setStrokeColor(black)
    c.setLineWidth(3)
    c.line(center_x, head_y - 0.8*cm, center_x, y + 3*cm)
    
    # Arms raised in V
    c.line(center_x, head_y - 0.3*cm, center_x - 1.2*cm, head_y + 1*cm)
    c.line(center_x, head_y - 0.3*cm, center_x + 1.2*cm, head_y + 1*cm)
    
    # Legs
    c.line(center_x, y + 3*cm, center_x - 0.8*cm, y + 0.5*cm)
    c.line(center_x, y + 3*cm, center_x + 0.8*cm, y + 0.5*cm)
    
    # Emotion lines
    c.setStrokeColor(COLORS['rosa_fuerte'])
    c.setLineWidth(2)
    c.line(center_x - 1.2*cm, head_y + 0.3*cm, center_x - 1.5*cm, head_y + 0.5*cm)
    c.line(center_x - 1.2*cm, head_y, center_x - 1.6*cm, head_y)
    
    c.setStrokeColor(COLORS['lila_fuerte'])
    c.line(center_x + 1.2*cm, head_y + 0.3*cm, center_x + 1.5*cm, head_y + 0.5*cm)
    c.line(center_x + 1.2*cm, head_y, center_x + 1.6*cm, head_y)

def draw_personaje4(c, x, y, width, height):
    """Draw character 4 - With graduation cap"""
    center_x = x + width / 2
    head_y = y + height - 1.5*cm
    
    # Graduation cap on head
    cap_y = head_y + 0.8*cm
    
    # Base
    c.setFillColor(black)
    c.rect(center_x - 1.25*cm, cap_y, 2.5*cm, 0.3*cm, fill=1, stroke=0)
    
    # Top square board
    c.rect(center_x - 1.5*cm, cap_y + 0.3*cm, 3*cm, 3*cm, fill=1, stroke=0)
    
    # Button
    c.setFillColor(COLORS['dorado'])
    c.circle(center_x, cap_y + 1.8*cm, 0.2*cm, fill=1, stroke=0)
    
    # Tassel
    c.setStrokeColor(COLORS['dorado'])
    c.setLineWidth(3)
    c.line(center_x, cap_y + 1.8*cm, center_x + 1*cm, cap_y - 0.5*cm)
    c.setFillColor(COLORS['dorado'])
    c.circle(center_x + 1*cm, cap_y - 0.5*cm, 0.3*cm, fill=1, stroke=0)
    
    # Face
    c.setStrokeColor(black)
    c.setLineWidth(3)
    c.circle(center_x, head_y, 0.8*cm, fill=0, stroke=1)
    
    # Eyes
    c.setFillColor(black)
    c.circle(center_x - 0.3*cm, head_y + 0.2*cm, 0.08*cm, fill=1, stroke=0)
    c.circle(center_x + 0.3*cm, head_y + 0.2*cm, 0.08*cm, fill=1, stroke=0)
    
    # Proud smile
    c.setStrokeColor(black)
    c.setLineWidth(2)
    p = c.beginPath()
    p.arc(center_x - 0.4*cm, head_y - 0.6*cm, center_x + 0.4*cm, head_y - 0.1*cm, 0, 180)
    c.drawPath(p, stroke=1, fill=0)
    
    # Body
    c.setLineWidth(3)
    c.line(center_x, head_y - 0.8*cm, center_x, y + 3*cm)
    
    # Arms slightly raised
    c.line(center_x, head_y - 0.3*cm, center_x - 1.2*cm, head_y + 0.3*cm)
    c.line(center_x, head_y - 0.3*cm, center_x + 1.2*cm, head_y + 0.3*cm)
    
    # Legs
    c.line(center_x, y + 3*cm, center_x - 0.8*cm, y + 0.5*cm)
    c.line(center_x, y + 3*cm, center_x + 0.8*cm, y + 0.5*cm)
    
    # Falling confetti
    import random
    random.seed(101)
    colors = [COLORS['rosa_fuerte'], COLORS['lila_fuerte'], COLORS['dorado'], COLORS['amarillo']]
    for i in range(12):
        cx = x + random.random() * width
        cy = y + height / 2 + random.random() * height / 2
        size = 0.15*cm
        color = random.choice(colors)
        c.saveState()
        c.setFillColorRGB(color.red, color.green, color.blue, alpha=0.6)
        if random.random() > 0.5:
            c.circle(cx, cy, size, fill=1, stroke=0)
        else:
            c.rect(cx, cy, size, size, fill=1, stroke=0)
        c.restoreState()

def draw_tab(c, x, y, width, height, label):
    """Draw tab for pop-up with fold line"""
    # Tab rectangle
    c.setStrokeColor(black)
    c.setLineWidth(1)
    c.rect(x, y, width, height, fill=0, stroke=1)
    
    # Fold line (red dashed)
    c.setStrokeColor(COLORS['rojo'])
    c.setLineWidth(0.5)
    c.setDash([2, 2])
    c.line(x, y, x + width, y)
    c.setDash([])
    
    # Label
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 7)
    text_width = c.stringWidth(label, "Helvetica-Bold", 7)
    c.drawString(x + (width - text_width) / 2, y + height / 2 - 0.1*cm, label)

def create_personajes_pdf():
    """Create PDF with 4 pop-up characters"""
    filename = "imprimibles/personajes-popup.pdf"
    
    c = canvas.Canvas(filename, pagesize=A4)
    c.setTitle("Personajes Pop-up para Tarjeta de Graduación")
    
    # Character dimensions
    char_width = 5*cm
    char_height = 7*cm
    tab_width = 3*cm
    tab_height = 2*cm
    total_height = tab_height + char_height + tab_height  # 11cm total
    
    # Layout: 2x2 grid
    margin_x = 3*cm
    margin_y = 3*cm
    spacing_x = 3*cm
    spacing_y = 2*cm
    
    positions = [
        (margin_x, A4[1] - margin_y - total_height),  # Top left
        (margin_x + char_width + spacing_x, A4[1] - margin_y - total_height),  # Top right
        (margin_x, A4[1] - margin_y - total_height * 2 - spacing_y),  # Bottom left
        (margin_x + char_width + spacing_x, A4[1] - margin_y - total_height * 2 - spacing_y),  # Bottom right
    ]
    
    draw_funcs = [draw_personaje1, draw_personaje2, draw_personaje3, draw_personaje4]
    
    for i, (px, py) in enumerate(positions):
        # Top tab
        tab_x = px + (char_width - tab_width) / 2
        draw_tab(c, tab_x, py + char_height + tab_height, tab_width, tab_height, "PEGAR ARRIBA")
        
        # Character body
        c.setStrokeColor(black)
        c.setLineWidth(1)
        c.rect(px, py + tab_height, char_width, char_height, fill=0, stroke=1)
        
        # Draw character
        draw_funcs[i](c, px, py + tab_height, char_width, char_height)
        
        # Bottom tab
        draw_tab(c, tab_x, py, tab_width, tab_height, "PEGAR ABAJO")
    
    c.save()
    print(f"Created {filename}")

def create_readme():
    """Create README with printing instructions"""
    filename = "imprimibles/README-IMPRIMIR.md"
    
    content = """# Archivos Listos para Imprimir

## Opción 1: Impresora A3
1. Descarga `tarjeta-completa-A3.pdf`
2. Descarga `personajes-popup.pdf`
3. Imprime en cartulina:
   - Tarjeta: 240gr
   - Personajes: 180gr
4. Configuración: Máxima calidad, sin escalar

## Opción 2: Impresora A4
1. Descarga `tarjeta-completa-A4-parte1.pdf`
2. Descarga `tarjeta-completa-A4-parte2.pdf`
3. Descarga `personajes-popup.pdf`
4. Imprime las 3 hojas en cartulina
5. Une las partes 1 y 2 con cinta por detrás

## Armado
1. Corta siguiendo líneas punteadas
2. Dobla en líneas de doblez (alternando montaña/valle)
3. Pega personajes con lengüetas a 90°

Ver INSTRUCCIONES.md para detalles completos.
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created {filename}")

def main():
    """Generate all PDFs"""
    print("Generating graduation pop-up card PDFs...")
    print("-" * 50)
    
    # Create directory if it doesn't exist
    os.makedirs("imprimibles", exist_ok=True)
    
    # Generate all PDFs
    create_a3_pdf()
    create_a4_part1_pdf()
    create_a4_part2_pdf()
    create_personajes_pdf()
    create_readme()
    
    print("-" * 50)
    print("All PDFs generated successfully!")
    print("\nGenerated files:")
    print("  - imprimibles/tarjeta-completa-A3.pdf")
    print("  - imprimibles/tarjeta-completa-A4-parte1.pdf")
    print("  - imprimibles/tarjeta-completa-A4-parte2.pdf")
    print("  - imprimibles/personajes-popup.pdf")
    print("  - imprimibles/README-IMPRIMIR.md")

if __name__ == "__main__":
    main()
