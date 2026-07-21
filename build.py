#!/usr/bin/env python3
"""
Nohrskov Fonden - static site generator.
Rediger indhold i PAGES nedenfor og kor: python3 build.py
Genererer alle .html-filer i roden af repoet.
"""

IMG = "https://files.builder.nu/"

GALLERY = [
    "44/f6/44f6eadd-dd74-46eb-b04e-4d7d269febfa.jpeg",
    "9d/0f/9d0f6091-dd54-4890-9e78-d49cb04c59b7.jpg",
    "eb/46/eb4672d9-3af8-4203-9a34-efbc18b61299.jpg",
    "93/0d/930d0c79-296c-4cb5-bcdb-7b1212cf27c4.jpeg",
    "b2/96/b296d21a-e8f8-462e-bf03-5b02a35ce435.jpeg",
    "2d/5a/2d5a25a5-0b6b-40a7-a571-00ee9d164adc.jpeg",
    "f8/d2/f8d2b780-8956-4662-83cc-b6476fda48f0.jpg",
    "02/2a/022aa7ae-fde6-49b7-bb25-8fad8a94e6b2.jpeg",
    "7d/19/7d1916fe-75d4-4882-98d3-f418b0a8f8cd.jpeg",
    "d0/c6/d0c6e125-48be-429b-852b-1024bf56bb8f.jpeg",
    "76/4a/764a3d77-b620-495e-ba45-a3acea228e23.jpeg",
    "52/98/52983d9c-893f-406e-9650-df541af05fdb.jpeg",
    "70/42/70421df6-6dd6-4b09-8589-eb982ac9e0ec.jpg",
    "e1/93/e193ee2e-5b48-407f-9d37-0e55dca1e31f.JPEG",
    "56/3b/563baf8e-68bb-4c79-862e-d78d53045223.jpg",
    "a9/2a/a92a5fdf-2680-4395-bc5a-2803229b4a28.jpg",
    "55/84/5584f4f1-a9e2-4369-ab78-b753309e63bf.jpg",
    "15/52/15522dc6-89ff-4eac-b2a5-0afa122dcf99.jpg",
    "5b/11/5b11c42a-f64c-41e1-b76c-3253e3e781ef.jpg",
    "4a/5f/4a5f2f45-4d19-49c3-9780-baa02db65097.jpg",
    "81/36/8136a4ba-9faf-4007-9512-1935baa346f5.jpg",
    "b1/d4/b1d4080d-e0cb-474b-99c9-9942c20878aa.jpg",
    "e9/3c/e93c1958-742c-4902-827b-ab2730f15157.jpg",
    "4f/18/4f183484-955d-4c7f-b36b-bdc5306529be.jpg",
    "cf/3f/cf3fe08d-38c5-40c2-bf08-5daa99e08efc.jpg",
    "6a/6b/6a6bd8e1-e5bd-43b0-8731-d796920959f9.jpeg",
    "d4/87/d4879909-83ab-4b71-8b22-941717ac990b.jpeg",
    "c1/ea/c1eaf401-8c25-4eed-9595-1274b17b9980.jpeg",
    "97/6d/976d5f3d-98a4-4b82-a43e-199880ca915b.JPG",
    "b6/98/b69845fc-8347-4efc-bbcc-ce541a59d497.jpg",
    "bc/cc/bccc62e8-6130-407e-940f-cea2681f57f0.jpeg",
    "2f/1b/2f1b84a4-2390-417f-bad9-09b14584576a.jpeg",
]

LOGO_SVG = """<svg viewBox="0 0 420 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Nohrskov Fonden">
  <g fill="currentColor">
    <text x="0" y="58" font-family="Georgia, 'Times New Roman', serif" font-size="56" letter-spacing="4">N</text>
    <g transform="translate(66,36)">
      <circle cx="0" cy="0" r="21" fill="none" stroke="currentColor" stroke-width="4.5"/>
      <circle cx="-7" cy="-5" r="2.6"/>
      <circle cx="7" cy="-5" r="2.6"/>
      <path d="M -9 5 Q 0 13 9 5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
    </g>
    <text x="94" y="58" font-family="Georgia, 'Times New Roman', serif" font-size="56" letter-spacing="4">HRSK</text>
    <g transform="translate(310,36)">
      <circle cx="0" cy="0" r="21" fill="none" stroke="currentColor" stroke-width="4.5"/>
      <circle cx="-7" cy="-5" r="2.6"/>
      <circle cx="7" cy="-5" r="2.6"/>
      <path d="M -9 5 Q 0 13 9 5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
    </g>
    <text x="338" y="58" font-family="Georgia, 'Times New Roman', serif" font-size="56" letter-spacing="4">V</text>
    <line x1="10" y1="95" x2="130" y2="95" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
    <text x="210" y="106" text-anchor="middle" font-family="Caveat, cursive" font-size="52" font-weight="600">Fonden</text>
    <line x1="290" y1="95" x2="410" y2="95" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
  </g>
</svg>"""

WAVE_SVG = """<svg viewBox="0 0 1440 80" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><path d="M0,40 C240,80 480,0 720,30 C960,60 1200,10 1440,45 L1440,80 L0,80 Z" fill="#ffffff"/></svg>"""
WAVE_TINT = WAVE_SVG.replace("#ffffff", "#F4F9FD")

NAV = [
    ("Om fonden", None, [
        ("Historien bag", "om-fonden.html"),
        ("Holdet bag", "holdet-bag.html"),
        ("Ambassadører", "ambassadoerer.html"),
        ("Stemmer fra fællesskabet", "stemmer-fra-faellesskabet.html"),
        ("Kontakt", "kontakt.html"),
    ]),
    ("Ønskebrønden", None, [
        ("Om Ønskebrønden", "oenskebroenden.html"),
        ("Ansøg", "ansoeg.html"),
    ]),
    ("Events", "events.html", None),
    ("På hospitalerne", "paa-hospitalerne.html", None),
    ("Partnere", None, [
        ("Vores partnere", "partnere.html"),
        ("Bliv partner", "bliv-partner.html"),
    ]),
    ("Sådan kan du støtte", None, [
        ("Oversigt", "stoet.html"),
        ("Støt som privatperson", "stoet-som-privatperson.html"),
        ("Støt som virksomhed", "stoet-som-virksomhed.html"),
        ("Støt som fond", "stoet-som-fond.html"),
        ("Familiepanelet", "familiepanelet.html"),
    ]),
]

FB = "https://www.facebook.com/NohrskovFonden/"
LI = "https://www.linkedin.com/company/nohrskov-fonden/"

FB_ICON = '<svg viewBox="0 0 24 24"><path d="M13.5 21v-8h2.7l.4-3.2h-3.1V7.7c0-.9.3-1.5 1.6-1.5h1.6V3.3c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.4-4 4.1v2.5H7.5V13h2.8v8h3.2z"/></svg>'
LI_ICON = '<svg viewBox="0 0 24 24"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.2 8h4.6v14H.2V8zm7.4 0h4.4v1.9h.1c.6-1.2 2.1-2.4 4.4-2.4 4.7 0 5.5 3.1 5.5 7V22h-4.6v-6.6c0-1.6 0-3.6-2.2-3.6s-2.6 1.7-2.6 3.5V22H7.6V8z"/></svg>'


def nav_html(active):
    items = []
    for label, href, children in NAV:
        if children:
            links = "".join(f'<a href="{h}">{t}</a>' for t, h in children)
            items.append(
                f'<div class="nav-item"><button class="nav-link" type="button">{label}'
                f'<span class="caret"></span></button><div class="dropdown">{links}</div></div>'
            )
        else:
            items.append(f'<div class="nav-item"><a class="nav-link" href="{href}">{label}</a></div>')
    items.append('<a class="btn btn-primary header-cta" href="stoet.html">Støt nu</a>')
    return "".join(items)


def hero(h1, lead, actions="", sub=True, eyebrow=""):
    cls = "hero hero-sub" if sub else "hero"
    eb = f'<span class="eyebrow" style="color:#023351">{eyebrow}</span>' if eyebrow else ""
    act = f'<div class="hero-actions">{actions}</div>' if actions else ""
    return f"""<section class="{cls}">
  <div class="cloud cloud-1"></div><div class="cloud cloud-2"></div><div class="cloud cloud-3"></div>
  <div class="hero-inner">{eb}<h1>{h1}</h1><p class="lead">{lead}</p>{act}</div>
  <div class="wave">{WAVE_SVG}</div>
</section>"""


