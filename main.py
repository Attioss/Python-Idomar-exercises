import random

def gondolt_szam(gondolt_szam):

    tipp = input('Szerinted melyik szamra gondolok 1 és 5 kozott?')
    tipp = int(tipp)
    if gondolt_szam == tipp:
        print('Eltalaltad!')
        print('Szep volt!')
    else:
        print('Ez nem jott ossze...')


def jelszo_elfogadas():
    password = ('pwasd')
    tipp2 = input('Please enter the password! ')

    if password == tipp2:
        print('Access Granted')
    else:
        print('Access Denied')


def szamok_osszege():
    sz1 = 3
    sz2 = 5
    eredmeny = 8
    tipp3 = input('Mennyi ' + str(sz1) + ' + ' + str(sz2) + ' ? ')
    tipp3 = int(tipp3)
    if tipp3 == eredmeny:
        print('Ja, annyi')
    else:
        print('Ez most komoly? ')

def if_else_statements():
    num = 5
    gondolt_szam(num)
    jelszo_elfogadas()
    szamok_osszege()


def complex_statements():

    season = input('Melyik evszak van most? (ny/o) ')
    esik = input('Esik? (i/n) ')
    szel = input('Fuj a szel? (i/n) ')
    if season == 'ny' and szel == 'n' or season == 'o' and esik == 'n' and szel == 'n':
        print('Megyunk turazni! ')
    else:
        print('Filmet nezunk! ')


def complex_st_task():
    szam = int(input('Irj be egy egesz szamot!'))
    szam2 = int(input('Irj be egy masik egesz szamot!'))
    if szam > szam2:
        valasz = ('Az elso szam a nagyobb. ')
    elif szam == szam2:
        valasz = ('A ket szam egyenlo. ')
    else:
        valasz = ('A masodik szam a nagyobb. ')
    print(valasz)


def complex_st_task2():
    ppl = int(input('Hello! Hanyadik lettel az utolso versenyeden? '))
    if ppl < 4:
        print('dobogos')
    else:
        print('loser')


def complex_st_task3():
    ppl = int(input('Hello! Hanyadik lettel a futoversenyen? '))
    if ppl == 1:
        valasz = ('Aranyermes!? Gratulalok!!! ')
    elif ppl == 2:
        valasz = ('Ezust? Wow :) ')
    elif ppl == 3:
        valasz = ('Hmm, szep volt! ')
    else:
        valasz = ('loser')
    print (valasz)


def complex_st_task4():
    oldal1 = int(input('Mekkora a haromgszog a oldala? '))
    oldal2 = int(input('Mekkora a haromgszog b oldala? '))
    oldal3 = int(input('Mekkora a haromgszog c oldala? '))
    if oldal1 + oldal2 > oldal3 and oldal1 + oldal3 > oldal2 and oldal3 + oldal2 > oldal1:
        valasz = ('Ez a haromszog megszerkesztheto! ')
    else:
        valasz = ('Ilyen haromszog nem letezik! ')
    print(valasz)


def while_cycle():
    v = 1
    while v != 1000:
        print('v erteke: ', v)
        v = v + 1
    print(v)


def while_with_ifelse():
    gondolt_szam = 4
    kitalalta = False
    elhasznalt_lehetosegek = 0
    while not kitalalta and elhasznalt_lehetosegek < 3:
        tipp = int(input('Melyik szamra gondoltam 1 és 5 kozott? '))
        elhasznalt_lehetosegek += 1
        if tipp == gondolt_szam:
            kitalalta = True
        else:
            elteres = abs(tipp - gondolt_szam)
            print(str(elteres),'-vel tersz el a helyes megoldastol. ')

    if kitalalta:
        print('Ez az! Eltalaltad! ')
    else:
        print('Sajnalom, de nincs tobb lehetoseged tippelni! ')


def diophantos():
    age = 0
    while age/6 + age/12 + age/7 + 5 + age/2 + 4 != age:
        age += 1
    print(age, 'evet elt. ')

    x = 0
    while x**2 + x*2 + 5 != 11668:
        x += -1
    print(x, 'a megoldas')


def avoid_infinity_cycle():
    age = 0
    while age / 7 + age / 12 + age / 7 + 5 + age / 2 + 4 != age and age < 200:
         # ha a ciklus age / 6-al kezdődik, akkor fut le megfelelően.
        age += 1
    if age < 200:
        print('He lived', age, 'years. ' )
    else:
        print('There is no solution! ')


def while_in_while():
    row = 0
    while row < 25:
        column = 0
        while column != row + 1:
            print('0', end='')
            column += 1
        print('')
        row += 1


def random_gondolt():
    gondolt_szam = random.randint(1,5)
    kitalalta = False
    decided = True
    nem = "n"
    elhasznalt_lehetosegek = 0
    while not kitalalta and elhasznalt_lehetosegek < 3 and decided:
        tipp = int(input('Melyik szamra gondoltam 1 és 5 kozott? '))
        elhasznalt_lehetosegek += 1
        if tipp == gondolt_szam:
            kitalalta = True
        else:
            elteres = abs(tipp - gondolt_szam)
            print(str(elteres), '-vel tersz el a helyes megoldastol. ')
            decide = input('Szeretnel ujra probalkozni? (y/n) ')
            if decide == nem:
                decided = False

    if kitalalta:
        print('Ez az! Eltalaltad! ')
    elif decided == False:
        print('Rendben, koszonom a jatekot! ')
    else:
        print('Sajnalom, de nincs tobb lehetoseged tippelni! ')


