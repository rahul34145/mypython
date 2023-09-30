
import sys
while True :    
    print("\t\t\t\t<----WELCOME TO AGRICULTURE MANAGEMENT---->\n")
    print('\n\t<---DETAILS REGARDING FARMER--->')
    Name=input('Farmer Name:')
    Adres=input('Farmer Adrresss details:')
    ph=int(input('Farmer Phone number:\n'))


    print('\n\n\t<----DETAILS REGARDING CROP INVESTMENT---->')
    print('Enter the crop details here!')
    no=int(input('Enter the number of crops:\n'))
    for i in range(0,no):
        crop=input('Enter the'+str(i)+'th crop type name :')
        seed=int(input('Enter the cost required to purchase  '+crop+'\'s seed:'))
        pest=int(input('Total Cost required for pesticydes:'))
        per=int(input('Enter cost required to bowing '+crop+ '\'s seeeds: '))
        cut=int(input('Cost for cutting crop :'))
        cr_i=seed+pest+per+cut
        print('Total investment for crops is ',cr_i)
        t_amnt=int(input('After selling crop Enter  total amount:'))
    
    


    print('\n\n\t <----DETAILS REGARDING TRACTOR INVESTMENT ----> ')
    nag=int(input('Enter cost required for cultivation  farm: '))  
    mal=int(input('Cost required for threshing  crop:')) 
    sply=int(input('Cost to transportation:'))
    t_trc=nag+mal+sply
    print('Total investment for tractor is ',t_trc)
    
    print('\n\n\t<----DETAILS REGARDING LABOUR---->')
    t_lab=int(input('Enter the total number of labours worked:'))
    for i in range(0,t_lab):
        #t_si=0
        nm=input('Enter the name of '+str(i)+'th  labour:')
        td=int(input('Total days '+nm+' came :'))
        sal=int(input('Salary measure:\n'))
        t_sal=td*sal
        print('Total amount for  '+nm+'  is: ',t_sal)
        t_si=t_sal+t_sal
    print('Total salary investment for labour is :',t_si)
    t_i=cr_i+t_trc+t_si
    t_p=t_amnt-t_i
    print('\n\n\tTOTAL INVESTMENT DONE BY '+Name+' IS ',t_i)
    print('Description as below---->')
    print('Farmer Name--->',Name)
    print('Phone-->',ph)
    print('Crop Invest--->',cr_i)
    print('Tractor Invest--->',t_trc)
    print('Labour Invest--->',t_si)
    print('Total Invest--->',t_i)
    print('Total Gain--->',t_amnt)
    if t_p<=0:
        print('No profit and loss by--->',t_p)
    else:
        print('Total Profit--->',t_p)
    a=int(input('\n\n\tENTER -->1 IF MORE FARMER ELSE ENTER --> 0 IF FARMER OVER\n '))
    if a==0:
        exit(0)
    elif a==1:
        print('<--ONCE AGAIN --> ')