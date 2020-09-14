import pyautogui
import time
import os
import pyperclip
import PySimpleGUI as sg
from colorama import Fore
def clear ():
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear')

def spam (repeats, delay):
	for i in range(repeats):
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")
		time.sleep(delay)
	print("Дело сделано!")
	
def main ():
	print (Fore.GREEN+'''
   █─█─█───████─████──████─███
   █─█─█───█──█─█──██─█──█─█
   █─█─█───████─█──██─█──█─███
   ███─█───█──█─█──██─█──█───█
   ─█──███─█──█─████──████─███


███─████─███─███─█───█─████─████─███
█───█──█─█────█──█───█─█──█─█──█─█
███─█──█─███──█──█─█─█─████─████─███
──█─█──█─█────█──█████─█──█─█─█──█
███─████─█────█───█─█──█──█─█─█──███
		''')
	message = input(Fore.WHITE+"Какое сообщение вы хотите отправлять: ")
	repeats = int(input("Сколько сообщений вы хотите отправить: "))
	delay = int(input("Задержка между сообщениями (в секундах): "))
	sleeping = int(input("Время до начала спама (в секундах): "))
	print("Нажмите мышкой на поле ввода, а потом нажмите 'Enter'. Через " + str(sleeping) + " секунд запустится спам!")
	pyperclip.copy(message)
	if pyperclip.paste() == message:
		time.sleep(sleeping)
		spam(repeats, delay)
layout = [  [sg.Text('Какое сообщение вы хотите отправлять:',size=(35,1)),sg.Input(size=(50,1),key="input0")],
            [sg.Text('Сколько сообщений вы хотите отправить:',size=(35,1),key='gg'), sg.Input(size=(50,1),key="input1")],
            [sg.Text('Задержка между сообщениями (в секундах):',size=(35,1)),sg.Input(size=(50,1),key="input2")],
            [sg.Text('Время до начала спама (в секундах):',size=(35,1)),sg.Input(size=(50,1),key="input3")],
            [sg.Output(size=(90,1),key="output0")],
            [sg.Text("",size=(35,1),key='good')],
            [sg.Button('Ok'), sg.Button('Refresh'), sg.Button('Cancel')] ]
window = sg.Window('Spamer by VladOS', layout, return_keyboard_events=True)
if (__name__=="__main__"):
    while True:                             # The Event Loop
        event, values = window.read()
        window.Refresh()
        if event in ('Refresh'):
            window['input0'].update("")
            window['input1'].update("")
            window['input2'].update("")
            window['input3'].update("")
            #window['output0'].update("")
        if event in ('Cancel'):
            break
        if event in ('Ok'):
            print("Нажмите мышкой на поле ввода, а потом нажмите 'Enter'. Через " + str(values['input3']) + " секунд запустится спам!")
            window.Refresh()
            pyperclip.copy(values['input0'])
            if pyperclip.paste() == values['input0']:
                time.sleep(int(values['input3']))
                spam(int(values['input1']),int(values['input2']))
        window['good'].update(event)
    #clear ()	
    #main ()
