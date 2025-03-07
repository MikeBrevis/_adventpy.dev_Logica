""" Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su taller 🖼️, pero el marco debe cumplir unas reglas específicas. Tu tarea es ayudar a los elfos a generar este marco mágico.

Reglas:

Dado un array de nombres, debes crear un marco rectangular que los contenga a todos.
Cada nombre debe estar en una línea, alineado a la izquierda.
El marco está construido con * y tiene un borde de una línea de ancho.
La anchura del marco se adapta automáticamente al nombre más largo más un margen de 1 espacio a cada lado. """

def createFrame(names):

    long_horizontal_frame = 0 

    for x in range(len(names)) :

        if len(names[x]) > long_horizontal_frame :
            long_horizontal_frame = len(names[x])
    
    top_button_frames = "*" * (long_horizontal_frame + 4)
    frames_elements = []

    for x in range(len(names)) :

        space_texts = names[x].ljust(long_horizontal_frame)
        frames_elements.append("* " + space_texts + " *")

    final_frame = f"{top_button_frames}\n{"\n".join(frames_elements)}\n{top_button_frames}"
    
    return final_frame


frame_1 = createFrame(['midu', 'madeval', 'educalvolpz'])
print(frame_1)

