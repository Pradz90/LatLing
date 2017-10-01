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
    using_classes = input("Do you want to convert tokens to phonetical classes? (Standard is YES)\nY, N -> ")
    if using_classes == "N":
        using_classes = "N"
    else:
        using_classes = "Y"
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
    num_languages = len(languages)
    num_cognates = len(cognates)
    print("Detected languages:",num_languages,",",languages)
    print("Detected cognates:",num_cognates,",",cognates)

    #BUILDING THE DATA MATRIX
    Mat = [[[0 for i in range(num_cognates)] for j in range(num_languages)] for k in range(num_languages)]

    segment = 100/num_languages
    finished = 0

    #MAIN ALGORITHM:
    for i in range(num_languages):
        for j in range(num_languages):
            for k in range(num_cognates):
                if i == j:
                    Mat[i][j][k] = 0
                else:
                    zwischenergebnis = compare(languages[i],languages[j],cognates[k],using_classes)
                    Mat[i][j][k] = zwischenergebnis

        #INFO: Subresult / Completion
        finished = segment*(i+1)
        finished = round(finished,1)
        print("Processing",languages[i],"...\n(",finished,"% finished )")

    Out = [[0 for i in range(num_languages)] for j in range(num_languages)]
    for i in range(num_languages):
        for j in range(num_languages):
            value = 0
            counter = 0
            for k in range(num_cognates):
                aktwert = Mat[i][j][k]
                if aktwert != "nocog":
                    value = value + aktwert
                    counter += 1
            if counter == 0:
                Out[i][j] = 1
            else:
                Out[i][j] = value/counter
    #print(Mat)
    #print(Out)
    createnexoutput(Out, languages, num_languages)
    return
