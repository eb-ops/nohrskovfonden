# Nohrskov Fonden - nohrskovfonden.dk

Statisk website. Ingen dependencies, ingen build-tools udover Python 3.

## Struktur

- `build.py` - Sitegenerator. AL indholdsredigering sker her (PAGES-dict). Kør `python3 build.py` for at regenerere alle .html-filer.
- `assets/css/style.css` - Alt styling. Farver og fonte styres via CSS-variabler i `:root`.
- `assets/js/main.js` - Navigation, dropdowns, scroll-reveal.
- `*.html` - Genererede sider. Rediger dem IKKE direkte - rediger `build.py` og regenerer.

## Workflow

1. Rediger indhold i `build.py`
2. `python3 build.py`
3. Commit og push

## Deploy

GitHub Pages: Settings -> Pages -> Deploy from branch -> main -> / (root).
Custom domain: nohrskovfonden.dk (tilføj CNAME-fil og DNS A-records mod GitHub Pages).

## TODO

- Partnerlogoer (placeholders på partnere.html)
- Citater på stemmer-fra-faellesskabet.html (placeholders)
- Portrætfotos på holdet-bag.html og ambassadoerer.html (viser initialer nu)
- Billeder hotlinkes fra files.builder.nu (det gamle CMS) - download og læg dem i assets/img/ inden det gamle site lukkes
- Ansøgningsformularer (event + Ønskebrønden) - pt. mailto-links
