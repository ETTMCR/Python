
# -*- coding: utf-8 -*-

import tkinter.messagebox
def def_about():
    tkinter.messagebox.showinfo("ABOUT", "I dedicate this software to my DAD. \nMy DAD is suffer from AMD, Age-related Macular Degeneration.\
                                \n AMD is the first cuase for vision impairment in the developed countries.\
                                    \n With Regards and may we all have a good health, and look for good in any creature. \
                                        \n Eliran Tal - elirantal1985@gmail.com ")   
def def_exitme():
    # import sys
    #sys.exit()
    
    ttl ='EXIT'
    msg = 'Do you want to exit the program ? '
    MsgBox = messagebox.askquestion (ttl,msg,icon = 'warning')
    #print ("dg")
    if MsgBox == 'yes':
        cam.release()
        ikkuna.destroy()
        raise SystemExit
    else:
        return
                                        
import subprocess  
# def run_again(cmd):
#     subprocess.call(["bash", "-c", "source ~/.profile; " + cmd]) 
    
import os as os
import sys
def def_reset_all():
    # os.system("completes1 style two.py")
    # os.execl(sys.executable, sys.executable, *sys.argv)
    
    #run_again("completes1 style two.py")
    
    cam.release()
    ikkuna.destroy()
    #def_exitme()
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:]) #restart the program

    

def def_keys():      
        #print ( key_stroke)
        global  fx1,fy1
        how_much_wait = 1
        key_stroke = cv2.waitKey(how_much_wait) #+ & 0xFF
        #print (key_stroke)
        
        # print(cv2.waitKey(0))
        if key_stroke%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            print (cv2.waitKey(1))
            #cam.release()
            #cv2.destroyAllWindows()
            def_exitme()

            
        if key_stroke == 43: #43 # org ==1 
            # - key
            # ord('+')
            fy1 -= 0.1
            fx1 -= 0.1# -5
            print (cv2.waitKey(1))
            
        #cv2.waitkey(1) = 82 or 84 # you can use the arrow keys,
        if key_stroke == 45 : #cv2.waitKey(1) == 45: # 45 # org ==0
            # + key
            # ord('-')
            fx1 += 0.1  # +5
            fy1 += 0.1            
            print (cv2.waitKey(1))
            
        if key_stroke == 43: #43 # org ==1 
            # - key
            # ord('+')
            print (cv2.waitKey(1))

        if key_stroke == 113: #43 # org ==1 
            # - key
            # ord('+')
            print (cv2.waitKey(1))
            def_exitme()
            
        if (cv2.waitKey(1) & 0xFF) == ord("q"): #113
            print (cv2.waitKey(1))
            #cam.release()
            #cv2.destroyAllWindows()
            def_exitme()


global factor
factor =  1
def def_factor_minus():
        global factor
        if factor != 1  :
            factor -= 1 
        my_scale1.set(factor)
def def_factor_plus():
        global factor
        if factor >= 1  :
            factor +=    1         
        my_scale1.set(factor)
        
def my_scale_bar_upd(value):
    global factor
    factor = (my_scale1.get())

    
def def_changeState(): # disabling / enabling some buttons aregarding to video mode ON / OFF

    if (button_1['state'] == NORMAL): #bigger
        button_1['state'] = DISABLED
    else:
        button_1['state'] = NORMAL
        
    if (my_scale1['state'] == NORMAL): #bigger
        my_scale1['state'] = DISABLED
    else:
        my_scale1['state'] = NORMAL
        
    if (button_2['state'] == NORMAL): #bigger
        button_2['state'] = DISABLED
    else:
        button_2['state'] = NORMAL
        
    if (button_3['state'] == NORMAL): #smaller
        button_3['state'] = DISABLED
    else:
        button_3['state'] = NORMAL        

    if (button_4['state'] == NORMAL): #<> flip
        button_4['state'] = DISABLED
    else:
        button_4['state'] = NORMAL  

    if (button_0['state'] == NORMAL): # start 
        button_0['state'] = DISABLED
    else:
        button_0['state'] = NORMAL  
        
    if (button_7['state'] == NORMAL): # start 
        button_7['state'] = DISABLED
    else:
        button_7['state'] = NORMAL       
        
    if (button_8['state'] == NORMAL): # start 
        button_8['state'] = DISABLED
    else:
        button_8['state'] = NORMAL          
        
    if (button_6['state'] == NORMAL): # reset_canvas 
        button_6['state'] = DISABLED
    else:
        button_6['state'] = NORMAL   
    


