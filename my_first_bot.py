import pyautogui as robot
import time, keyboard, webbrowser

def abrepaint():
    robot.press("win")
    time.sleep(1)
    keyboard.write("paint")
    time.sleep(1)
    robot.press("enter")
    time.sleep(1)

def abreyoutube():
    webbrowser.open("http://www.youtube.com/watch")

def documentogoogle():
    webbrowser.open("https://docs.google.com/document/u/0/?tgif=d")
    time.sleep(2)
    robot.moveTo(326, 356, duration=1)
    robot.leftClick()