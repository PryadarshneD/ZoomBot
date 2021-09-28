import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid,pswd):
   
    #Opens up the zoom app
   
    subprocess.call(["enter the path of zoom.exe"])
    time.sleep(5)
    

    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('enter the path of join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(2)
    
    # Type the meeting ID
    pyautogui.write(meetingid)

     # Hits the join button
    join_btn2 = pyautogui.locateCenterOnScreen('enter the path of join_btn.png')
    pyautogui.moveTo(join_btn2)
    pyautogui.click()
    time.sleep(5)

    #Types the password and hits enter
    pyautogui.write(pswd)
    join_btn3 = pyautogui.locateCenterOnScreen('enter the path of join_btn2.png')
    pyautogui.moveTo(join_btn3)
    pyautogui.click()

# Reading the file
df = pd.read_csv('enter the path of timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(40)
       print('signed in')
