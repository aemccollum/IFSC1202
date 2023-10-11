inputfilename = "07.Project Angles Input.txt"
outputfilename = "07. Project Angles Output.txt"
Outputrecord = 0
inputfile = open(inputfilename,'r')
outputfile = open(outputfilename, 'w')
def parse_dms(dms_str):
    parse = dms_str.split('(chr(176))')
    if len(parse) != 2:
        return None
    deg = int(parse[0])
    parse = parse[1].split('\'')
    if len(parse) != 2:
        return None
    min = int(parse[0])
    sec_str = parse[1].replace('"', ''.strip)
    if sec_str.isdigit():
        sec = int(sec_str)
    else: 
        return float(deg), float(min), float(sec)
def DD(deg, min, sec):
    return deg + min/60 + sec / 3600
for line in inputfile:
    line = line.strip()
    parse_line = parse_dms(line)
    if parse_line is not None:
        deg, min, sec = parse_line
        decimal_degree = float(DD(deg, min, sec))
    else:
        outputfile.write("\n")
        Outputrecord += 1
    line = inputfile.readline()
outputfile.close()
inputfile.close()
print(Outputrecord, "records processed")
   