def def_flip ():
    global  DO_FLIP_ONCE, frame,flipped
    #frame = cv2.flip(frame, 1)
    DO_FLIP_ONCE = True # change only once
    # if flipped :
    #     #frame = cv2.flip(frame, 0)
    #     flipped = False
    # else:
    #     #frame = cv2.flip(frame, -1)
    #     flipped = True
    #button_4.clicked.connect(Pass)
    
def def_open_folder(): # !!!!!!!!!!!!!!!! why it shutting down the app ?
    path =  os.getcwd()
    os.startfile(path)            


     
def scale1_grid_forget():
    # my_scale1.grid_forget() # not seen in the canvas 
    my_scale1.grid(row=10,column=10, sticky=NE)
    # my_scale1.grid_remove()
    # # three lines above doesn't work
    
    ikkuna.wm_attributes('-transparentcolor', '#ab23ff')
    my_scale1.wm_attributes('-transparentcolor', '#ab23ff') #AttributeError: 'Scale' object has no attribute 'wm_attributes'


def def_save():
    global saved
    #https://www.pythonfixing.com/2022/06/fixed-how-to-save-tkinter-canvas-as.html
    #https://getridbug.com/python/how-can-i-convert-canvas-content-to-an-image/
    import datetime
    #now = str(datetime.now())
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now =  now.replace('-', '')
    now =  now.replace(":", '')
    now =  now.replace(".", '')
    now =  now.replace(" ", '')
    name = f"capture_{now}"
    # scale1_grid_forget()
    
    try: # The try block lets you test a block of code for errors.
        # ikkuna.wm_attributes('-transparentcolor', '#ab23ff')
        my_scale1.wm_attributes('-transparentcolor', '#ab23ff') #AttributeError: 'Scale' object has no attribute 'wm_attributes'

    except : # The except block lets you handle the error. 
        my_scale1.grid(row=10,column=10, sticky=NE)
        my_scale1.grid_forget() 

        ImageGrab.grab(bbox=(
            capture_Canvas.winfo_rootx(),
            capture_Canvas.winfo_rooty(),
            capture_Canvas.winfo_rootx() + capture_Canvas.winfo_width() +300, #not giving the exact box of capture_Canvas
            capture_Canvas.winfo_rooty() + capture_Canvas.winfo_height() + 200 # !!!! #why ????????????
        )).save(name+'.jpg')
    # print (saved)
    # if saved :

    #     # my_scale1.grid() #  showing the canvas again
    #     # my_scale1.grid(row=0,column=0, sticky=NE)  
    #     saved = False
        
    # else :
    #     # my_scale1.grid(row=10,column=10, sticky=NE)
    #     # my_scale1.grid_forget() 
    #     saved = True
    #     def_save()

    
def def_stop(): 
    global cam
    cam.release()
    button_1.grid_forget()
    cv2.destroyAllWindows()
    def_changeState()
    button_0.grid(row=1,column=1, pady=10,padx=10,sticky=SW ) 
    button_0['state']=NORMAL
    
def def_bigger ():
    global scale_count , fx1, fy1
    # if cv2.waitKey(1)  == 45 : #cv2.waitKey(1) == 45: # 45 # org ==0
    #     # + key
    #     # ord('-')
    #     fx1 += 0.1  # +5
    #     fy1 += 0.1
    #     print (cv2.waitKey(1))
    if scale_count <=19 :
        scale_count +=1
        fx1 += 0.1  # +5
        fy1 += 0.1        
    else:
        #beep
        winsound.Beep(440, 500)

    #need to enhance contrast in bigger scales
