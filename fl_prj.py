#taking details
print('Enter your details here for future reference :')
nm=input('Your name:')
ad=input('Your address:')
ph=int(input('Your phone number:'))
ed=input('Your qualification :')
ag=int(input('Your age:'))
# writing a file
f=open('f_data','w')
f.write('   Name--->' +nm.upper() )
f.write('   Address--->'+ad.upper() )
f.write('   Phone Number--->'+str(ph).upper() )
f.write('   Qualification--->'+ed.upper() )
f.write('\n')
f.write('   Age--->'+str(ag).upper())
#to display
print('Do you want to see your details file?')
se=int(input('Then enter 1 for look else 0\n'))
if se==1:
    f=open('f_data','r')
    content=f.read()
    print(content)
else:
    print('Thanks for giving detalis')
f.close()
