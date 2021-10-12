from typing import List

def show_menu():
    print('1. Citire lista')
    print('2. Afisare cea mai lunga subsecventa cu toate numerele pare//Problema 10.')
    print('3. Afisare cea mai lunga subsecventa cu numere ce au aceelasi numar de divizori//Problema 12.')
    print('x. Exit')


def read_list() -> List[int]:
    '''
    Functie pentru citire lista>
    :return:lista citita
    '''
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


def main():

    lst = []
    while True:

        show_menu()
        opt = input('Alege optiunea: ')
        if opt == '1':
            lst = read_list()
        elif opt == '2':
            print('Cea mai lunga subsecv cu toate numerele pare este:', get_longest_all_even(lst))
        elif opt == '3':
            print('Cea mai lunga subsecv cu numerele ce au acelasi numar de divizori. :',
                  get_longest_same_div_count(lst))

        elif opt == 'x':
            break
        else:
            print('Optiune invalida!')


if __name__ == '__main__':
    test_get_longest_all_even(List[int])
    test_get_longest_same_div_count(List[int])
    main()