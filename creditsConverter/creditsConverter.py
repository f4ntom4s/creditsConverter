from parser import Parser, ParserResponse

import sys

if len(sys.argv) > 1:
    fp = open(sys.argv[1], 'r')
    p = Parser()
    for line in fp.readlines():
        try:
            response = p.parse_instruction(line)
            if response.text != "" :
                print response.text
        except ValueError as exception:
            print exception

    fp.close()
