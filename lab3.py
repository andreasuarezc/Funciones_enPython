def isYearLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
            if year % 100 == 0 and year %400 == 0:
                    return True
            else:
                    return False

def daysInMonth(year, month):
    if isYearLeap(year)==True:
            if month==2:
                        return 29
    if month==2:
            return 28
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            return 31
    if month==4 or month==6 or month== 9 or month==11:
            return 30

def coeficienteA(year):
    if year>=1700 and year<=1799:
        return 5
    else:
        if year>=1800 and year<=1899:
            return 3
        else:
            if year>=1900 and year<=1999:
                return 1
            else:
                if year>=2000 and year<=2099:
                    return 0
                else:
                    if year>=2100 and year<=2199:
                        return -2
                    else:
                        if year>=2200 and year<=2299:
                            return -4

def coeficienteB(year):
    return year%100+((year%100)//4)

def coeficienteC(year, month):
    if daysInMonth(year, month)==29:
        return -1
    else:
        if isYearLeap(year)==True and month==1:
            return -1
        else:
            return 0

def coeficineteD(month):
    mes=[1,2,3,4,5,6,7,8,9,10,11,12]
    valor=[6,2,2,5,0,3,5,1,4,6,2,4]
    for x in range (len(mes)):
        if month==mes[x]:
            d=valor[x]
    return d

def dayOfYear(year, month, day):
    algoritmo=(coeficienteA(year)+coeficienteB(year)+coeficienteC(year, month)+coeficineteD(month)+day)%7
    diasSemana=["Domingo","Lunes","martes","Miercoles","Jueves","Viernes","Sábado"]
    dia=(diasSemana[algoritmo])
    return dia
    
print(dayOfYear(2000, 12, 31))
    
















