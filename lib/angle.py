#-*- coding: utf-8 -*-
import math

'''
angleVecteurs

@param  {tup}   v1
@param  {tup}   v2
@return {float}     angle entre les deux vecteurs en degrés
'''
def angleVecteurs (v1, v2) :

    x1, y1 = v1
    x2, y2 = v2

    proj = x1*x2 + y1*y2

    hypo = math.hypot(x2, y2)

    if hypo == 0 :
        t = 0
    else :
        t = math.acos(proj / hypo)

    return math.degrees(t)
