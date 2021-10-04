import pyautogui
import time
import pyperclip
from IPython.display import display

pyautogui.PAUSE = 1
#abrir navegador
#abrir link maneira 1
pyautogui.press("winleft")
pyautogui.write("microsoft edge")
pyautogui.press("enter")


link = "https://time.ibm.com/week"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(15)

#descobrir posição do mouse
#time.sleep(5)
#print(pyautogui.position())

#clicar
pyautogui.click(1312, 560, clicks=1)
pyautogui.click(1139, 667, clicks=1)
import pandas as pd

df = pd.read_excel(r"C:\Users\VitorBetti\Documents\HorasILC.xlsx", sheet_name="Horas")

display (df)

segunda = df['Segunda']
terca = df['Terça']
quarta = df['Quarta']
quinta = df['Quinta']
sexta = df['Sexta']


#print(seg2)
#print(sexta)

time.sleep(5)
pyautogui.click(859, 667, clicks=1)
pyperclip.copy(int(segunda))
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")

pyperclip.copy(int(terca))
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")

pyperclip.copy(int(quarta))
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")

pyperclip.copy(int(quinta))
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")

pyperclip.copy(int(sexta))
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")

