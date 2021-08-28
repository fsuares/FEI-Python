def magico(dia, mes, ano):
    if dia*mes == ano % 100:
        print('%d/%d/%d' % (dia, mes ,ano))

def main():
    dia = 1
    mes = 1
    ano = 1901
    while ano <= 2000:
        magico(dia,mes,ano)
        if mes == 1:
            if dia <= 30:
                dia += 1
            elif dia == 31:
                dia = 1
                mes = 2

        elif mes == 2:
            if ano%400 == 0 or ano%4 == 0 and ano%100!=0:
                if dia <= 28:
                    dia += 1
                elif dia == 29:
                    dia = 1
                    mes = 3
            else:
                if dia <= 27:
                    dia += 1
                elif dia == 28:
                    dia = 1
                    mes = 3

        elif mes == 3:
            if dia <= 30:
                dia += 1
            elif dia == 31:
                dia = 1
                mes = 4

        elif mes == 4:
            if dia <= 29:
                dia += 1
            elif dia == 30:
                dia = 1
                mes = 5

        elif mes == 5:
            if dia <= 30:
                dia += 1
            elif dia == 31:
                dia = 1
                mes = 6

        elif mes == 6:
            if dia <= 29:
                dia += 1
            elif dia == 30:
                dia = 1
                mes = 7

        elif mes == 7:
            if dia <= 30:
                dia += 1
            elif dia == 31:
                dia = 1
                mes = 8

        elif mes == 8:
            if dia <= 30:
                dia += 1
            elif dia == 31:
                dia = 1
                mes = 9

        elif mes == 9:
            if dia <= 29:
                dia += 1
            elif dia == 30:
                dia = 1
                mes = 10

        elif mes == 10:
            if dia <= 30:
                dia += 1
            elif dia == 31:
                dia = 1
                mes = 11

        elif mes == 11:
            if dia <= 29:
                dia += 1
            elif dia == 30:
                dia = 1
                mes = 12

        elif mes == 12:
            if dia <= 30:
                dia += 1
            elif dia == 31:
                dia = 1
                mes = 1
                ano += 1

main()