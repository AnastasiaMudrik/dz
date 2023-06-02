# Упражнение 8-3
def make_shirt(size='M' , text_labele='sochi 2014'):
    return f'Make shirt: size = {size}, labele = {text_labele}'
print(make_shirt())
print(make_shirt('S','Russia'))
# Упражнение 8-4
def make_shirt(size='L', text_labele='I love Python'):
    return f'Make shirt: size = {size}, labele = {text_labele}'
print(make_shirt())
print(make_shirt('XL','ПИВОЗАВР'))
# Упражнение 8-5
def describe_city(sity='Moscow' , country='Russia'):
    return f'{sity} is in {country}'
print(describe_city())
print(describe_city('Krasnodar'))
print(describe_city('Kropotkin'))
print(describe_city('New York','USA'))