def page(slug, title, description, body, active=""):
    return f"""<!DOCTYPE html>
<html lang="da">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Nohrskov Fonden</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amatic+SC:wght@400;700&family=Caveat:wght@600&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Ccircle cx='24' cy='24' r='20' fill='none' stroke='%23023351' stroke-width='4'/%3E%3Ccircle cx='17' cy='19' r='2.5' fill='%23023351'/%3E%3Ccircle cx='31' cy='19' r='2.5' fill='%23023351'/%3E%3Cpath d='M15 28 Q24 36 33 28' fill='none' stroke='%23F46F25' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E">
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="logo" href="index.html" aria-label="Nohrskov Fonden - forside">{LOGO_SVG}</a>
    <nav class="nav">{nav_html(active)}</nav>
    <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="footer-wave">{WAVE_SVG}</div>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-logo" style="color:#fff">{LOGO_SVG}
        <p>Sammen om det der er større. Vi skaber nærvær, oplevelser, håb og retning for alvorligt syge børn og deres familier.</p>
      </div>
      <div>
        <h4>Fonden</h4>
        <a href="om-fonden.html">Historien bag</a>
        <a href="holdet-bag.html">Holdet bag</a>
        <a href="ambassadoerer.html">Ambassadører</a>
        <a href="stemmer-fra-faellesskabet.html">Stemmer fra fællesskabet</a>
        <a href="privatliv.html">Privatliv &amp; GDPR</a>
      </div>
      <div>
        <h4>Indsatser</h4>
        <a href="events.html">Events</a>
        <a href="paa-hospitalerne.html">På hospitalerne</a>
        <a href="oenskebroenden.html">Ønskebrønden</a>
        <a href="ansoeg.html">Ansøg Ønskebrønden</a>
      </div>
      <div>
        <h4>Støt os</h4>
        <a href="stoet.html">Sådan kan du støtte</a>
        <a href="bliv-partner.html">Bliv partner</a>
        <a href="mailto:info@nohrskovfonden.dk">info@nohrskovfonden.dk</a>
        <a href="stoet-som-privatperson.html">MobilePay #110754</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Nohrskov Fonden &middot; Stiftet 2023</span>
      <div class="socials">
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{FB_ICON}</a>
        <a href="{LI}" target="_blank" rel="noopener" aria-label="LinkedIn">{LI_ICON}</a>
      </div>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>"""


def img(i, alt=""):
    return f'<figure class="reveal"><img src="{IMG}{GALLERY[i]}" alt="{alt}" loading="lazy"></figure>'


def person(name, role=""):
    initials = "".join(w[0] for w in name.split()[:2]).upper()
    r = f"<span>{role}</span>" if role else ""
    return f'<div class="person reveal"><div class="avatar">{initials}</div><h4>{name}</h4>{r}</div>'


def cta(h, p, btn_text, btn_href):
    return f"""<section class="section"><div class="container">
  <div class="cta-banner reveal"><h2>{h}</h2><p>{p}</p>
  <a class="btn btn-primary" href="{btn_href}">{btn_text}</a></div>
</div></section>"""


# ================= PAGES =================

PAGES = {}

# ---------- Forside ----------
gallery_home = "".join(img(i) for i in range(12))
PAGES["index"] = {
    "title": "Sammen om det der er større",
    "desc": "Nohrskov Fonden samler familier, hospitaler, fonde, virksomheder og frivillige om at skabe nærvær, oplevelser, håb og retning for alvorligt syge børn og deres familier.",
    "body": hero(
        "Sammen om det <span class=\"squiggle\">der er større</span>",
        "Når alvorlig sygdom rammer et barn, rammer det hele familien. Vi skaber nærvær, oplevelser, håb og retning midt i det svære.",
        actions='<a class="btn btn-primary" href="stoet.html">Støt nu</a>'
                '<a class="btn btn-secondary" href="events.html">Se kommende events</a>',
        sub=False,
    ) + f"""
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Det gør vi</span>
      <h2 class="section-title">Tre indsatser, ét fælles formål</h2>
      <p class="lead">Gennem månedlige events, en landsdækkende hospitalsindsats og Ønskebrønden giver vi familierne små stykker tilbage af den lethed, glæde og tryghed, sygdommen ofte tager med sig.</p>
    </div>
    <div class="card-grid">
      <div class="card reveal">
        <div class="card-icon">&#127914;</div>
        <h3>Events</h3>
        <p>Oplev nærvær, fællesskab og små pauser fra sygdommen. Se vores kommende events og find et lyspunkt at glæde jer til.</p>
        <a class="btn btn-ghost" href="events.html">Se events</a>
      </div>
      <div class="card reveal">
        <div class="card-icon">&#127973;</div>
        <h3>På hospitalerne</h3>
        <p>Vi besøger børneafdelinger i hele landet med gaver, overraskelser og oplevelser, der fylder gangene med grin og glæde.</p>
        <a class="btn btn-ghost" href="paa-hospitalerne.html">Læs mere</a>
      </div>
      <div class="card reveal">
        <div class="card-icon">&#11088;</div>
        <h3>Ønskebrønden</h3>
        <p>To gange om året gør vi små og store drømme til virkelighed for børn og unge ramt af alvorlig sygdom. Måske er det din tur næste gang?</p>
        <a class="btn btn-ghost" href="ansoeg.html">Ansøg</a>
      </div>
    </div>
  </div>
</section>
<section class="quote-band">
  <div class="stars">&#9733; &#9733; &#9733; &#9733; &#9733;</div>
  <blockquote>“Alle skal have lov til en barndom, for nogle er det svært, men I gør det lidt nemmere – tak”</blockquote>
  <cite>&mdash; Ditte, mor til Alva</cite>
</section>
<section class="section tinted">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Hvorfor vi er her</span>
        <h2 class="section-title">Når mennesker står sammen, kan selv små øjeblikke gøre en verden til forskel</h2>
        <p class="lead" style="margin-top:1rem">Nohrskov Fonden samler familier, hospitaler, fonde, virksomheder, frivillige og privatpersoner i ét fælles formål: at skabe nærvær, oplevelser, håb og retning midt i det svære.</p>
        <p style="margin-top:1rem;color:var(--navy-soft)">Netop derfor står vi sammen, om det der er større.</p>
        <a class="btn btn-primary" href="om-fonden.html" style="margin-top:1.6rem">Historien bag fonden</a>
      </div>
      <div class="split-media reveal"><img src="{IMG}{GALLERY[3]}" alt="Glæde til et af fondens events" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Øjeblikke</span>
      <h2 class="section-title">Små pauser fra det svære</h2>
    </div>
    <div class="gallery">{gallery_home}</div>
  </div>
</section>
""" + cta("Vær med til at gøre en forskel",
          "Din støtte er med til at skabe håb, nærvær og lysglimt for alvorligt syge børn og deres familier – og der er flere måder, du kan være med på.",
          "Sådan kan du støtte", "stoet.html"),
}

