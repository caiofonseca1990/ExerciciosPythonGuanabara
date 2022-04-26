#Tocar uma música MP3
import pygame

pygame.init()

pygame.mixer.music.load('E:\Desktop\Exercicios Curso em Video\musicasExer18\gloria.mp3')

pygame.mixer.music.play()

pygame.event.wait()


