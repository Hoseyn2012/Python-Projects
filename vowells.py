s=str(input("Soz de "))
sait="aioueAIOUE"
count=0
for i in s:
    if i in sait:
        count+=1
print("Saitlerin sayi:",count)