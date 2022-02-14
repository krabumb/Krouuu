
from CImpl.CFileCreation import CFileCreation
from TDI.TDI import TDI


if __name__ == '__main__':
    # Test TDI
    tdi = TDI()
    # Test CFileCreation
    cfc = CFileCreation()
    cfc.create_main_file()
    print(cfc.get_code('main.c'))
    