# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:53:20 2023

@author: berta
"""
#download Bluestack X( a mobile simulator), open Instagram on it then code is ready to run.
import os
import time
import pyautogui
from datetime import datetime
import shutil

def open():
    
    bluestacks_path = r"C:\Program Files (x86)\BlueStacks X\BlueStacks X.exe"

    instagram_path = r"C:\Users\berta\OneDrive\Desktop\INFLOW APP\Instagram.lnk"
    
    time.sleep(5)  
    
    os.startfile(instagram_path)
    
    time.sleep(10)  

    try:
        usernames = ["fabiabengs,benblack"]
        for i in usernames:
            
            pyautogui.click(x=820, y=982)  # location of Button
            time.sleep(2)
            pyautogui.click(x=750, y=84)    # location of search_box
            time.sleep(2)
            pyautogui.typewrite(i)          # username_writer
            time.sleep(2)
            
            
            pyautogui.click(x=767, y=192)  # open_
           
            time.sleep(5)  
            
           
            pyautogui.click(x=707, y=130)  
            
           
            influencer_doc_path = r"C:\Users\berta\OneDrive\Desktop\INFLOW APP\ekran_goruntuleri\{}".format(i)
            os.makedirs(influencer_doc_path, exist_ok=True)
            
           
               
            time.sleep(2)  
                
            left = 670   
            top = 45    
            width = 522  
            height = 964 

            date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = r"C:\Users\berta\OneDrive\Desktop\INFLOW APP\ekran_goruntuleri\{}\{}_{}.png".format(i, i, date)
            screenshot = pyautogui.screenshot(screenshot_path, region=(left, top, width, height))
           
                
            pyautogui.click(x=1153, y=550)  
                
            print("{} : screenshot taken and saved to file".format(i))
        return i
    except Exception as e:
        print("Error:", str(e))

open()
