from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT = "Manual_SigmaPDV.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=2.2*cm, leftMargin=2.2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

W, H = A4

AZUL      = colors.HexColor("#2563eb")
AZUL_ESC  = colors.HexColor("#1e3a5f")
CINZA_FND = colors.HexColor("#f1f5f9")
CINZA_TX  = colors.HexColor("#64748b")
VERDE     = colors.HexColor("#16a34a")
BRANCO    = colors.white
PRETO     = colors.HexColor("#0f172a")

styles = getSampleStyleSheet()

titulo_principal = ParagraphStyle("titulo_principal",
    fontSize=26, fontName="Helvetica-Bold",
    textColor=BRANCO, alignment=TA_CENTER, spaceAfter=4)

subtitulo = ParagraphStyle("subtitulo",
    fontSize=13, fontName="Helvetica",
    textColor=colors.HexColor("#93c5fd"), alignment=TA_CENTER, spaceAfter=0)

secao = ParagraphStyle("secao",
    fontSize=13, fontName="Helvetica-Bold",
    textColor=AZUL, spaceBefore=18, spaceAfter=6)

passo_num = ParagraphStyle("passo_num",
    fontSize=22, fontName="Helvetica-Bold",
    textColor=AZUL, alignment=TA_CENTER)

passo_titulo = ParagraphStyle("passo_titulo",
    fontSize=12, fontName="Helvetica-Bold",
    textColor=PRETO, spaceAfter=3)

corpo = ParagraphStyle("corpo",
    fontSize=10.5, fontName="Helvetica",
    textColor=colors.HexColor("#374151"),
    leading=16, spaceAfter=6)

nota = ParagraphStyle("nota",
    fontSize=10, fontName="Helvetica",
    textColor=CINZA_TX, leading=14)

aviso = ParagraphStyle("aviso",
    fontSize=10.5, fontName="Helvetica-Bold",
    textColor=colors.HexColor("#92400e"))

rodape = ParagraphStyle("rodape",
    fontSize=9, fontName="Helvetica",
    textColor=CINZA_TX, alignment=TA_CENTER)

story = []

# ── CAPA ──
capa_data = [[
    Paragraph("SigmaPDV", titulo_principal),
]]
capa = Table(capa_data, colWidths=[W - 4.4*cm])
capa.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), AZUL_ESC),
    ("ROUNDEDCORNERS", [10]),
    ("TOPPADDING",    (0,0), (-1,-1), 36),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ("LEFTPADDING",   (0,0), (-1,-1), 20),
    ("RIGHTPADDING",  (0,0), (-1,-1), 20),
]))
story.append(capa)

sub_data = [[Paragraph("Manual de Instalação e Ativação", subtitulo)]]
sub_table = Table(sub_data, colWidths=[W - 4.4*cm])
sub_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), AZUL_ESC),
    ("BOTTOMPADDING", (0,0), (-1,-1), 32),
    ("TOPPADDING",    (0,0), (-1,-1), 0),
]))
story.append(sub_table)
story.append(Spacer(1, 22))

# ── INTRO ──
story.append(Paragraph("Bem-vindo ao SigmaPDV", secao))
story.append(Paragraph(
    "Este manual vai guiá-lo passo a passo para instalar e ativar o sistema no seu computador. "
    "Não é preciso instalar o Python nem qualquer outro programa — o SigmaPDV já vem pronto para uso.",
    corpo))
story.append(Spacer(1, 8))

