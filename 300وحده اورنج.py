import requests,hashlib


# number=input("Enter your number: ")

# password=input("Enter your password: ")

number=("01285498704")
print()
password=("elsaftye")

#استخراج ال ctv و ال htv

url="https://services.orange.eg/GetToken.svc/GenerateToken"
header={
  "Content-Type": "application/json; charset=UTF-8"
  }
data='{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'

ctv=requests.post(url,headers=header,data=data).json()["GenerateTokenResult"]["Token"]

htv = hashlib.sha256((ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()

#print(ctv)
#print(htv)


#استخراج ال userid

url2="https://services.orange.eg/SignIn.svc/SignInUser"
header2={
"_ctv":ctv,
"_htv":htv,
"Content-Type":"application/json; charset=UTF-8"
}

data2='{"appVersion": "6.0.1","channel":{"ChannelName":"MobinilAndMe", "Password": "ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"'+number+'","isAndroid": "true","password":"'+password+'"}'

userid=requests.post(url2, headers=header2, data=data2).json()["SignInUserResult"]["UserData"]["UserID"]

#print(userid)


#سحب بيانات الخط 

url1="https://backend.orange.eg/api/V2/Account/GetDialInfo"

hdd= {
"_ctv":ctv,
"_htv":htv,
"OsVersion":"Android10",
"AppVersion":"700",
"IsEasyLogin":"false",
"IsAndroid":"true",
"Content-Type":"application/json; charset=UTF-8",
"Content-Length":"190",
"Host":"backend.orange.eg",
"Connection":"Keep-Alive",
"Accept-Encoding":"gzip",
"User-Agent":"okhttp/3.14.9",
    
    }
    
data3='{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"CurrentVersion":"700","dial":"'+number+'","isCoin":"true","lang":"ar","isEasyLogin":false,"password":"'+password+'"}'


resp=requests.post(url1,headers=hdd,data=data3).json()

print(resp)

#تحكم في الرد واخراج بيانات محدده

system=resp["PlanName"]

print(system)

if "الو" in system:
 print("نظام خطك مطابق ")
else:
 print("عفوأ نظامك خطك غير متوافق")
 
 
url6="https://services.orange.eg/CoinServices.svc/MigrateServiceClass"
 
ctv=requests.post(url,headers=header,data=data).json()["GenerateTokenResult"]["Token"]

htv = hashlib.sha256((ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()

 
head={
 
 "_ctv":ctv,
 "_htv":htv,
 "Content-Type":"application/json; charset=UTF-8",
 "Content-Length":"327",
 "Host":"services.orange.eg",
 "Connection":"Keep-Alive",
 "Accept-Encoding":"gzip",
 "User-Agent":"okhttp/3.14.9"
  }
 
json={"acp":0,"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"currentServiceClassID":"1062","dial":number,"isCoin":"true","lang":"ar","migratedToTariffPlanID":"82","migratedToTariffPlanName":"الو 14","userID":userid,"isEasyLogin":"false","password":password}
 
 
respp=requests.post(url6,headers=head,json=json).json()
 
print(respp)