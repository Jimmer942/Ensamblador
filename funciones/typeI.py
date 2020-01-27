#!/usr/bin/python3#!/usr/bin/python3

from funciones.complemento_2 import com2

def i_type(inst, function, flag):
        st = ''
        Registers = {'$0' : '00000', '$at': '00001',
                     '$v0': '00010', '$v1': '00011',
                     '$a0': '00100', '$a1': '00101', '$a2': '00110', '$a3': '00111',
                     '$t0': '01000', '$t1': '01001', '$t2': '01010', '$t3': '01011',
                     '$t4': '01100', '$t5': '01101', '$t6': '01110', '$t7': '01111',
                     '$s0': '10000', '$s1': '10001', '$s2': '10010', '$s3': '10011',
                     '$s4': '10100', '$s5': '10101', '$s6': '10110', '$s7': '10111',
                     '$t8': '11000', '$t9': '11001', '$k0': '11010', '$k1': '11011',
                     '$gp': '11100', '$sp': '11101', '$fp': '11110', '$ra': '11111'}
        if flag == 0:
                st += function
                st += Registers[inst[2]]
                st += Registers[inst[1]]
                if inst[3][0] == "–":
                        a = inst[3][1:]
                        a = '{0:016b}'.format(int(a))
                        aux = com2(a)
                else:
                        a = int(inst[3])
                        aux = str('{0:016b}'.format(a))
                st += aux
        else:
                st += function
                st += Registers[inst[3]]
                st += Registers[inst[1]]
                if inst[2][0] == "–":
                        a = inst[2][1:]
                        a = '{0:016b}'.format(int(a))
                        aux = com2(a)
                else:
                        aux = str('{0:016b}'.format(int(inst[2])))
                st += aux
        return st
