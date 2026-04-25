#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica-desafio020.mp3')
pygame.mixer.music.play()
input('Dê enter para parar a música \u23F9\uFE0F')