def def_0_0():
    #https://stackoverflow.com/questions/3950773/how-to-scroll-a-tkinter-canvas-to-an-absolute-position
    global capture_Canvas
    capture_Canvas.xview_moveto (0)
    capture_Canvas.yview_moveto (0)

    
def def_smaller ():
    global scale_count  , fx1, fy1
    if scale_count >=2 :
        scale_count -=1        
        fx1 -= 0.1  # +5
        fy1 -= 0.1        
    else:
        #beep
        winsound.Beep(440, 500)

# make canvas draggable - method 3
class DRAG_HERE:
    def left(e):
        drag_x = -20
        drag_y = 0
        capture_Canvas.moveto(img, drag_x, drag_y)
        #ikkuna.config(cursor="fleur")
    def right(e):
        drag_x= 20
        drag_y = 0
        capture_Canvas.moveto(img, drag_x, drag_y)
        #ikkuna.config(cursor="fleur")
    def up(e):
        drag_x = 0
        drag_y = -20
        capture_Canvas.moveto(img, drag_x, drag_y)
        #ikkuna.config(cursor="fleur")
    def down(e):
        drag_x,  = 0
        drag_y = 20
        capture_Canvas.moveto(img, drag_x, drag_y)
        #ikkuna.config(cursor="fleur")
    # Define a function to allow the image to move within the canvas
    def move(e):
        #global capture_Canvas
        global  img
        global drag_x, drag_y
        drag_x = e.x
        drag_y = e.y
        img = capture_Canvas.create_image(drag_x, drag_y, image=show_now)
        ikkuna.config(cursor="fleur")


        
        
def def_start():
    global frame
    global cam

    global DO_FLIP_ONCE, flipped
    global fx, fy, fx1, fy1

    
    def_changeState()
    button_0.grid_remove()
    button_1.grid(row=1,column=1, pady=10,padx=10,sticky=SW ) 
    button_1['state']=NORMAL
    
    #cv2.namedWindow("Experience_in_AI camera")
    cam = cv2.VideoCapture(0)
    while True:

        # button_7['state'] = NORMAL #F-
        # button_8['state'] = NORMAL #F+
        button_5['state'] = NORMAL #save
      
        #@@@@@@@@@@@@@@@@@@@@@@@@@@
        #https://stackoverflow.com/questions/50870405/how-can-i-zoom-my-webcam-in-open-cv-python
        #cv2.imshow_now('Original image', image)
        # if mirror: 
           # image = cv2.flip(image, 1)
        #print (mirror)
        #image = cv2.flip(image, 1)
        #image = cv2.flip(image, -1)
        #image = cv2.flip(image, 0)
        

            

        #global fx, fy
        ret, frame = cam.read()
        #frame = cv2.resize(frame, None, fx1, fy1, interpolation=cv2.INTER_AREA)
        frame = cv2.resize(frame, None, fx=fx1, fy=fy1, interpolation=cv2.INTER_AREA)
        # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) #ORG
        # frame = cv2.flip(frame, 1)
        #frame = cv2.flip(frame, -1)
        #frame = cv2.flip(frame, 0)
        #cv2.imshow_now('Input', frame)


        if DO_FLIP_ONCE : 
            print (DO_FLIP_ONCE)
            #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) #cv2.ROTATE_180
            DO_FLIP_ONCE = False
            if flipped :
                frame = cv2.flip(frame, 0)
                flipped = False
            else:
                #frame = cv2.rotate(frame, cv2.ROTATE_180)
                frame = cv2.flip(frame, -1)
                flipped = True
            print (flipped) # why it prints twice , and it is the reason the picture flipped over right over #https://stackoverflow.com/questions/42715895/how-to-make-a-button-perform-single-click-instead-of-double-click
            
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) 
                
        global begin,img,ikkuna,show_now,capture_Canvas #  ,ccc
        img = Image.fromarray(frame)
        w,h = img.size
        img = img.resize((w*factor,h*factor))
        show_now = ImageTk.PhotoImage(img)
        id = capture_Canvas.create_image(0,0,anchor=tkinter.NW,image=show_now)
        #capture_Canvas.moveto(id,-100,-100)
        # ccc = capture_Canvas.create_image(0,0,anchor=tkinter.NW,image=show_now)
        
        ikkuna.update()         
        

        # #frame= cv2.resize(frame1, (width, height))#(width*size_vid, height*size_vid))
        # #size_vid=int(1.25)
        # #frame= cv2.resize(frame1,(width*size_vid, height*size_vid))
        # #frame= cv2.resize(frame1, (1920, 1080))
        # #frame= cv2.resize(frame1, (640, 480)) # as the video camerea lifecam 30 microsoft
        #frame= cv2.resize(frame, (800, 600)) # go well with (640, 480) camera type
        # # frame= cv2.resize(frame, (1024,768))

        if not ret:
            print("failed to grab frame")
            break
        
        # make canvas draggable - method 1
        #Canvas_On() #https://stackoverflow.com/questions/18884220/moving-around-a-python-canvas-without-using-scrollbars
        # make canvas draggable - method 2 
        #make_draggable(capture_Canvas) # https://www.codegrepper.com/code-examples/python/Tkinter+canvas+draggable
        
                
        # make canvas draggable - method 3
        # https://www.tutorialspoint.com/how-to-move-a-tkinter-canvas-with-mouse
        #capture_Canvas.bind("<B1-Motion>", DRAG_HERE.move) ## ??? why it doesn't work , I want that the global img will stay in the last darg_y darg_x ???
        ikkuna.config(cursor="arrow")
        ##capture_Canvas.after(100, movement) ## cool effect 1
        ##capture_Canvas.moveto(img, drag_x, drag_y) ## cool effect 2
        
        
        def_keys() ## ??? why it doesn't work ???
        
        
        #capture_Canvas.bind('<Double-Button-1>', def_fullscreen) ## ??? why it doesn't work ???
        #https://stackoverflow.com/questions/56604453/double-click-event-fires-after-every-successive-click-in-python-tkinter

# def def_cng_start_stop ():
#     global cng_start_stop,button_0 ,button_1
#     if cng_start_stop:
#         button_0.grid_forget()
#         def_start()
#         button_1.grid()
#         cng_start_stop = False
#     else :
#         button_0.grid()
#         button_1.grid_forget()
#         cng_start_stop = True
#         def_stop()
       
import tkinter
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk

import numpy as np
from PIL import Image, ImageTk , ImageGrab
import cv2

import os
import winsound

global i_frame  #for cascading frame capturing and saving
i_frame = 1

global cam , frame , show_now , img

global key_stroke

global flipped
flipped = True
global  DO_FLIP_ONCE
DO_FLIP_ONCE = False

global  scale_count
scale_count = 1

global fx, fy, fx1, fy1
fx1=0.5
fy1=0.5
cam = cv2.VideoCapture(0)


ikkuna=tkinter.Tk()
ikkuna.title("WEBCAM for visual impaired as CCTV")
#ikkuna.geometry('640x480')
screen_width = ikkuna.winfo_screenwidth()
screen_height = ikkuna.winfo_screenheight()


#As well as set its x and y location properties concatenating with "+":
#window.geometry("{}x{}+{}+{}".format(window_width, window_height, x-coord, y-coord))
ikkuna.geometry("{}x{}".format(screen_width, screen_height)) #, sticky='ew')) # tkinter screen window size
ikkuna.resizable(width=0, height=0) # unsizeable
# ikkuna.resizable(width=1, height=1) # sizeable

##method 1
#ikkuna.attributes('-fullscreen', True) # fullscreen, sizeable, but see all buttons

##method 2
ikkuna.overrideredirect(False)
ikkuna.state('zoomed')  # fullscreen sizeable
ikkuna.lift()
# ???? How to make fullscreen and sizeable and seeing the horizental bottom scrollbar ????