def list_heroes():
    heroes = []
    hero = None
    while hero != '':
        hero = input('Write a hero! ')
        if hero:
            heroes.append(hero)
    print(heroes)


def for_cycle():
    writers = []
    products = []
    writer = None
    while writer != '':
        writer = input('Write a writer name! ')
        if writer:
            writers.append(writer)
    print(writers)
    for writer in writers:
        product = input('Write a ' + writer + ' product')
        products.append(product)
    print(writers, '\n', products)


def drawing():
    for i in range(2, 1001, 5):
        print(i)


def range_exc():
    for i in range(51, 100, 2):
        print(i)


def range_exc2():
    for i in range(200, 99, -5):
        print(i)


def cycles():
    for n in range(500, 1001, 2):
        print(n, n**2, n**4)
    sz = 500
    while sz <= 1000:
        print(sz, sz**2, sz**4)
        sz = sz + 1


def drawing_2():
    row = 0
    column = 5
    while row < 10:
        for i in range(column):
            print('o ', end='')
        print('')
        row += 1


def drawing_3():
    length = int(input('How long should it be?' ))
    print('+ ', end='')
    for i in range(length):
        print('- ', end='')
    print('+ ', end='')


def drawing_4():
    length = 6
    row = 0
    print('+ ', end='')
    for i in range(length):
        print('- ', end='')
    print('+ ', end='')
    print('' )
    while row < 12:
        print('| ', end='')
        for k in range(length):
            print(': ', end='')
        row += 1
        print('| ', end='')
        print('' )
    print('+ ', end='')
    for i in range(length):
        print('- ', end='')
    print('+ ', end='')
    print('' )


def drawing_5():
    print('Answer with a number to the following questions to draw shapes! 0 = new shape, 1000 = exitcode ')
    exit = True
    while exit:
        blocks = int(input('Number? '))
        space = (9 - blocks)
        if blocks > 999:
            exit = False
        elif blocks < 1:
            print('')
        else:
            for i in range(space):
                print(' ', end='')
            for k in range(blocks):
                print('o ', end='')
            for i in range(space):
                print(' ', end='')


def list_func():
    autoim = ['Dacia', 'Jeep', 'Opel', 'Lotus', 'Volvo',
              'Fiat', 'Aston Martin', 'Mazda', 'Saab', 'Toyota', 'Audi']

    uj_autoim = []
    uj_auto = None

    while uj_auto != '':
        uj_auto = input('Milyen autot vettel ma? ')
        if uj_auto != '':
            uj_autoim.append(uj_auto)

    print('Uj autoim:', uj_autoim)

    autoim.extend(uj_autoim)
    print('Midenfele autoim:', autoim)

    eladnivalo_auto = input('Mit adjunk el? ')
    autoim.remove(eladnivalo_auto)
    print('Autoim eladas utan:', autoim)
    print(eladnivalo_auto, '-bol maradt meg:', autoim.count(eladnivalo_auto))


def list_excercise():
    results = []
    throws_num = 0
    while throws_num < 10001:
        throws = str(random.randint(1, 6))
        results.extend(throws)
        throws_num += 1
    print('Results:', results)
    print('A 1-es szam', results.count('1'), 'alkalommal fordul')
    print('A 2-es szam', results.count('2'), 'alkalommal fordul')
    print('A 3-es szam', results.count('3'), 'alkalommal fordul')
    print('A 4-es szam', results.count('4'), 'alkalommal fordul')
    print('A 5-es szam', results.count('5'), 'alkalommal fordul')
    print('A 6-es szam', results.count('6'), 'alkalommal fordul')


