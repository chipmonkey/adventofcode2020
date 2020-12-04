DEBUG = False

class filethingy:

    values = []

    def __init__(self):
        self.values = []
        f = open('testinput.txt', 'r')
        for line in f:
            self.values.append(int(line))

        print("input: ", self.values)


# class find2020s:

#     mydata = filethingy()

#     def getfirstresult(self):
#         for x in range(len(self.mydata.values)-1):
#             for y in range(x+1, len(self.mydata.values)):
#                 if DEBUG:
#                     print(x,y, self.mydata.values[x] + self.mydata.values[y])
#                 if (self.mydata.values[x] + self.mydata.values[y]) == 2020:
#                     print(x, y, self.mydata.values[x], self.mydata.values[y], self.mydata.values[x]*self.mydata.values[y])
#                     exit()

class findN2020s:

    mydata = filethingy()
    
    def __init__(self, n, s):
        """ find the first n entries in the values list which sum to s
        """

        self.n = n
        self.s = s
    
        print(self.n, self.s)

    def solve(self):
        result = self.recurseN(self.n, self.s, 0)
    
    def recurseN(self, n, s, i):
        """recursive function that finds n elements which sum to s
        from a SUBSET of self.mydata.values, namely in the range [i, len(values)]
        """

        print(f"recursed with ({n}, {s}, {i})")
        # Could make this its own more useful class, but a dict of lists is OK for now
        solution = {'solutionIndexes': [],
                    'solutionValues': []}

        for candidateIndex in range(i, len(self.mydata.values) - n + 1):  # Must test for off-by-one errors
            print(f"Depth: {n} at candidateIndex: {candidateIndex}, with len(values) = {len(self.mydata.values)}")
            candidate = self.mydata.values[candidateIndex]
            if n == 1:   # Only terminate if we are here
                if candidate == s:
                    solution['solutionIndexes'] = [candidateIndex]
                    solution['solutionValues'] = [candidate]
                    print(f"yay: {solution}")
                    return(solution)
                else:
                    continue
            else:
                if candidate > s:  # Short circuit
                    print ("Nope: {candidate} > {s}")
                    continue
                else:
                    rMore = self.recurseN(n-1, s-candidate, candidateIndex+1)
                    if rMore:
                        solution['solutionIndexes'].extend(rMore['solutionIndexes'])
                        solution['solutionValues'].extend(rMore['solutionValues'])
                        solution['solutionIndexes'].extend([candidateIndex])
                        solution['solutionValues'].extend([candidate])
                        print("Solved ({n}, {s}, {i}) with:")
                        print(solution)
                        return(solution)
            
            return None
                        

# mything = find2020s()
# mything.getfirstresult()

mything2 = findN2020s(2, 2020)
mything2.solve()
