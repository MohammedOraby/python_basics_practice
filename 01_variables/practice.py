## f string practice with strinh fuctions 

email = "ma3oraby@gmail.com"
username = email[ :email.index( '@')]
stop = email.index('.')
at_symbol = email.index('@')+1
print(f"this is my username {username}")
print(f"Hi this is my email {email}")
print (f"and my domain is {email [at_symbol:stop]}")

