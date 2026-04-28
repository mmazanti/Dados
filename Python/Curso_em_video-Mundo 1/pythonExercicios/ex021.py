#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica-ex021.mp3')
pygame.mixer.music.play()
print('Dê o enter para parar a música \u23F9\uFE0F')
