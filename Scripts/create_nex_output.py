def createnexoutput():
    
    output = open("Output/output.nex","w")
    output.write("#nexus\n")
    output.write("\n")
    output.write("BEGIN Taxa;\n")
    #1 auf languagenumber setzen
    strg = "DIMENSIONS ntax=" + str(1) + ";\n"
    output.write(strg)
    output.write("TAXABELS\n")
    #[1] 'L1'
    #[2] 'L2'
    output.write(";\n")
    output.close()
