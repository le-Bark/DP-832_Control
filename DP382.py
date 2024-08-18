import pyvisa

class DP832():
    def __init__(self):
        print("dp832_init")
        self.instr = None
        self.connected = False
        self.CH1setp = (0,0,0)

        self.CH1Vsetp = 0
        self.CH1Isetp = 0
        self.CH2Vsetp = 0
        self.CH2Isetp = 0
        self.CH3Vsetp = 0
        self.CH3Isetp = 0

        self.CH1Vmeas = 0
        self.CH1Imeas = 0
        self.CH1Pmeas = 0
        self.CH2Vmeas = 0
        self.CH2Imeas = 0
        self.CH2Pmeas = 0
        self.CH3Vmeas = 0
        self.CH3Imeas = 0
        self.CH3Pmeas = 0

        self.CH1Outp = 0
        self.CH2Outp = 0
        self.CH3Outp = 0

    def disconnect(self):
        self.instr = None
        self.connected = False
    def connect(self,ressource):
        self.instr = None
        self.connected = False
        try:
            self.instr = pyvisa.ResourceManager().open_resource(ressource)
        except:
            return
        if self.instr:
            
            self.instr.read_termination = '\r\n'
            self.instr.write_termination = '\r\n'
            self.instr.timeout = 100
            idn = self.instr.query("*IDN?").strip()
            if "DP832" in idn:
                self.connected = True
            else:
                self.instr = None
            print(idn)
    
    def readSetps(self):
        try:
            res = self.instr.query(":APPL? " "CH1")
            res = res.strip().split(",")
            self.CH1Vsetp = float(res[1])
            self.CH1Isetp = float(res[2])

            res = self.instr.query(":APPL? " "CH2")
            res = res.strip().split(",")
            self.CH2Vsetp = float(res[1])
            self.CH2Isetp = float(res[2])

            res = self.instr.query(":APPL? " "CH3")
            res = res.strip().split(",")
            self.CH3Vsetp = float(res[1])
            self.CH3Isetp = float(res[2])
        except:
            self.disconnect()

    def measAll(self):
            try:
                res = self.instr.query(":meas:all? " "CH1")
            except:
                self.instr = None
                self.connected = False
                return
            res = res.strip().split(",")
            self.CH1Vmeas = float(res[0])
            self.CH1Imeas = float(res[1])
            self.CH1Pmeas = float(res[2])

            res = self.instr.query(":meas:all? " "CH2")
            res = res.strip().split(",")
            self.CH2Vmeas = float(res[0])
            self.CH2Imeas = float(res[1])
            self.CH2Pmeas = float(res[2])

            res = self.instr.query(":meas:all? " "CH3")
            res = res.strip().split(",")
            self.CH3Vmeas = float(res[0])
            self.CH3Imeas = float(res[1])
            self.CH3Pmeas = float(res[2])

    def readOutp(self):
            outp = {"ON":1, "OFF":0}
            res = self.instr.query(":OUTP? " "CH1").strip()
            self.CH1Outp = outp[res]
            res = self.instr.query(":OUTP? " "CH2").strip()
            self.CH2Outp = outp[res]
            res = self.instr.query(":OUTP? " "CH3").strip()
            self.CH3Outp = outp[res]
    
    def setOutps(self):
         onoff = ["OFF","ON"]
         self.instr.write(":OUTP CH1," + onoff[int(self.CH1Outp)])
         self.instr.write(":OUTP CH2," + onoff[int(self.CH2Outp)])
         self.instr.write(":OUTP CH3," + onoff[int(self.CH3Outp)])

    def SetChannelStps(self,channel,v,i):
         self.instr.write(":APPL CH{},{:.2f},{:.2f}".format(channel,v,i))