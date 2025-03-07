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

















