# LatLing
Historical Linguistics for Latin and the Romance Languages with Python
This code was originally created for the course 'Computergestützer Sprachvergleich mit Pyhon und Java Script' in summer 2015. For more information about this course and the used source codes please visit https://github.com/LinguList/pyjs-seminar

Sermo vulgaris / Sermo plebeius / Vulgar latin / Development / Romance languages

Scripts:

scripts/sequence_align.py

	align(seqA,seqB)
	================
	Aligns to sequences using the Wagner-Fisher algorithm. 
	Returns two lists of the aligned sequences (algnA, algnB) 
	and the minimum edit distance (Distance). The algorithm works for both strings and lists.

scripts/open_textfile.py

	???(???.txt)
	================
	Converts a text document (a table with 4 cloumns separated by \t) into a list with two levels.

scripts/converter.py

	strtopho(string,conversion_rules)
	=================
	Converts a string to a phonetical codes (e.g. Kölner Phonetik) according to the implemented rules in file "Data/conversion_rules.txt". Returns the phonetical codes as well as a save string of the original input. Allows the implementation of differen conversion_rules as optional input.

	ipatostr(???,???) 
