import pyautogui, time
time.sleep(5)
word = "I love you to the moon and back"
n = 10
while n > 0:
    pyautogui.typewrite(word)
    time.sleep(0.5)
    pyautogui.press("enter")
    n = n - 1 
    time.sleep(2)
