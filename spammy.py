import pyautogui, time
time.sleep(5)
word = "I love you"
n = 5
while n > 0:
    pyautogui.typewrite(word)
    time.sleep(0.5)
    pyautogui.press("enter")
    n = n - 1 
    time.sleep(2)
