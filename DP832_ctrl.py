import wx
import string
from DP832 import DP832
from setpCtrl import setpCtrl, setpValidator
import os
import json

configFileName = "DP832_config.json"

class controlConfig():
    def __init__(self,filename):
        self.filename = filename
        self.config = {
            "IP":"",
            "test": 22
        }

    def readConfig(self):
        if os.path.isfile(self.filename):
            f = open(self.filename,"r")
            readConfig = json.load(f)
            for k in readConfig.keys():
                if k in self.config.keys():
                    self.config[k] = readConfig[k]
    def writeConfig(self):
        f = open(self.filename,"w")
        json.dump(self.config,f)

class Frame(wx.Frame,controlConfig):
    def __init__(self, title):
        frameStyle = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.STAY_ON_TOP
        wx.Frame.__init__(self, None, title=title, pos=(150,150), size=(350,200), style=frameStyle)
        controlConfig.__init__(self,configFileName)
        panel = wx.Panel(self)
        grid = wx.GridBagSizer(hgap=10,vgap=10)
        #grid.AddStretchSpacer()
        ch1Text = wx.StaticText(panel,-1,"CH1")
        grid.Add(ch1Text,pos=wx.GBPosition(0,1),flag=wx.ALIGN_CENTER_HORIZONTAL)
        ch2Text = wx.StaticText(panel,-1,"CH2")
        grid.Add(ch2Text,pos=wx.GBPosition(0,2),flag=wx.ALIGN_CENTER_HORIZONTAL)
        ch3Text = wx.StaticText(panel,-1,"CH3")
        grid.Add(ch3Text,pos=wx.GBPosition(0,3),flag=wx.ALIGN_CENTER_HORIZONTAL)
        #voltage measurements
        measSizerFlags =  wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT
        measVText = wx.StaticText(panel,-1,"meas V")
        grid.Add(measVText,pos=wx.GBPosition(1,0),flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT)
        self.CH1measVctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH1measVctrl,pos=wx.GBPosition(1,1),flag=measSizerFlags)
        self.CH2measVctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH2measVctrl,pos=wx.GBPosition(1,2),flag=measSizerFlags)
        self.CH3measVctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH3measVctrl,pos=wx.GBPosition(1,3),flag=measSizerFlags)
        ##Current measurements
        measIText = wx.StaticText(panel,-1,"meas I")
        grid.Add(measIText,pos=wx.GBPosition(2,0),flag=measSizerFlags)
        self.CH1measIctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH1measIctrl,pos=wx.GBPosition(2,1),flag=measSizerFlags)
        self.CH2measIctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH2measIctrl,pos=wx.GBPosition(2,2),flag=measSizerFlags)
        self.CH3measIctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH3measIctrl,pos=wx.GBPosition(2,3),flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        ##Power measurements
        measPText = wx.StaticText(panel,-1,"meas P")
        grid.Add(measPText,pos=wx.GBPosition(3,0),flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT)
        self.CH1measPctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH1measPctrl,pos=wx.GBPosition(3,1),flag=measSizerFlags)
        self.CH2measPctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH2measPctrl,pos=wx.GBPosition(3,2),flag=measSizerFlags)
        self.CH3measPctrl = wx.TextCtrl(panel,style=wx.TE_READONLY)
        grid.Add(self.CH3measPctrl,pos=wx.GBPosition(3,3),flag=measSizerFlags)
        
        ##line separator
        line = wx.StaticLine(panel,size=wx.Size(0,3),style=wx.LI_HORIZONTAL)
        grid.Add(line,pos=wx.GBPosition(4,0),span=wx.GBSpan(1,5),flag=wx.EXPAND)

        #setpoint
        
        setpVText = wx.StaticText(panel,-1,"V setp.")
        grid.Add(setpVText,pos=wx.GBPosition(5,0),flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT)
        self.CH1Vsetpctrl = wx.SpinCtrlDouble(panel,initial=0,min=0,max=30,inc=0.02)
        grid.Add(self.CH1Vsetpctrl,pos=wx.GBPosition(5,1),flag=measSizerFlags | wx.EXPAND)
        self.CH2Vsetpctrl = wx.SpinCtrlDouble(panel,initial=0,min=0,max=30,inc=0.02)
        grid.Add(self.CH2Vsetpctrl,pos=wx.GBPosition(5,2),flag=measSizerFlags | wx.EXPAND)
        self.CH3Vsetpctrl = wx.SpinCtrlDouble(panel,initial=0,min=0,max=5,inc=0.02)
        grid.Add(self.CH3Vsetpctrl,pos=wx.GBPosition(5,3),flag=measSizerFlags | wx.EXPAND)
        setpIText = wx.StaticText(panel,-1,"I setp.")
        grid.Add(setpIText,pos=wx.GBPosition(6,0),flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT)
        self.CH1Isetpctrl = wx.SpinCtrlDouble(panel,initial=0,min=0,max=3,inc=0.02)
        grid.Add(self.CH1Isetpctrl,pos=wx.GBPosition(6,1),flag=measSizerFlags | wx.EXPAND)
        self.CH2Isetpctrl = wx.SpinCtrlDouble(panel,initial=0,min=0,max=3,inc=0.02)
        grid.Add(self.CH2Isetpctrl,pos=wx.GBPosition(6,2),flag=measSizerFlags | wx.EXPAND)
        self.CH3Isetpctrl = wx.SpinCtrlDouble(panel,initial=0,min=0,max=3,inc=0.02)
        grid.Add(self.CH3Isetpctrl,pos=wx.GBPosition(6,3),flag=measSizerFlags | wx.EXPAND)

        #buttons
        self.CH1outpButton = wx.ToggleButton(panel,label="CH1")
        grid.Add(self.CH1outpButton,pos=wx.GBPosition(7,1),flag=measSizerFlags | wx.EXPAND)
        self.CH2outpButton = wx.ToggleButton(panel,label="CH2")
        grid.Add(self.CH2outpButton,pos=wx.GBPosition(7,2),flag=measSizerFlags | wx.EXPAND)
        self.CH3outpButton = wx.ToggleButton(panel,label="CH3")
        grid.Add(self.CH3outpButton,pos=wx.GBPosition(7,3),flag=measSizerFlags | wx.EXPAND)

        self.menubar = wx.MenuBar()
        self.connectMenu = wx.Menu()
        self.menubar.Append(self.connectMenu,"Connect")
        self.configMenu = wx.Menu()
        self.menubar.Append(self.configMenu,"Configure")

        self.connectMenu.Bind(wx.EVT_MENU_OPEN,self.onConnect)
        self.configMenu.Bind(wx.EVT_MENU_OPEN,self.onConfigure)

        self.SetMenuBar(self.menubar)
        
        grid.Add(0,0,pos=wx.GBPosition(8,4),flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        panel.SetSizer(grid)
        grid.Fit(self)


        self.meastimer = wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER, self.OnMeasTimer, self.meastimer)
        self.setptimer = wx.Timer(self,-1)
        self.Bind(wx.EVT_TIMER, self.OnSetpTimer, self.setptimer)        

        self.Bind(wx.EVT_TOGGLEBUTTON,self.OnOutpEdit,self.CH1outpButton)
        self.Bind(wx.EVT_TOGGLEBUTTON,self.OnOutpEdit,self.CH2outpButton)
        self.Bind(wx.EVT_TOGGLEBUTTON,self.OnOutpEdit,self.CH3outpButton)

        self.Bind(wx.EVT_SPINCTRLDOUBLE,self.OnCh1Edit,self.CH1Vsetpctrl)
        self.Bind(wx.EVT_SPINCTRLDOUBLE,self.OnCh1Edit,self.CH1Isetpctrl)
        self.Bind(wx.EVT_SPINCTRLDOUBLE,self.OnCh2Edit,self.CH2Vsetpctrl)
        self.Bind(wx.EVT_SPINCTRLDOUBLE,self.OnCh2Edit,self.CH2Isetpctrl)
        self.Bind(wx.EVT_SPINCTRLDOUBLE,self.OnCh3Edit,self.CH3Vsetpctrl)
        self.Bind(wx.EVT_SPINCTRLDOUBLE,self.OnCh3Edit,self.CH3Isetpctrl)
        #self.Bind(wx.EVT_TEXT_ENTER,self.OnCh1Edit,self.CH1Vsetpctrl)
        #self.Bind(wx.EVT_TEXT_ENTER,self.OnCh1Edit,self.CH1Isetpctrl)
        print(self.CH1measIctrl.GetSize())
        self.psu = DP832()

    def onConnect(self,evt):
        self.readConfig()
        if self.psu.connected:
            self.psu.disconnect()
        else:
            self.psu.connect('TCPIP0::{}::INSTR'.format(self.config["IP"]))        
        if self.psu.connected:
            self.menubar.SetMenuLabel(0,"Disconnect")
            self.psu.readSetps()
            self.psu.readOutp()
            self.updateSetps()
            self.meastimer.Start(50)
            print("Connected")
        else:
            self.menubar.SetMenuLabel(0,"Connect")  
    
        #evt.Skip()

    def onConfigure(self,evt):
        dialog = ConfigPopup(self,0)
        dialog.ShowModal()

    def OnMeasTimer(self,evt):
        if self.psu.connected == 0:
            self.meastimer.Stop()
            self.setptimer.Stop()
            self.menubar.SetMenuLabel(0,"Connect")
            return
        self.psu.measAll()

        if self.psu.connected == 0:
            self.meastimer.Stop()
            self.setptimer.Stop()
            self.menubar.SetMenuLabel(0,"Connect")
            return
        self.updateMeas()

    def OnSetpTimer(self,evt):
        if self.psu.connected == 0:
            self.meastimer.Stop()
            self.setptimer.Stop()
            return
        self.psu.readSetps()
        self.psu.readOutp()

        if self.psu.connected == 0:
            self.meastimer.Stop()
            self.setptimer.Stop()
            return
        self.updateSetps()

    def OnOutpEdit(self,evt):
        self.psu.CH1Outp = self.CH1outpButton.Value
        self.psu.CH2Outp = self.CH2outpButton.Value
        self.psu.CH3Outp = self.CH3outpButton.Value
        self.psu.setOutps()
        self.psu.readOutp()
        self.updateSetps()
    
    def OnCh1Edit(self,evt):
        self.psu.SetChannelStps(1,self.CH1Vsetpctrl.Value,self.CH1Isetpctrl.Value)
        self.psu.readSetps()
        self.psu.readOutp()
        self.updateSetps()

    def OnCh2Edit(self,evt):
        self.psu.SetChannelStps(2,self.CH2Vsetpctrl.Value,self.CH2Isetpctrl.Value)
        self.psu.readSetps()
        self.psu.readOutp()
        self.updateSetps()

    def OnCh3Edit(self,evt):
        self.psu.SetChannelStps(3,self.CH3Vsetpctrl.Value,self.CH3Isetpctrl.Value)
        self.psu.readSetps()
        self.psu.readOutp()
        self.updateSetps()

    def updateMeas(self):
        self.CH1measVctrl.SetValue("{:.2f} V".format(self.psu.CH1Vmeas))
        self.CH1measIctrl.SetValue("{:.2f} A".format(self.psu.CH1Imeas))
        self.CH1measPctrl.SetValue("{:.2f} W".format(self.psu.CH1Pmeas))
        self.CH2measVctrl.SetValue("{:.2f} V".format(self.psu.CH2Vmeas))
        self.CH2measIctrl.SetValue("{:.2f} A".format(self.psu.CH2Imeas))
        self.CH2measPctrl.SetValue("{:.2f} W".format(self.psu.CH2Pmeas))
        self.CH3measVctrl.SetValue("{:.2f} V".format(self.psu.CH3Vmeas))
        self.CH3measIctrl.SetValue("{:.2f} A".format(self.psu.CH3Imeas))
        self.CH3measPctrl.SetValue("{:.2f} W".format(self.psu.CH3Pmeas))

    def updateSetps(self):
        self.CH1Vsetpctrl.SetValue(self.psu.CH1Vsetp)
        self.CH1Isetpctrl.SetValue(self.psu.CH1Isetp)
        self.CH2Vsetpctrl.SetValue(self.psu.CH2Vsetp)
        self.CH2Isetpctrl.SetValue(self.psu.CH2Isetp)
        self.CH3Vsetpctrl.SetValue(self.psu.CH3Vsetp)
        self.CH3Isetpctrl.SetValue(self.psu.CH3Isetp)
        self.CH1outpButton.SetValue(self.psu.CH1Outp)
        self.CH2outpButton.SetValue(self.psu.CH2Outp)
        self.CH3outpButton.SetValue(self.psu.CH3Outp)

    def OnInCtrl(self,evt):
        self.outctrl.SetValue(self.inctrl.Value)
    def OnInCtrl2(self,evt):
        self.outctrl.SetValue("asd")

