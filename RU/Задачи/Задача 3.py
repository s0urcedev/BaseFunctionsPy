from typing import final


try:
    a = 1 / 0
except:
    print("На ноль делить нельзя")
finally:
    print("Ошибки обработаны")