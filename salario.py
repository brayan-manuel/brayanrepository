try:
    horas = float(input('Introduzca Horas: '))
    tarifa = float(input('Introduzca Tarifa por Hora: '))

    def calculo_salario(horas, tarifa):
        if horas > 40:
            horas_extra = horas - 40
            tarifa_extra = tarifa * 1.5
            total_extra = horas_extra * tarifa_extra
            print('Salario:', total_extra + (tarifa * 40))
        else:
            print('Salario:', horas * tarifa)
    calculo_salario(horas, tarifa)
except:
    print('ERROR, ingrese un número.')
