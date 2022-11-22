from sys import argv

script, infile, outfile = argv

def main(file, out):
    file = open(file, 'r')
    out = open(out, 'w+')
    for line in file:
        line = line.rstrip()
        if line[0] == "-":
            continue
        elif line[0] == "*":
            continue
        elif "*" in line:
            continue
        else:
            out.write('\n'+line)
    out.close()

main(infile, outfile)
