## calculate BIM 
## EArly optimization is the root of all evil
height = {"mohamed":172,"sara":165,"ahmed":177,"ali":188}
weight = {"mohamed":84,"sara":64,"ahmed":97,"ali":100}

bmi = {}
bmi_classification = {}
for key in height :
    bmi[key] = round(weight[key] / (height[key] / 100)**2,2)
# print(bmi)

for person in bmi :
    if bmi[person]<18 :
        bmi_classification [person] = "underweight"
    elif bmi[person]<25 :
        bmi_classification [person] = "normal"
    elif bmi[person]<30 :
        bmi_classification [person] = "overweight"
    else :
        bmi_classification [person] = "obese"

    
    #print (f"{person}'s BMI ({bmi[person]}) is {bmi_classification}")
# print(bmi)
# print(bmi_classification)

for person ,classification in bmi_classification.items() :
    print (f"{person} is {classification}")
