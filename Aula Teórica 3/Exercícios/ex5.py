v1 = input('Telefonou para a vítima? ')
v2 = input('Esteve no local do crime? ')
v3 = input('Mora perto da vítima? ')
v4 = input('Devia para a vítima? ')
v5 = input('Já trabalhou para a vítima? ')

if (v1 == 'sim') and (v2 == 'sim') and (v3 == 'sim') and (v4 == 'sim') and (v5 == 'sim'):
    print('Assassino')

elif ((v1 == 'não') and (v2 == 'não')) or ((v1 == 'não') and (v3 == 'não')) or ((v1 == 'não') and (v4 == 'não')) or ((v1 == 'não') and (v5 == 'não')) or ((v2 == 'não') and (v3 == 'não')) or ((v2 == 'não') and (v4 == 'não')) or ((v2 == 'não') and (v5 == 'não')) or ((v3 == 'não') and (v4 == 'não')) or ((v3 == 'não') and (v5 == 'não')) or ((v4 == 'não') and (v5 == 'não')):
    print("Cumplice")

elif ((v1 == 'sim') and (v2 == 'sim')) or ((v1 == 'sim') and (v3 == 'sim')) or ((v1 == 'sim') and (v4 == 'sim')) or ((v1 == 'sim') and (v5 == 'sim')) or ((v2 == 'sim') and (v3 == 'sim')) or ((v2 == 'sim') and (v4 == 'sim')) or ((v2 == 'sim') and (v5 == 'sim')) or ((v3 == 'sim') and (v4 == 'sim')) or ((v3 == 'sim') and (v5 == 'sim')) or ((v4 == 'sim') and (v5 == 'sim')):
    print("Suspeito")

else:
    print("inocente")