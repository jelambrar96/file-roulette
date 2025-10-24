# Ruleta de Archivo Aleatorio

Este repositorio contiene dos formas de "ruleta" para mostrar líneas de un archivo (.txt o .csv) en orden aleatorio:

- `roulette.py` — script de consola en Python que lee un archivo, lo mezcla y muestra una línea por vez cada vez que presionas ENTER.
- `index.html` — interfaz web estática que permite cargar un archivo en el navegador, mezclar las filas (opcionalmente con semilla) y mostrar las líneas una por una en un área de salida.

## Estructura del repositorio

Archivos principales:

- `roulette.py` — script de Python (línea de comandos).
- `index.html` — página web interactiva (HTML + JS).
- `frutas.csv`, `frutas.txt` — ejemplos/archivos de datos que puedes usar para probar.

## 1) Cómo funciona `roulette.py` (script de Python)

Descripción rápida

- Lee un archivo `.txt` o `.csv` (una entrada por línea).
- Opcionalmente elimina la primera fila si se trata de un encabezado.
- Opcionalmente aplica una semilla para que la mezcla sea reproducible.
- Mezcla las filas con `random.shuffle`.
- Muestra las filas una a una; para pasar a la siguiente fila el usuario presiona ENTER.

Uso

Desde la terminal ejecuta:

```bash
python3 roulette.py --file ruta/al/archivo.txt
```

Opciones disponibles:

- `--file` / `-f` (obligatorio): ruta al archivo `.txt` o `.csv`.
- `--seed` / `-s` (opcional): número entero para inicializar la semilla del generador aleatorio (hace la mezcla reproducible).
- `--remove-header` / `-r` (opcional): si se indica, se elimina la primera fila antes de mezclar (útil cuando el archivo tiene encabezado).

Ejemplos

Mezclar `frutas.txt` y usar semilla 42:

```bash
python3 roulette.py -f frutas.txt -s 42
```

Eliminar la primera fila (encabezado) y usar `frutas.csv`:

```bash
python3 roulette.py -f frutas.csv -r
```

Comportamiento interactivo

- Tras ejecutar el script verás un mensaje indicando que presiones ENTER para mostrar la siguiente línea.
- Presiona Ctrl+C para salir en cualquier momento.

Limitaciones y notas

- El script asume que el archivo está en UTF-8.
- No hace parsing CSV especializado (cada línea se trata como una cadena completa). Si necesitas parseo de columnas, se puede extender fácilmente usando el módulo `csv`.

## 2) Cómo funciona `index.html` (interfaz web)

Descripción rápida

- Página HTML/JS que permite seleccionar un archivo local (`.txt` o `.csv`) desde el navegador.
- Opcionalmente puedes indicar una semilla numérica para que la mezcla sea reproducible desde la misma semilla.
- Opción para eliminar la primera fila (encabezado) antes de mezclar.
- Botones:
  - `Preparar`: lee el archivo, aplica las opciones (eliminar encabezado, semilla) y mezcla las filas.
  - `Siguiente`: muestra la siguiente línea mezclada dentro del área de salida.
  - `Reset`: limpia el área de salida y reinicia el contador para empezar desde la primera fila mezclada.
- Se muestran alertas informativas: cuando el archivo está preparado, cuando se termina la lista de filas (alert), y al reiniciar la salida (alert).

Cómo probar la página localmente

La forma más simple es abrir `index.html` en el navegador (doble clic sobre el archivo). Sin embargo, algunos navegadores imponen restricciones de seguridad al leer archivos locales o ejecutan diferente comportamiento con FileReader. Si quieres servir la página vía HTTP local puedes usar Python:

```bash
# desde la carpeta del proyecto
python3 -m http.server 8000
# luego abre en el navegador:
# http://localhost:8000/index.html
```

Flujo de uso

1. Abrir `index.html` en el navegador.
2. (Opcional) Introducir un número en "Semilla" para obtener un orden reproducible.
3. (Opcional) Marcar "Eliminar primera fila" si tu archivo tiene encabezado.
4. Seleccionar un archivo con el control "Seleccionar archivo (.txt o .csv)".
5. Pulsar `Preparar`.
6. Pulsar `Siguiente` para mostrar línea por línea. Cuando se acaben las filas aparece una alerta que lo indica.
7. Pulsar `Reset` para limpiar la salida y reiniciar (muestra otra alerta al reiniciar).

Notas de implementación

- El mezclado en JavaScript usa una función PRNG basada en `mulberry32` cuando se proporciona semilla; si no se proporciona semilla utiliza `Math.random()`.
- La página no sube archivos a ningún servidor; todo el procesamiento se hace localmente en el navegador usando `FileReader`.

Sugerencias / mejoras posibles

- Reemplazar los `alert()` por "toasts" o mensajes no intrusivos en la UI para una experiencia de usuario más fluida.
- Añadir previsualización/parseo CSV para mostrar columnas específicas en lugar de la fila completa.
- Añadir opción para exportar el orden mezclado a un nuevo archivo.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para el texto completo o visita: https://opensource.org/licenses/MIT


---

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)
