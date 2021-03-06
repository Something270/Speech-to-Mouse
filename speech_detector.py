from typing import Text
import speech_recognition
import gui_automation

def spech_detector():

    # The gui instance will be used to call GUI functions defined by us in 'gui_automation.py'
    gui = gui_automation.gui_control()
    recognizer = speech_recognition.Recognizer()
    print("\n\nThreshold Value Before calibration:" + str(recognizer.energy_threshold))

    with speech_recognition.Microphone() as src:
        
        while True:
            
            try:
                audio = recognizer.adjust_for_ambient_noise(src)
                print("\n\nThreshold Value After calibration:" + str(recognizer.energy_threshold))
                print("\nAwaiting command")
                yield "Awaiting command"
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
                yield "I heard : " + speech_to_txt
                #speech_to_txt = recognizer.recognize_google_cloud(audio)
            except Exception as ex:
                print("Sorry. Could not understand.\n\n")
                continue
                
            print("I heard : " + speech_to_txt)
            
            #---------------------------------------------------------------------
            # The following if-else block is for the commands I have chosen and 
            # call their respective GUI action
            #---------------------------------------------------------------------
            if (speech_to_txt == "quit program") or (speech_to_txt == "exit program"):
                yield "Speech to Mouse"
                break
            elif speech_to_txt == "stop":
                yield "Awaiting command" 
            elif speech_to_txt == "mouse up" or speech_to_txt == "move up":
                gui.mouse_up(recognizer, src)
            elif speech_to_txt == "mouse down" or speech_to_txt == "move down":
                gui.mouse_down(recognizer, src)
            elif speech_to_txt == "mouse left" or speech_to_txt == "move left":
                gui.mouse_left(recognizer,src)
            elif speech_to_txt == "mouse right" or speech_to_txt == "move right":
                gui.mouse_right(recognizer, src)
            elif speech_to_txt == "left click" or speech_to_txt == "click" or speech_to_txt == "left-click":
                gui.left_click(recognizer, src)
            elif speech_to_txt == "right click" or speech_to_txt == "right-click":
                gui.right_click(recognizer, src)
            elif speech_to_txt == "double click" or speech_to_txt == "double-click":
                gui.double_click(recognizer, src)