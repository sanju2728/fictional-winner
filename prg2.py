#program to check if a person is eligible to vote based on age,nationality and gender
print('enter the age')
age=int(input())
print('enter the nationality')
nationality=input()
print('enter the gender')
gender=input()
if(age>=18 and nationality=='indian' and (gender=='male' or gender=='female')):
    print('the person is eligible')
else:
    print('the person is not eligible')