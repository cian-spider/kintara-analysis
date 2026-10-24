#!/usr/bin/env python3
"""Render the Kintara 'live vs unpublished' card.

Every number on the card is one of the figures measured on 2026-10-24T05:11Z and
recorded in the article it accompanies. The card says UNOFFICIAL because the
bounty forbids presenting it as a Kintara announcement.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 1200
BG = (11, 13, 20)
PANEL = (22, 26, 38)
LINE = (46, 52, 70)
FG = (232, 236, 245)
DIM = (150, 160, 180)
ACCENT = (126, 231, 165)
WARN = (247, 190, 96)

F = "/usr/share/fonts/truetype/dejavu/"
def f(name, size):
    return ImageFont.truetype(F + name, size)

bold = lambda s: f("DejaVuSans-Bold.ttf", s)
reg = lambda s: f("DejaVuSans.ttf", s)
mono = lambda s: f("DejaVuSansMono.ttf", s)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# header
logo = Image.open("kins.png").convert("RGB").resize((104, 104), Image.LANCZOS)
img.paste(logo, (64, 60))
d.text((192, 66), "KINTARA", font=bold(56), fill=FG)
d.text((196, 128), "an isometric MMO where your wallet is the account", font=reg(22), fill=DIM)

d.text((64, 200), "UNOFFICIAL ANALYSIS", font=bold(20), fill=WARN)
d.text((64, 228), "AI-created for a Mycelium Finance bounty · data read 2026-10-24 05:11 UTC",
       font=reg(19), fill=DIM)

y = 290
def panel(x, y, w, h, title, rows, title_col=FG):
    d.rounded_rectangle([x, y, x + w, y + h], 16, fill=PANEL, outline=LINE, width=2)
    d.text((x + 26, y + 22), title, font=bold(24), fill=title_col)
    yy = y + 66
    for head, body in rows:
        d.text((x + 26, yy), head, font=bold(21), fill=FG)
        yy += 28
        for line in body:
            d.text((x + 26, yy), line, font=reg(19), fill=DIM)
            yy += 25
        yy += 12
    return yy

panel(64, y, 520, 400, "LIVE TODAY", [
    ("Free to level 10", ["Wallet connect, no email login.", "Mainland, Whisperwood, The Pond,", "Wilderness realms are playable."]),
    ("Hold 1,000 $KINS", ["Opens The Shores, Dunes, Emberstone,", "Venomweaver. 24h held unlocks", "trading and Marketplace selling."]),
    ("Verifiable on-chain", ["Supply fixed: 991,692,981.41 $KINS", "Mint + freeze authority revoked."]),
])

panel(616, y, 520, 400, "NOT PUBLISHED", [
    ("No roadmap", ["No dated plan on kintara.com or in", "the game guide as of this reading."]),
    ("No emission schedule", ["Docs list token sinks but no source of", "new $KINS demand beyond the gate."]),
    ("No holder breakdown", ["Team, treasury and vesting splits are", "not disclosed anywhere public."]),
], title_col=WARN)

y2 = 726
d.rounded_rectangle([64, y2, 1136, y2 + 300], 16, fill=PANEL, outline=LINE, width=2)
d.text((90, y2 + 20), "WHAT THE TOKEN DOES", font=bold(24), fill=FG)
d.text((90, y2 + 60), "1,000 $KINS access gate  ≈  $0.32", font=mono(22), fill=ACCENT)
d.text((90, y2 + 92), "at $0.0003208 / $KINS (DexScreener, pumpswap pool)", font=reg(18), fill=DIM)
d.text((90, y2 + 132), "Paid spinner spin: $5 of $KINS  →  50% burned, 50% treasury", font=mono(20), fill=FG)
d.text((90, y2 + 164), "Gold-for-$KINS Marketplace sale: 5% treasury, 95% seller", font=mono(20), fill=FG)
d.text((90, y2 + 204), "Market cap $318,231   Liquidity $92,038   Volume 24h $111,124", font=mono(19), fill=DIM)
d.text((90, y2 + 232), "7-day change -47.2%   Players online 472   Total players 69,433", font=mono(19), fill=DIM)
d.text((90, y2 + 262), "Sources: kintara.com/#docs · DexScreener · Solana RPC · CoinGecko", font=reg(17), fill=(110, 120, 140))

d.text((64, 1056), "Mycelium Strategy holds $KINS at 9.2% of $29,454 live capital",
       font=bold(22), fill=FG)
d.text((64, 1088), "via the MYC/KINS Raydium pool (unlocked LP). Not an official Kintara or Mycelium statement.",
       font=reg(19), fill=DIM)
d.text((64, 1130), "Not investment advice. No price prediction. Figures change; each one carries the time it was read.",
       font=reg(17), fill=(110, 120, 140))

img.save("kintara-card.png", optimize=True)
print("wrote kintara-card.png", img.size)
