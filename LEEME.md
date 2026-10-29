# Tarjeta de presentación con QR — Garanza

Al escanear el QR impreso en la tarjeta física, el teléfono abre una página con el
logo de Garanza, la foto de Guillermo y sus datos de contacto, con botones para
llamar, escribir por WhatsApp y guardarlo en la agenda.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `plantilla.html` | El diseño de la tarjeta. Es el que se edita. |
| `generar.py` | Genera el `index.html` de cada persona a partir de la plantilla. |
| `index.html` y `<clave>/index.html` | Páginas generadas. Son las que se publican. |
| `colaboradores.js` | Los datos de cada persona (nombre, puesto, celular, correo). Una línea por colaborador. |
| `generador-qr.html` | Genera el QR que se manda a imprimir y prepara las imágenes. |
| `logo-blanco.png` | Logo en blanco, sin fondo. El que se usa en el encabezado guinda. |
| `logo.png` | Logo a color, sin fondo. Para el encabezado blanco o para otros usos. |
| `logo-original.jpeg` | Archivo original que mandó el cliente. No se publica. |

Los dos HTML funcionan con doble clic, sin instalar nada y sin conexión.

## Una tarjeta por colaborador

Cada persona tiene su propia página independiente en su carpeta:
`.../garanza/isanchez/`, `.../garanza/ccampos/`, etc. La de Guillermo también queda
en la raíz (`index.html`), así que su QR ya impreso sigue funcionando.

- Los datos de cada quien están en `colaboradores.js` (una línea por persona).
- El diseño está en `plantilla.html`.
- Después de editar cualquiera de los dos, ejecuta `python generar.py`. Eso reescribe
  todas las páginas. **No edites a mano los `index.html` generados**: se sobrescriben.
- Foto opcional en `fotos/<clave>.jpg`; si no existe, no se muestra.

## QR de cada persona

`python generar_qr.py` crea `qr/<clave>.svg` y `qr/<clave>.png` para las 16 personas
y la hoja `qrs.html` con todos juntos. Cada QR apunta a
`https://garanzaseguros.github.io/TarJeta-Digital/<clave>/`. Para imprenta, el SVG.
Requiere `pip install segno pillow`.

## Datos configurados (Guillermo)

```
Guillermo Ortega Reyes
Director General · Garanza Fianzas
Tel:      55 1475 5018     (enlace: +52 55 1475 5018)
Correo:   gortega@garanza.com.mx
LinkedIn: linkedin.com/in/guillermo-ortega-reyes-81439536
Colores:  #8a2338 guinda · #a5b0b6 gris · blanco · negro
```

Para cambiarlos, abre `plantilla.html` con el Bloc de notas (clic derecho → Abrir con)
y edita el bloque `const DATOS = {` al inicio del script. Es lo único que hay que tocar.
Lo que dejes en `""` no aparece en la tarjeta.

## Estilo del encabezado

El campo `encabezado` acepta dos valores:

- `"guinda"` — franja guinda con el logo en blanco. **Es el que está puesto.**
- `"blanco"` — franja blanca con el logo a color y una banda guinda debajo.

El logo a color no se puede usar sobre el fondo guinda: la "G" y la palabra "Fianzas"
son de ese mismo guinda y desaparecen. Por eso cada estilo usa su propia versión del
logo, y el cambio entre ellos es automático.

## Pendientes

- **Foto de Guillermo.** Guárdala como `foto.jpg` en esta carpeta y vuelve a publicar.
  Mientras no esté, aparece un círculo guinda con las iniciales *GO*. Que sea cuadrada
  o vertical, con la cara centrada: se recorta en círculo.
- **Sitio web.** El campo `sitio` está vacío. Si Garanza tiene página, ponla ahí y
  aparecerá una fila más con el enlace.
- **WhatsApp.** Se asumió que el 55 1475 5018 tiene WhatsApp. Si no lo tiene, pon
  `whatsapp: ""` y el botón desaparece solo.
- **Dirección.** El campo `direccion` está vacío. Si la pones, se agrega una fila que
  abre Google Maps.

## Publicar cambios

El sitio vive en GitHub Pages. Después de editar `index.html` o de agregar `foto.jpg`:

```bash
git add -A
git commit -m "Actualiza los datos de la tarjeta"
git push
```

En uno o dos minutos el sitio queda actualizado. **El QR ya impreso sigue funcionando**,
porque apunta a la dirección, no a los datos.

## Generar el QR

Abre `generador-qr.html`, pega la dirección del sitio y descarga el código. Ya viene
con el guinda #8a2338 puesto.

- **SVG** es lo que conviene mandar a la imprenta: es vectorial, no se pixelea a
  ningún tamaño.
- **PNG** sirve para pruebas y para diseños digitales.

Antes de mandar a imprimir, **escanea el código desde la pantalla con dos teléfonos
distintos** para confirmar que abre bien.

## Para que el QR funcione bien impreso

- **Tamaño mínimo 2 cm por lado.** Por debajo de eso muchos teléfonos fallan.
- **Deja el margen blanco** alrededor (los 4 módulos que trae por defecto). Sin ese
  espacio el código no se detecta.
- **Contraste alto:** guinda sobre blanco funciona bien. Nunca guinda sobre el gris
  #a5b0b6: no hay contraste suficiente y el lector falla.
- Si le pones el logo al centro, usa corrección **H** y pruébalo antes de imprimir.
- No lo pongas sobre el doblez, el barniz brillante ni muy pegado al borde.

## Detalles técnicos

- El botón *Guardar contacto* genera un archivo `.vcf` estándar (vCard 3.0) que
  Android y iPhone abren directamente para agregar el contacto, con nombre, empresa,
  puesto, teléfono, correo y LinkedIn.
- El teléfono se guarda como `+525514755018`, en formato internacional, para que
  funcione cuando alguien marque desde el extranjero. La clave de país se controla
  con el campo `paisTelefono`.
- El logo se recortó del JPEG original quitando el fondo blanco con una rampa de
  transparencia entre los valores 8 y 30 de distancia al blanco, lo que conserva el
  suavizado de los bordes sin dejar halo.
- El generador trae su propio codificador de códigos QR según la norma
  ISO/IEC 18004, en modo byte, versiones 1 a 40. No usa librerías externas ni
  servicios en línea, así que **los datos nunca salen de la computadora**.
- Verificado contra la librería de referencia `qrcode`: las matrices generadas son
  idénticas módulo a módulo, y los códigos se leen correctamente con el decodificador
  independiente `jsQR` en las 40 versiones y los 4 niveles de corrección.
