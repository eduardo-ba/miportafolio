from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "cv-luis-eduardo-barron.pdf"

FONT_REGULAR = Path("C:/Windows/Fonts/arial.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/arialbd.ttf")

pdfmetrics.registerFont(TTFont("Arial", FONT_REGULAR))
pdfmetrics.registerFont(TTFont("Arial-Bold", FONT_BOLD))

INK = HexColor("#0B0E0D")
TEXT = HexColor("#262B28")
MUTED = HexColor("#667069")
LINE = HexColor("#D8DDD6")
LIME = HexColor("#C8F45A")
PAPER = HexColor("#FAFAF7")


def wrapped_lines(text: str, font: str, size: float, max_width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if pdfmetrics.stringWidth(candidate, font, size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    *,
    font: str = "Arial",
    size: float = 8.4,
    leading: float = 11.2,
    color=TEXT,
) -> float:
    pdf.setFont(font, size)
    pdf.setFillColor(color)
    for line in wrapped_lines(text, font, size, width):
        pdf.drawString(x, y, line)
        y -= leading
    return y


def section_title(pdf: canvas.Canvas, title: str, x: float, y: float, width: float) -> float:
    pdf.setFillColor(INK)
    pdf.setFont("Arial-Bold", 8.2)
    pdf.drawString(x, y, title.upper())
    pdf.setStrokeColor(INK)
    pdf.setLineWidth(0.8)
    pdf.line(x, y - 5, x + width, y - 5)
    return y - 19


def label(pdf: canvas.Canvas, text: str, x: float, y: float, color=MUTED) -> None:
    pdf.setFont("Arial-Bold", 7.2)
    pdf.setFillColor(color)
    pdf.drawString(x, y, text.upper())


def project(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    year: str,
    name: str,
    description: str,
    stack: str,
) -> float:
    label(pdf, year, x, y)
    pdf.setFont("Arial-Bold", 10.3)
    pdf.setFillColor(INK)
    pdf.drawString(x + 40, y, name)
    y -= 14
    y = draw_wrapped(pdf, description, x + 40, y, width - 40, size=8.1, leading=10.4)
    y -= 1
    y = draw_wrapped(pdf, stack, x + 40, y, width - 40, font="Arial-Bold", size=7.1, leading=9, color=MUTED)
    return y - 11


def experience(
    pdf: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    date: str,
    role: str,
    bullets: list[str],
) -> float:
    label(pdf, date, x, y)
    y = draw_wrapped(pdf, role, x + 58, y, width - 58, font="Arial-Bold", size=9.6, leading=11.2, color=INK)
    y -= 2
    for bullet in bullets:
        pdf.setFillColor(LIME)
        pdf.circle(x + 62, y + 2.6, 1.5, stroke=0, fill=1)
        y = draw_wrapped(pdf, bullet, x + 70, y, width - 70, size=7.8, leading=9.7)
        y -= 2
    return y - 8


def sidebar_group(pdf: canvas.Canvas, x: float, y: float, width: float, title: str, items: list[str]) -> float:
    label(pdf, title, x, y, INK)
    y -= 13
    for item in items:
        pdf.setFont("Arial", 7.8)
        pdf.setFillColor(TEXT)
        for line in wrapped_lines(item, "Arial", 7.8, width):
            pdf.drawString(x, y, line)
            y -= 9.6
        y -= 2.4
    return y - 8


def build_cv() -> None:
    width, height = A4
    pdf = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    pdf.setTitle("CV - Luis Eduardo Barrón - Web Developer")
    pdf.setAuthor("Luis Eduardo Barrón Alvarez")
    pdf.setSubject("Web Developer - Astro, TypeScript y JavaScript")

    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, width, height, stroke=0, fill=1)

    header_height = 128
    pdf.setFillColor(INK)
    pdf.rect(0, height - header_height, width, header_height, stroke=0, fill=1)
    pdf.setFillColor(LIME)
    pdf.rect(42, height - 44, 24, 4, stroke=0, fill=1)

    pdf.setFillColor(HexColor("#F4F5EC"))
    pdf.setFont("Arial-Bold", 22.5)
    pdf.drawString(42, height - 70, "LUIS EDUARDO BARRÓN ALVAREZ")
    pdf.setFillColor(LIME)
    pdf.setFont("Arial-Bold", 11.5)
    pdf.drawString(42, height - 92, "WEB DEVELOPER  /  ESTUDIANTE DE INGENIERÍA EN TI")
    pdf.setFillColor(HexColor("#B9BEB5"))
    pdf.setFont("Arial", 7.5)
    contact = "Mazatlán, Sinaloa  ·  +52 669 329 2473  ·  leduardobarron@gmail.com  ·  github.com/eduardo-ba"
    pdf.drawString(42, height - 111, contact)
    pdf.linkURL("mailto:leduardobarron@gmail.com", (214, height - 115, 334, height - 104), relative=0)
    pdf.linkURL("https://github.com/eduardo-ba", (384, height - 115, 497, height - 104), relative=0)

    left_x, left_w = 42, 338
    side_x, side_w = 406, 147
    body_top = height - header_height - 28

    y = section_title(pdf, "Perfil", left_x, body_top, left_w)
    summary = (
        "Estudiante de Ingeniería en Tecnologías de la Información enfocado en desarrollo web. "
        "Construyo sitios responsivos y experiencias orientadas al contenido con Astro, TypeScript y JavaScript. "
        "Mi experiencia en redes, servidores y soporte aporta una visión práctica de rendimiento, confiabilidad y resolución de problemas."
    )
    y = draw_wrapped(pdf, summary, left_x, y, left_w, size=8.5, leading=11.2)
    y -= 15

    y = section_title(pdf, "Proyectos seleccionados", left_x, y, left_w)
    y = project(
        pdf,
        left_x,
        y,
        left_w,
        "2026",
        "Blonded Visual Archive",
        "Publicación digital bilingüe con rutas dinámicas, búsqueda, filtros, RSS, sitemap, notas locales y optimización de imágenes.",
        "Astro · TypeScript · CSS · i18n · SEO",
    )
    y = project(
        pdf,
        left_x,
        y,
        left_w,
        "2026",
        "Portafolio multilingüe",
        "Portafolio en español, inglés y francés con componentes reutilizables, contenido tipado, imágenes optimizadas y metadatos localizados.",
        "Astro · TypeScript · Tailwind CSS · i18n",
    )
    y = project(
        pdf,
        left_x,
        y,
        left_w,
        "2025",
        "Micrositio de Estructuras de Datos",
        "Sitio académico responsive con maquetación semántica y navegación móvil accesible.",
        "HTML · CSS · JavaScript · jQuery",
    )

    y = section_title(pdf, "Experiencia", left_x, y, left_w)
    y = experience(
        pdf,
        left_x,
        y,
        left_w,
        "2023—2024",
        "Responsable de Soporte Técnico y Redes · CETis No. 127",
        [
            "Renové la infraestructura de red con cableado UTP Cat6 e implementé videovigilancia IP.",
            "Administré switches, routers y segmentación con VLAN; brindé soporte a personal administrativo y docente.",
        ],
    )
    y = experience(
        pdf,
        left_x,
        y,
        left_w,
        "2024",
        "Técnico de redes independiente",
        ["Instalé y mejoré redes Wi-Fi y cableadas para pequeños negocios en Mazatlán."],
    )

    y = section_title(pdf, "Competencias", left_x, y, left_w)
    y = draw_wrapped(
        pdf,
        "Resolución de problemas  ·  Comunicación  ·  Trabajo en equipo  ·  Gestión del tiempo  ·  Pensamiento estratégico",
        left_x,
        y,
        left_w,
        size=8.2,
        leading=11,
    )
    y -= 16
    pdf.setFillColor(LIME)
    pdf.roundRect(left_x, y - 43, left_w, 54, 6, stroke=0, fill=1)
    label(pdf, "Objetivo actual", left_x + 14, y - 7, INK)
    draw_wrapped(
        pdf,
        "Prácticas, proyectos junior y colaboraciones remotas en desarrollo web.",
        left_x + 14,
        y - 23,
        left_w - 28,
        font="Arial-Bold",
        size=8.6,
        leading=10.5,
        color=INK,
    )

    side_y = section_title(pdf, "Stack principal", side_x, body_top, side_w)
    side_y = sidebar_group(pdf, side_x, side_y, side_w, "Frontend", ["TypeScript · JavaScript", "HTML5 · CSS3", "Responsive UI · Accesibilidad"])
    side_y = sidebar_group(pdf, side_x, side_y, side_w, "Ecosistema web", ["Astro · React · Node.js", "Vite · SEO técnico"])
    side_y = sidebar_group(pdf, side_x, side_y, side_w, "Datos y sistemas", ["MySQL · SQLite · Firebase", "Python · Java · Linux", "Git · GitHub"])

    side_y = section_title(pdf, "Educación", side_x, side_y, side_w)
    label(pdf, "2027 · En curso", side_x, side_y)
    side_y -= 13
    side_y = draw_wrapped(pdf, "Ingeniería en Tecnologías de la Información e Innovación Digital", side_x, side_y, side_w, font="Arial-Bold", size=8.3, leading=10.5, color=INK)
    side_y = draw_wrapped(pdf, "Universidad Politécnica de Sinaloa", side_x, side_y - 2, side_w, size=7.8, leading=9.8, color=MUTED)
    side_y -= 10
    label(pdf, "2024", side_x, side_y)
    side_y -= 13
    side_y = draw_wrapped(pdf, "Técnico en soporte y mantenimiento de equipo de cómputo", side_x, side_y, side_w, font="Arial-Bold", size=8.1, leading=10.3, color=INK)
    side_y = draw_wrapped(pdf, "CETis No. 127", side_x, side_y - 2, side_w, size=7.8, leading=9.8, color=MUTED)
    side_y -= 12

    side_y = section_title(pdf, "Certificaciones", side_x, side_y, side_w)
    certs = [
        "CCNA: Switching, Routing, and Wireless Essentials",
        "CCNA: Introduction to Networks",
        "Administrador de servidores",
        "Fundamentos de Linux",
        "Técnico instalador de cableado estructurado",
        "Conceptos básicos de redes",
    ]
    side_y = sidebar_group(pdf, side_x, side_y, side_w, "Cisco NetAcad / Capacítate", certs)

    side_y = section_title(pdf, "Idiomas", side_x, side_y, side_w)
    side_y = draw_wrapped(pdf, "Español nativo  ·  Inglés B1", side_x, side_y, side_w, size=8.1, leading=10.2)

    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(0.6)
    pdf.line(42, 31, width - 42, 31)
    pdf.setFont("Arial", 6.8)
    pdf.setFillColor(MUTED)
    pdf.drawString(42, 19, "Portfolio: miportafolio.netlify.app")
    pdf.drawRightString(width - 42, 19, "Actualizado en agosto de 2026")
    pdf.linkURL("https://miportafolio.netlify.app", (42, 15, 156, 28), relative=0)

    pdf.showPage()
    pdf.save()


if __name__ == "__main__":
    build_cv()
    print(OUTPUT)
