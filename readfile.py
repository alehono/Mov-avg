def readata(filename):
    file1 = open(filename, 'r')
    fname = filename
    data = file1.readlines()
    bcount = []
    pcount = []
    header = data[22].split(' '+'\t')
    header[2] = "moving average"
    for i in range(23,len(data)):
        line = data[i].split()
        bcount.append(int(line[0]))
        pcount.append(int(line[1]))
    file1.close()
    return fname, header, bcount, pcount
