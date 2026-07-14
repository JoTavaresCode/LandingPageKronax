from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT = "Manual_Backup_SigmaPDV.pdf"

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
VERDE_FND = colors.HexColor("#f0fdf4")
VERDE_BRD = colors.HexColor("#86efac")
AMARELO   = colors.HexColor("#fffbeb")
AMARELO_B = colors.HexColor("#fbbf24")
AMARELO_T = colors.HexColor("#92400e")
VERMELHO  = colors.HexColor("#fef2f2")
VERMELHO_B= colors.HexColor("#fca5a5")
VERMELHO_T= colors.HexColor("#991b1b")
BRANCO    = colors.white
PRETO     = colors.HexColor("#0f172a")

def estilo(nome, **kwargs):
    base = {
        "fontName": "Helvetica",
        "fontSize": 10.5,
        "textColor": colors.HexColor("#374151"),
        "leading": 16,
    }
    base.update(kwargs)
    return ParagraphStyle(nome, **base)

titulo_capa  = estilo("tc",  fontSize=24, fontName="Helvetica-Bold", textColor=BRANCO, alignment=TA_CENTER, spaceAfter=4)
sub_capa     = estilo("sc",  fontSize=12, textColor=colors.HexColor("#93c5fd"), alignment=TA_CENTER)
secao        = estilo("sec", fontSize=13, fontName="Helvetica-Bold", textColor=AZUL, spaceBefore=18, spaceAfter=6)
corpo        = estilo("co",  spaceAfter=6)
negrito      = estilo("nb",  fontName="Helvetica-Bold", textColor=PRETO, spaceAfter=4)
nota_pequena = estilo("np",  fontSize=10, textColor=CINZA_TX, leading=14)
rodape_st    = estilo("ro",  fontSize=9,  textColor=CINZA_TX, alignment=TA_CENTER)
passo_titulo = estilo("pt",  fontSize=12, fontName="Helvetica-Bold", textColor=PRETO, spaceAfter=3)
passo_num_st = estilo("pn",  fontSize=20, fontName="Helvetica-Bold", textColor=AZUL, alignment=TA_CENTER)
aviso_titulo = estilo("at",  fontSize=11, fontName="Helvetica-Bold", textColor=AMARELO_T)
aviso_corpo  = estilo("ac",  fontSize=10, textColor=colors.HexColor("#78350f"), leading=14)
ok_texto     = estilo("ok",  fontSize=10, textColor=colors.HexColor("#166534"), leading=14)

story = []

# ── CAPA ──
capa = Table([[Paragraph("PDV", titulo_capa)]], colWidths=[W - 4.4*cm])
capa.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), AZUL_ESC),
    ("TOPPADDING",    (0,0), (-1,-1), 32),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(capa)

sub = Table([[Paragraph("Guia de Backup e Proteção de Dados", sub_capa)]], colWidths=[W - 4.4*cm])
sub.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), AZUL_ESC),
    ("TOPPADDING",    (0,0), (-1,-1), 0),
    ("BOTTOMPADDING", (0,0), (-1,-1), 28),
]))
story.append(sub)
story.append(Spacer(1, 22))

# ── INTRODUÇÃO ──
story.append(Paragraph("Por que fazer backup?", secao))
story.append(Paragraph(
    "Todos os dados do PDV — vendas, produtos, estoque, clientes — ficam salvos num arquivo "
    "chamado <b>sistema.db</b> dentro da pasta do sistema no seu computador.",
    corpo))
story.append(Paragraph(
    "Se o computador quebrar, for formatado ou precisar ser trocado, esse arquivo pode ser perdido. "
    "O backup é a cópia de segurança desse arquivo, guardada em outro lugar — como o Google Drive ou um pendrive.",
    corpo))
story.append(Spacer(1, 6))

# ── CAIXA DESTAQUE ──
destaque = Table([[
    Paragraph("💡", estilo("ic", fontSize=22, alignment=TA_CENTER)),
    Paragraph(
        "<b>Com o backup ativo, mesmo que o computador quebre completamente, você não perde nenhum dado. "
        "Basta instalar o sistema num computador novo e restaurar o backup.</b>",
        estilo("ds", fontSize=11, textColor=AZUL_ESC, leading=16))
]], colWidths=[1.2*cm, W - 4.4*cm - 1.2*cm])
destaque.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#eff6ff")),
    ("BOX",           (0,0), (-1,-1), 1.5, AZUL),
    ("TOPPADDING",    (0,0), (-1,-1), 14),
    ("BOTTOMPADDING", (0,0), (-1,-1), 14),
    ("LEFTPADDING",   (0,0), (-1,-1), 14),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("ROUNDEDCORNERS", [8]),
]))
story.append(destaque)
story.append(Spacer(1, 20))

