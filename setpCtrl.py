import wx
import string

class setpCtrl(wx.Panel):

    def __init__(self, parent, max,size=wx.DefaultSize):
        self.max = max
        wx.Panel.__init__(self,parent,size=size)

        self.sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.textCtrl = wx.TextCtrl(self)
        self.sizer.Add(self.textCtrl,flag=wx.EXPAND,proportion=1)
        self.spin1 = wx.SpinButton(self)
        self.sizer.Add(self.spin1,flag=wx.EXPAND,proportion=0)
        self.spin2 = wx.SpinButton(self)
        self.sizer.Add(self.spin2,flag=wx.EXPAND,proportion=0)
        self.spin3 = wx.SpinButton(self)
        self.sizer.Add(self.spin3,flag=wx.EXPAND,proportion=0)
        print("test")

        self.SetSizer(self.sizer)
        self.sizer.Fit(self)



class setpValidator(wx.PyValidator):
    def __init__(self, max):
        wx.Validator.__init__(self)
        self.max = max
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        return setpValidator(self.max)

    def Validate(self, win):
        return True
    
    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

    def OnChar(self, event):
        keycode = int(event.GetKeyCode())
        key = chr(keycode)
        
        if key in string.digits or key == ".":
            text = self.GetWindow().Value + key 
            if text.count(".") > 1:
                return
            if float(text) > self.max:
                return
            event.Skip()
        elif key in string.ascii_letters or key in string.punctuation:
            return
        event.Skip()
