def account():
    print('press 1 to log in')

    print('press 2 to creat an acount')
    print('if its your first time you have to creat an account first')
    while True:
        
        num=str(input('enter number:'))
        if num=='2':
            
            number=input('enter your cellphone number')

            password=input('enter your password')
            confirm_password=input('confirm your password')
            while password!=confirm_password:
                
                print('password dont match')
                password=input('enter your password')
                confirm_password=input('confirm your password')
            if password==confirm_password:
                
                print('account set up')
                
            break
    
        elif num=='1':
            

            x=input('enter a cnumber ')
            y=input('enter password')
            while x !=number and y!=confirm_password:

                print('incorrect details')
                x=input('enter a cnumber ')
            y=input('enter password')
            if x==number and y==confirm_number:
                print('logged in')

            break

    
    
   


            
                
    

        


        

        


    


account()