def calculations():
    print(1/3)
    print(3* 0.3333333333333333)   # nem tud tárolni akkora értéket, ezért rossz a számolás
    print(1/3*3)
    print(1.1 + 2.2 - 3.3)
    print(9/2)
    print(9//2)   # csak az egészeket kapom
    print(9%2)    # maradékot kapok
    num = 3.33333
    kerekit = round(num, 2)   # a rossz tárolás miatt rossz a kerekites pl: 0,5 = 0  de 1,5 =2
    print(kerekit)


def amount():
    osszeg = 0
    elem = 0
    szorzat = 1
    for szam in range(1, 101):
        osszeg += szam
        elem += 1
        szorzat *= szam
    print('Atlag =', osszeg/elem)  # print(sum(szamok)/len(szamok))
    print('Szamok osszege=', osszeg)  # egyebkent sum - al csinálni print(sum(szamok))
    print('A számok szorzata =', szorzat)


def amount_ex():
    jegyeim = []
    kapott_jegyek = None
    while kapott_jegyek != '':
        kapott_jegyek = (input('Milyen jegyeid vannak? '))
        if kapott_jegyek != '':
            kapott_jegyek = int(kapott_jegyek)
            jegyeim.append(kapott_jegyek)
            print(jegyeim)
    print(sum(jegyeim)/len(jegyeim))


def decision():
    nums = [1, 5, 6]
    contain6 = False
    i = 0
    while i < len(nums) and not contain6:
        if nums[i] == 6:
            contain6 = True
        i += 1
    if contain6:
        print('Yes')
    else:
        print('No')


def decision2():
    nums = [1, 5, 6]
    for num in nums:
        print(num)
        if num % 2 == 0:   # paros szam kereses
            print('Yes')
            break
    else:
        print('No')


def choose():
    my_cars = ['Dacia', 'Jeep', 'Opel', 'Lotus', 'Volvo',
              'Fiat', 'Aston Martin', 'Mazda', 'Saab', 'Toyota', 'Audi']
    who = input('What kind of car do you search?' )
    for i in range(len(my_cars)):
        if my_cars[i] == who:
            print('The audi is ', i+1,'.', sep = '' )
            break
    else:
        print('No')

    print(my_cars.index(who)+1)   # 1 soros versio


def choose_ex():
    list = [1, 54, 35, 67, 12]
    print(list)
    e = 0     # itt kikommentelhetem az e-t úgyis működik????
    for e in list:
        if e % 2 == 0:
            print('Az elso paros szam:', e)
            break
    else:
        print('None')
    print('Az elso paros szam sorszama:', list.index(e)+1)
    for hettel_oszt in list:
        if hettel_oszt % 7 == 0:
            print('Az elso hettel oszthato szam:', hettel_oszt)
            break
    else:
        print('None')
    for h in list:
        if h-60>0 and h-70<0:
            print('Az elso 60 es 70 koze eso szam:', h)
            break
    else:
        print('None')
    for t in list:
        if t == 12:
            print('A 12-es szam, ', list.index(t)+1, '. a listaban!', sep='')


def choose_ex2():
    list = ['Elza', 'Melinda', 'Ferenc', 'Barbara', 'Vilma', 'Miklós', 'Ambrus', 'Mária', 'Natália', 'Judit', 'Árpád',
            'Gabriella', 'Luca', 'Szilárda', 'Valér', 'Aletta', 'Lázár', 'Auguszta', 'Viola', 'Teofil', 'Tamás',
            'Zénó', 'Viktória', 'Ádám', 'Eugénia', 'István', 'János', 'Kamilla', 'Tamara', 'Dávid', 'Szilveszter']
    Teofil = 0
    for Teofil in list:
        if Teofil == 'Teofil':
            print('Teofil nevnapjanak datuma: december', list.index(Teofil)+1)


def euklides_algoritm():
    print('Ket szam legnagyobb kozos osztojat fogjuk kiszamolni! ')
    a = int(input('Adja meg az elso szamot! '))
    b = int(input('Adja meg a masodik szamot! '))
    egyenlo = False
    while not egyenlo:
        if a == b:
            egyenlo = True
            print('Ennek a ket szamnak a legnagyobb kozos osztoja:', a)
        else:
            if a > b:
                a= a-b
            else:
                b = b-a


def lkkt():
    print('Ket szam legkisebb kozos tobbszoroset fogjuk kiszamolni! ')
    szam = int(input('Adja meg az elso szamot! '))
    szam2 = int(input('Adja meg a masodik szamot! '))
    if szam > szam2:
        nagyobb = szam
    else:
        nagyobb = szam2
    for i in range(nagyobb, szam*szam2+1):
        if i % szam == 0 and i % szam2 == 0:
            print(i, 'a legkisebb kozos tobbszoros!')
            break


def lin_search():
    list = [5, 4, 3, 4, 5, 4, 4, 5, 3, 1]  # Van-e olyan szam a listaban, ami egymas utan ismetlodik?
    for i in range(len(list)):
        if list[i] == list[i-1]:
            print(list[i])
            break
    else:
        print('Nem volt ilyen a listaban! ')

    list2 = ['Sanyi', 'Manyi', 'Jani', 'Pali', 'Olga', 'Pali', 'Pista'] # Van-e ket megegyezo nev a listaban?
    i = 0
    vege = False
    while i < len(list2) and not vege:
        j = 0
        i += 1
        while j < len(list2) and not vege:
            if list2[i] == list2[j] and i != j:
                vege = True
            else:
                j += 1
    if vege:
        print(list2[i])

    list3 = [3, 6, 4, 9, 8, 11, 12, 20] # Van-e két olyan szam a listaban, amik csak 1-el ternek el egymastol?
    for i in range(len(list3)):
        if abs(list3[i] - list3[i+1]) == 1:
            print('Ezek a szamok: ', list3[i], 'és', list3[i+1])
            break
    else:
        print('Sajnos nincsenek ilyen szamok! ')


def count():
    list = []
    count = 0
    for i in range(0, 100):
        if i<30 or i>60:
            list.append(i)
            count += 1
    print(list)
    print(count)


def main():
    count()



if __name__ == "__main__":
    main()