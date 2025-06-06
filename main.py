import os
import requests
import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Carga variables de entorno desde .env si existe
load_dotenv()

# Inicializa cliente de OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Inicializa FastAPI
app = FastAPI()

# Prompt para evaluación técnica con respuesta HTML
PROMPT_BASE = """
Actúa como un revisor experto en desarrollo web. Se te dará el contenido de un proyecto hecho por un estudiante que comienza con HTML y CSS. Evalúa con base en estas 4 métricas (escala del 1 al 4):

- Funcionalidad: ¿Cumple su propósito básico?
- Comprensión: ¿El estudiante demuestra que entiende lo que hizo?
- Buenas prácticas: ¿El código está bien indentado, ordenado, sin errores o etiquetas mal cerradas?
- Creatividad: ¿El diseño tiene algún toque personal?

Devuelve tu respuesta como HTML limpio para mostrarse con innerHTML en React. Usa:
- Una lista <ul> con cada métrica y su calificación.
- Un párrafo <p> con retroalimentación técnica breve (máx. 500 caracteres).
- Usa <code> para destacar etiquetas HTML mal usadas.
- No incluyas emojis, estilos inline ni frases motivacionales.
"""

# Modelo del body del POST
class AnalisisRequest(BaseModel):
    url: str
    token_id: str

# Descarga el HTML
def fetch_html_file(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise HTTPException(status_code=400, detail=f"No se pudo descargar el archivo: {response.status_code}")

# Envia a OpenAI
def analyze_with_openai(html_content: str) -> str:
    full_prompt = PROMPT_BASE + "\n\n" + html_content
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Eres un experto en desarrollo frontend."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0,
        max_tokens=1000
    )
    return completion.choices[0].message.content

# Endpoint POST
@app.post("/analizar")
async def analizar(data: AnalisisRequest):
    try:
        html = fetch_html_file(data.url)
        resultado = analyze_with_openai(html)
        return {
            "token_id": data.token_id,
            "resultado": resultado  # HTML string
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Para correrlo manualmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)

