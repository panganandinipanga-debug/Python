class wv1:
    def __init__(self,messaging,status,audiocall):
        self.messaging = messaging
        self.status    = status
        self.audiocall = audiocall
    def features(self):
        print(f'message  = {self.messaging}')
        print(f'status   = {self.status}')
        print(f'audiocall= {self.audiocall}')
class wv2(wv1):
    def __init__(self,messaging,status,audiocall,vdcall,voicemsg):
        wv1.__init__(self,messaging,status,audiocall)
        self.vdcall = vdcall
        self.voicemsg = voicemsg
    def fetures(self):
        wv1.features(self)
        print(f'vdcall   = {self.vdcall}')
        print(f'voicemsg = {self.voicemsg}')
class wv3(wv2):
    def __init__(self,messaging,status,audiocall,vdcall,voicemsg,payments,meta):
       super().__init__(messaging,status,audiocall,vdcall,voicemsg)
       self.payments = payments
       self.meta = meta
    def fetures(self):
        wv2.features(self)
        print(f'payments = {self.payments}')
        print(f'meta     = {self.meta}')
user3=wv3('hello','possible','possible','possible','possible','possible','possible')
user3.features()


                 

