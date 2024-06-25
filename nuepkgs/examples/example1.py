import datetime

st = datetime.datetime.now()
print(st)

abc = []

for i in range(1,9999):
	print(i)

print("DONE")

et = datetime.datetime.now()
print(et)

print(F"\n\n\tDONE IN: {et-st}\n\n")

