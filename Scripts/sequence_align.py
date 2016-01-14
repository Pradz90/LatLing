# author:   Nils F. Schmidt
# email:    nils.schmidt@uni-duesseldorf.de
# created:  2016-01-14
# note:     This algorithm was inspired by Johann-Mattis List. Visit lingulist.de for more information.


def align(seqA, seqB):
   """
   Alignment of two sequences with the Wagner-Fisher algorithm.
   """

   # save the length of both sequences
   lenA = 1+len(seqA)
   lenB = 1+len(seqB)

   # create matrix and traceback and initialise
   Mat = [[0 for i in range(lenB)] for j in range(lenA)]
   Tra = [[0 for i in range(lenB)] for j in range(lenA)]

   for i in range(lenA): 
      Mat[i][0] = i
   for i in range(lenB):
      Mat[0][i] = i
   for i in range(1,lenA):
      Tra[i][0] = 1
   for i in range(1,lenB):
      Tra[0][i] = 2

   # print "Matrix:"
   # print Mat
   # print "Traceback:"
   # print Tra

   # main algorithm
   for i in range(1,lenA):
      for j in range(1,lenB):

         # get the chars
         charA = seqA[i-1]
         charB = seqB[j-1]

         # check identity
         if charA == charB:
            match = Mat[i-1][j-1]
         else:
            match = Mat[i-1][j-1] + 1

         # get the gaps
         gapA = Mat[i-1][j] + 1
         gapB = Mat[i][j-1] + 1

         # compare the stuff
         if match <= gapA and match <= gapB:
            Mat[i][j] = match
         elif gapA <= gapB:
            Mat[i][j] = gapA
            Tra[i][j] = 1
         else:
            Mat[i][j] = gapB
            Tra[i][j] = 2

         # print "Matrix:"
         # print Mat
         # print "Traceback:"
         # print Tra

   # Calculating the minimum edit distance
   Distance = Mat[i][j]
   # print "Minimum edit distance:"
   # print Distance

   # start the traceback
   i,j = lenA-1,lenB-1

   algnA,algnB = [],[]

   while i > 0 or j > 0:
      if Tra[i][j] == 0:
         algnA += [seqA[i-1]]
         algnB += [seqB[j-1]]
         i -= 1
         j -= 1
      elif Tra[i][j] == 1:
         algnA += [seqA[i-1]]
         algnB += ["-"]
         i -= 1
      else:
         algnA += ["-"]
         algnB += [seqB[j-1]]
         j -= 1

   # reverse
   algnA = algnA[::-1]
   algnB = algnB[::-1]

   # print algnA
   # print algnB

   return algnA, algnB, Distance

# def main():
#    align("wort","words")

# if __name__ == "__main__":
#    main()


