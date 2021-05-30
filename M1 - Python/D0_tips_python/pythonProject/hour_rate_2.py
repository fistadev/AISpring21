sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter a number")
    quit()

print(fh, sr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr

print("Pay: ", xp)
print("---------")
if fh > 40 :
    print("Overtime: ", otp)