# ── CONFIGURAR BACKUP AUTOMÁTICO ──
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0")))
story.append(Spacer(1, 10))
story.append(Paragraph("Parte 1 — Configurar o Backup Automático", secao))
story.append(Paragraph(
    "Faça isso uma única vez. Depois, o sistema cuida do backup sozinho toda vez que for aberto.",
    corpo))
story.append(Spacer(1, 8))

passos_config = [
    ("1", "Instale o Google Drive no computador",
     "Acesse <b>drive.google.com</b>, clique em \"Baixar Drive para Desktop\" e instale. "
     "Após instalar, uma pasta do Google Drive aparecerá automaticamente no seu computador "
     "(geralmente em <b>C:\\Users\\SeuNome\\Google Drive</b>)."),
    ("2", "Crie uma pasta para os backups",
     "Dentro da pasta do Google Drive, crie uma nova pasta chamada <b>Backups PDV</b>. "
     "Tudo que for salvo aqui ficará automaticamente na nuvem."),
    ("3", "Abra as Configurações do PDV",
     "No menu lateral, clique em <b>Configurações</b> (ícone de engrenagem no rodapé do menu). "
     "Você precisa estar logado como <b>administrador</b>."),
    ("4", "Cole o caminho da pasta",
     "Na seção <b>Backup Automático</b>, cole o caminho completo da pasta criada. Exemplo:<br/>"
     "<b>C:\\Users\\João\\Google Drive\\Backups PDV</b><br/>"
     "Para copiar o caminho: abra a pasta no Explorador de Arquivos, clique na barra de endereço "
     "no topo e copie o texto que aparecer."),
    ("5", "Clique em Salvar pasta",
     "Pronto! A partir de agora, toda vez que o SPDV for iniciado ele fará o backup "
     "automaticamente. Os últimos <b>30 backups</b> são mantidos — os mais antigos são apagados sozinhos."),
]

for num, titulo, desc in passos_config
    t = Table([[
        Paragraph(num, passo_num_st),
        [Paragraph(titulo, passo_titulo), Paragraph(desc, corpo)]
    ]], colWidths=[1.4*cm, W - 4.4*cm - 1.4*cm])
    t.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("BACKGROUND",   (0,0), (0,0),   CINZA_FND),
        ("TOPPADDING",   (0,0), (-1,-1), 10),
        ("BOTTOMPADDING",(0,0), (-1,-1), 10),
        ("LEFTPADDING",  (1,0), (1,0),   12),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("BOX",          (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

# ── BACKUP MANUAL ──
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0")))
story.append(Spacer(1, 10))
story.append(Paragraph("Parte 2 — Fazer Backup Manual", secao))
story.append(Paragraph(
    "Além do automático, você pode fazer um backup a qualquer momento — antes de uma atualização, "
    "por exemplo.",
    corpo))

manual_passos = [
    "Abra o SigmaPDV e vá em <b>Configurações</b>.",
    "Role a página até a seção <b>Backup Automático</b>.",
    "Clique no botão <b>Fazer backup agora</b>.",
    "Uma mensagem verde confirmará onde o arquivo foi salvo.",
]
for i, p in enumerate(manual_passos, 1):
    row = Table([[
        Paragraph(str(i), estilo("mn", fontSize=11, fontName="Helvetica-Bold", textColor=AZUL, alignment=TA_CENTER)),
        Paragraph(p, corpo)
    ]], colWidths=[0.8*cm, W - 4.4*cm - 0.8*cm])
    row.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",   (0,0), (-1,-1), 7),
        ("BOTTOMPADDING",(0,0), (-1,-1), 7),
        ("LEFTPADDING",  (1,0), (1,0),   10),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ]))
    story.append(row)

story.append(Spacer(1, 16))

# ── RESTAURAR ──
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0")))
story.append(Spacer(1, 10))
story.append(Paragraph("Parte 3 — Restaurar o Backup (troca de computador)", secao))
story.append(Paragraph(
    "Se precisar instalar o sistema em um computador novo, siga estes passos para recuperar todos os seus dados:",
    corpo))
story.append(Spacer(1, 8))

restaurar_passos = [
    ("Instale o SigmaPDV no novo computador",
     "Extraia o arquivo .zip enviado pelo suporte e execute o SigmaPDV.exe normalmente."),
    ("Ative com uma nova chave",
     "O novo computador terá um ID diferente. Entre em contato com o suporte enviando o novo ID "
     "para receber a chave de ativação transferida."),
    ("Abra as Configurações e vá em Restaurar Backup",
     "Clique em <b>Escolher arquivo</b> e selecione o arquivo .db mais recente da sua pasta do Google Drive "
     "(ex: <b>SigmaPDV_backup_20260615_143022.db</b>)."),
    ("Clique em Restaurar agora",
     "O sistema substituirá os dados em branco pelos seus dados anteriores. "
     "Uma mensagem confirmará o sucesso."),
    ("Feche e reabra o SigmaPDV",
     "Todos os seus dados — produtos, estoque, clientes, vendas — estarão de volta."),
]

