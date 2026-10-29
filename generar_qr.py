"""Genera un QR por colaborador (SVG y PNG) y la hoja qrs.html.  Uso:  python generar_qr.py
Requiere:  pip install segno pillow
Los QR apuntan a  BASE + <clave> + "/".  Si cambia la direccion, cambia BASE y se vuelve a ejecutar.
"""
import json, re, pathlib, html, segno
BASE = "https://garanzaseguros.github.io/TarJeta-Digital/"
GUINDA = "#8a2338"
raiz = pathlib.Path(__file__).parent
js = (raiz / "colaboradores.js").read_text(encoding="utf-8")
cuerpo = js[js.index("{", js.index("const COLABORADORES")):js.rindex("}") + 1]
cuerpo = re.sub(r'([{,]\s*)([A-Za-z_]\w*)\s*:', r'\1"\2":', cuerpo)
cuerpo = re.sub(r',(\s*[}\]])', r'\1', cuerpo)
personas = json.loads(cuerpo)

(raiz / "qr").mkdir(exist_ok=True)
tarjetas = []
for clave, p in personas.items():
    url = BASE + clave + "/"
    qr = segno.make(url, error="m", boost_error=False)
    qr.save(raiz / "qr" / f"{clave}.svg", scale=10, border=4, dark=GUINDA, light="#ffffff", xmldecl=True)
    qr.save(raiz / "qr" / f"{clave}.png", scale=30, border=4, dark=GUINDA, light="#ffffff")
    nombre = f'{p["pila"]} {p["apellidos"]}'
    tarjetas.append(
        f'<div class="t"><img src="qr/{clave}.svg" alt="QR de {html.escape(nombre)}">'
        f'<b>{html.escape(nombre)}</b><span>{html.escape(p["puesto"])}</span>'
        f'<a href="{url}">{url.replace("https://", "")}</a>'
        f'<small><a href="qr/{clave}.svg" download>SVG</a> · <a href="qr/{clave}.png" download>PNG</a></small></div>')
    print("ok", clave, url)

(raiz / "qrs.html").write_text(f'''<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>QR de las tarjetas - Garanza</title>
<style>
body{{margin:0;padding:28px 16px;background:#eef0f1;font-family:"Segoe UI",system-ui,Arial,sans-serif;color:#000}}
h1{{font-size:22px;margin:0 0 4px}} p{{color:rgba(0,0,0,.56);margin:0 0 22px;font-size:14px}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px;max-width:1100px;margin:0 auto}}
.t{{background:#fff;border-radius:14px;padding:16px;text-align:center;box-shadow:0 4px 14px rgba(0,0,0,.08);display:flex;flex-direction:column;gap:4px}}
.t img{{width:100%;max-width:190px;margin:0 auto}} b{{font-size:15px}} span{{font-size:13px;color:#8a2338;font-weight:600}}
a{{color:rgba(0,0,0,.6);font-size:11.5px;word-break:break-all}} small{{margin-top:4px}}
@media print{{body{{background:#fff}}.t{{box-shadow:none;border:1px solid #ccc;break-inside:avoid}}small{{display:none}}}}
</style></head><body>
<h1>QR de las tarjetas digitales</h1>
<p>Cada QR abre la tarjeta de esa persona. Para imprenta usa el SVG.</p>
<div class="g">
{chr(10).join(tarjetas)}
</div></body></html>''', encoding="utf-8")
