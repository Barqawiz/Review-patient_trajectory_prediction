#!/usr/bin/python
import os, sys

max_file_size = 1000000
def splitDocument(sizeInMo):
    """Split the MIMIC III document for every 50 Mo (about) without cutting a note"""
    root = os.path.expanduser("~/dl4hl/data/data/")
    dirchunks = os.path.join(root, "chunkssmall/")

    if not os.path.exists(root+'chunkssmall'):
        os.makedirs(root+'chunkssmall')
    if not os.path.exists(root+'outputchunkssmall'):
        os.makedirs(root+'outputchunkssmall')
    i = 1
    make_new_file = True
    outputFile = ""
    output_file_path = sys.argv[1]
    print('output_file_path: ', output_file_path)
    with open(output_file_path) as fread:
        fread.readline() # avoid first line
        for index, line in enumerate(fread.readlines()):
            # skip empty lines
            if not line.strip():
                continue
            count_comma = line.count(',')
            count_quote = line.count('"')
            # print('count_comma: ', count_comma)
            # print('count_quote: ', count_quote)
            if count_comma >= 10 and count_quote >= 1:
                if make_new_file :
                    make_new_file = False
                    outputFile = dirchunks+str(i)+".csv"
            if index % 100:
                print('outputFile: ', outputFile)
            with open(outputFile, 'a') as fwrite:
                fwrite.write(line)
            if os.path.getsize(outputFile) > sizeInMo*max_file_size and make_new_file is False:
                i += 1
                make_new_file = True


def main():
    """ Provides an argument : a path to the csv file (including the name of the csv) """
    if len(sys.argv) != 2:
        print("One argument is necessary : the path to the csv file")
        return -1
    splitDocument(50)


if __name__ == '__main__':
    main()
