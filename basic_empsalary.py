ename = input("Enter employee name:")
edes = input("Enter employee desgnation:")
esal = int(input("Enter employee salary:"))

print("------------------------------")
print("employee name:", ename)
print("employee desgnation:", edes)
print("before employee salary:", esal)

if edes=="HR" or edes=="hr" or edes=="Hr":
	# esal = esal + (esal*0.10)
	esal = esal * 1.10
elif edes=="TL" or edes=="tl" or edes=="Tl":
	esal = esal + (esal*0.15)
elif edes=="MANAGER" or edes=="manager" or edes=="Manager":
	esal = esal + (esal*0.20)

print("after employee salary:",esal)