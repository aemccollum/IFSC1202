inputfilename = "06.Project Input File.txt"
outputfilename = "06. Project Output File.txt"
InputRecord = 0
MergeRecord = 0
OutputRecord = 0
inputfile = open(inputfilename,'r')
outputfile = open(outputfilename, 'w')
line = inputfile.readline()
while line != '':
      if line == "**Insert Merge File Here**\n":
            mergefile = open("06.Project Merge File.txt", "r")
            merge = mergefile.readline()
            while merge != "":
                  outputfile.write(merge)
                  OutputRecord += 1
                  merge = mergefile.readline()
                  MergeRecord += 1
            outputfile.write("\n")
            mergefile.close()
      else:
            outputfile.write("\n")
            OutputRecord += 1
            InputRecord += 1
      line = inputfile.readline()
outputfile.close()
inputfile.close()
print(InputRecord, "input file record")
print(MergeRecord, "merge file record")
print(OutputRecord, "output file record")
