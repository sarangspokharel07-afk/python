#find whether a student passed or failed, needing 40% total and 33% in each subject
phy=int(input("enter physics marks"))
chem=int(input("enter chemistry marks"))
math=int(input("enter mathematics marks"))
total=(phy+chem+math)/3
if(total>=40 and phy>=33 and chem>=33 and math>=33):
    print("student has passed")
else:
    print("student has failed")