class ConfigPopup(wx.Dialog,controlConfig):
    def __init__(self, parent, style):
        wx.Dialog.__init__(self, parent, style,title="Instrument configuration")
        controlConfig.__init__(self,configFileName)
        self.panel = wx.Panel(self)
        self.readConfig()
        v1s = wx.BoxSizer(wx.VERTICAL)

        h1s = wx.BoxSizer(wx.HORIZONTAL)
        self.ipText = wx.StaticText(self.panel,-1,"IP : ")
        h1s.Add(20,0)
        h1s.Add(self.ipText)
        self.ipTextctrl = wx.TextCtrl(self.panel)
        self.ipTextctrl.Value = self.config["IP"]
        h1s.Add(self.ipTextctrl)
        h1s.Add(20,0)

        v1s.Add(0,20)
        v1s.Add(h1s)

        self.okButton = wx.Button(self.panel, label="OK")
        v1s.Add(self.okButton,1,wx.ALIGN_CENTER)

        self.okButton.Bind(wx.EVT_BUTTON,self.onOk)

        v1s.Add(0,20)

        self.panel.SetSizer(v1s)
        v1s.Fit(self)
        self.Centre() 

        self.Show()
        
    def onOk(self,evt):
        self.config["IP"] = self.ipTextctrl.Value
        self.writeConfig()
        self.Close()
        

app = wx.App(redirect=False)
top = Frame("DP832 Control")
top.Show()
app.MainLoop()


