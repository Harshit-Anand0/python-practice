user = input('Enter your Email address: ')
try:
# Program breaker
    def find_error(value):
        if not value:
            raise ValueError('Email is not valid.')
        return value

# Part 1 basic validation of whole email address.
    def basic_validation(Email=""):

        allowed_char = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&*-+=/^_`}{|~?@.')

        for ch in Email:                                                                                                    
            if ch not in allowed_char:
                return False

        if (len(Email.split('@')) > 2 or
            Email == "" or
            " " in Email or
            ".." in Email or
            "@" not in Email or
            "." not in Email or
            "@@" in Email):
            return False

        return Email

    user = basic_validation(user)
    print('run1',user)
    find_error(user)

# Part 2 complete validation of local part.
    def local_part_validation(Email):

        email = Email.split("@")[0]

        if (not email or
            email.startswith(".")  or
            email.endswith(".")):
            return False 
    
        return Email

    user = local_part_validation(user)
    print('run2',user)
    find_error(user)

# Part 3 complete validation of subdomain names.
    def subdomain_and_domain_validation(labels):

        if labels.split("@")[1].startswith('.'):
            return False

        labels = labels.split("@")[1].split(".")

        for ch in labels:
            if (ch.startswith("-") or
                ch.endswith("-") or
                "." in ch or
                "_" in ch or
                len(ch) > 64):
                return False
    
        return labels 

    user = subdomain_and_domain_validation(user)
    print('run3',user)
    find_error(user)
        
# Part 4 complete validation of domain name.
    def top_level_domain_validation(tld):

        tld = tld[-1]

        if (not tld or
            len(tld) < 2 or
            not tld.isalpha()):
            return False
    
        return tld

    user = top_level_domain_validation(user)
    print('run4',user)
    find_error(user)

    print("Your Email address is Valid.")

except ValueError as _:
    print(_)


    
    

    
