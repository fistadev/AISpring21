sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, sr)
if fh > 40 :
    # print("Overtime")
    reg = fr * fh # we have 40 hours at the regular rate
    otp = (fh - 40.0) * (fr * 0.5) # all overtime hours at overtime rate
    # print(reg, otp)
    xp = reg + otp # our total pay will be our regular pay + overtime pay
else:
    print("Regular")
    xp = fh * fr # else our total pay will be just regular pay

print("Pay: ", xp)
print("---------")
if fh > 40 :
    print("Overtime: ", otp)


# Overtime
# Extra hours worked multiplied by new rate (50% * normal rate)