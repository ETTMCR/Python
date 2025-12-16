import cv2
import pyautogui
import imageio.v2 as imageio

def Show_sirene ():
    # טוען את קובץ ה-GIF
    gif_path = "alert-siren1.gif"
    gif = imageio.mimread(gif_path)  # קריאת כל הפריימים של ה-GIF
    screen_width, screen_height = pyautogui.size() # מקבל את גודל המסך
    frame_height, frame_width, _ = gif[0].shape # קבלת גודל הפריים הראשון של ה-GIF (כדי לדעת מה גודלו)
    cv2.namedWindow("alert", cv2.WINDOW_AUTOSIZE)    # יצירת חלון בגודל מקורי של ה-GIF
    # חישוב המיקום המרכזי של החלון
    x_offset = (screen_width - frame_width) // 2
    y_offset = (screen_height - frame_height) // 2
    cv2.moveWindow("alert", x_offset, y_offset)    # הזזת החלון למרכז המסך
    # לולאת השמעה
    for _ in range(10):  # מנגן את ה-GIF 10 פעמים
        for frame in gif:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # המרה לפורמט של OpenCV
            cv2.imshow("alert", frame)            # הצגת הפריים בגודלו המקורי
            # יציאה בלחיצה על ESC
            if cv2.waitKey(100) & 0xFF == 27:
                break
    cv2.destroyAllWindows()

'''
def Show_sirene ():#(bool_Show_sirene)
    bool_Show_sirene = True
    if bool_Show_sirene :
        cv2.namedWindow('Raw Image', cv2.WINDOW_NORMAL)
        # Get your image and process it
        # Then display
        cv2.imshow('Raw Image', 'alert-siren1.gif')
        # Then move your windows to where you want them
        cv2.moveWindow('Raw Image',  parameters['ZONE_2_X_START'], parameters['ZONE_2_YSTART'])
        ## waits for user to press any key
        # (this is necessary to avoid Python kernel form crashing)
        #cv2.waitKey(0)
'''

'''
import imageio
def Show_sirene ():#(bool_Show_sirene)
    bool_Show_sirene = True
    if bool_Show_sirene :
        gif_path = "alert-siren1.gif"
    gif = imageio.mimread(gif_path)  # Read GIF frames
    #while True:
    for _ in range(10):
        for frame in gif:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
            cv2.imshow("GIF Player", frame)
            if cv2.waitKey(100) & 0xFF == 27:  # Press 'Esc' to exit
                break

    cv2.destroyAllWindows()
'''  
'''
import imageio
def Show_sirene ():
# Load the GIF using imageio
    gif_path = "alert-siren1.gif"  # Replace with your GIF file
    gif = imageio.mimread(gif_path)  # Read GIF as a list of frames

    # Convert frames to OpenCV format
    frames = [cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) for frame in gif]

    # Create a window and move it to a specific location
    window_name = "GIF Viewer"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window_name, 1840//2, 1200//2)  # Move window to (100, 200)

    # Play the GIF in a loop
    for _ in range(10):
        for frame in frames:
            cv2.imshow(window_name, frame)
            # if cv2.waitKey(100) & 0xFF == 27:  # 100ms delay, press 'Esc' to exit
            #     cv2.destroyAllWindows()
            #     exit()

    cv2.destroyAllWindows()
'''

