sample_name_list = [
    'Tareq',
    'Afsana',
    'Imtiaz',
    'Pulok',
    'Robin',
    'Samia',
    'Rupok'
]

query = input('Provide your input: ').strip().lower()

matches = [name for name in sample_name_list if query in name.lower()]

print(matches)
