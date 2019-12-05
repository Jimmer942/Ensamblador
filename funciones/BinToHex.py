#!/usr/bin/env python3

def BinToHex(code):
        Hdic = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        cont1 = 0
        cont2 = 0
        pos = 0
        l = ""
        hexa = "0x"
        suma = 0

        while(cont1 < 8):
                b = 32
                while(cont2 < 4):
                        l += code[pos]
                        pos += 1
                        cont2 += 1
                cont2 = 0
                cont1 += 1
                hexa += Hdic[l]
                l = ""
        return(hexa)
