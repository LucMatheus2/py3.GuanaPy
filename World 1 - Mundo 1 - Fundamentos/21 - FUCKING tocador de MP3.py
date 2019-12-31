'''
# Algoritmo : Tocador MP3
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''
#Bibliotecas
import pygame

#Processamento - Inicializar
print("\033[36m")
pygame.init()

#Processamento - Tocar música
pygame.mixer.music.load('dog.mp3')
pygame.mixer.music.play()

#Esperar
pygame.event.wait()
