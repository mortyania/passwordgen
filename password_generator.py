#!/bin/python3
import random
import re

chars = 'ABCDEFGHIJKLMNOPQRSTVUWXYZabcdefghijklmnopqrstvuwxyz0123456789!£$%^&*(){~}@:?><|,./#[;]'
passwords = []

amount = input('number of passwords to generate? ')
length = input('Length of password? ')
for x in range(int(amount)) :
    password = ''
    for c in range(int(length)) :
        password += random.choice(chars)
    passwords.append(password)

for x in passwords :
    password_scores = {0:'Horrible', 1:'Weak', 2:'Medium', 3:'Strong'}
    password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num'], False)
    if re.search(r'[A-Z]', x):
        password_strength['has_upper'] = True
    if re.search(r'[a-z]', x):
        password_strength['has_lower'] = True
    if re.search(r'[0-9]', x):
        password_strength['has_num'] = True

    score = len([b for b in password_strength.values() if b])

    print ('Password: ' + x + ' -- Strength: ' + password_scores[score])