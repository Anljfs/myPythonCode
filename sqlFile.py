#!/usr/bin/python
# -*- coding: utf-8 -*-

def transfile(filename,outfile):
    rfile = open(filename,"r",encoding= 'utf-8')
    wfile = open(outfile,"w",encoding= 'utf-8')
    linelist = []
    linelists = []
    codelist =[]
    print(codelist)
    for line in rfile.readlines():
        print(line)
        linelist = []
        linelist = line.split(";")
        if linelist[0] not in codelist:
            codelist.append(linelist[0])
            linelists.extend(linelist)
            wfile.write(line)

    rfile.close()
    wfile.close()

if __name__ == "__main__":
    transfile("a.csv", "b.csv")
