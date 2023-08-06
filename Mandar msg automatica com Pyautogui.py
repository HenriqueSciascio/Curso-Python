# mandar msg automatica
import pyautogui as pg
import time
"""
time.sleep(5)
print(pg.position()) #Point(x=-1970, y=572)
"""

pg.moveTo(-1970, 572)
pg.leftClick()
time.sleep(2)
pg.moveTo(-1685, 724)
pg.leftClick()
time.sleep(2)
pg.moveTo(-1260, 1227)
pg.leftClick()
time.sleep(2)
for c in range(0, 1):
    pg.write('ola amigo')
    time.sleep(0.1)
    pg.press('enter')
    time.sleep(0.1)
pg.alert(text='trabalho concluido', title='sucesso', button='ok')