# ---------- Historien bag ----------
PAGES["om-fonden"] = {
    "title": "Historien bag",
    "desc": "Nohrskov Fonden blev stiftet i 2023 med et dybfølt ønske om at skabe lys, håb og glæde for syge børn og deres familier.",
    "body": hero("Historien <span class=\"squiggle\">bag</span>",
                 "Nohrskov Fonden blev stiftet i 2023 med et dybfølt ønske om at skabe lys, håb og glæde for syge børn og deres familier.",
                 eyebrow="Om fonden") + f"""
<section class="section"><div class="container"><div class="prose reveal">
  <p>At være barn eller ung med alvorlig sygdom er en livsomstændighed, der rækker langt ud over diagnosen. Det påvirker hele familien og kan betyde færre fællesskaber, færre oplevelser og et savn af den lethed og glæde, som ellers kendetegner en barndom. Netop dér ønsker Nohrskov Fonden at gøre en forskel – med nærvær, fællesskab og oplevelser, der giver pauser fra det svære og skaber minder, der varer ved.</p>
</div></div></section>
<section class="quote-band">
  <blockquote>“I de øjeblikke mærker man, hvor meget små tegn på omsorg kan betyde”</blockquote>
  <cite>&mdash; Camilla Christoffersen, stifter</cite>
</section>
<section class="section"><div class="container"><div class="prose reveal">
  <p>Nohrskov Fonden udspringer af personlige erfaringer med livet tæt på sygdom. Som mor til en søn med en medfødt hjertefejl og senere en kræftdiagnose har stifter Camilla Christoffersen selv siddet ved hospitalssengen, hvor verden udenfor står stille, og hvor håb, frygt og ubetinget kærlighed fylder alt. I de øjeblikke mærker man, hvor meget små tegn på omsorg betyder. Man mærker også, hvor meget sygdom kan tage – spontane oplevelser, tryghed, overskud og følelsen af retning.</p>
  <p>Det blev begyndelsen på Nohrskov Fonden. Et ønske om at give familier midt i det svære et lille åndehul, et glimt af lys og følelsen af ikke at stå alene. Et ønske om at give noget tilbage af det, som sygdommen har taget.</p>
  <h2>Hvorfor Nohrskov?</h2>
  <p>Navnet Nohrskov rummer essensen af det, vi ønsker at være. Det er ikke blot et navn, det er vores værdigrundlag, vores løfte og vores hjerte.</p>
</div>
<div class="card-grid" style="max-width:980px;margin:40px auto 0">
  <div class="card card-tinted reveal"><h3>N &ndash; Nærvær</h3><p>Fordi det er i de stille øjeblikke sammen, at tryghed opstår, og hvor man mærker, at man ikke står alene.</p></div>
  <div class="card card-tinted reveal"><h3>O &ndash; Oplevelser</h3><p>Fordi små øjeblikke af glæde kan give ny energi, når hverdagen er tung, og skabe minder, der lyser længe efter.</p></div>
  <div class="card card-tinted reveal"><h3>H &ndash; Håb</h3><p>Fordi håbet er det, der bærer både børn og familier gennem det uvisse og giver styrke til at tage én dag ad gangen.</p></div>
  <div class="card card-tinted reveal"><h3>R &ndash; Retning</h3><p>Fordi vi ønsker at give noget at se frem til og en følelse af, at der stadig er lys på vejen.</p></div>
</div>
<div class="prose reveal" style="margin-top:48px">
  <p><strong>Skov</strong> symboliserer fællesskabet. Mange store, stærke træer står side om side, og under overfladen bindes de sammen af et solidt netværk af rødder, der giver styrke og stabilitet. De store, stærke træer er holdet bag Nohrskov Fonden – de mennesker, der står sammen om at gøre en forskel. De stærke rødder er vores samarbejdspartnere, som er med til at understøtte vores værdigrundlag og give os styrke til at vokse.</p>
  <h2>Vores indsats – tre ben, ét fælles formål</h2>
  <p><strong>Oplevelser og fællesskab.</strong> Vi afholder månedlige events, hvor børn og familier inviteres ind i fællesskaber fyldt med grin, nærvær og gode oplevelser. Her skabes rum for at være noget andet end “den syge” og for at være sammen med andre, der forstår.</p>
  <p><strong>Besøg på børneafdelinger.</strong> Vi besøger børneafdelinger på sygehuse rundt om i landet med gaver og små overraskelser. En håndsrækning, et smil og en påmindelse om, at nogen tænker på dem, også midt i indlæggelser og lange behandlingsforløb.</p>
  <p><strong>Ønskebrønden.</strong> Gennem Ønskebrønden opfylder vi personlige ønsker og drømme for børn og unge. Ønsker, der giver håb, motivation og noget at se frem til – og som ofte rækker langt ud over selve oplevelsen.</p>
  <h2>Et levende fællesskab i udvikling</h2>
  <p>I dag står Nohrskov Fonden på et stærkt fundament. Vi har engagerede protektorer, et dedikeret ambassadørhold, frivillige med hjertet på rette sted og et voksende fællesskab af Nohrskovens Venner, der alle bidrager til at gøre vores arbejde muligt.</p>
  <p>Vi er vokset hurtigt, men altid med hjertevarmen, nærværet og mennesket i centrum. Nohrskov Fonden er mere end en organisation – det er et fællesskab bygget på erfaring, omsorg og ønsket om at gøre en reel forskel. Én oplevelse, ét ønske og ét smil ad gangen.</p>
</div></div></section>
""" + cta("Vil du være en del af fællesskabet?", "Mød menneskene bag fonden, eller se hvordan du selv kan bidrage.", "Mød holdet bag", "holdet-bag.html"),
}

# ---------- Holdet bag ----------
def people_section(title, names):
    grid = "".join(person(n, r) for n, r in names)
    return f"""<section class="section"><div class="container">
  <h2 class="section-title reveal" style="text-align:center;margin-bottom:40px">{title}</h2>
  <div class="people-grid">{grid}</div>
</div></section>"""

PAGES["holdet-bag"] = {
    "title": "Holdet bag",
    "desc": "Mød sekretariatet, protektorerne, advisory boardet, de frivillige og Nohrskovens Venner.",
    "body": hero("Holdet <span class=\"squiggle\">bag</span>",
                 "Bag Nohrskov Fonden står et hold af dedikerede mennesker, der hver dag arbejder for at skabe lys og glæde for syge børn og deres familier.",
                 eyebrow="Organisationen")
    + people_section("Sekretariatet", [
        ("Camilla Christoffersen", "Stifter"), ("Chris Christoffersen", ""), ("Trine Skriver", "Projektleder, hospitalsindsatsen"),
        ("Jane Ditmer", ""), ("Marianne Ivarsen", ""), ("Louise Rasmussen", "")])
    + """<section class="section tinted"><div class="container">
  <h2 class="section-title reveal" style="text-align:center;margin-bottom:40px">Protektorer</h2>
  <div class="people-grid" style="max-width:700px;margin:0 auto">"""
    + person("Renée Toft Simonsen", "Protektor") + person("Claus Hommelhoff", "Protektor") + person("Ny protektor på vej", "")
    + """</div></div></section>"""
    + people_section("Advisory Board", [
        ("Frank Høedt", ""), ("Flemming Dybbøl", ""), ("Andreas Steenholt", ""),
        ("Rasmus Munch", ""), ("Julie Østergaard", ""), ("Steen R. Søndergaard", "")])
    + """<section class="section tinted"><div class="container">
  <h2 class="section-title reveal" style="text-align:center;margin-bottom:40px">Frivilligteamet</h2>
  <div class="people-grid">"""
    + "".join(person(n) for n in ["Mattias Bak Faccini","Maja Dochweiler","Carolina Brask","Noah Dam","Trine Vinther","Marica Thingvad","Sally Busch","Zofiia Rose","Jacob Christensen","Nis Marcussen","Nadja Jørgensen","Tine Beck","Anna-Gry Bygdin","Mette Christensen","Thomas Christensen","Laura Bramstorp"])
    + person("Her er plads til dig", "Bliv frivillig") + person("..og dig!", "Bliv frivillig")
    + """</div></div></section>
<section class="section"><div class="container">
  <div class="section-head reveal">
    <span class="eyebrow">Fællesskab</span>
    <h2 class="section-title">Nohrskovens Venner</h2>
    <p class="lead">Nohrskovens Venner er et varmt fællesskab af mennesker, der med deres nærvær, engagement og rækkevidde hjælper med at sprede budskabet om Nohrskov Fonden og gøre en forskel for familier i svære perioder.</p>
  </div>
  <div class="people-grid" style="max-width:900px;margin:0 auto">"""
    + "".join(person(n) for n in ["Sofie Bregnhøj Suhr","Rasmus Lund-Sørensen","Stine Petersen","Sandra Sommer"])
    + person("Ny ven på vej", "") + person("Ny ven på vej", "")
    + "</div></div></section>"
    + cta("Vil du med på holdet?", "Vi er altid klar på at byde nye frivillige velkommen. Kontakt os for en snak.", "Kontakt os", "kontakt.html"),
}

# ---------- Ambassadører ----------
PAGES["ambassadoerer"] = {
    "title": "Ambassadører",
    "desc": "Nohrskov Fondens ambassadørhold hjælper med at sprede kendskabet og åbne dørene for magiske øjeblikke.",
    "body": hero("<span class=\"squiggle\">Ambassadører</span>",
                 "Engagerede og passionerede mennesker, som hvert år vælger at bruge deres tid, erfaring, synlighed og hjertevarme på at hjælpe os med at sprede kendskabet og åbne dørene for magiske øjeblikke til vores familier.",
                 eyebrow="Om fonden")
    + """<section class="section"><div class="container"><div class="people-grid">"""
    + "".join(person(n) for n in ["Wafande","Ane Høgsberg","Albert Harson","Malene Qvist","Rune Klan","Zelma Lewerissa","Anne Grethe Bjarup Riis","Rune Viborg","Marie Holm","Manu Sareen","Johanne Louise Schmidt","Mattias Hundebøll","Jim Lyngvild","Merete Mærkedahl","Sandra Meinich Juhl","Katrine Bille","Michael Hausted"])
    + person("Ny ambassadør på vej", "")
    + "</div></div></section>"
    + cta("Kunne du tænke dig at blive ambassadør?", "Ræk ud, hvis du vil bruge din stemme til at gøre en forskel for syge børn og deres familier.", "Kontakt os", "kontakt.html"),
}

