from typing import List

def show_menu():
    print('1. Citire lista')
    print('2. Afisare cea mai lunga subsecventa cu toate numerele pare.')
    print('3. Afisare cea mai lunga subsecventa cu numere ce au aceelasi numar de divizori.')
    print('4. Determina cea mai lunga secventa de numere prime din lista.')
    print('x. Exit')


def read_list() -> List[int]:
    lst = []
    lst_str = input('Dati numerele separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst


def get_longest_all_even(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa in care toate elementele cifre pare.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''

    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            is_ok = True
            for num in lst[ st : dr + 1]:
                if num % 2 != 0:
                    is_ok = False
                    break
            if is_ok:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def test_get_longest_all_even(lst: List[int]) -> List[int]:
    assert get_longest_all_even([1, 2, 3, 4]) == [2]
    assert get_longest_all_even([3, 4, 8, 6]) == [4, 8, 6]
    assert get_longest_all_even([1, 3, 5, 7]) == []


def div_count(n):
    '''
    :param n:Primeste un numar n,care urmeaza sa ii se mumere ,toti divizorii
    :return: Returneaza numarul de divizori
    '''
    d = 0
    for i in range(1, (int)(n ** 0.5) + 1):
        if n % i == 0:
            if n / i == i:
                d = d + 1
            else:
                d = d + 2
    return d


def get_longest_same_div_count(lst: List[int]) -> List[int]:
    '''
    :param lst:
    :return:
    '''
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            nr_div = div_count(lst[st])
            for num in lst[st:dr + 1]:
                if div_count(num) != nr_div:
                    nr_div = -1
                    break

            if (nr_div != -1):
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def test_get_longest_same_div_count(lst: List[int]) -> List[int]:
    assert get_longest_same_div_count([7, 7, 7]) == [7, 7, 7]
    assert get_longest_same_div_count( [0] ) == [0]
    assert get_longest_same_div_count([1, 4, 9, 3, 5, 7, 9, 11]) == [3, 5, 7]

def is_prime(n) -> bool:
    """
    Verifica daca un numar n este prim.
    :param n: elementul verificat daca este prim
    :return: returneaza true daca e prim ,false altfel
    """
    if n < 2:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(12) == False
    assert is_prime(31) == True
    assert is_prime(48) == False
    assert is_prime(13) == True


def get_longest_all_primes(lista: list[int]) -> list[int]:

    """
    Determina cea mai lunga secventa de numere prime din lista.
    :param lista: lista in care se afla valorile
    :return: cea mai lunga secventa de numere prime lista, salvate in prim_list
    """
    prim_list = []
    contor = 0
    lung_max = 0
    start = -1
    start_list = 0

    for i in range(0, len(lista)):
        if is_prime(lista[i]):
            contor += 1
            if start == -1:
                start = i
            if contor > lung_max:
                lung_max = contor
                start_list = start
        elif lung_max:
            start_list = start
            start = -1
            lung_max = contor
            contor = 0
    for i in range(start_list, lung_max + start_list):
        prim_list.append(lista[i])
    return prim_list

def test_get_longest_all_primes(lista: List[int]) -> List[int]:
    assert get_longest_all_primes([3, 7, 11, 13]) == [3, 7, 11, 13]
    assert get_longest_all_primes([4 ,6 ,8 , 10]) == []

def main():

    lst = []
    while True:

        show_menu()
        opt = input('Alege optiunea:')
        if opt == '1':
            lst = read_list()

        elif opt == '2':
            print('Cea mai lunga subsecv cu toate numerele pare este:', get_longest_all_even(lst))

        elif opt == '3':
            print('Cea mai lunga subsecv cu numerele ce au acelasi numar de divizori. :',get_longest_same_div_count(lst))

        elif opt =='4':
            print('cea mai lunga secventa de numere prime din lista.',get_longest_all_primes(lst))

        elif opt == 'x':
            break
        else:
            print('Optiune invalida!')


if __name__ == '__main__':
    test_get_longest_all_even(List[int])
    test_get_longest_same_div_count(List[int])
    test_get_longest_all_primes(List[int])

    main()