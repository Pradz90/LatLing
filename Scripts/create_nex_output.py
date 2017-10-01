def createnexoutput(matx, languages, numleng):
    
    output = open("Output/output.nex","w")
    output.write("#nexus\n")
    output.write("\n")
    output.write("BEGIN Taxa;\n")
    #1 auf languagenumber setzen
    strg = "DIMENSIONS ntax=" + str(numleng) + ";\n"
    output.write(strg)
    output.write("TAXLABELS\n")
    for i in range(numleng):
        nummer = str(i + 1)
        string = "["+nummer+"] '"+languages[i]+"'\n"
        output.write(string)
    output.write(";\n")
    output.write("END; [Taxa]\n\nBEGIN Distances;\n")
    output.write(strg)
    output.write("FORMAT labels=left diagonal triangle=both;\n")
    output.write("MATRIX\n")
    for i in range(numleng):
        lstr = "["+str(i+1)+"] '"+languages[i]+"'\t\t"
        for j in range(numleng):
            lstr = lstr+str(matx[i][j])+" "
        lstr = lstr+"\n"
        output.write(lstr)
    output.write(";\n")
    output.write("END; [Distances]")
    output.close()
