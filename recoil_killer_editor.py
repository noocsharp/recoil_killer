from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import os
import win32gui

#Dialog to add vector to recoil
class AddDialog(tkinter.simpledialog.Dialog):
    def __init__(self, parent, host, mode, title = None):
        self.host =  host
        self.mode = mode
        #If mode is 0 then it is in add mode, if 1 it is edit mode, mostly for aesthetic reasons
        super(AddDialog, self).__init__(parent, title=title)
    
    
    def body(self, parent):
        self.x = StringVar()
        self.y = StringVar()
        
        Label(parent, text="x:").grid(row=0)
        Label(parent, text="y:").grid(row=1)

        self.e_x = Entry(parent, textvariable=self.x)
        self.e_x.grid(row=0, column=1)
        
        self.e_y = Entry(parent, textvariable=self.y)
        self.e_y.grid(row=1, column=1)
        
    def validate(self):
        try:
            #saves input in format (x,y) as a tuple
            self.result = (int(self.x.get()), int(self.y.get()))
            return 1
        except ValueError:
            tkinter.messagebox.showwarning("Bad Input", "Please enter valid values")
            return 0
    
	#sends data back instance of app class
    def apply(self):
        if self.mode == 0: self.host.save_data(self.result)
        elif self.mode == 1: self.host.edit_data(self.result)
        elif self.mode == 2: self.host.insert_data(self.result)