# ---------- Stemmer fra fællesskabet ----------
PAGES["stemmer-fra-faellesskabet"] = {
    "title": "Stemmer fra fællesskabet",
    "desc": "Familier, sundhedspersonale, frivillige og partnere deler deres oplevelser med Nohrskov Fonden.",
    "body": hero("Stemmer fra <span class=\"squiggle\">fællesskabet</span>",
                 "Hver dag møder vi familier, børn, unge, sundhedspersonale, frivillige og samarbejdspartnere, som deler deres oplevelser med Nohrskov Fonden. Deres ord fortæller bedst, hvad nærvær, oplevelser, håb og retning kan betyde, når livet er allersværest.",
                 eyebrow="Om fonden") + f"""
<section class="quote-band">
  <div class="stars">&#9733; &#9733; &#9733; &#9733; &#9733;</div>
  <blockquote>“Alle skal have lov til en barndom, for nogle er det svært, men I gør det lidt nemmere – tak”</blockquote>
  <cite>&mdash; Ditte, mor til Alva</cite>
</section>
<section class="section"><div class="container">
  <div class="section-head reveal"><h2 class="section-title">Familierne</h2></div>
  <div class="card-grid">
    <div class="card reveal"><p class="script" style="font-size:1.5rem">“Citat fra en familie kommer her”</p><p style="margin-top:12px;font-weight:800">&mdash; Navn, relation</p></div>
    <div class="card reveal"><p class="script" style="font-size:1.5rem">“Citat fra en familie kommer her”</p><p style="margin-top:12px;font-weight:800">&mdash; Navn, relation</p></div>
    <div class="card reveal"><p class="script" style="font-size:1.5rem">“Citat fra en familie kommer her”</p><p style="margin-top:12px;font-weight:800">&mdash; Navn, relation</p></div>
  </div>
</div></section>
<section class="section tinted"><div class="container">
  <div class="section-head reveal"><h2 class="section-title">Hospitalerne</h2></div>
  <div class="card-grid" style="max-width:800px;margin:0 auto">
    <div class="card reveal"><p class="script" style="font-size:1.5rem">“Citat fra sundhedspersonale kommer her”</p><p style="margin-top:12px;font-weight:800">&mdash; Navn, afdeling</p></div>
    <div class="card reveal"><p class="script" style="font-size:1.5rem">“Citat fra sundhedspersonale kommer her”</p><p style="margin-top:12px;font-weight:800">&mdash; Navn, afdeling</p></div>
  </div>
</div></section>
<section class="section"><div class="container">
  <div class="section-head reveal"><h2 class="section-title">Partnere</h2></div>
  <div class="card-grid" style="max-width:800px;margin:0 auto">
    <div class="card reveal"><p class="script" style="font-size:1.4rem">“Nohrskov Fonden skaber håb, nærvær og små åndehuller for alvorligt syge børn og deres familier i en hverdag præget af bekymringer og usikkerhed. Det er en indsats, der rummer både menneskelighed, omsorg og fællesskab.”</p><p style="margin-top:12px;font-weight:800">&mdash; Lone Hejlskov, Fondskoordinator, Sol &amp; Strand</p></div>
  </div>
</div></section>
""" + cta("Har du en historie at dele?", "Vi vil elske at høre, hvad Nohrskov Fonden har betydet for jer.", "Skriv til os", "kontakt.html"),
}

# ---------- Kontakt ----------
PAGES["kontakt"] = {
    "title": "Kontakt",
    "desc": "Kontakt Nohrskov Fonden på info@nohrskovfonden.dk.",
    "body": hero("Kontakt <span class=\"squiggle\">os</span>",
                 "Har du spørgsmål, idéer eller lyst til at være med? Vi hører gerne fra dig.",
                 eyebrow="Om fonden") + f"""
<section class="section"><div class="container">
  <div class="card-grid" style="max-width:980px;margin:0 auto">
    <div class="card reveal">
      <div class="card-icon">&#9993;</div>
      <h3>Skriv til os</h3>
      <p>Vi svarer hurtigst muligt på alle henvendelser.</p>
      <a class="btn btn-primary" href="mailto:info@nohrskovfonden.dk">info@nohrskovfonden.dk</a>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#128153;</div>
      <h3>Støt fonden</h3>
      <p>Støt med et valgfrit beløb via MobilePay #110754 – eller se de andre måder, du kan bidrage på.</p>
      <a class="btn btn-ghost" href="stoet.html">Sådan kan du støtte</a>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#128075;</div>
      <h3>Følg med</h3>
      <p>Følg vores arbejde, events og øjeblikke på de sociale medier.</p>
      <a class="btn btn-ghost" href="{FB}" target="_blank" rel="noopener">Facebook</a>
    </div>
  </div>
</div></section>
""",
}

# ---------- Privatliv ----------
PAGES["privatliv"] = {
    "title": "Privatliv & GDPR",
    "desc": "Sådan behandler Nohrskov Fonden dine personoplysninger.",
    "body": hero("Privatliv <span class=\"squiggle\">&amp; GDPR</span>",
                 "Hos Nohrskov Fonden passer vi godt på dine oplysninger.", eyebrow="Opdateret 18.05.2026") + """
<section class="section"><div class="container"><div class="prose reveal">
  <p>Når du søger om at deltage i et event eller få opfyldt et ønske gennem Ønskebrønden, behandler vi nogle personlige oplysninger om dig og/eller dit barn. Vi gør det kun for at kunne behandle ansøgningen og for at kunne gennemføre selve ønsket. Vi videresælger aldrig oplysninger til tredjepart og deler dem kun med de parter, der er nødvendige for at gøre ønsket muligt – og altid i overensstemmelse med denne privatlivspolitik.</p>
  <h2>Hvem er dataansvarlig?</h2>
  <p>Nohrskov Fonden er dataansvarlig for de personoplysninger, vi modtager. Det betyder, at vi har ansvar for, at dine oplysninger bliver behandlet sikkert og i overensstemmelse med lovgivningen. Du kan kontakte os på <a href="mailto:info@nohrskovfonden.dk">info@nohrskovfonden.dk</a>.</p>
  <h2>Hvad bruger vi oplysningerne til?</h2>
  <p>Vi indsamler og behandler kun de oplysninger, der er nødvendige for:</p>
  <ul>
    <li>At behandle ansøgninger til events</li>
    <li>At behandle ansøgninger til Ønskebrønden</li>
    <li>At kunne opfylde ønsket (fx koordinere oplevelser, bestille udstyr eller lignende)</li>
    <li>At kommunikere med dig om ansøgningen</li>
    <li>At sikre dokumentation i forhold til sygdom og relation til barnet</li>
  </ul>
  <h2>Hvilke oplysninger behandler vi?</h2>
  <ul>
    <li>Almindelige kontaktoplysninger (navn, adresse, e-mail, telefonnummer)</li>
    <li>Oplysninger om barnets sygdom (nødvendig dokumentation i forbindelse med ønsket)</li>
    <li>Relation til barnet (fx forælder, værge eller anden pårørende)</li>
    <li>Selve ønsket</li>
  </ul>
  <p>Vi behandler ikke oplysninger offentligt uden samtykke. Billeder eller videoer bruges kun, hvis du har givet os lov.</p>
  <h2>Deling af oplysninger</h2>
  <p>Vi deler kun oplysninger med Nohrskov Fondens bestyrelse (til behandling af ansøgningen) og vores samarbejdspartnere, når det er nødvendigt for at opfylde et ønske (fx rejsebureau, butik eller eventarrangør). Der laves altid databehandleraftaler, hvor det er relevant.</p>
  <h2>Hvor længe gemmer vi oplysningerne?</h2>
  <p>Vi opbevarer oplysninger så længe, det er nødvendigt i forhold til ansøgningen og opfyldelsen af ønsket – og i op til fem år derefter af praktiske og administrative hensyn.</p>
  <h2>Dine rettigheder</h2>
  <ul>
    <li>Ret til indsigt – du kan få at vide, hvilke oplysninger vi har om dig</li>
    <li>Ret til rettelse – du kan få rettet forkerte oplysninger</li>
    <li>Ret til sletning – i særlige tilfælde kan du få slettet oplysninger</li>
    <li>Ret til begrænsning – du kan i visse tilfælde få begrænset vores behandling</li>
    <li>Ret til indsigelse – du kan gøre indsigelse mod, at vi behandler dine oplysninger</li>
    <li>Ret til dataportabilitet – du kan i visse tilfælde få dine oplysninger udleveret</li>
  </ul>
  <p>Hvis du vil bruge dine rettigheder, kan du kontakte os. Du kan også læse mere på <a href="https://www.datatilsynet.dk/" target="_blank" rel="noopener">www.datatilsynet.dk</a>, hvor du desuden kan klage, hvis du mener, vi ikke håndterer dine oplysninger korrekt.</p>
  <h2>Ændringer</h2>
  <p>Vi opdaterer denne privatlivspolitik, hvis der sker ændringer i, hvordan vi behandler personoplysninger. Øverst kan du altid se, hvornår den sidst er opdateret.</p>
</div></div></section>
""",
}

