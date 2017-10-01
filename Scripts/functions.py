def changefunction(eingabe):
    potenz = 8
    ausgabe = (1-(1/(eingabe+1)))**potenz
    return round(ausgabe,7)

def test_changefunction():
    for i in range(50):
        print(i,": ",changefunction(i))
