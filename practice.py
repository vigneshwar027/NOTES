import re



email  = 'arun@das.com'

a = re.search("arun|vignesh@\w{3,10}\.\w{2,3}",email)

print(a)
if a is None:
    print('not valid')
else:
    print('valid')

