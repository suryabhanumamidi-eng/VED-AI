import edge_tts
import asyncio
import pygame
import os


async def speak(text: str):
    output_file = "response.mp3"
    voice = "en-GB-RyanNeural"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

    pygame.mixer.init()
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.quit()
    if os.path.exists(output_file):
        os.remove(output_file)
