# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:53:20 2023

@author: berta
"""
import os
import time
import pyautogui
from datetime import datetime
import shutil

def instagram_hikaye_ekran_goruntusu():
    
    bluestacks_yolu = r"C:\Program Files (x86)\BlueStacks X\BlueStacks X.exe"

    instagram_yolu = r"C:\Users\berta\OneDrive\Desktop\INFLOW APP\Instagram.lnk"
    
    time.sleep(5)  
    
    os.startfile(instagram_yolu)
    
    time.sleep(10)  

    try:
        influencer_kullanici_adi = ["fabiabengs,benblack"]
        for i in influencer_kullanici_adi:
            
            pyautogui.click(x=820, y=982)  # Button
            time.sleep(2)
            pyautogui.click(x=750, y=84)    # search_box
            time.sleep(2)
            pyautogui.typewrite(i)          # username_writer
            time.sleep(2)
            
            
            pyautogui.click(x=767, y=192)  # open_
           
            time.sleep(5)  
            
           
            pyautogui.click(x=707, y=130)  
            
           
            influencer_klasor_yolu = r"C:\Users\berta\OneDrive\Desktop\INFLOW APP\ekran_goruntuleri\{}".format(i)
            os.makedirs(influencer_klasor_yolu, exist_ok=True)
            
           
               
            time.sleep(2)  
                
            left = 670   
            top = 45    
            width = 522  
            height = 964 

            tarih = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            ekran_goruntusu_yolu = r"C:\Users\berta\OneDrive\Desktop\INFLOW APP\ekran_goruntuleri\{}\{}_{}.png".format(i, i, tarih)
            ekran_goruntusu = pyautogui.screenshot(ekran_goruntusu_yolu, region=(left, top, width, height))
           
                
            pyautogui.click(x=1153, y=550)  
                
            print("{} için ekran görüntüleri kaydedildi!".format(i))
        return i
    except Exception as e:
        print("Bir hata oluştu:", str(e))


instagram_hikaye_ekran_goruntusu()
