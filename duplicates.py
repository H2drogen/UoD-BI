lines_seen = set() # holds lines already seen
outfile = open('IPnodup.csv', "w")
for line in open('IP.csv', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()