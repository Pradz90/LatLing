#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
from Scripts.open_textfile import *
print ("\t'Open Textfile' loaded.")
from Scripts.create_nex_output import *
print ("\t'Create Nex Output' loaded.")
from Scripts.functions import *
print ("\t'Functions' loaded.")
print ('--> Use the function "process()" to start the processing of linguistic sound changes.')
print ('--> The function "latling_help()" shows a discription of all available functions.')

def process():
    """
    Processes a set of cognates and calculates the distances betwen the different languages based on the minimum edit distance between pairwise compared cognates.
    """
    #INITIALISE: INPUT FILE & OUTPUT FORMAT
    input_cluster = input("Please enter the name of the input cluster file in LatLing/Data:\n-> ")
    input_cluster = "Data/"+input_cluster
    output_format = input("Please enter the output format:\n(Available formats: NEX)\n-> ")
    if output_format != "NEX":
        print("Output format is not available.")
        return
    print("Loading input cluster file (",input_cluster,") using",output_format,"...")

    #LOADING INPUT CLUSTER FILE
    source = open(input_cluster, "r")
    language = False
    cognate = False
    languages = []
    cognates = []
    for line in source:
        current_line = line.rstrip()
        if current_line == "[LANGUAGES]":
            language = True
        elif current_line == "[COGNATES]":
            language = False
            cognate = True
        else:
            if language:
                languages.append(current_line)
            if cognate:
                cognates.append(current_line)
    source.close()
    print("Detected languages:",len(languages),",",languages)
    print("Detected cognates:",len(cognates),",",cognates)
    return
