
def if_else_statements():

    gondolt_szám = 5
    tipp = input('Szerinted melyik számra gondolok 1 és 5 között?' )
    tipp = int(tipp)
    if gondolt_szám == tipp:
        print('Eltaláltad!')
        print('Szép volt!')
    else:
        print('Ez nem jött össze...')

    password = ('Lasagne1')
    tipp2 = input('Please enter the password! ')

    if password == tipp2:
        print('Access Granted')
    else:
        print('Access Denied')

    sz1 = 3
    sz2 = 5
    eredmény= 8
    tipp3 = input('Mennyi'+ str(sz1) + '+' + str(sz2) + '? ')
    tipp3 = int(tipp3)
    if tipp3 == eredmény:
        print('Ja, annyi')
    else:
        print('Ez most komoly? ')


def complex_statements():

    season = input('Melyik évszak van most? (ny/ő) ')
    esik = input('Esik? (i/n) ')
    szél = input('Fúj a szél? (i/n) ')
    if season == 'ny' and szél == 'n' or season == 'ő' and esik == 'n' and szél == 'n':
        print('Megyünk túrázni! ')
    else:
        print('Filmet nézünk! ')


def complex_st_task():
    szám = int(input('Írj be egy egész számot!'))
    szám2 = int(input('Írj be egy másik egész számot!'))
    if szám > szám2:
        válasz = ('Az első szám a nagyobb. ')
    elif szám == szám2:
        válasz = ('A két szám egyenlő. ')
    else:
        válasz = ('A második szám a nagyobb. ')
    print(válasz)


def complex_st_task2():
    ppl = int(input('Hello! Hanyadik lettél az utolsó versenyeden? '))
    if ppl < 4:
        print('dobogós')
    else:
        print('loser')


def complex_st_task3():
    ppl = int(input('Hello! Hanyadik lettél a futóversenyen? '))
    if ppl == 1:
        válasz = ('Aranyérmes!? Gratulálok!!! ')
    elif ppl == 2:
        válasz = ('Ezüst? Wow :) ')
    elif ppl == 3:
        válasz = ('Hmm, szép volt! ')
    else:
        válasz = ('loser')
    print (válasz)


def complex_st_task4():
    oldal1 = int(input('Mekkora a hárömgszög a oldala? '))
    oldal2 = int(input('Mekkora a hárömgszög b oldala? '))
    oldal3 = int(input('Mekkora a hárömgszög c oldala? '))
    if oldal1 + oldal2 > oldal3 and oldal1 + oldal3 > oldal2 and oldal3 + oldal2 > oldal1:
        válasz = ('Ez a háromszög megszerkeszthető! ')
    else:
        válasz = ('Ilyen háromszög nem létezik! ')
    print(válasz)


def while_cycle():
    v = 1
    while v != 1000:
        print('v értéke: ', v)
        v = v + 1
    print(v)


def while_with_ifelse():
    gondolt_szám = 4
    kitalálta = False
    elhasznált_lehetőségek = 0
    while not kitalálta and elhasznált_lehetőségek < 3:
        tipp = int(input('Melyik számra gondoltam 1 és 5 között? '))
        elhasznált_lehetőségek += 1
        if tipp == gondolt_szám:
            kitalálta = True
        else:
            eltérés = abs(tipp - gondolt_szám)
            print(str(eltérés),'-vel térsz el a helyes megoldástól. ')

    if kitalálta:
        print('Ez az! Eltaláltad! ')
    else:
        print('Sajnálom, de nincs több lehetőséged tippelni! ')












def main():
    while_with_ifelse()


if __name__ == "__main__":
    main()