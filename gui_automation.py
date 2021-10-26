import pyautogui

# Faster: Moves mouse pointer by 200 pixels
# SLOWER: Moves mouse pointer by 20 pixels
FASTER=200
SLOWER=20


class gui_control:
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        pyautogui.size()

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer UPWARDS from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------
    def mouse_up(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse up :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, -1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
            
    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer DOWNWARDS from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------        
    def mouse_down(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, 1*SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse down :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, 1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, 1*SLOWER, duration=0.25)

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer LEFTWARD from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------ 
    def mouse_left(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse left :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(-1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer RIGHTWARD from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------ 
    def mouse_right(self,recognizer, src):
        #print("Move mouse right")
        pyautogui.moveRel(100, 0, duration=0.25)
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse right :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
    
    #------------------------------------------------------------------------------------
    # CLICKS the LEFT Mouse button it's current position 
    #------------------------------------------------------------------------------------    
    def left_click(self):
        pyautogui.click()
 
    #------------------------------------------------------------------------------------
    # CLICKS the RIGHT Mouse button it's current position 
    #------------------------------------------------------------------------------------  
    def right_click(self):
        print("Right Clicking")
        pyautogui.click(button='right', clicks=2, interval=0.25)
 
    #------------------------------------------------------------------------------------
    # DOUBLE CLICKS the LEFT Mouse button it's current position 
    #------------------------------------------------------------------------------------  
    def double_click(self):
        print("Double Clicking")
        pyautogui.click(button='left', clicks=2, interval=0.25)