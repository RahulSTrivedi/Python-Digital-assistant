import wx
import wikipedia
import wolframalpha
import os
import pyttsx3
import win32

engine=pyttsx3.init()
engine.setProperty("rate",115)
engine.setProperty("volume",0.9)
engine.say("Welcome! How can I help you?")
engine.runAndWait()
#set a main class for the app frame


class cannotfind(Exception):
    pass

class MyFrame(wx.Frame):
    def __init__(self):        
        #set some basic gui info about the app
        wx.Frame.__init__(self, None, 
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, 
        label="Hello I am  Python  Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        
        #set up a simple text box with the following properties
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        print("Wait a moment...")
        try:
        #wolframalpha code here
            #app_id = "Q2HXJ5-GYYYX6PYYP"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text 
            
            engine.say("You are searching for"+str(input))
            engine.runAndWait()

            print(answer)

            engine.say("The answer is"+str(answer))
            engine.runAndWait()
      
    
        except:
        #wikipedia code here
             engine.say("You are searching for"+str(input))
             engine.runAndWait()
             output=wikipedia.summary(input)
             print(output)
           

    #run the app with the below code
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
        