# ---------- Om Ønskebrønden ----------
PAGES["oenskebroenden"] = {
    "title": "Om Ønskebrønden",
    "desc": "Ønskebrønden gør drømme til virkelighed for børn og unge i svære livssituationer.",
    "body": hero("Om <span class=\"squiggle\">Ønskebrønden</span>",
                 "Når omsorg bliver til virkelighed. Vi skaber øjeblikke, hvor sygdom, bekymringer og begrænsninger træder i baggrunden – og hvor glæde, håb og nærvær får plads.",
                 actions='<a class="btn btn-primary" href="ansoeg.html">Ansøg Ønskebrønden</a>',
                 eyebrow="Ønskebrønden") + f"""
<section class="section"><div class="container"><div class="prose reveal">
  <p>I Ønskebrønden arbejder vi for at gøre en reel forskel for børn og unge i svære livssituationer. For os handler det ikke blot om at opfylde ønsker – det handler om at skabe øjeblikke, hvor sygdom, bekymringer og begrænsninger træder i baggrunden, og hvor glæde, håb og nærvær får plads.</p>
  <h2>Små ønsker – stor betydning</h2>
  <p>I 2025 har Ønskebrønden skabt øjeblikke, hvor børn og unge for en stund kunne slippe sygdom og bekymringer – og bare være børn. For nogle begyndte det med en drøm om at komme ud i naturen og mærke friheden på ryggen af en hest. For andre var det mødet med et idol, hvor nervøsitet blev til grin, stjernestøv og et minde, der vil blive fortalt igen og igen.</p>
  <p>Vi har set, hvordan en ny computer kan åbne verden igen for en ung, der ellers føler sig sat på sidelinjen – og hvordan noget så grundlæggende som en elevationsseng kan give ro, bedre søvn og mere overskud i hverdagen. Vi har fyldt stuer og hospitalsstuer med legetøj, merchandise og overraskelser, der skabte smil og leg, dér hvor alvoren ellers fylder mest.</p>
  <p>Og så har vi skabt oplevelser, der rækker langt ud over øjeblikket. Som når et barn får lov at træde ind i rampelyset og opleve magien ved Vild med dans – ikke som patient, men som deltager, gæst og barn med lys i øjnene.</p>
  <p>Fælles for alle ønskerne er ikke størrelsen eller værdien i kroner og øre, men den følelse de efterlader: følelsen af at blive set, holdt af og husket.</p>
</div></div></section>
<section class="section tinted"><div class="container">
  <div class="split">
    <div class="reveal">
      <span class="eyebrow">Samarbejde</span>
      <h2 class="section-title">Tæt samarbejde med sundhedsvæsenet</h2>
      <p class="lead" style="margin-top:1rem">Vi har styrket vores samarbejde med børneafdelingerne på AUH, OUH og Rigshospitalet, hvor Ønskebrønden nu to gange årligt deler gaver ud direkte til indlagte børn.</p>
      <p style="margin-top:1rem;color:var(--navy-soft)">Her oplever vi, hvordan selv små overraskelser kan forandre en hospitalsdag og bringe glæde ind i et rum, der ellers kan være præget af alvor.</p>
    </div>
    <div class="split-media reveal"><img src="{IMG}{GALLERY[8]}" alt="Gaver til indlagte børn" loading="lazy"></div>
  </div>
</div></section>
<section class="section"><div class="container"><div class="prose reveal">
  <h2>Sammen gør vi mere muligt</h2>
  <p>Intet af dette kunne lade sig gøre uden vores samarbejdspartnere. Vi har indgået et værdifuldt samarbejde med CoolUnite samt en lang række engagerede virksomheder og mennesker, som med deres støtte, produkter og ressourcer er med til at gøre ønskerne mulige.</p>
  <p>For vores samarbejdspartnere og investorer er Ønskebrønden et konkret bevis på, at social ansvarlighed kan omsættes til reel, mærkbar værdi – for rigtige børn, rigtige familier og rigtige liv.</p>
  <h2>Derfor findes Ønskebrønden</h2>
  <p>Ønskebrønden findes, fordi børn i svære livssituationer har brug for mere end behandling og støtte. De har brug for håb, glæde og øjeblikke, hvor de bare får lov til at være børn. Hvert opfyldt ønske er et bevis på, at omsorg virker – og at fællesskab kan skabe lys, selv når livet er allermest udfordrende.</p>
  <p>Tak til alle, der har været med til at gøre 2025 til endnu et år fyldt med smil, varme og drømme, der blev til virkelighed. Vi glæder os til, at Ønskebrønden åbner endnu en runde i maj og november 2026.</p>
</div></div></section>
""" + cta("Har dit barn et ønske?", "Ønskebrønden åbner for ansøgninger i maj og november. Måske er det jeres tur næste gang.", "Sådan ansøger du", "ansoeg.html"),
}

