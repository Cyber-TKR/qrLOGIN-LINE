# Coder: CyberTK
# Thx All Support Team
from cybertk.line.api.path import CyberTKQR, \
process, \
  threads, \
    apsss, \
      format1, \
        format2, \
    format3, \
  format4, \
format5

CRED = '\033[91m'
CEND = '\033[0m'

CyberTKAPIWEB = CyberTKQR()

print(CRED + process + CEND)
input(CRED + threads + CEND)

app1 = ["desktopwin"]
app2 = ["lite"]
app3 = ["ipad"]
app4 = ["chrome"]
app5 = ["desktopmac"]


Apps = int(input(CRED + apsss + CEND))

UygulamaADI = ""
if Apps == 1:
  UygulamaADI = UygulamaADI.join(app1) 
  print(CRED + format1 + CEND)
elif Apps == 2:
  UygulamaADI = UygulamaADI.join(app2) 
  print(CRED + format2 + CEND)
elif Apps == 3:
  UygulamaADI = UygulamaADI.join(app3)
  print(CRED + format3 + CEND)
elif Apps == 4:
  UygulamaADI = UygulamaADI.join(app4)
  print(CRED + format4 + CEND)
elif Apps == 5:
  UygulamaADI = UygulamaADI.join(app5)
  print(CRED + format5 + CEND)
else:
    print(CRED + "\nLütfen Geçerli bir uygulama adı seçiniz!\n"+ CEND)
    
WEBS = CyberTKAPIWEB.LOGINAPICLIENT(UygulamaADI)

print("{}".format(WEBS.accessToken))
