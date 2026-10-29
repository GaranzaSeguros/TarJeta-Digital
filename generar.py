"""Genera una pagina independiente por colaborador a partir de plantilla.html
y colaboradores.js.  Uso:  python generar.py
  - La primera persona (gortega) tambien queda como index.html en la raiz.
  - Las demas quedan en <clave>/index.html  ->  .../garanza/<clave>/
"""
import json, re, pathlib
raiz = pathlib.Path(__file__).parent
plantilla = (raiz / "plantilla.html").read_text(encoding="utf-8")
js = (raiz / "colaboradores.js").read_text(encoding="utf-8")
cuerpo = js[js.index("{", js.index("const COLABORADORES")):js.rindex("}") + 1]
# el archivo es JS (claves sin comillas): se pasa a JSON
cuerpo = re.sub(r'([{,]\s*)([A-Za-z_]\w*)\s*:', r'\1"\2":', cuerpo)
cuerpo = re.sub(r',(\s*[}\]])', r'\1', cuerpo)
personas = json.loads(cuerpo)

def pagina(clave, p, ruta):
    return (plantilla.replace("/*CLAVE*/", clave).replace("/*RUTA*/", ruta)
            .replace("/*PERSONA*/null", json.dumps(p, ensure_ascii=False)))

for i, (clave, p) in enumerate(personas.items()):
    if i == 0:
        (raiz / "index.html").write_text(pagina(clave, p, ""), encoding="utf-8")
    carpeta = raiz / clave
    carpeta.mkdir(exist_ok=True)
    (carpeta / "index.html").write_text(pagina(clave, p, "../"), encoding="utf-8")
    print("ok", clave)