# ---------- Ansøg ----------
PAGES["ansoeg"] = {
    "title": "Ansøg Ønskebrønden",
    "desc": "Søg om at få opfyldt et ønske gennem Ønskebrønden. Der kan søges i maj og november.",
    "body": hero("Ansøg <span class=\"squiggle\">Ønskebrønden</span>",
                 "Gennem Ønskebrønden gør vi drømme til virkelighed for børn og unge i svære livssituationer. Hvert opfyldt ønske skaber et øjeblik fyldt med glæde, tryghed og nærvær.",
                 eyebrow="Ønskebrønden") + """
<section class="section"><div class="container">
  <div class="section-head reveal">
    <span class="eyebrow">Ansøgningsperioder</span>
    <h2 class="section-title">Der kan søges i maj og november</h2>
  </div>
  <div class="card-grid" style="max-width:760px;margin:0 auto">
    <div class="card reveal" style="text-align:center">
      <h3 style="margin:0 auto">Forårsrunden</h3>
      <p class="display" style="font-size:2.6rem;color:var(--navy)">1. maj &ndash; 30. maj</p>
    </div>
    <div class="card reveal" style="text-align:center">
      <h3 style="margin:0 auto">Efterårsrunden</h3>
      <p class="display" style="font-size:2.6rem;color:var(--navy)">1. nov &ndash; 14. nov</p>
    </div>
  </div>
</div></section>
<section class="section tinted"><div class="container">
  <div class="section-head reveal">
    <h2 class="section-title">Hvad sker der, når ansøgningen er sendt?</h2>
  </div>
  <div class="steps">
    <div class="step reveal"><div class="step-num">1</div><div>
      <h3>Vi modtager din ansøgning</h3>
      <p>Vi modtager hvert år mange ansøgninger og sender derfor ikke en automatisk kvittering. Vi beder om tålmodighed i behandlingsperioden.</p>
    </div></div>
    <div class="step reveal"><div class="step-num">2</div><div>
      <h3>Besked inden for én måned</h3>
      <p>Senest én måned efter ansøgningsfristens udløb får alle ansøgere besked om, hvorvidt deres ansøgning går videre til næste vurderingsrunde.</p>
    </div></div>
    <div class="step reveal"><div class="step-num">3</div><div>
      <h3>Grundig vurdering</h3>
      <p>Går ansøgningen videre, påbegynder vi en grundig vurdering af mulighederne. Processen kan tage op til fire måneder, da vi ofte skal undersøge finansiering, samarbejdsmuligheder og praktiske rammer.</p>
    </div></div>
    <div class="step reveal"><div class="step-num">4</div><div>
      <h3>Endeligt svar</h3>
      <p>Når vurderingen er afsluttet, giver vi besked til alle familier, hvis ansøgninger er gået videre – uanset om ønsket kan imødekommes eller ej.</p>
    </div></div>
  </div>
  <p class="lead reveal" style="text-align:center;max-width:640px;margin:32px auto 0">Vi ved, at ventetid kan være svær, særligt når man håber på noget vigtigt. Derfor gør vi vores bedste for at behandle alle ansøgninger med den omsorg og grundighed, de fortjener.</p>
</div></section>
<section class="section"><div class="container">
  <div class="section-head reveal"><h2 class="section-title">Godt at vide, før du søger</h2></div>
  <div class="accordion reveal">
    <details>
      <summary>Prioriteringskriterier</summary>
      <p>Ved vurdering af ansøgninger lægger vi vægt på, at barnet er væsentligt påvirket i sin dagligdag og har særlige støttebehov, som ikke allerede dækkes af offentlige tilbud. Det kan for eksempel være børn, som har begrænsede muligheder for deltagelse i skole, fritid eller sociale fællesskaber. Ønsket skal kunne skabe en mærkbar forbedring i barnets trivsel, tryghed eller livskvalitet. Ved prioritering kan der lægges særlig vægt på børn med komplekse udfordringer eller omfattende støttebehov samt på familier, som har begrænsede muligheder for selv at opfylde ønsket.</p>
    </details>
    <details>
      <summary>Hvilke ønsker kan vi opfylde?</summary>
      <p>Ønsket skal gå direkte til barnet og understøtte barnets trivsel, udvikling eller livskvalitet. Det skal være konkret og realistisk at gennemføre, og oplevelsesønsker skal finde sted i Danmark.</p>
    </details>
    <details>
      <summary>Hvad støtter vi ikke?</summary>
      <p>Vi støtter ikke rejser til udlandet, computere, mobiler eller tablets, økonomisk støtte, løbende driftsudgifter eller ønsker, som ikke går direkte til barnet.</p>
    </details>
    <details>
      <summary>Hvad skal ansøgningen indeholde?</summary>
      <p>Ansøgningen skal indeholde en kort beskrivelse af barnet og hvordan barnets situation påvirker hverdagen. Oplysninger om barnet og om hvem, der søger på vegne af barnet, skal også medtages. Ansøgningen kan indsendes af forældre, værger eller en fagperson. Derudover skal ønsket beskrives præcist og tydeligt, med forklaring på, hvorfor det er vigtigt for barnet. Et prisoverslag skal vedhæftes, og det er en fordel at inkludere et link til det ønskede, hvis det er muligt.</p>
    </details>
  </div>
</div></section>
""" + cta("Klar til at ansøge?", "Send din ansøgning i ansøgningsperioden – vi behandler den med omsorg og grundighed.", "Kontakt os om ansøgning", "mailto:info@nohrskovfonden.dk"),
}

# ---------- Events ----------
def event(day, month, title, meta, desc, link=None):
    l = f'<a class="btn btn-ghost" href="{link}" target="_blank" rel="noopener">Læs mere</a>' if link else ""
    return f"""<div class="event reveal">
  <div class="event-date"><div class="d">{day}</div><div class="m">{month}</div></div>
  <div><h3>{title}</h3><div class="meta">{meta}</div><p>{desc}</p></div>
  {l}
</div>"""

PAGES["events"] = {
    "title": "Kommende events",
    "desc": "Se Nohrskov Fondens kommende events for familier med sygdomsramte børn.",
    "body": hero("Kommende <span class=\"squiggle\">events</span>",
                 "Her finder I vores kommende events, som familier med sygdomsramte børn kan ansøge om at deltage i.",
                 eyebrow="Events") + """
<section class="section"><div class="container">
  <div class="info-box reveal" style="max-width:860px;margin:0 auto 48px">
    <strong>Sådan ansøger I</strong>
    Der er ofte stor interesse for arrangementerne, og en ansøgning er derfor ikke ensbetydende med en plads. Vi giver besked hurtigst muligt, når pladserne er fordelt. Når I ansøger, beder vi jer oplyse barnets navn og alder, barnets sygdom eller diagnose, adresse, telefonnummer samt hvor mange familiemedlemmer der ønsker at deltage.
  </div>
  <div class="event-list">
""" + event("23", "Juni", "Cirkus Summarum, Ballerup", "Tirsdag d. 23. juni kl. 17.00",
            "Glæd jer til at opleve Motor Mille, Hr. Skæg, Kristian, Sælma og Onkel Reje til forpremieren i Cirkus Summarum. Skuespiller Pelle Emil Rex Hebsgaard vender også tilbage til cirkusmanegen, denne gang som cirkusdirektør. Det bliver magisk, vildt og virkelig sjovt!")
    + event("&mdash;", "Dato kommer", "Leos Legeland, Aarhus", "Dato kommer",
            "Kom med til fri leg fra kl. 11.00 til så længe I orker (lukker kl. 19.00) og hygge i Leo's Legeland i Aarhus. Glæd jer til en dag fyldt med grin, leg og gode oplevelser sammen.")
    + event("&mdash;", "Juni", "AGF Meet'n Greet", "Juni 2026 – dato kommer snart",
            "Glæd jer til at møde alle MESTRENE fra AGF!")
    + event("&mdash;", "Juni", "AGF Hjemmekamp", "Juni 2026 – dato kommer snart",
            "Vi tager 25 børn og deres familier afsted – det bliver fedt!")
    + event("21", "Juli", "Cirkus Summarum, Aarhus", "Tirsdag d. 21. juli kl. 15.30",
            "Magisk cirkusoplevelse for hele familien i Aarhus.")
    + event("16", "Aug", "Rundvisning på Aros", "Søndag d. 16. august kl. 9.30",
            "Glæd jer til en hyggelig rundvisning med fokus på det nye Turell-værk \"The Dome\". Derefter er der krea-aktiviteter, som I kan opleve på egen hånd.")
    + event("18", "Aug", "Sportscar event, Sjællandsringen", "Tirsdag d. 18. august",
            "Sammen med Sportscar inviterer vi børn med alvorlig sygdom og deres forældre til nogle fantastiske timer med frokost, fart, grin og gode oplevelser. Hvert barn kan medbringe én forælder.",
            "https://sportscarevent.dk/#Kommende-events")
    + event("22", "Aug", "Rockbæk", "Lørdag d. 22. august",
            "Rockbæk Arena forvandles endnu en gang til en magisk musikscene under åben himmel. Her inviteres forældre til en uforglemmelig smuk sensommerdag med nogle af Danmarks største musiknavne, når bl.a. The Minds of 99 og Medina indtager scenen.")
    + event("8", "Sep", "Sportscar event, Jyllandsringen", "Tirsdag d. 8. september",
            "Fart, frokost, grin og gode oplevelser sammen med Sportscar – hvert barn kan medbringe én forælder.",
            "https://sportscarevent.dk/#Kommende-events")
    + event("26", "Sep", "Den Blå Planet", "Lørdag d. 26. september kl. 13.00",
            "Glæd jer til en dag fyldt med spændende oplevelser, fascinerende havdyr, hyggeligt samvær og et pusterum fra hverdagen, hvor vi skaber gode minder sammen.")
    + event("3", "Okt", "Gangster Granny, Kulturhuset Skanderborg", "Lørdag d. 3. oktober",
            "Kom med i biografen – vi har den helt for os selv!")
    + event("&mdash;", "Dato kommer", "Racehall, Aarhus &amp; København", "Datoer kommer",
            "Glæd jer til, at vi inden længe kan invitere en masse børn og unge med til Racehall i Aarhus og i København.") + """
  </div>
</div></section>
""" + cta("Vil du gøre et event muligt?", "Vores events bliver til i samarbejde med virksomheder og partnere, der åbner dørene for vores familier.", "Bliv partner", "bliv-partner.html"),
}

