#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author:   Nils F. Schmidt
# email:    nils.schmidt@uni-duesseldorf.de
# created:  2017-12-27
# note:	    This file loads all necessary scripts to use LatLing. For the available functions please look at the readme-file.

print("LatLing Version 1.5")
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
    input_format = input("Please enter the input format:\n(Available format: EDICTOR, CUSTOM)\n-> ")
    input_cluster = input("Please enter the name of the input cluster file (e.g. romania.tsv) in LatLing/Data:\n-> ")
    input_cluster = "Data/"+input_cluster
    output_format = input("Please enter the output format:\n(Available formats: NEX)\n-> ")
    using_classes = input("Do you want to convert tokens to phonetical classes? (Standard is YES)\nY, N -> ")
    if using_classes == "N":
        using_classes = "N"
    else:
        using_classes = "Y"
    if input_format == "EDICTOR":
        
    # *************************
    # PROCESSING EDICTOR FORMAT
    # *************************
    
        if output_format != "NEX":
            print("Output format is not available.")
            return
        print("Loading input cluster file (",input_cluster,") using",output_format,"...")
        
        # LOADING INPUT CLUSTER FILE
        
        source = open(input_cluster, "r", 1, "utf_8")
        
        # DETECTING LANGUAGES
        
        languages = []
        cognates = []
        concepts = []
        input_correct = False
        for line in source:
            current_line = line.rstrip()
            current_line_split = current_line.split("\t")
            if (current_line_split[0] == "ID") & (current_line_split[1] == "DOCULECT") & (current_line_split[2] == "CONCEPT") & (current_line_split[3] == "CONCEPTICON_ID") & (current_line_split[4] == "ALIGNMENT") & (current_line_split[5] == "COGID"):
                input_correct = True
            else:
                if input_correct == True:
                    languages.append(current_line_split[1])
                    concepts.append(current_line_split[2])
                    cognates.append(current_line_split[5])
                else:
                    print("ERROR: Input file damaged or invalid syntax! Required syntax: ID DUCOLECT CONCEPT CONCEPTICON_ID ALIGNMENT COGID")
                    return
        source.close()
        languages = removeduplicates(languages)
        concepts = removeduplicates(concepts)
        cognates = removeduplicates(cognates)

        
        #BUILDING LANGUAGE DICTIONARY
        languagedict = {}
        for i in range(len(languages)):
            newlanguage = {str(i):languages[i]}
            languagedict.update(newlanguage)
        
        print("DETECTED LANGUAGES")
        print("Languages:",languagedict,", # of languages: ",str(len(languages)))
        print("Concepts:",concepts,", # of concepts: ",str(len(concepts)))
        print("Cognates: # of cognates: ",str(len(cognates)))

        #BUILDING THE DATA MATRIX
        #Definition: Mat[Language1][Language2][Concept][Cognate]

        mat = [[[[0 for i in range(len(concepts))] for j in range(len(concepts))] for k in range(len(languages))] for l in range(len(languages))]

        #FILLING THE DATA MATRIX
        segment = 100/len(languages)
        finished = 0
        for i in range(len(languages)):
            finished = finished+segment
            finished_output = round(finished, 1)
            print("Processing language no. ",str(i+1),", ", finished_output,"% completed.")
            for j in range(len(languages)):
                for k in range(len(concepts)):
                    for l in range(len(cognates)):
                        if i == j:
                            mat[i][j][k][l] = 0
                        else:
                            seqlanga = ""
                            seqlangb = ""
                            islanga = False
                            islangb = False
                            source = open(input_cluster, "r", 1, "utf_8")
                            for line in source:
                                current_line = line.rstrip()
                                current_line_split = current_line.split("\t")
                                if (current_line_split[1] == languagedict[str(i)]) & (current_line_split[3] == str(k)) & (current_line_split[5] == str(l)):
                                    seqlanga = current_line_split[4]
                                    islanga = True
                                elif (current_line_split[1] == languagedict[str(j)]) & (current_line_split[3] == str(k)) & (current_line_split[5] == str(l)):
                                    seqlangb = current_line_split[4]
                                    islangb = True
                            source.close()
                            if ((islanga == True) & (islangb == True)):
                                if using_classes == "Y":
                                    seqlanga = convert_ipa_to_class(seqlanga)
                                    seqlangb = convert_ipa_to_class(seqlangb)
                                aln1, aln2, med = align(seqlanga, seqlangb)
                                mat[i][j][k][l] = changefunction(med)
                            else:
                                mat[i][j][k][l] = "nocog"

        #BUILDING THE CLUSTER
        # *** Clustering the Cognate-IDs ***
        #DEFINITION: Cluster[Language1][Language2][Concept]
        cluster = [[[0 for i in range(len(concepts))] for j in range(len(languages))] for k in range(len(languages))]

        for i in range(len(languages)):
            for j in range(len(languages)):
                for k in range(len(concepts)):
                    value = 0
                    counter = 0
                    for l in range(len(cognates)):
                        aktwert = mat[i][j][k][l]
                        if aktwert != "nocog":
                            value = value + aktwert
                            counter += 1
                        if counter == 0:
                            cluster[i][j][k] = 1
                        else:
                            cluster[i][j][k] = value/counter
        
        #BUILDING THE SUPERCLUSTER
        # *** Clustering the Concepts ***
        #DEFINITION: Supercluster[Language1][Language2]
        supercluster = [[0 for i in range(len(languages))] for j in range(len(languages))]

        for i in range(len(languages)):
            for j in range(len(languages)):
                value = 0
                counter = 0
                for k in range(len(concepts)):
                    aktwert = cluster[i][j][k]
                    value = value + aktwert
                    counter += 1
                supercluster[i][j] = value/counter
        createnexoutput(supercluster, languages, len(languages))
        print("Output stored in Output/output.nex")
                        
       
    # *****************************
    # PROCESSING CUSTOM FILE FORMAT
    # *****************************
    else:
    
        print("CUSTOM or invalid input format entered. Continue with custom format!")
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
