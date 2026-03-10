# Program to eliminate repeated lines from a file

lines_seen_so_far = set()

with open("Repeated.txt","r") as inputFile, open("UpdatedFile.txt","w") as outputFile:

    print("Eliminating duplicate lines....")

    for line in inputFile:
        if line not in lines_seen_so_far:
            outputFile.write(line)
            lines_seen_so_far.add(line) 