from tkinter import *
import os
import pyHook

class RecoilKillerClient:
    def __init__(self, master):
        self.master = master
        
        self.can_spray = False
        self.spraying = False
        
        frame = Frame(master)
        frame.pack(fill=BOTH, expand=True)
        
        self.scrollbar = Scrollbar(frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.listbox = Listbox(frame)
        self.listbox.pack(fill=BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        self.script_files = [file for file in os.listdir("scripts") if os.path.isfile(os.path.join("scripts", file))]
        
        self.hm = pyHook.HookManager()
        self.hm.MouseAll = self.OnMouseEvent
        self.hm.HookMouse()
        
        self.hm.KeyAll = self.OnKeyboardEvent
        self.hm.HookKeyboard()
        
        for i in self.script_files:
            self.listbox.insert(END, i)
            
    def onselect(self, evt):
        w = evt.widget
        if w is self.listbox:
            self.current_file = self.listbox.get(ACTIVE)
            print(self.current_file)
    
    def run_script(self):
        os.system("python " + os.path.join("scripts", self.current_file))
    
    def OnMouseEvent(self, event):
        # called when mouse events are received

        if event.MessageName == "mouse left down" and event.WindowName == "Counter-Strike: Global Offensive":
            if self.can_spray:
                self.run_script()
                self.spraying = True
                return False
        # return True to pass the event to other handlers
        return True
    
    def OnKeyboardEvent(self, event):
        if event.Key == '1' and event.WindowName == "Counter-Strike: Global Offensive":
            self.can_spray = True
        
        elif (event.Key == '2' or event.Key == '3' or event.Key == '4') and event.WindowName == "Counter-Strike: Global Offensive":
            self.can_spray = False
        return True
        
if __name__ == "__main__":
    root = Tk()
    root.wm_title("Recoil Killer")
    app = RecoilKillerClient(root)
    
    root.mainloop()