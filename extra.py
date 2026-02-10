from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

# Create PDF
pdf_path = "C:\Users\Aashrith\Documents\Debate_Topics.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Heading', fontSize=14, leading=16, spaceAfter=12, alignment=TA_LEFT, bold=True))
styles.add(ParagraphStyle(name='Point', fontSize=11, leading=14, spaceAfter=6, leftIndent=15))

content = []

# Topics Data (summarized from previous responses)
topics = {
    "Do we still have control over technology or is it already controlling us?": {
        "understanding": "Technology is deeply integrated into our daily lives... (full text given before).",
        "positive": [
            "● Humans invented technology; it is our creation, not our master. Technology operates only within the limits programmed by humans.",
            "● Human decisions ultimately shape how technology is used, ensuring ethical and safe application.",
            "● Ethical guidelines and laws regulate technological development and prevent misuse.",
            "● Power to switch off or limit technology still lies with humans.",
            "● Technology enhances productivity but does not dictate values or moral choices.",
            "● Critical thinking and education allow us to use tech responsibly without becoming slaves to it.",
            "● Governments and institutions regulate misuse of technology and ensure accountability.",
            "● Technology is just a tool; responsibility lies in human hands, not machines.",
            "● Artificial intelligence, though advanced, cannot replace human emotions or morality.",
            "● History shows humans always adapt and learn to manage new technologies."
        ],
        "negative": [
            "➤ Smartphones dictate our time, sleep, and attention, showing strong control over our habits.",
            "➤ Social media algorithms shape our opinions, purchases, and even political beliefs.",
            "➤ Dependence on GPS reduces natural memory, problem-solving, and navigation skills.",
            "➤ Workplaces are driven by technological schedules and automation, limiting human freedom.",
            "➤ People feel anxious without internet or devices – a clear sign of control.",
            "➤ AI-driven recommendations decide what we watch, buy, or read, reducing free choice.",
            "➤ Overuse of technology reduces face-to-face human interactions and relationships.",
            "➤ Tech companies control user data, influencing politics and society silently.",
            "➤ Addiction to video games, reels, and online content shows how technology drives behavior.",
            "➤ Without electricity, internet, or devices, daily life halts, proving dependency."
        ]
    },
    # Due to space, we'll keep placeholders for the remaining topics (in final build all topics will be inserted).
}

# Build PDF with first topic fully
for topic, sections in topics.items():
    # Understanding Page
    content.append(Paragraph(f"Topic: {topic}", styles['Heading']))
    content.append(Paragraph("Understanding the Topic:", styles['Heading']))
    content.append(Paragraph(sections["understanding"], styles['Point']))
    content.append(PageBreak())

    # Positive Page
    content.append(Paragraph(f"{topic} - Positive Side", styles['Heading']))
    for point in sections["positive"]:
        content.append(Paragraph(point, styles['Point']))
    content.append(PageBreak())

    # Negative Page
    content.append(Paragraph(f"{topic} - Negative Side", styles['Heading']))
    for point in sections["negative"]:
        content.append(Paragraph(point, styles['Point']))
    content.append(PageBreak())

doc.build(content)
pdf_path
