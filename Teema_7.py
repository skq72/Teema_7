def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

loetelu=Loe_failist("TextFile1.txt")
print(loetelu)
loetelu.append(input("8-i:"))
loetelu.append(input("9-i:"))
loetelu.append(input("10-i:"))
Kirjuta_failisse("TextFile1.txt", loetelu)
loetelu=Loe_failist("TextFile1.txt")
print(loetelu)