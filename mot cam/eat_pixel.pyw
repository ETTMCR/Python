#https://chatgpt.com/share/67c0d2cc-e984-800f-a0f1-86b29ce21203
'''
The coder Eliran Tal
https://ettmcr.github.io/my_site/
'''
import cv2
import winsound
import time
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image
import pyautogui
import numpy as np
import os

#num_alert_beeps=2

bool_toggle_log = True
bool_toggle_visual = True


#org
# Default values for zones and settings
#parameters={}
# def Default_parameters():
#     global parameters
parameters = {
    'ZONE_1_X_START': 78, 'ZONE_1_Y_START': 75, 'ZONE_1_X_END': 880, 'ZONE_1_Y_END': 600,
    'ZONE_2_X_START': 78, 'ZONE_2_Y_START': 675, 'ZONE_2_X_END': 880, 'ZONE_2_Y_END': 1200,
    'ZONE_3_X_START': 1040, 'ZONE_3_Y_START': 675, 'ZONE_3_X_END': 1840, 'ZONE_3_Y_END': 1200,
    'ZONE_4_X_START': 1040, 'ZONE_4_Y_START': 75, 'ZONE_4_X_END': 1840, 'ZONE_4_Y_END': 600,
    'ZONE_BIG_X_START': 150, 'ZONE_BIG_Y_START': 150, 'ZONE_BIG_X_END': 1840, 'ZONE_BIG_Y_END': 1200,
    'start_deley': 5,
    'time_interval': 2,
    'AREA': 10,
    'mute': 0 , # 0 = sound on, 1 = mute
    'ZONE_1_seek' : False,
    'ZONE_2_seek' : False,
    'ZONE_3_seek' : True,
    'ZONE_4_seek' : True,
    'num_alert_beeps' : 2
}


