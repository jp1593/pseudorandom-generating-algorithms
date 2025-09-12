# Generadores de Números Pseudoaleatorios — Análisis de Datos

Este repositorio contiene código y materiales relacionados con la generación de números pseudoaleatorios y el análisis de sus propiedades estadísticas. El objetivo es estudiar varios algoritmos clásicos, compararlos y evaluar su comportamiento.

---

## 📂 Contenido

| Archivo / Módulo | Descripción |
|------------------|-------------|
| `middle-square.py` | Implementación del método **Middle-Square** para generar números pseudoaleatorios. |
| `lcg.py` | Generador **congruencial lineal** (Linear Congruential Generator). |
| `randu.py` | Implementación del generador **RANDU** (ejemplo clásico de mal generador). |
| `mersenne.py` | Generador **Mersenne Twister**, estándar en muchos lenguajes modernos. |
| `blumblum.py` | Generador **Blum Blum Shub**, criptográficamente seguro. |
| `montecarlo.py` | Experimentos de **Monte Carlo** usando los generadores para aproximar integrales. |
| `P1-3-C.py` | Casos de prueba y experimentos adicionales. |
| `T2-Data Analysis.pdf` | Informe de análisis de datos con resultados, gráficos y conclusiones. |

---

## ⚙️ Instalación y uso

1. Clona este repositorio:

   ```bash
   git clone https://github.com/jp1593/pseudorandom-generating-algorithms.git
   cd pseudorandom-generating-algorithms

2. Asegúrate de tener instalado Python 3.x. 

3. (Opcional) Crear un entorno virtual:
python3 -m venv venv
source venv/bin/activate   # en Linux / macOS
venv\Scripts\activate      # en Windows

4. Instalar dependencias necesarias:
pip install numpy matplotlib scipy

5. Ejecutar los scripts. Ejemplo:
python middle-square.py
python lcg.py
python montecarlo.py

### 🧪 Experimentos realizados

- Comparación de la uniformidad de los generadores mediante histogramas y pruebas de chi-cuadrado.

- Evaluación del periodo de cada generador (tiempo hasta repetición de secuencias).

- Uso de Monte Carlo para aproximar integrales, comparando precisión según el tamaño de muestra.

- Estudio de correlaciones y patrones en generadores clásicos (ejemplo: RANDU).

### 📊 Resultados destacados
- Mersenne Twister → gran uniformidad y periodo extremadamente largo.

- RANDU / Middle-Square → muestran patrones y fallos estadísticos notorios.

- Blum Blum Shub → robusto y seguro, aunque más lento.

- Monte Carlo → precisión mejora con mayor número de muestras, pero depende de la calidad del generador usado.

### 👤 Autor: jp1593