class RecoilKillerEditor:
    
    def __init__(self, master):
        self.master = master
		#default values for items that will later be prompted for
        self.sensitivity=1.0
        self.current_file = None
        self.time_interval = .1
        self.data = []
        
		#sets up gui element in main window
        frame = Frame(master)
        frame.pack(fill=BOTH, expand=True)
        
        frame_lb = Frame(frame)
        frame_lb.pack(fill=BOTH, expand=True)
        
        self.scrollbar = Scrollbar(frame_lb)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.listbox = Listbox(frame_lb)
        self.listbox.pack(side=TOP, fill=BOTH, expand=True)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        button_frame = Frame(frame)
        button_frame.pack(fill=X)
        
        self.b_add = Button(button_frame, text="Add", command=self.open_add_dialog)
        self.b_add.pack(side=LEFT, fill=X, expand=1)

        self.b_add = Button(button_frame, text="Edit", command=self.open_edit_dialog)
        self.b_add.pack(side=LEFT, fill=X, expand=1)
        
        self.b_add = Button(button_frame, text="Insert", command=self.open_insert_dialog)
        self.b_add.pack(side=LEFT, fill=X, expand=1)
        
        self.b_delete = Button(button_frame, text="Delete", command=self.delete_data)
        self.b_delete.pack(side=LEFT, fill=X, expand=1)
        
        button_frame2 = Frame(frame)
        button_frame2.pack(fill=X)
        
        self.b_sensitivity = Button(button_frame2, text="Sensitivity", command=self.prompt_sensitivity)
        self.b_sensitivity.pack(side=LEFT, fill=X, expand=1)
        
        self.b_sensitivity = Button(button_frame2, text="Time Interval", command=self.prompt_time_interval)
        self.b_sensitivity.pack(side=RIGHT, fill=X, expand=1)

        button_frame3 = Frame(frame)
        button_frame3.pack(fill=X)
        
        self.b_write = Button(button_frame3, text="Write", command=self.write)
        self.b_write.pack(side=LEFT, fill=X, expand=1)

        self.b_read = Button(button_frame3, text="Read", command=self.read)
        self.b_read.pack(side=LEFT, fill=X, expand=1)
        
        self.b_read = Button(button_frame3, text="Write + Test", command=self.write_and_test)
        self.b_read.pack(side=RIGHT, fill=X, expand=1)

        
	#takes data from AddDialog and updates app class and gui
    def save_data(self, result):
        self.listbox.insert(END, ", ".join([str(i) for i in result]))
        self.data.append(result)
        print(self.data)
    
    def delete_data(self, index):
        self.listbox.delete(index)
        del self.data[index-1]
        print(self.data)
       
    def edit_data(self, result):
        self.insert_data(result)
        self.delete_data(self.listbox.index(ACTIVE))
        print(self.data)
        
    def insert_data(self, result):
        self.listbox.insert(ACTIVE, ", ".join([str(i) for i in result]))
        self.data.insert(self.listbox.index(ACTIVE), result)
        print(self.data)
	#creates an add dialog as a callback
    def open_add_dialog(self):
        a = AddDialog(parent=root, host=self, mode=0, title="Add vector")
    
    def open_edit_dialog(self):
        a = AddDialog(parent=root, host=self, mode=1, title="Edit vector")
	
    def open_insert_dialog(self):
        a = AddDialog(parent=root, host=self, mode=2, title="Insert vector")
    
	#creates sensitivity prompt and validates
    def prompt_sensitivity(self):
        self.sensitivity = tkinter.simpledialog.askfloat("Change Sensitivity", "New sens", initialvalue=self.sensitivity)
        
    def prompt_time_interval(self):
        self.time_interval = tkinter.simpledialog.askfloat("Change time inverval", "New time interval", initialvalue=self.time_interval)
    
	#creates filename, doesn't validate
    def prompt_filename(self):
        self.current_file = tkinter.simpledialog.askstring("Filename", "Filename", initialvalue=(self.current_file if self.current_file else ""))
    
    def update_listbox(self):
        self.listbox.delete(0, END)
        for i in self.data:
            self.listbox.insert(END, str(i[0]) + ", " + str(i[1]))
    
	#writes data to a python script
    def write(self):
        self.prompt_filename()
        if self.current_file:
            file = open(os.path.join("scripts", self.current_file), 'w')
            file.write("#" + str(len(self.data)) + "," + str(self.sensitivity) + "," + str(self.time_interval) + "\n#")
            for i in self.data:
                file.write(str(i[0]) + "," + str(i[1]) + "*")
            
            file.write("\n")
            file.write("""
import win32api, win32con
import time
sens = {0}
time_interval = {1}

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
""".format(self.sensitivity, self.time_interval))
            for i in self.data:
                file.write("""
time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int({0}/sens),int({1}/sens))\n""".format(i[0], i[1]))
        
            file.write("win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)")
            file.close()
        
		
	#reads data from a python script
    def read(self):

        self.prompt_filename()
        if self.current_file:
            file = open(os.path.join("scripts", self.current_file), 'r')
            
            var_data = file.readline()[1:-1].split(",")
            print (var_data)
            self.sensitivity = float(var_data[1])
            self.time_interval = float(var_data[2])
            
            #reads seconds line with data
            data_string = file.readline()
            
            temp_data = []
            split_data = data_string[1:].split("*")[:-1]
            print(split_data)
            for i in split_data:
                temp_data.append(tuple([int(j) for j in i.split(",")]))
            
            self.data = temp_data
            print(self.data)
            file.close()
            
            self.update_listbox()
        
    def write_and_test(self):
        if self.current_file:
            file = open(os.path.join("scripts", self.current_file), 'w')
            file.write("#" + str(len(self.data)) + "," + str(self.sensitivity) + "," + str(self.time_interval) + "\n#")
            for i in self.data:
                file.write(str(i[0]) + "," + str(i[1]) + "*")
            
            file.write("\n")
            file.write("""
import win32api, win32con
import time
sens = {0}
time_interval = {1}

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
""".format(self.sensitivity, self.time_interval))
            for i in self.data:
                file.write("""
time.sleep(time_interval)
win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int({0}/sens),int({1}/sens))\n""".format(i[0], i[1]))
        
            file.write("win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)")
            file.close()
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if "Counter-Strike: Global Offensive" in i[1]:
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                break
        else:
            tkinter.messagebox.showwarning("CS not open", "Please open CS:GO")

        if self.current_file:
            os.system("python " + os.path.join("scripts", self.current_file))
        else:
            self.prompt_filename()
            os.system("python " + os.path.join("scripts", self.current_file))

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Recoil Killer Editor")
    root.geometry('{0}x{1}'.format(200,300))
    app = RecoilKillerEditor(root)

    root.mainloop()