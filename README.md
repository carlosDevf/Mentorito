# 🧠 Mentorito — Evaluador HTML con cariño educativo 🇲🇽

**Mentorito** es una API en FastAPI que analiza proyectos de HTML/CSS subidos por estudiantes, usando el poder de OpenAI para generar retroalimentación clara, directa y en formato HTML para ser mostrado dentro de una plataforma React o similar.

Ideal para bootcamps, senseis con muchos alumnos, y revisiones automáticas de exámenes prácticos.

---

## 🚀 ¿Qué hace?

- ✅ Descarga archivos HTML desde una URL raw (como GitHub)
- ✅ Evalúa 4 métricas clave: Funcionalidad, Comprensión, Buenas Prácticas, Creatividad
- ✅ Devuelve una respuesta **en HTML formateado** para uso con `dangerouslySetInnerHTML`
- ✅ Resalta errores comunes y sugiere mejoras reales
- ✅ Puede integrarse en cualquier sistema educativo con frontend React, Next.js, etc.

---

## 🛠 Instalación

```bash
git clone https://github.com/tuusuario/mentorito.git
cd mentorito
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt

