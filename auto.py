import win32api, win32con
import time
import sys

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def start(arrows): 
    for i in range(0,(arrows/150)+1,1):
        print 150*(i+1), ' arrows'
        click(1249,386)
        time.sleep(3)
        click(987,516)
        time.sleep(12) 
    print '----'
    print 'Done'

arrows = int(sys.argv[1])
start(arrows)