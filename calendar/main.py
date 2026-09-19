#start

September = {
    "1 sept": "no plans",
    '2 sept': 'no plans',
    '3 sept': 'no plans',
    '4 sept': 'no plans',
    '5 sept': 'no plans',
    '6 sept': 'no plans',
    '7 sept': 'no plans',
    '8 sept': 'no plans',
    '9 sept': 'no plans',
    '10 sept': 'no plans',
}

print(September['1 sept'])
September['1 sept'] = 'work'
print(September['1 sept'])


September['1 sept'] = input('Any plans? ')
print(September['1 sept'])