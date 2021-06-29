Weight = input('Weight:  ')
L = 'pounds'
K = 'kilograms'
units = input('(L)bs or (K)gs: ').upper()
if units == 'L':
    Weight = float(Weight) * 0.45
    print(f'You are {Weight} kilos. ')
elif units == 'K':
    Weight = float(Weight) * 2.23
    print(f'You are {int(Weight)} pounds')
else:
    print('End')