# Load parameters from file
def load_parameters():
    global parameters
    try:
        with open('parameters.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    parameters[key.strip()] = int(value.strip())

        ZONE_1_seek = bool(parameters['ZONE_1_seek'])
        ZONE_2_seek = bool(parameters['ZONE_2_seek'])
        ZONE_3_seek = bool(parameters['ZONE_3_seek'])
        ZONE_4_seek = bool(parameters['ZONE_4_seek'])

    except FileNotFoundError:
        #Default_parameters()
        for i in range(7, 0, -1):
            winsound.Beep(5500, 200)
            time.sleep(1) 
        print('parameters.txt not found, using default values.')
'''
# Booleans for enabling zone scans
ZONE_1_seek = bool(parameters['ZONE_1_seek'])
ZONE_2_seek = bool(parameters['ZONE_2_seek'])
ZONE_3_seek = bool(parameters['ZONE_3_seek'])
ZONE_4_seek = bool(parameters['ZONE_4_seek'])
'''


'''
ZONE_1_seek =parameters['ZONE_1_seek']
ZONE_2_seek = parameters['ZONE_2_seek']
ZONE_3_seek = parameters['ZONE_3_seek']
ZONE_4_seek = parameters['ZONE_4_seek']
'''
'''
if ZONE_2_seek==1:
    ZONE_2_seek=True
    for i in range(delay, 0, -1):
        winsound.Beep(5500, 200)
        time.sleep(1) 
else:
    ZONE_2_seek=False
'''

'''
parameters['ZONE_1_seek']=False
parameters['ZONE_2_seek']=False
parameters['ZONE_3_seek']=False
parameters['ZONE_4_seek']  =False
'''

# Countdown beeps before scanning starts
def countdown_beeps(delay):
    if parameters['mute'] == 0:
        for i in range(delay, 0, -1):
            winsound.Beep(1000, 200)
            time.sleep(1)
    else:
        time.sleep(delay)

# Capture screenshot
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #return cv2.imread(frame, cv2.IMREAD_GRAYSCALE)

# Detect motion between two frames in the specified zone
def detect_motion(frame1, frame2, x_start, y_start, x_end, y_end):
    zone1 = frame1[y_start:y_end, x_start:x_end]
    zone2 = frame2[y_start:y_end, x_start:x_end]
    diff = cv2.absdiff(zone1, zone2)

    #org 
    #non_zero_count = cv2.countNonZero(cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY))
    #return non_zero_count > parameters['AREA']


    #new works
    threshold =50
    gray_diff = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    non_zero_count = np.count_nonzero(gray_diff >parameters['threshold'] )

    #new save images
    #if non_zero_count > 0:
    #    cv2.imashow('gray_diff ',gray_diff )

    return non_zero_count > 0

# Main scanning function
def start_scanning():
    time.sleep(parameters['start_deley'])
    countdown_beeps(parameters['start_deley'])
    frame1 = capture_screenshot()
    time.sleep(parameters['time_interval'])

    while True:
        frame2 = capture_screenshot()

        if ZONE_1_seek and detect_motion(frame1, frame2, parameters['ZONE_1_X_START'], parameters['ZONE_1_Y_START'], parameters['ZONE_1_X_END'], parameters['ZONE_1_Y_END']):
            alert(1)

            if parameters['mute'] == 0:
                winsound.PlaySound("one.wav",0)
            #print ("ZONE_1 is alerted")
        if ZONE_2_seek and detect_motion(frame1, frame2, parameters['ZONE_2_X_START'], parameters['ZONE_2_Y_START'], parameters['ZONE_2_X_END'], parameters['ZONE_2_Y_END']):
            alert(2)
            if parameters['mute'] == 0:
                winsound.PlaySound("two.wav",0)
            #print ("ZONE_2 is alerted")
        if ZONE_3_seek and detect_motion(frame1, frame2, parameters['ZONE_3_X_START'], parameters['ZONE_3_Y_START'], parameters['ZONE_3_X_END'], parameters['ZONE_3_Y_END']):
            alert(3)
            if parameters['mute'] == 0:
                winsound.PlaySound("three.wav",0)
            #print ("ZONE_3 is alerted")
        if ZONE_4_seek and detect_motion(frame1, frame2, parameters['ZONE_4_X_START'], parameters['ZONE_4_Y_START'], parameters['ZONE_4_X_END'], parameters['ZONE_4_Y_END']):
            alert(4)
            if parameters['mute'] == 0:
                winsound.PlaySound("four.wav",0)
            #print ("ZONE_4 is alerted")

        frame1 = frame2.copy()
        time.sleep(parameters['time_interval'])



# Alert function (beeps 10 times)
# also printint the  zone number of alert and date and hour.
def alert(zone_num):
    if parameters['mute'] == 0:
        for _ in range(parameters['num_alert_beeps']): 
        #     winsound.Beep(1500, 100)  ##### new line
            winsound.PlaySound("beepi.wav",0)##### new line

##### new lines STARTS    
    Show_sirene()
    current_time = time.localtime()
    # Format and print in terminal
    if bool_toggle_log == True:
        with open("log_file.txt", "a") as file:  # "a" mode appends to the file; use "w" to overwrite
            file.write(f"alert in zone number {zone_num} at {current_time.tm_hour:02}:{current_time.tm_min:02}:{current_time.tm_sec:02} {current_time.tm_mday:02}/{current_time.tm_mon:02}/{current_time.tm_year}\n")

import my_gif_mdl

import imageio.v2 as imageio
def Show_sirene ():
    if bool_toggle_visual == True:
        my_gif_mdl.Show_sirene()           
        '''
        # טוען את קובץ ה-GIF
        gif_path = "alert-siren1.gif"
        gif = imageio.mimread(gif_path)  # קריאת כל הפריימים של ה-GIF
        screen_width, screen_height = pyautogui.size() # מקבל את גודל המסך
        frame_height, frame_width, _ = gif[0].shape # קבלת גודל הפריים הראשון של ה-GIF (כדי לדעת מה גודלו)
        cv2.namedWindow("GIF Centered", cv2.WINDOW_AUTOSIZE)    # יצירת חלון בגודל מקורי של ה-GIF
        # חישוב המיקום המרכזי של החלון
        x_offset = (screen_width - frame_width) // 2
        y_offset = (screen_height - frame_height) // 2
        cv2.moveWindow("GIF Centered", x_offset, y_offset)    # הזזת החלון למרכז המסך
        # לולאת השמעה
        for _ in range(10):  # מנגן את ה-GIF 10 פעמים
            for frame in gif:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # המרה לפורמט של OpenCV
                cv2.imshow("GIF Centered", frame)            # הצגת הפריים בגודלו המקורי
                # יציאה בלחיצה על ESC
                if cv2.waitKey(100) & 0xFF == 27:
                    break
        cv2.destroyAllWindows()
         '''

##### new lines EnDS

def helping():
    os.system("Help.pdf")

def Show_log():
    os.system('log_file.txt')

def about_menu() :
    url = "https://ettmcr.github.io/my_site/"
    #os.system(f"start {url}") 
    #url = 'ettmcr.mhtml'
    #os.system("start \"\" "+url)
    #os.system(url)
    os.system("about.png")

def areas_picture() :
    os.system('area_taged.jpg')

# Taskbar icon setup
def setup_tray_icon():
    global ZONE_1_seek, ZONE_2_seek, ZONE_3_seek, ZONE_4_seek, bool_toggle_log,bool_toggle_visual
    bool_toggle_log = True
    bool_toggle_visual = True
    ZONE_1_seek = bool(parameters['ZONE_1_seek'])
    ZONE_2_seek = bool(parameters['ZONE_2_seek'])
    ZONE_3_seek = bool(parameters['ZONE_3_seek'])
    ZONE_4_seek = bool(parameters['ZONE_4_seek'])
    icon = Icon('MotionDetector')
    icon.icon = Image.open('icon.PNG')
    icon.menu = Menu(
        MenuItem('Enable Areas', Menu(
            MenuItem('ZONE_1', lambda: toggle_zone(1), checked=lambda item: ZONE_1_seek),
            MenuItem('ZONE_2', lambda: toggle_zone(2), checked=lambda item: ZONE_2_seek),
            MenuItem('ZONE_3', lambda: toggle_zone(3), checked=lambda item: ZONE_3_seek),
            MenuItem('ZONE_4', lambda: toggle_zone(4), checked=lambda item: ZONE_4_seek)
        )),
        MenuItem('Log', Menu(
            MenuItem('Open log',Show_log),
            #MenuItem('delete log',os.system('log_file.txt') )
            MenuItem('Enable log',lambda: toggle_log(), checked=lambda item: bool_toggle_log)
        )),
        MenuItem('Alerts', Menu(
            MenuItem('MUTE', toggle_mute, checked=lambda item: parameters['mute'] == 1),
            MenuItem('VISUAL',lambda: toggle_visual(), checked=lambda item: bool_toggle_visual)

        )),
        
        MenuItem('Parameters file', open_parameters),        
        MenuItem('Areas picture', areas_picture),
        MenuItem('Help', helping),
        MenuItem('About', about_menu),
        #MenuItem(str(parameters['ZONE_2_seek']), about_menu),
        MenuItem('Exit', exit_app)
    )
    icon.run()

# Toggle zone scanning
def toggle_zone(zone):
    global ZONE_1_seek, ZONE_2_seek, ZONE_3_seek, ZONE_4_seek
    if zone == 1: ZONE_1_seek = not ZONE_1_seek
    if zone == 2: ZONE_2_seek = not ZONE_2_seek
    if zone == 3: ZONE_3_seek = not ZONE_3_seek
    if zone == 4: ZONE_4_seek = not ZONE_4_seek

def toggle_log():
    global bool_toggle_log
    if bool_toggle_log == True: 
        bool_toggle_log = not bool_toggle_log
    else:
        bool_toggle_log = not bool_toggle_log

def toggle_visual():
    global bool_toggle_visual
    if bool_toggle_visual == True: 
        bool_toggle_visual = not bool_toggle_visual
    else:
        bool_toggle_visual = not bool_toggle_visual


# Toggle mute function
def toggle_mute(icon, item):
    parameters['mute'] = 1 if parameters['mute'] == 0 else 0

# Open parameters file for editing
def open_parameters():
    import os
    os.system('notepad parameters.txt')
    load_parameters()

# Exit application
def exit_app(icon, item):
    icon.stop()
    #exit( )
    #quit() 
    os._exit(1) #https://stackoverflow.com/questions/173278/is-there-a-way-to-prevent-a-systemexit-exception-raised-from-sys-exit-from-bei

# Load parameters and start scanning thread
load_parameters()
th = threading.Thread(target=start_scanning)
th.start()
setup_tray_icon()
