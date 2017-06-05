#20,2.0,0.1
#0,0*0,8*0,28*0,36*0,42*0,44*0,60*52,52*20,0*-30,15*-30,14*-30,-10*0,-50*-50,0*-50,0*50,50*0,0*-50,-50*0,0*0,0*

import win32api, win32con
import time
sens = 2.0
time_interval = 0.1

#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(0/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(8/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(28/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(36/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(42/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(44/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(60/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(52/sens),int(52/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(20/sens),int(0/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(-30/sens),int(15/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(-30/sens),int(14/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(-30/sens),int(-10/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(-50/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(-50/sens),int(0/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(-50/sens),int(0/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(50/sens),int(50/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(0/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(-50/sens),int(-50/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(0/sens))

time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(0/sens),int(0/sens))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)