frame=np.random.randint(0,255,[100,100,3],dtype='uint8')
img = ImageTk.PhotoImage(Image.fromarray(frame))

#message="You can see some \nclassification results \nhere after you add some intelligent  \nadditional code to your combined and handy \n tkinter & CV2 solution!"
# message="bla"
# board_text=tkinter.Label(ikkuna,text=message)
# board_text.grid(row=1,column=1,pady=1,padx=10)

# @@@@@@@@@@@@@ canvas @@@@@@@@@@@@@@@@@
#capture_Canvas = tkinter.Canvas(ikkuna, bd=2, bg="blue", height=768, width=1024) # main canvas of video camera
#capture_Canvas = tkinter.Canvas(ikkuna, bd=2, bg="blue", height=600, width=800) # main canvas of video camera

# works + scrollbars 
# capture_Canvas = tkinter.Canvas(ikkuna, bd=2, bg="blue", height=800, width=1280 ) # main canvas of video camera
# capture_Canvas.grid( row = 0,column = 0)
#create a scrollbar widget and set its command to the text widget
## WORKS as + move_canvas scrolls

## @@@@@@@@@@@@@@@@ capture_Canvas
# Add a canvas in that frame
#capture_Canvas = tkinter.Canvas(ikkuna,height=790, width=1280, bg="blue", scrollregion = "0 0 4000 4000") # goes with  #ikkuna.resizable(width=0, height=00) # 0,0 for unsizeable
capture_Canvas = tkinter.Canvas(ikkuna,height=780, width=1280, bg="blue", scrollregion = "0 0 4000 4000")
capture_Canvas.grid(row=0, column=0, sticky="new")

# @@@@@@@@@@@@@@@@ Link a scrollbar to the canvas
vsb = tkinter.Scrollbar(ikkuna, orient="horizontal", command=capture_Canvas.xview,width = 50)
vsb.grid(row=1, column=0, sticky='ew')
capture_Canvas.configure(xscrollcommand=vsb.set)
hsb = tkinter.Scrollbar(ikkuna, orient="vertical", command=capture_Canvas.yview, width = 50)
hsb.grid(row=0, column=1, sticky='sn')
capture_Canvas.configure(yscrollcommand=hsb.set)

## @@@@@@@@@@@@@@@@ button_Canvas
button_Canvas = tkinter.Canvas(ikkuna, bd=2, bg="grey", height=600, width=200)#,sticky=NS)#, padx=10, pady=10)
button_Canvas.grid( row =0 ,column = 4)

## @@@@@@@@@@@@@@@@  move_Canvas
move_Canvas = tkinter.Canvas(button_Canvas, bd=2, bg="grey", height=300, width=300)#, padx=10, pady=10)
move_Canvas.grid( row = 8,column = 1)

## @@@@@@@@@@@@@@@@ move_canvas scrolls like + 
scrollbar_X = Scrollbar(move_Canvas, orient='horizontal', command=capture_Canvas.xview,width = 15)#, bg = 'green')
#scrollbar_X = ttk.Scrollbar(move_Canvas, orient='horizontal', command=capture_Canvas.xview,width = 35)#, bg = 'green')
## https://docs.python.org/3/library/tkinter.ttk.html#ttk-styling
scrollbar_X.grid(row=0, column=1,pady=10,padx=10) # sticky=ttk.NS
scrollbar_Y =Scrollbar(move_Canvas, orient='vertical', command=capture_Canvas.yview,width =15 )
scrollbar_Y.grid(row=0, column=1,pady=10,padx=10)#, sticky=NS)
##bad option "-width": must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
#  communicate back to the scrollbar
capture_Canvas['yscrollcommand'] = scrollbar_Y.set
capture_Canvas['xscrollcommand'] = scrollbar_X.set
#scrollbar_Y['state'] = DISABLED


