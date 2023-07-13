from nltk.sentiment import SentimentIntensityAnalyzer

def obtener_emocion(frase):
    analizador = SentimentIntensityAnalyzer()
    puntajes = analizador.polarity_scores(frase)
    
    if puntajes['compound'] >= 0.5:
        return 'feliz'
    elif puntajes['compound'] <= -0.5:
        return 'enojado'
    else:
        return 'neutral'

tareas = []

while True:
    tarea = input("Ingresa una tarea o escribe 'salir' para terminar: ")
    if tarea.lower() == 'salir':
        break
    
    emocion = input("Selecciona una etiqueta emocional para la tarea (feliz, enojado, neutral): ")
    
    tarea_emocion = {
        'tarea': tarea,
        'emocion': emocion.lower()
    }
    tareas.append(tarea_emocion)

estado_emocional_actual = input("Ingresa tu estado emocional (feliz, enojado, neutral): ")

tareas_recomendadas = []

for tarea_emocion in tareas:
    tarea = tarea_emocion['tarea']
    emocion = tarea_emocion['emocion']
    
    if emocion == estado_emocional_actual:
        tareas_recomendadas.append(tarea)

print("Tareas recomendadas:")
for tarea in tareas_recomendadas:
    print(tarea)