# ---------- På hospitalerne ----------
PAGES["paa-hospitalerne"] = {
    "title": "På hospitalerne",
    "desc": "Nohrskov Fondens landsdækkende hospitalsindsats bringer gaver, forkælelse og oplevelser til børneafdelingerne.",
    "body": hero("På <span class=\"squiggle\">hospitalerne</span>",
                 "Vi besøger børneafdelinger i hele landet med gaver, overraskelser og oplevelser, der fylder gangene med musik, grin og glæde.",
                 eyebrow="Hospitalsindsatsen") + f"""
<section class="section"><div class="container">
  <div class="card-grid">
    <div class="card reveal">
      <div class="card-icon">&#127873;</div>
      <h3>Gaver til børneafdelingerne</h3>
      <p>Nye legesager og kreative aktiviteter til børneafdelingerne, som inviterer til leg, fantasi og små pauser fra hospitalsrutinerne.</p>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#9749;</div>
      <h3>Forkælelse til forældrene</h3>
      <p>En kærlig og anerkendende boost til dem, der står ved siden af deres barn døgnet rundt, ofte med søvnløse nætter, bekymringer og svære beslutninger.</p>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#127950;</div>
      <h3>Oplevelser</h3>
      <p>Gaverne ankommer i nogle af landets fedeste racerbiler, og børnene får lov at komme med på en tur og mærke fart, frihed og sus i maven. Andre gange er det minikoncerter eller besøg af et idol, der fylder gangene og hjerterne med musik, grin og glæde.</p>
    </div>
  </div>
</div></section>
<section class="section tinted"><div class="container">
  <div class="split">
    <div class="split-media reveal"><img src="{IMG}{GALLERY[10]}" alt="Hospitalsbesøg" loading="lazy"></div>
    <div class="reveal">
      <span class="eyebrow">Kontakt</span>
      <h2 class="section-title">Trine, projektleder for hospitalsindsatsen</h2>
      <p class="lead" style="margin-top:1rem">Har din afdeling lyst til besøg, eller vil du høre mere om indsatsen? Ræk ud.</p>
      <a class="btn btn-primary" href="mailto:info@nohrskovfonden.dk" style="margin-top:1.4rem">Kontakt Trine</a>
    </div>
  </div>
</div></section>
""" + cta("Vær med til at sprede glæde på gangene", "Produkter, oplevelser og økonomisk støtte gør hospitalsindsatsen mulig.", "Støt indsatsen", "stoet.html"),
}

# ---------- Partnere ----------
PAGES["partnere"] = {
    "title": "Partnere",
    "desc": "Mød de partnere, der gør Nohrskov Fondens arbejde muligt.",
    "body": hero("Vores <span class=\"squiggle\">partnere</span>",
                 "Uden vores partnere var der ingen events, ingen hospitalsindsats og ingen Ønskebrønd. Tak, fordi I står sammen med os om det, der er større.",
                 eyebrow="Partnere") + """
<section class="section"><div class="container">
  <h2 class="tier-title reveal" style="color:var(--navy)">Hovedpartnere</h2>
  <div class="logo-grid" style="max-width:760px;margin:0 auto">
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
  </div>
  <h2 class="tier-title gold reveal">Guldpartnere</h2>
  <div class="logo-grid" style="max-width:900px;margin:0 auto">
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
  </div>
</div></section>
<section class="quote-band">
  <blockquote>“Nohrskov Fonden skaber håb, nærvær og små åndehuller for alvorligt syge børn og deres familier. Det er en indsats, der rummer både menneskelighed, omsorg og fællesskab.”</blockquote>
  <cite>&mdash; Lone Hejlskov, Fondskoordinator, Sol &amp; Strand</cite>
</section>
<section class="section"><div class="container">
  <h2 class="tier-title silver reveal">Sølvpartnere</h2>
  <div class="logo-grid">
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
  </div>
  <h2 class="tier-title bronze reveal">Bronzepartnere</h2>
  <div class="logo-grid">
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
    <div class="logo-tile reveal">Partnerlogo</div>
  </div>
</div></section>
""" + cta("Skal jeres logo stå her?", "Kombiner sociale værdier med forretning og styrk jeres CSR- og ESG-strategi på en måde, der gør en reel forskel.", "Bliv partner", "bliv-partner.html"),
}

# ---------- Bliv partner ----------
PAGES["bliv-partner"] = {
    "title": "Bliv partner",
    "desc": "Indgå et partnerskab med Nohrskov Fonden og skab håndgribelige øjeblikke af glæde og håb.",
    "body": hero("Bliv <span class=\"squiggle\">partner</span>",
                 "Et samarbejde med Nohrskov Fonden er mere end et partnerskab – det er en mulighed for at være med til at skabe håndgribelige øjeblikke af glæde og håb for børn ramt af sygdom og deres familier.",
                 actions='<a class="btn btn-primary" href="mailto:info@nohrskovfonden.dk">Kontakt os om partnerskab</a>',
                 eyebrow="Partnere") + """
<section class="section"><div class="container">
  <div class="split">
    <div class="reveal">
      <span class="eyebrow">Værdi for jer</span>
      <h2 class="section-title">CSR og ESG med mærkbar effekt</h2>
      <p class="lead" style="margin-top:1rem">Gennem partnerskaber, sponsorater eller samarbejdsaftaler kan din virksomhed eller organisation kombinere sociale værdier med forretning – og samtidig styrke jeres CSR- og ESG-strategi på en måde, der gør en reel forskel.</p>
      <p style="margin-top:1rem;color:var(--navy-soft)">Sammen skaber vi små pusterum, hvor bekymringerne kan fylde lidt mindre, og hvor glæde, mod og drømme får plads til at vokse.</p>
    </div>
    <div class="reveal">
      <div class="card card-tinted"><h3>Sådan kommer I i gang</h3>
      <p>Kontakt os på <a href="mailto:info@nohrskovfonden.dk"><strong>info@nohrskovfonden.dk</strong></a> og hør mere om, hvordan vi sammen kan gøre den lille forskel stor – sammen.</p>
      <a class="btn btn-primary" href="mailto:info@nohrskovfonden.dk">Skriv til os</a></div>
    </div>
  </div>
</div></section>
""" + cta("Se hvem der allerede er med", "Mød de partnere, der gør vores arbejde muligt.", "Se vores partnere", "partnere.html"),
}

# ---------- Støt (oversigt) ----------
PAGES["stoet"] = {
    "title": "Sådan kan du støtte",
    "desc": "Støt Nohrskov Fonden som privatperson, virksomhed eller fond.",
    "body": hero("Sådan kan du <span class=\"squiggle\">støtte</span>",
                 "Når du støtter Nohrskov Fonden, bliver du en del af et fællesskab, der skaber nærvær, oplevelser, håb og retning for alvorligt syge børn og deres familier. Sammen giver vi familierne noget at glæde sig til, små pauser fra sygdommen og følelsen af ikke at stå alene.",
                 eyebrow="Støt os") + """
<section class="section"><div class="container">
  <div class="card-grid">
    <div class="card reveal">
      <div class="card-icon">&#129505;</div>
      <h3>Støt som privatperson</h3>
      <p>MobilePay, medlemskab, frivillighed, egen indsamling, testamente eller legat – der er mange måder at være med på.</p>
      <a class="btn btn-primary" href="stoet-som-privatperson.html">Læs mere</a>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#127970;</div>
      <h3>Støt som virksomhed</h3>
      <p>Økonomiske bidrag, produktsponsorater eller indsamlinger – alt hvad der kan skabe glæde, nærvær og gode oplevelser.</p>
      <a class="btn btn-primary" href="stoet-som-virksomhed.html">Læs mere</a>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#127793;</div>
      <h3>Støt som fond</h3>
      <p>Et samarbejde bygget på fælles værdier, håb og nærvær – støt samlet, fast eller en valgfri indsats.</p>
      <a class="btn btn-primary" href="stoet-som-fond.html">Læs mere</a>
    </div>
  </div>
  <div class="info-box reveal" style="max-width:760px;margin:48px auto 0">
    <strong>Familie med sygdomsramt barn?</strong>
    Bliv en del af Familiepanelet og hjælp os med at styrke støtten til familier med alvorligt syge børn.
    <a href="familiepanelet.html" style="font-weight:800">Læs om Familiepanelet &rarr;</a>
  </div>
</div></section>
""" + cta("Hurtigste vej til at gøre en forskel", "Støt med et valgfrit beløb via MobilePay #110754.", "Støt som privatperson", "stoet-som-privatperson.html"),
}

