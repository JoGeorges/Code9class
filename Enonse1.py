print("\tBonjou, bonswa chè itilizatè,")
print("\tMwen espere ke ou anfòm gras ak Bondye.")
print("\tPwogram sa la, pou l pèmèt ou kalkile mwayèn ou.")
print("\tByenvini nan pwogram sila a,")
num_notes = int(input("\tPou konbyen nòt ou vle chèche mwayèn lan: "))
deno = int(input("\tSou konbyen nòt sa yo te korije: "))
sum = 0
for i in range(1, num_notes+1):
    note = input("\t - Rantre valè nòt N* " + str(i) + ": ")
    sum += int(note)
print("\tMwayèn ou fè pou nòt sa yo se: " + str((sum/deno)*(10**len(str(deno-1)))) + "/" + str(deno*num_notes))
if ((sum/(deno*num_notes)) >= 0.9):
    print("\tOu jwenn mansyon A\n")
elif ((sum/(deno*num_notes)) < 0.9 and (sum/(deno*num_notes)) >= 0.8):
    print("\tOu jwenn mansyon B\n")
elif ((sum/(deno*num_notes)) < 0.8 and (sum/(deno*num_notes))>= 0.7):
    print("\tOu jwenn mansyon C\n")
elif ((sum/(deno*num_notes)) < 0.7 and (sum/(deno*num_notes)) >= 0.6):
    print("\tOu jwenn mansyon D\n")
else:
    print("\tOu jwenn mansyon F")
print("\tMèsi dèske ou te pran tan pou w itlize pwogram sila a.")
print("\t__GEORGES Jonathan___\n")