# @@@@@@@@@@@@@ canvas @@@@@@@@@@@@@@@@@


# @@@@@@@@@@@@@ buttons @@@@@@@@@@@@@@@@@     
from idlelib.tooltip import Hovertip
       
height_btn=2
button_0=tkinter.Button(button_Canvas,text="V\nStart\nV",command=def_start,height=5,width=20,  bg='green', fg='#ffffff')
button_0.grid(row=1,column=1, pady=10,padx=10,sticky=SW ) 
button_0.config(height=1*height_btn,width=7)
myTip = Hovertip(button_0,'Begins the video.')

button_1=tkinter.Button(button_Canvas,text="X\nStop\nX",command=def_stop,height=5,width=20,bg='red')
button_1.grid(row=2,column=1, pady=10,padx=10,sticky=SW ) 
button_1.config(height=1*height_btn,width=7)
#button_1.grid_forget
button_1.grid_remove()
#button_1['state'] = DISABLED



# global cng_start_stop , button_0 ,button_1
# cng_start_stop = True

# button_0=tkinter.Button(button_Canvas,text="V\nStart\nV",command=def_cng_start_stop(),height=5,width=20,  bg='green', fg='#ffffff')
# button_0.grid(row=1,column=1, pady=10,padx=10,sticky=SW ) 
# button_0.config(height=1*height_btn,width=7)
# myTip = Hovertip(button_0,'Begins the video.')

# button_1=tkinter.Button(button_Canvas,text="X\nStop\nX",command=def_cng_start_stop(),height=5,width=20,bg='red')
# button_1.grid(row=2,column=1, pady=10,padx=10,sticky=SW ) 
# button_1.config(height=1*height_btn,width=7)
# button_1['state'] = DISABLED




button_2=tkinter.Button(button_Canvas,text="+\nbigger\n+",command=def_bigger,height=5,width=20 ,bg='yellow')
button_2.grid(row=3,column=1, pady=10,padx=10,sticky=SW ) 
button_2.config(height=1*height_btn,width=7)
button_2['state'] = DISABLED

button_3=tkinter.Button(button_Canvas,text="_\nsmaller\n-",command=def_smaller,height=5,width=20,bg='orange')
button_3.grid(row=4,column=1, pady=10,padx=10,sticky=SW ) 
button_3.config(height=1*height_btn,width=7)
button_3['state'] = DISABLED

button_4=tkinter.Button(button_Canvas,text="<> flip",command=def_flip,height=5,width=20,bg='purple')
button_4.grid(row=6,column=1, pady=10,padx=10,sticky=SW ) 
button_4.config(height=1*height_btn,width=7)
button_4['state'] = DISABLED
myTip = Hovertip(button_4,'inverse the framed video.')

button_5=tkinter.Button(button_Canvas,text="save\nframe",command=def_save,height=5,width=20,bg='lightblue')
button_5.grid(row=5,column=1, pady=10,padx=10,sticky=SW ) 
button_5.config(height=1*height_btn,width=7)
button_5['state'] = DISABLED
myTip = Hovertip(button_5,'save picture of \nthe current framed video, \nin the folder of the program.')
global saved
saved = False

button_6=tkinter.Button(move_Canvas,text="0,0",command=def_0_0,height=5,width=20,bg='pink')
button_6.grid(row=3,column=1,pady=10,padx=10)
button_6.config(height=1,width=2)
button_6['state'] = DISABLED
myTip = Hovertip(button_6,'move back the video to \nthe edges of the window.')

button_9=tkinter.Button(move_Canvas,text="RST",command=def_reset_all,height=5,width=20,bg='pink')
button_9.grid(row=3,column=2,pady=10,padx=10)
button_9.config(height=1,width=3)
#button_9['state'] = DISABLED
myTip = Hovertip(button_9,'restart the program \nall over again.')

button_7=tkinter.Button(move_Canvas,text="F-",command=def_factor_minus,height=5,width=20,bg='pink')
button_7.grid(row=1,column=1,pady=10,padx=10)
button_7.config(height=1,width=2)
button_7['state'] = DISABLED

