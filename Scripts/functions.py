from Scripts.converter import *
from Scripts.sequence_align import *

def changefunction(eingabe):
    potenz = 8
    ausgabe = (1-(1/(eingabe+1)))**potenz
    return round(ausgabe,7)

def test_changefunction():
    for i in range(50):
        print(i,": ",changefunction(i))

def compare(language1, language2, cognate, using_classes):
    ausgabe = "B"

    # LOADING CURRENT COGNATE FILE
    
    filepath = "Data/"+cognate
    cognate_source = open(filepath, "r")
    dict_cognates = {}
    single_cognate = {}
    subcognate = []
    for line in cognate_source:
        subcognate = line.split('>')
        single_cognate = {subcognate[0]:subcognate[1]}
        dict_cognates.update(single_cognate)
    if language1 in dict_cognates:
        if language2 in dict_cognates:
            if using_classes == "Y":
                clas1 = convert_ipa_to_class(dict_cognates[language1])
                clas2 = convert_ipa_to_class(dict_cognates[language2])
            else:
                clas1 = dict_cognates[language1]
                clas2 = dict_cognates[language2]
            aln1, aln2, med = align(clas1, clas2)
            ausgabe = changefunction(med)
        else:
            ausgabe = "nocog"
    else:
        ausgabe = "nocog"
    return ausgabe