# ---------- Støt som privatperson ----------
PAGES["stoet-som-privatperson"] = {
    "title": "Støt som privatperson",
    "desc": "Støt via MobilePay, bliv medlem, frivillig eller opret indsamling, testamente eller legat.",
    "body": hero("Støt som <span class=\"squiggle\">privatperson</span>",
                 "Gør en forskel for syge og sårbare børn og deres familier. Som privatperson kan du være med til at skabe håb, glæde og værdifulde oplevelser for familier, der står i nogle af livets sværeste situationer.",
                 eyebrow="Støt os") + """
<section class="section"><div class="container">
  <div class="card-grid">
    <div class="card reveal">
      <div class="card-icon">&#128241;</div>
      <h3>MobilePay</h3>
      <p>Støt med et valgfrit beløb via MobilePay <strong>#110754</strong>.</p>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#127775;</div>
      <h3>Medlem</h3>
      <p>Bliv medlem af Nohrskov Fonden for 150 kr. om året ved at overføre 150 kr. til MobilePay <strong>#110754</strong> og skrive “medlem” i feltet.</p>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#129309;</div>
      <h3>Frivillig</h3>
      <p>Har du lyst til at være med til at gøre en forskel? Vi er altid klar på at byde nye frivillige velkommen på holdet. Kontakt os for en snak.</p>
      <a class="btn btn-ghost" href="kontakt.html">Kontakt os</a>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#127881;</div>
      <h3>Start din egen indsamling</h3>
      <p>Fejrer du fødselsdag, har du jubilæum, eller afholder du eller din by et kulturevent? Lad pengene gå til Nohrskov Fondens arbejde. Kontakt os, så hjælper vi dig godt i gang.</p>
      <a class="btn btn-ghost" href="kontakt.html">Kontakt os</a>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#128220;</div>
      <h3>Testamente</h3>
      <p>Du kan vælge at donere hele eller dele af din arv til Nohrskov Fonden. Sammen med Legal Desk tilbyder vi dig et gratis testamente, når du laver en donation til Nohrskov Fonden i testamentet.</p>
      <a class="btn btn-ghost" href="https://www.legaldesk.dk/dokumenter/arv/testamente" target="_blank" rel="noopener">Få dit gratis testamente</a>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#128142;</div>
      <h3>Legat</h3>
      <p>Du kan også oprette et legat, hvor du giver Nohrskov Fonden et vist beløb af din arv. Legal Desk tilbyder gratis hjælp til at oprette dit legat.</p>
      <a class="btn btn-ghost" href="https://www.legaldesk.dk/privat/testamente/hvad-er-et-legat" target="_blank" rel="noopener">Opret legat</a>
    </div>
  </div>
</div></section>
""" + cta("Hver krone gør en forskel", "Din støtte bliver til events, hospitalsbesøg og opfyldte ønsker.", "Se de andre måder at støtte", "stoet.html"),
}

# ---------- Støt som virksomhed ----------
PAGES["stoet-som-virksomhed"] = {
    "title": "Støt som virksomhed",
    "desc": "Støt Nohrskov Fonden med økonomiske bidrag, produktsponsorater eller indsamlinger.",
    "body": hero("Støt som <span class=\"squiggle\">virksomhed</span>",
                 "Vær med til at støtte vores indsatser og gør en konkret forskel for alvorligt syge børn og deres familier.",
                 eyebrow="Støt os") + """
<section class="section"><div class="container">
  <div class="card-grid">
    <div class="card reveal">
      <div class="card-icon">&#128176;</div>
      <h3>Økonomisk bidrag</h3>
      <p>Vær med til at støtte vores indsatser med et bidrag.</p>
      <div class="info-box" style="margin:16px 0 0"><strong>Sydbank</strong>Reg.nr.: 7045<br>Kontonr.: 0001628351</div>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#127873;</div>
      <h3>Produktsponsorat</h3>
      <p>Støt med produkter, forplejning, lokaler, oplevelser, transport eller aktiviteter. Alt hvad der kan skabe glæde, nærvær og gode oplevelser for børnene og deres familier.</p>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#128588;</div>
      <h3>Indsamling</h3>
      <p>Lad medarbejdere, kunder eller events samle ind til Nohrskov Fonden og vær med til at gøre en konkret forskel sammen som virksomhed. Kontakt os, så hjælper vi jer godt i gang.</p>
      <a class="btn btn-ghost" href="kontakt.html">Kontakt os</a>
    </div>
  </div>
</div></section>
""" + cta("Vil I mere end et bidrag?", "Som partner bliver jeres engagement synligt og langsigtet.", "Bliv partner", "bliv-partner.html"),
}

# ---------- Støt som fond ----------
PAGES["stoet-som-fond"] = {
    "title": "Støt som fond",
    "desc": "Fonde kan støtte Nohrskov Fondens samlede indsatser, blive fast støttepartner eller støtte en valgfri indsats.",
    "body": hero("Støt som <span class=\"squiggle\">fond</span>",
                 "Repræsenterer du en fond med et ønske om at gøre en mærkbar forskel for alvorligt syge børn og deres familier? Så inviterer vi jer til et samarbejde bygget på fælles værdier, håb og nærvær.",
                 eyebrow="Støt os") + """
<section class="section"><div class="container">
  <div class="card-grid">
    <div class="card reveal">
      <div class="card-icon">&#127756;</div>
      <h3>Støt vores samlede indsatser</h3>
      <p>Giv et økonomisk bidrag her og nu og vær med til at skabe håb, nærvær og lyspunkter gennem vores events, hospitalsindsats og Ønskebrønden.</p>
      <div class="info-box" style="margin:16px 0 0"><strong>Sydbank</strong>Reg.nr.: 7045<br>Kontonr.: 0001628351</div>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#129682;</div>
      <h3>Bliv fast støttepartner</h3>
      <p>Indgå et længerevarende samarbejde med Nohrskov Fonden og vær med til at sikre, at vi kan skabe meningsfulde oplevelser og støtte til familier året rundt.</p>
      <a class="btn btn-ghost" href="mailto:info@nohrskovfonden.dk">Kontakt os</a>
    </div>
    <div class="card reveal">
      <div class="card-icon">&#127919;</div>
      <h3>Støt en valgfri indsats</h3>
      <p>Vælg selv, om I ønsker at støtte vores events, hospitalsindsats eller Ønskebrønden – og gør en mærkbar forskel dér, hvor det betyder allermest for jer.</p>
      <a class="btn btn-ghost" href="mailto:info@nohrskovfonden.dk">Kontakt os</a>
    </div>
  </div>
</div></section>
""" + cta("Lad os tage en snak", "Skriv til os og hør, hvordan jeres fond kan gøre en mærkbar forskel.", "info@nohrskovfonden.dk", "mailto:info@nohrskovfonden.dk"),
}

# ---------- Familiepanelet ----------
PAGES["familiepanelet"] = {
    "title": "Familiepanelet",
    "desc": "Bliv en del af Familiepanelet og hjælp os med at styrke støtten til familier med alvorligt syge børn.",
    "body": hero("<span class=\"squiggle\">Familiepanelet</span>",
                 "Hjælp os med at styrke støtten til familier med alvorligt syge børn.",
                 eyebrow="Støt os") + """
<section class="section"><div class="container">
  <div class="split">
    <div class="reveal">
      <span class="eyebrow">Jeres erfaringer tæller</span>
      <h2 class="section-title">Bliv en del af Familiepanelet</h2>
      <p class="lead" style="margin-top:1rem">I Nohrskov Fonden arbejder vi for at skabe bedre støtte til familier med alvorligt syge børn. For at gøre det bedst muligt har vi brug for jeres erfaringer fra hverdagen.</p>
      <p style="margin-top:1rem;color:var(--navy-soft)">Vi vil gerne høre, hvad der virkelig betyder noget for jer, og hvad der skal til for at gøre en forskel. Vi vil også gerne høre mere om, hvordan Nohrskov Fonden har været med til at gøre en positiv forskel for jeres familie.</p>
      <a class="btn btn-primary" href="mailto:info@nohrskovfonden.dk" style="margin-top:1.6rem">Meld jer til panelet</a>
    </div>
    <div class="reveal">
      <div class="card card-tinted">
        <h3>Hvad indebærer det?</h3>
        <p>Som del af Familiepanelet deler I jeres erfaringer og perspektiver, som er med til at forme fondens indsatser – fra events til hospitalsindsats og Ønskebrønden.</p>
      </div>
    </div>
  </div>
</div></section>
""" + cta("Sammen gør vi støtten bedre", "Jeres stemme hjælper os med at hjælpe endnu bedre.", "Kontakt os", "mailto:info@nohrskovfonden.dk"),
}


# ================= BUILD =================

import os

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    for slug, p in PAGES.items():
        html = page(slug, p["title"], p["desc"], p["body"])
        path = os.path.join(root, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  {slug}.html")
    print(f"\n{len(PAGES)} sider genereret.")

if __name__ == "__main__":
    main()
