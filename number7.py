def _1(array):
    if array[4] == 2007:
        return 0
    if array[4] == 1962:
        return 1
    else:
        return 2


def _2(array):
    if array[4] == 2007:
        return 4
    if array[4] == 1962:
        return 5
    else:
        return 6


def _1986(array):
    if array[1] == 'VCL':
        return _1(array)
    if array[1] == 'APL':
        return 3
    else:
        return _2(array)


def _3(array):
    if array[0] == 'SASS':
        return 7
    else:
        return 8


def _4(array):
    if array[1] == 'VCL':
        return 9
    if array[1] == 'APL':
        return 10
    else:
        return 11


def _2011(array):
    if array[4] == 2007:
        return _3(array)
    if array[4] == 1962:
        return _4(array)
    else:
        return 12


def _CUDA(array):
    if array[3] == 1986:
        return _1986(array)
    if array[3] == 2011:
        return _2011(array)
    else:
        return 13


def main(array):
    if array[2] == 'CUDA':
        return _CUDA(array)
    else:
        return 14


print(main(['MAX', 'VCL', 'ATS', 1969, 2007]))
print(main(['MAX', 'APL', 'CUDA', 1986, 1974]))
print(main(['SASS', 'EAGLE', 'CUDA', 2011, 1974]))
print(main(['SASS', 'EAGLE', 'CUDA', 2011, 1962]))
print(main(['MAX', 'VCL', 'CUDA', 1969, 1974]))