button_8=tkinter.Button(move_Canvas,text="F+",command=def_factor_plus,height=5,width=20,bg='pink')
#button_8.grid(row=2,column=1,pady=10,padx=10)
button_8.grid(row=1,column=2,pady=10,padx=10)
button_8.config(height=1,width=2)
button_8['state'] = DISABLED

# @@@@@@@@@@@@@   define font   @@@@@@@@@@@@@@@@@
myFont = font.Font(family='Helvetica', size=20, weight='bold')
button_0['font'] = myFont
button_1['font'] = myFont
button_2['font'] = myFont
button_3['font'] = myFont
button_5['font'] = myFont
#button_4['font'] = myFont
button_7['font'] = myFont
button_6['font'] = myFont
button_8['font'] = myFont
button_9['font'] = myFont
# @@@@@@@@@@@@@   define font   @@@@@@@@@@@@@@@@@


# @@@@@@@@@@@@@ buttons @@@@@@@@@@@@@@@@@

my_menu = Menu(ikkuna)
ikkuna.config(menu=my_menu)
fileMenu = Menu(my_menu)
fileMenu.add_command(label="open folder" ,command=def_open_folder,accelerator="Ctrl+o" )
fileMenu.add_command(label="Exit",  command=def_exitme,accelerator="Ctrl+Q")
fileMenu.add_separator()
fileMenu.add_command(label="About", command=def_about,accelerator="Ctrl+A")
my_menu.add_cascade(label="File", menu=fileMenu)
#my_menu['font'] = myFont
fileMenu['font'] = myFont

# @@@@@@@@@@@@@ scrollbars @@@@@@@@@@@@@@@@@

#styled scrollbar help
##https://stackoverflow.com/questions/64538934/how-to-change-the-width-of-a-tkk-scrollbar-in-a-custom-style
##https://stackoverflow.com/questions/18598182/making-a-tkinter-scrollbar-wider
## https://stackoverflow.com/questions/49279580/adjust-scrollbar-height-in-tkinter#:~:text=))%0A%0Amaster.mainloop()-,Now%20it%20is%20working%20properly.%20Here%20the%20complete%20code.,-from%20tkinter%20import
##!https://www.autoscripts.net/horizontal-scrollbar-tkinter-using-grid/

# capture_Canvas.config(scrollregion=capture_Canvas.bbox("all"))

# @@@@@@@@@@@@@ scrollbars @@@@@@@@@@@@@@@@@


# @@@@@@@@@@@@@     Scale bar     @@@@@@@@@@@@@@@@@
#my_scale1 = tkinter.Scale(capture_Canvas, from_=1, to=20, orient='horizontal',command=my_scale_bar_upd,length=200,sliderlength=40,relief='solid',
#my_scale1 = tkinter.Scale(move_Canvas, from_=1, to=20, orient='horizontal',command=my_scale_bar_upd,length=200,sliderlength=40,relief='solid', #instead of f+ f- buttons
my_scale1 = tkinter.Scale(ikkuna, width =50 ,from_=1, to=20, orient='horizontal',command=my_scale_bar_upd,length=200,sliderlength=40,
relief='ridge',
#releif = raised , sunken ,flat, ridge, solid & groove
activebackground='red',bg='yellow',
#sliderwidth=20, #unknown option "-sliderwidth ,sliderheight=40
bd=10,fg='blue',cursor='fleur')


my_scale1.grid(row=0,column=0, sticky=NE) 
my_scale1['state'] = DISABLED
my_scale1['font'] = myFont
# @@@@@@@@@@@@@     Scale bar     @@@@@@@@@@@@@@@@@

path = "./icon/webcam magnifyer icon.ico"
#path = "(__file__)/icon/webcam magnifyer icon.ico"
ikkuna.iconbitmap(path)
  
ikkuna.protocol("WM_DELETE_WINDOW", def_exitme)

ikkuna.mainloop()
# cam.release()
