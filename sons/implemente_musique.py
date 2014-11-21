'''implementer musique - type musique de fond pour un niveau - menu
'''
from pygame import mixer

mixer.music.load()
''' recupere un fichier son type.mp3'''

mixer.music.play(loops=0, start=0.0)
'''loops : nombre de fois ou on le joue ( joue 1 + loops fois), si -1, repete indefiniment
start : position temporelle de depart dans le fichier '''