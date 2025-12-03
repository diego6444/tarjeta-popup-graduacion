# 🎓 Tarjeta Pop-up de Graduación

Una hermosa tarjeta pop-up personalizada para celebrar la graduación de Augusto. Esta tarjeta incluye 5 páginas conectadas en formato acordeón con 4 personajes 3D que se despliegan al abrir cada página.

## ⬇️ DESCARGAR PDFs LISTOS PARA IMPRIMIR

**Los archivos PDF están en la carpeta [`imprimibles/`](./imprimibles/)**

### 📥 Descarga Directa:

**Opción A3 (recomendada):**
- 📄 [tarjeta-completa-A3.pdf](./imprimibles/tarjeta-completa-A3.pdf) - Tarjeta completa
- 📄 [personajes-popup.pdf](./imprimibles/personajes-popup.pdf) - 4 personajes pop-up

**Opción A4:**
- 📄 [tarjeta-completa-A4-parte1.pdf](./imprimibles/tarjeta-completa-A4-parte1.pdf) - Parte 1 de 2
- 📄 [tarjeta-completa-A4-parte2.pdf](./imprimibles/tarjeta-completa-A4-parte2.pdf) - Parte 2 de 2
- 📄 [personajes-popup.pdf](./imprimibles/personajes-popup.pdf) - 4 personajes pop-up

**Instrucciones:**
- 📖 [README-IMPRIMIR.md](./imprimibles/README-IMPRIMIR.md) - Guía rápida
- 📖 [INSTRUCCIONES.md](./imprimibles/INSTRUCCIONES.md) - Guía completa paso a paso

---

## 📦 Contenido del Repositorio

Este repositorio contiene archivos PDF listos para imprimir y armar una tarjeta de graduación profesional.

### Archivos Imprimibles (`/imprimibles/`)

#### Opciones de Impresión:

**Opción 1: Impresora A3** (Recomendada)
- `tarjeta-completa-A3.pdf` - Tarjeta completa en una sola hoja A3
- `personajes-popup.pdf` - 4 personajes para recortar y pegar

**Opción 2: Impresora A4**
- `tarjeta-completa-A4-parte1.pdf` - Primera mitad de la tarjeta
- `tarjeta-completa-A4-parte2.pdf` - Segunda mitad de la tarjeta
- `personajes-popup.pdf` - 4 personajes para recortar y pegar

#### Instrucciones:
- `README-IMPRIMIR.md` - Guía rápida de impresión
- `INSTRUCCIONES.md` - Instrucciones completas de armado paso a paso

### Herramientas

- `generate_pdfs.py` - Script Python para regenerar los PDFs
- `plantilla-word-instrucciones.md` - Instrucciones originales para crear en Word

## 🎨 Características de la Tarjeta

### Diseño

**Dimensiones:**
- Tarjeta completa: 60 cm × 18 cm (5 páginas de 12×18 cm cada una)
- Formato acordeón con dobleces alternados (montaña/valle)

**5 Páginas Temáticas:**

1. **Portada:** "Llegó el gran día!!! 2025"
   - Banderines coloridos
   - Birrete de graduación
   - Número 2025 multicolor
   - Confeti festivo

2. **Página 1:** "Nunca dudes de que lo puedes todo en la vida"
   - Mensaje de apoyo
   - Espacio para personaje pop-up
   - Fuegos artificiales decorativos

3. **Página 2:** "Quiero que sepas y que estamos muy orgullosos de vos"
   - Banderines superiores
   - Serpentinas decorativas
   - Espacio para personaje pop-up

4. **Página 3:** "Hoy se termina una etapa muy importante en tu vida y comienza otra mucho mejor"
   - Círculos pastel de fondo
   - Birretes decorativos
   - Espacio para personaje pop-up

5. **Página 4:** "Tu esfuerzo y dedicación dieron fruto - lo lograste Augusto!!! Te Amo hijo."
   - Mensaje personalizado con el nombre
   - Confeti celebratorio
   - Espacio para personaje pop-up

### Personajes Pop-up (3D)

4 personajes estilo "stick figure" minimalista:

1. **Personaje con Corazón:** Figura con corazón rosa flotante
2. **SOS INCREÍBLE:** Figura sosteniendo un cartel motivacional
3. **Celebrando:** Figura con brazos en alto en pose de victoria
4. **Con Birrete:** Figura con birrete de graduación y confeti

Cada personaje incluye lengüetas para pegar a 90° creando el efecto 3D.

## 🖨️ Cómo Usar

### Inicio Rápido

1. **Descarga los PDFs necesarios** de la carpeta `/imprimibles/`
2. **Imprime** en cartulina (240gr para tarjeta, 180gr para personajes)
3. **Sigue las instrucciones** en `imprimibles/INSTRUCCIONES.md`
4. **Corta, dobla y pega** siguiendo las guías marcadas
5. **¡Disfruta tu tarjeta personalizada!**

### Materiales Necesarios

- Cartulina 240gr (para la tarjeta)
- Cartulina 180gr (para personajes)
- Tijeras o cúter
- Pegamento en barra
- Regla (opcional)

## 📐 Especificaciones Técnicas

### Colores Utilizados

- Rosa suave: #FFD6E8
- Lila claro: #E6D5F5
- Amarillo: #FFF4CC
- Verde agua: #D5F5E3
- Azul cielo: #D6EAF8
- Rosa fuerte: #FF69B4
- Lila fuerte: #9B59B6
- Dorado: #FFD700

### Formato PDF

- Versión: PDF 1.4
- Tamaño A3: 420 × 297 mm (horizontal)
- Tamaño A4: 210 × 297 mm
- Resolución: Vectorial
- Modo de color: RGB (optimizado para impresión hogareña)

### Guías de Corte y Doblez

- Líneas de corte: Punteadas grises (0.5pt)
- Líneas de doblez: Continuas grises (0.3pt)
- Marcas de empalme: Rojas (para versión A4)
- Lengüetas: Líneas rojas punteadas

## 🔧 Regenerar PDFs

Si necesitas modificar los PDFs:

1. **Instalar dependencias:**
   ```bash
   pip install reportlab
   ```

2. **Ejecutar el generador:**
   ```bash
   python3 generate_pdfs.py
   ```

3. Los PDFs se regenerarán en la carpeta `/imprimibles/`

## 📝 Personalización

Para personalizar la tarjeta con otro nombre:

1. Edita `generate_pdfs.py`
2. Busca la función `draw_pagina4()`
3. Modifica la línea con `text = "Augusto!!!"`
4. Ejecuta el script para regenerar los PDFs

## 🎁 Resultado Final

Al armar la tarjeta obtendrás:

- Una tarjeta de 60 cm de largo en formato acordeón
- 4 personajes pop-up que se levantan en 3D al abrir la tarjeta
- Diseño colorido y festivo con mensajes personalizados
- Presentación profesional lista para entregar

## 📄 Licencia

Este proyecto es de uso personal. Los archivos pueden ser utilizados libremente para crear tarjetas de graduación.

## 🤝 Contribuciones

Este es un proyecto personal, pero si deseas mejorarlo:

- Puedes sugerir mejoras en los diseños
- Reportar problemas con los PDFs
- Compartir variaciones del diseño

## ✨ Créditos

Diseñado con amor para celebrar un logro importante. 

**Herramientas utilizadas:**
- Python 3
- ReportLab (generación de PDFs)
- Diseño vectorial original

---

**¡Felicitaciones a todos los graduados! 🎓🎉**
