# Copilot Guidance: Portafolio-de-Proyectos

Breve: Instrucciones enfocadas para agentes AI que editan, refactorizan o añaden funcionalidad en este repositorio.

- **Visión general**: Proyecto de ejemplos y micro-proyectos en Python. Contiene tres subproyectos: el convertidor de artículos a MP3 (`Conversor_mp3_voz.py`), un conjunto de juegos Pong (`Juego_pong.py`) y un esqueleto de pruebas de velocidad de escritura (`Prueba_escritura_veloz.py`). Los archivos son scripts Python de uso directo; la mayoría son ejecutables como programas independientes.

- **Puntos de entrada claves**:
  - Convertidor MP3: [Conversor_mp3_voz.py/texto_a_voz.py](Portafolios_proyectos.py/Conversor_mp3_voz.py/texto_a_voz.py) — funciones exportadas: `extraer_articulo`, `procesar_texto`, `convertir_texto_a_voz`, `convertir_articulo_a_audio`.
  - Ejemplos: [Conversor_mp3_voz.py/ejemplos_uso.py](Portafolios_proyectos.py/Conversor_mp3_voz.py/ejemplos_uso.py) — scripts de ejemplo que muestran casos de uso.
  - Verificación de imports: [Conversor_mp3_voz.py/verificar_importaciones.py](Portafolios_proyectos.py/Conversor_mp3_voz.py/verificar_importaciones.py) — utilidad para comprobar dependencias.
  - Pong: [Juego_pong.py/Version_IA.py](Portafolios_proyectos.py/Juego_pong.py/Version_IA.py) y [Juego_pong.py/Ping_pong.py](Portafolios_proyectos.py/Juego_pong.py/Ping_pong.py) — dos variantes de juego, una OOP con IA simple.

- **Arquitectura y patrones**:
  - Código organizado por script-folder; cada carpeta representa un micro-proyecto con su propio punto de entrada.
  - Conversor MP3 usa: `newspaper3k` para extracción, `nltk` para tokenización, `gtts` para TTS. Revisar `texto_a_voz.py` para el flujo: extraer → procesar → dividir → convertir y guardar en `audios/`.
  - Pong está implementado con `turtle`; Version_IA usa clases (`Paddle`, `Ball`, `Scoreboard`, `PongGame`) para separar responsabilidades.
  - Manejo de errores: usar patrones try/except que informan errores por consola y reintentos para gTTS; replicar estilo si agregas features.

- **Estilo de proyecto y requisitos**:
  - Idioma del código y comentarios: Español. Mantener coherencia en nuevos comentarios/strings.
  - Python 3.7+; dependencias listadas en `README_texto_a_voz.md` (ej.: `nltk`, `newspaper3k`, `gtts`, `requests`).
  - Entradas/outputs basadas en consola y archivos (por ejemplo `audios/` y `high_score.txt`). Evitar dependencias de entorno complejo.

- **Flujos de desarrollo recomendados**:
  - Para probar dependencias: ejecutar `python Conversor_mp3_voz.py/verificar_importaciones.py` y revisar impresiones.
  - Para verificar comportamiento de conversión: ejecutar `python Conversor_mp3_voz.py/ejemplos_uso.py` y seleccionar ejemplos. Esto simula el flujo real y es ideal para PRs que cambien `texto_a_voz.py`.
  - Para probar los juegos: ejecutar `python Juego_pong.py/Ping_pong.py` o `python Juego_pong.py/Version_IA.py` y validar la UI con `turtle`.

- **Patrones de diseño y convenciones específicas**:
  - Prefijo y salida de archivos: los nombres de archivos de salida se limpian y normalizan con regex (`re.sub`) y se reemplazan espacios/guiones por `_`. Mantén este comportamiento cuando agregues nombres de salida.
  - Fragmentación de texto para gTTS: `dividir_en_fragmentos` limita por cantidad de caracteres; gTTS suele colocar límites de request — respeta fragmentación y reintentos (`max_intentos`).
  - Carpeta `audios/` se crea en la carpeta del script (`Path(__file__).parent / 'audios'`). Si añades servicios, conservad rutas relativas a `__file__`.
  - Persistencia de récords: el juego guarda `high_score.txt` o `high_score_IA.txt` en el directorio de ejecución.

- **Integraciones y restricciones**:
  - gTTS (Google) depende de conexión. Añadir pruebas automáticas que requieran conexión sólo con opción `--integration` o entorno CI explícito.
  - `newspaper3k` y `nltk` pueden requerir descarga de recursos (`nltk.download('punkt')`) la primera vez.
  - `turtle` necesita entorno gráfico (no headless CI). CI tests should skip `turtle` runs.

- **Qué hacer cuando agregas código**:
  - Mantén la coherencia en idioma (español) y el estilo imperativo (scripts ejecutables en primer plano).
  - Si añades un CLI o empaquetas el proyecto, añade instrucciones de instalación en `README_texto_a_voz.md` y crea `requirements.txt`.
  - Evita añadir paquetes pesados o servicios externos sin incluir un modo `--offline` o `--mock` para tests.

- **Pruebas y validación rápida**:
  - Ejecutar: `python Conversor_mp3_voz.py/verificar_importaciones.py` (verificacion de imports)
  - Ejecutar un ejemplo: `python Conversor_mp3_voz.py/ejemplos_uso.py` y seleccionar un ejemplo.

- **Límites y notas**:
  - No asumas un package manager o tests; el código está compuesto por scripts. Si introduces unit tests, agrega `pytest` y `requirements.txt`.
  - Para operaciones que toquen la red o archivos locales, documenta el comportamiento esperado en `README_texto_a_voz.md`.

Si hay algo faltante o deseas que adapte las reglas a un estilo de trabajo (tests automáticos, CI, empaquetado), dime y actualizo el archivo.