# ── REQUISITOS ──
story.append(Paragraph("Requisitos mínimos", secao))
req = [
    ["Sistema",    "Windows 10 ou Windows 11"],
    ["Memória",    "2 GB de RAM ou mais"],
    ["Espaço",     "500 MB livres no disco"],
    ["Internet",   "Necessária apenas na ativação"],
]
req_table = Table(req, colWidths=[4*cm, 11*cm])
req_table.setStyle(TableStyle([
    ("BACKGROUND",   (0,0), (0,-1), CINZA_FND),
    ("FONTNAME",     (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTSIZE",     (0,0), (-1,-1), 10),
    ("TEXTCOLOR",    (0,0), (0,-1), AZUL),
    ("TEXTCOLOR",    (1,0), (1,-1), PRETO),
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [BRANCO, CINZA_FND]),
    ("BOX",          (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ("INNERGRID",    (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ("TOPPADDING",   (0,0), (-1,-1), 8),
    ("BOTTOMPADDING",(0,0), (-1,-1), 8),
    ("LEFTPADDING",  (0,0), (-1,-1), 12),
]))
story.append(req_table)
story.append(Spacer(1, 20))

# ── PASSOS ──
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0")))
story.append(Spacer(1, 14))
story.append(Paragraph("Instalação passo a passo", secao))
story.append(Spacer(1, 6))

passos = [
    ("1", "Baixe o arquivo", [
        "Acesse o link que você recebeu por e-mail ou WhatsApp.",
        "Faça o download do arquivo <b>SigmaPDV.zip</b>.",
        "Aguarde o download terminar completamente.",
    ]),
    ("2", "Extraia o arquivo", [
        "Localize o arquivo <b>SigmaPDV.zip</b> na pasta Downloads.",
        "Clique com o <b>botão direito</b> sobre ele.",
        'Selecione <b>"Extrair tudo"</b> e clique em <b>Extrair</b>.',
        "Uma pasta chamada <b>SigmaPDV</b> será criada.",
    ]),
    ("3", "Execute o sistema", [
        "Abra a pasta <b>SigmaPDV</b> extraída.",
        "Dê <b>dois cliques</b> no arquivo <b>SigmaPDV.exe</b>.",
        "Se aparecer um aviso do Windows, clique em <b>Executar assim mesmo</b>.",
        "O sistema vai abrir no navegador automaticamente.",
    ]),
    ("4", "Copie o ID da máquina", [
        "Na tela de ativação, você verá um código chamado <b>ID da Máquina</b>.",
        "Copie esse código e envie para o suporte por e-mail ou WhatsApp.",
        "Aguarde o recebimento da sua <b>Chave de Ativação</b>.",
    ]),
    ("5", "Ative o sistema", [
        "Cole a Chave de Ativação recebida no campo indicado.",
        "Marque a caixa <b>\"Li e aceito os termos\"</b>.",
        'Clique em <b>"Ativar"</b>.',
        "Pronto! O sistema está ativado e pronto para uso.",
    ]),
]

for num, titulo, itens in passos:
    passo_row = [[
        Paragraph(num, passo_num),
        [Paragraph(titulo, passo_titulo)] +
        [Paragraph(f"• {item}", corpo) for item in itens]
    ]]
    t = Table(passo_row, colWidths=[1.4*cm, W - 4.4*cm - 1.4*cm])
    t.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("BACKGROUND",   (0,0), (0,0),   CINZA_FND),
        ("LEFTPADDING",  (0,0), (0,0),   0),
        ("RIGHTPADDING", (0,0), (0,0),   10),
        ("TOPPADDING",   (0,0), (-1,-1), 10),
        ("BOTTOMPADDING",(0,0), (-1,-1), 10),
        ("LEFTPADDING",  (1,0), (1,0),   12),
        ("BOX",          (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

story.append(Spacer(1, 6))

# ── AVISO ──
aviso_data = [[
    Paragraph("⚠️  Atenção", aviso),
    Paragraph(
        "A licença é vinculada a este computador. Se você trocar ou formatar o computador, "
        "entre em contato com o suporte para transferir a ativação.",
        nota)
]]
aviso_table = Table(aviso_data, colWidths=[3.2*cm, W - 4.4*cm - 3.2*cm])
aviso_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#fffbeb")),
    ("BOX",           (0,0), (-1,-1), 1, colors.HexColor("#fbbf24")),
    ("LEFTPADDING",   (0,0), (-1,-1), 14),
    ("RIGHTPADDING",  (0,0), (-1,-1), 14),
    ("TOPPADDING",    (0,0), (-1,-1), 12),
    ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("ROUNDEDCORNERS", [6]),
]))
story.append(aviso_table)
story.append(Spacer(1, 20))

# ── DÚVIDAS ──
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0")))
story.append(Spacer(1, 14))
story.append(Paragraph("Dúvidas ou problemas?", secao))
story.append(Paragraph(
    "Entre em contato diretamente com o suporte. Respondemos rapidamente.",
    corpo))

contato_data = [
    ["E-mail", "SEU_EMAIL@email.com"],
    ["WhatsApp", "A definir"],
]
contato_table = Table(contato_data, colWidths=[3.5*cm, 10*cm])
contato_table.setStyle(TableStyle([
    ("FONTNAME",     (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTSIZE",     (0,0), (-1,-1), 10.5),
    ("TEXTCOLOR",    (0,0), (0,-1), AZUL),
    ("TEXTCOLOR",    (1,0), (1,-1), PRETO),
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [CINZA_FND, BRANCO]),
    ("BOX",          (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ("INNERGRID",    (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ("TOPPADDING",   (0,0), (-1,-1), 10),
    ("BOTTOMPADDING",(0,0), (-1,-1), 10),
    ("LEFTPADDING",  (0,0), (-1,-1), 12),
]))
story.append(contato_table)
story.append(Spacer(1, 30))

# ── RODAPÉ ──
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e2e8f0")))
story.append(Spacer(1, 10))
story.append(Paragraph("SigmaPDV — Sistema de Ponto de Venda  |  © 2026  |  Todos os direitos reservados", rodape))

doc.build(story)
print(f"PDF gerado: {OUTPUT}")
