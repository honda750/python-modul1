"""
    Tid og Dato
"""
from datetime import datetime as tid

iDag = tid.now()

dato = tid.strftime(iDag, '%d.%m.%Y')
klokkeslett = tid.strftime(iDag, '%H:%M:%S')

print(dato)
print(klokkeslett)
