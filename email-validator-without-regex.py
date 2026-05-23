#EMAIL VALIDATION PROGRAME(without regex)
while True:
    user = input('Enter a valid email: ')

    #checking empty,numeric start,spaces,double dot,@ and @ count
    if (len(user) == 0 
        or ' ' in user 
        or '..' in user 
        or '@' not in user 
        or user.count('@') != 1):
        print('Invalid email 1')
        continue
    
    #checking allowed char  
    allowed = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890._%+-@')
    invalid = False

    for char in user:
        if char not in allowed:
            print('Invalid email 2>',char)
            invalid = True
            break
    
    if invalid:
        invalid = False
        continue
#newemail@gmail.com
    #validating local part
    local_name = user.split('@')

    if (local_name[0].startswith('.') 
        or local_name[0] == '' 
        or local_name[0].endswith('.')):
        print('Invalid local name 1')
        continue 
        

    #validating domain name and top domain name
    domain_name = local_name[1].split('.')

    if len(domain_name[0]) < 1:
        print('Invalid domain name 1')
        continue

    allowed_domain = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-')

    

    for el in domain_name:
        for ch in el:
            if (ch not in allowed_domain 
                or el.startswith('-')
                or el.endswith('-')):
                print('Invalid domain name or top level domain name 1')
                invalid = True
                break
    if invalid:
        invalid = False
        continue

    if len(domain_name[-1]) < 2:
        print('Invalid top level domain name 1')
        continue
           
    #printing  final result
    print('Your correct email is: ',user)
    break
    
    

    
