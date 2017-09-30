# author:   Nils F. Schmidt
# email:    nils.schmidt@uni-duesseldorf.de
# created:  2017-09-30
# note:		This file loads all necessary scripts to use LatLing. For the available functions please look at the readme-file.

print("LatLing Version 1.0")
print("===================")
print("LatLing is optimised for Python 3.6.")
print("\tLoading scripts:")
from Scripts.sequence_align import *
print("\t'Sequence Align' loaded.")
from Scripts.converter import *
print ("\t'Converter' loaded.")
print ('--> Use the function "process()" to start the processing of linguistic sound changes.')
print ('--> The function "latling_help()" shows a discription of all available functions.')
