import keyboard
import time
import pyautogui

pyautogui.FAILSAFE = False
screenResWidth = 1920
goToX = 1920/2
goToY = 1080/2
hsp = 0
hspMultiplier = 1
vsp = 0
grv = 0.3

left_click_flag = False
left_hold_flag = False

right_click_flag = False
right_hold_flag = False

mouse_up_repeats = 0
mouse_up_repeatsR = 0

loop = True
start = True

while loop:
    key_left = keyboard.is_pressed("a")
    key_right = keyboard.is_pressed("d")
    key_up = keyboard.is_pressed("w")
    key_down = keyboard.is_pressed("s")
    key_left_click = keyboard.is_pressed("q")
    key_right_click = keyboard.is_pressed("e")
    key_stop = keyboard.is_pressed("z")

    if key_stop:
        loop = False
    
    if key_left_click and left_hold_flag == True:
        #pyautogui.click(button='left')
        pyautogui.mouseDown(button='left')
        mouse_up_repeats = 0
        left_hold_flag = False
        print("left click pressed")
    if not key_left_click:
        mouse_up_repeats += 1
        left_hold_flag = True
        if mouse_up_repeats < 2:
            pyautogui.mouseUp(button='left')
            

    if key_right_click and right_hold_flag == True:
        #pyautogui.click(button='left')
        pyautogui.mouseDown(button='right')
        mouse_up_repeatsR = 0
        right_hold_flag = False
        print("right click pressed")
    if not key_right_click:
        mouse_up_repeatsR += 1
        right_hold_flag = True
        if mouse_up_repeatsR < 2:
            pyautogui.mouseUp(button='right')

    if key_right:
        hsp += 1 * hspMultiplier
        hspMultiplier += 0.01
    if key_left:
        hsp -= 1 * hspMultiplier
        hspMultiplier += 0.01
    if key_up:
        vsp -= 1.2
    if key_down:
        vsp += 1

    if not key_right and not key_left:
        hspMultiplier = 1
    
    mouse_x, mouse_y = pyautogui.position()

    if goToY >= 1080:
        vsp = -5
        if vsp > 5:
            vsp = 5
    if goToY <= 0:
        vsp = -5
        if vsp < 5:
            vsp = 5
    
    goToX += (0 - goToX)/10

    pyautogui.moveTo(goToX,goToY,duration=0.1,_pause=False)
    goToX += hsp
    goToY += vsp

    vsp += grv
    
    time.sleep(1/60)
