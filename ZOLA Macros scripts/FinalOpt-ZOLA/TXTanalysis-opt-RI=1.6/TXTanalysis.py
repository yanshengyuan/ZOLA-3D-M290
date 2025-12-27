from math import ceil, isnan

# Open the text file
with open("bench.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

residuals=[]
for i in range(1, ceil(len(lines)/46)):
    residuals.append(float(lines[46*i][17:-1]))
    
fail=0
success=0
reconsErr=0.0
for i in range(len(residuals)):
    if(isnan(residuals[i])):
        fail+=1
    else:
        reconsErr+=residuals[i]
        success+=1
reconsErr/=success

print('\n')
print("ZOLA Phase Retrieval Report: Bench")
print("NME(pix): ", reconsErr)
print("Success: ", success)
print("Failure: ", fail)
print("Failure Rate: ", fail/3000)

with open("gaussian.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

residuals=[]
for i in range(len(lines)):
    if(lines[i][:6]=="global"):
        residuals.append(float(lines[i][17:-1]))
    
fail=0
success=0
reconsErr=0.0
for i in range(len(residuals)):
    if(isnan(residuals[i])):
        fail+=1
    else:
        reconsErr+=residuals[i]
        success+=1
reconsErr/=success

print('\n')
print("ZOLA Phase Retrieval Report: Gaussian")
print("NME(pix): ", reconsErr)
print("Success: ", success)
print("Failure: ", fail)
print("Failure Rate: ", fail/3000)

with open("tear.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

residuals=[]
for i in range(len(lines)):
    if(lines[i][:6]=="global"):
        residuals.append(float(lines[i][17:-1]))
    
fail=0
success=0
reconsErr=0.0
for i in range(len(residuals)):
    if(isnan(residuals[i])):
        fail+=1
    else:
        reconsErr+=residuals[i]
        success+=1
reconsErr/=success

print('\n')
print("ZOLA Phase Retrieval Report: Tear")
print("NME(pix): ", reconsErr)
print("Success: ", success)
print("Failure: ", fail)
print("Failure Rate: ", fail/3000)

with open("rec.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

residuals=[]
for i in range(len(lines)):
    if(lines[i][:6]=="global"):
        residuals.append(float(lines[i][17:-1]))
    
fail=0
success=0
reconsErr=0.0
for i in range(len(residuals)):
    if(isnan(residuals[i])):
        fail+=1
    else:
        reconsErr+=residuals[i]
        success+=1
reconsErr/=success

print('\n')
print("ZOLA Phase Retrieval Report: Rec")
print("NME(pix): ", reconsErr)
print("Success: ", success)
print("Failure: ", fail)
print("Failure Rate: ", fail/3000)

with open("hat.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

residuals=[]
for i in range(len(lines)):
    if(lines[i][:6]=="global"):
        residuals.append(float(lines[i][17:-1]))
    
fail=0
success=0
reconsErr=0.0
for i in range(len(residuals)):
    if(isnan(residuals[i])):
        fail+=1
    else:
        reconsErr+=residuals[i]
        success+=1
reconsErr/=success

print('\n')
print("ZOLA Phase Retrieval Report: Hat")
print("NME(pix): ", reconsErr)
print("Success: ", success)
print("Failure: ", fail)
print("Failure Rate: ", fail/3000)

with open("ring.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

residuals=[]
for i in range(len(lines)):
    if(lines[i][:6]=="global"):
        residuals.append(float(lines[i][17:-1]))
    
fail=0
success=0
reconsErr=0.0
for i in range(len(residuals)):
    if(isnan(residuals[i])):
        fail+=1
    else:
        reconsErr+=residuals[i]
        success+=1
reconsErr/=success

print('\n')
print("ZOLA Phase Retrieval Report: Ring")
print("NME(pix): ", reconsErr)
print("Success: ", success)
print("Failure: ", fail)
print("Failure Rate: ", fail/3000)