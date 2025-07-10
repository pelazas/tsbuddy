import json
from agents import llm

def run(state: dict):
    if not state["products"]:
        return {"messages": [{"role": "assistant", "content": "No product to evaluate."}]}

    system_message = """
        Eres un agente de evaluación de productos. Tu tarea es analizar la información proporcionada sobre un producto y asignarle una puntuación de calidad general del 1 al 10, donde:

        - 1 significa muy mala calidad o poco valor,
        - 10 significa excelente calidad y valor sobresaliente.

        Te proporcionaré un producto.

        Instrucciones:
        1. Considera el precio en relación con las especificaciones: mejores especificaciones a menor precio deben aumentar la puntuación.
        2. Usa la calificación sobre 5 como un factor importante, pero también analiza la distribución de calificaciones por posibles sesgos (por ejemplo, muchas calificaciones bajas pueden reducir la confianza).
        3. Considera qué tan potentes son la CPU y la pantalla en comparación con productos típicos de la categoría.
        4. Si faltan especificaciones o son claramente de gama baja, ajusta la puntuación en consecuencia.
        5. Devuelve solo un objeto JSON con dos claves:
        - "score": un entero del 1 al 10
        - "explanation": un resumen conciso en español de las principales razones detrás de la puntuación

        Ejemplo de salida:
        {
        "score": 8,
        "explanation": "Buen modelo de CPU con alta velocidad y caché suficiente, precio competitivo, calificación de 4.2 con la mayoría de opiniones positivas."
        }
        """

    for product in state["products"]:
        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": json.dumps(product, ensure_ascii=False, indent=2)
            }
        ]
        reply = llm.invoke(messages)
        try:
            result = json.loads(reply.content)
            product["score"] = result.get("score")
            product["explanation"] = result.get("explanation")
        except Exception:
            product["score"] = None
            product["explanation"] = "Evaluation failed."

    return {"messages": [{"role": "assistant", "content": "Products evaluated."}], "products": state["products"]}
