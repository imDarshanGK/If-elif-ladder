c=input('Enter single chracter:')
if c>='a' and c<='z':
    print('Lower case alphabet')
elif c>'A' and c<='Z':
    print('Upper case alphabet')
elif c>='0' and c<='9':
    print('Digit')
else:
    print('Special Character')