for i, (titulo, desc) in enumerate(restaurar_passos, 1):
    t = Table([[
        Paragraph(str(i), passo_num_st),
        [Paragraph(titulo, passo_titulo), Paragraph(desc, corpo)]
    ]], colWidths=[1.4*cm, W - 4.4*cm - 1.4*cm])
    t.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("BACKGROUND",   (0,0), (0,0),   CINZA_FND),
        ("TOPPADDING",   (0,0), (-1,-1), 10),
        ("BOTTOMPADDING",(0,0), (-1,-1), 10),
        ("LEFTPADDING",  (1,0), (1,0),   12),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("BOX",          (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

story.append(Spacer(1, 8))

# ── AVISO ──
aviso = Table([[
    Paragraph("⚠️", estilo("awi", fontSize=20, alignment=TA_CENTER)),
    [
        Paragraph("Atenção antes de restaurar", aviso_titulo),
        Paragraph(
            "Ao restaurar um backup, os dados atuais do sistema serão substituídos. "
            "O sistema salva automaticamente um backup de segurança antes de qualquer restauração, "
            "mas confirme que está selecionando o arquivo correto.",
            aviso_corpo)
    ]
]], colWidths=[1.2*cm, W - 4.4*cm - 1.2*cm])
aviso.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), AMARELO),
    ("BOX",           (0,0), (-1,-1), 1.2, AMARELO_B),
    ("TOPPADDING",    (0,0), (-1,-1), 12),
    ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ("LEFTPADDING",   (0,0), (-1,-1), 12),
    ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ("ROUNDEDCORNERS", [6]),
]))
story.append(aviso)
story.append(Spacer(1, 20))

# ── RESUMO RÁPIDO ──
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#e2e8f0")))
story.append(Spacer(1, 10))
story.append(Paragraph("Resumo Rápido", secao))

resumo_data = [
    ["O que fazer", "Quando", "Como"],
    ["Configurar backup automático", "Uma única vez", "Configurações → Backup Automático → Salvar pasta"],
    ["Backup manual", "Quando quiser", "Configurações → Fazer backup agora"],
    ["Restaurar backup", "Troca de PC ou problema", "Configurações → Restaurar Backup → Escolher arquivo"],
    ["Baixar banco de dados", "Qualquer momento", "Configurações → Baixar arquivo .db"],
]
resumo = Table(resumo_data, colWidths=[4.5*cm, 3.5*cm, W - 4.4*cm - 8*cm])
resumo.setStyle(TableStyle([
    ("BACKGROUND",     (0,0), (-1,0),  AZUL_ESC),
    ("TEXTCOLOR",      (0,0), (-1,0),  BRANCO),
    ("FONTNAME",       (0,0), (-1,0),  "Helvetica-Bold"),
    ("FONTSIZE",       (0,0), (-1,-1), 10),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [BRANCO, CINZA_FND]),
    ("BOX",            (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ("INNERGRID",      (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
    ("TOPPADDING",     (0,0), (-1,-1), 9),
    ("BOTTOMPADDING",  (0,0), (-1,-1), 9),
    ("LEFTPADDING",    (0,0), (-1,-1), 10),
    ("VALIGN",         (0,0), (-1,-1), "MIDDLE"),
]))
story.append(resumo)
story.append(Spacer(1, 22))

# ── CONTATO ──
contato = Table([[
    Paragraph("🆘", estilo("ct", fontSize=20, alignment=TA_CENTER)),
    [
        Paragraph("Precisa de ajuda?", estilo("ch", fontSize=11, fontName="Helvetica-Bold", textColor=PRETO, spaceAfter=4)),
        Paragraph("Entre em contato com o suporte. Respondemos rapidamente.", nota_pequena),
        Paragraph("E-mail: <b>SEU_EMAIL@email.com</b>  |  WhatsApp: <b>A definir</b>", nota_pequena),
    ]
]], colWidths=[1.2*cm, W - 4.4*cm - 1.2*cm])
contato.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), VERDE_FND),
    ("BOX",           (0,0), (-1,-1), 1, VERDE_BRD),
    ("TOPPADDING",    (0,0), (-1,-1), 14),
    ("BOTTOMPADDING", (0,0), (-1,-1), 14),
    ("LEFTPADDING",   (0,0), (-1,-1), 14),
    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
    ("ROUNDEDCORNERS", [8]),
]))
story.append(contato)
story.append(Spacer(1, 20))

# ── RODAPÉ ──
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e2e8f0")))
story.append(Spacer(1, 10))
story.append(Paragraph("SigmaPDV — Sistema de Ponto de Venda  |  © 2026  |  Todos os direitos reservados", rodape_st))

doc.build(story)
print(f"PDF gerado: {OUTPUT}")
