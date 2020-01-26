#!/usr/bin/env python3
from funciones.complemento_2 import com2

def select(string):
        flag = 0
        code = ''
        for i in string:
                if i != ',' and i != '(' and i != ')':
                        code += i
                if i == '(' or i == ')':
                        flag = 1
                        code += ' '
        inst = list(code.split(" "))
        st = ''

        Rdic = {'add': '100000', 'addu': '100001', 'sub': '100010', 'subu': '100011',
                'and': '100100', 'or': '100101', 'xor': '100110', 'nor': '100111',
                'slt': '101010', 'sltu': '101011', 'sll': '000000', 'srl': '000010',
                'sra': '000011', 'sllv': '000100', 'srlv': '000110', 'srav': '000111',
                'jr': '001000', 'jalr': '001001', 'syscall': '001100', 'break': '001101',
                'mfhi': '010000', 'mthi': '010001', 'mflo': '010010', 'mtlo': '01001',
                'mult': '011000', 'multu': '011001', 'div': '011010', 'divu': '011011'}

        Idic = {'sb': '101000', 'sh': '101001', 'sw': '101011', 'lwcl': '110001',
                'swcl': '111001', 'beq': '000100', 'bne': '000101', 'blez': '000110',
                'bgtz': '000111', 'addi': '001000', 'addiu': '001001', 'slti': '001010',
                'sltiu': '001011', 'andi': '001100', 'ori': '001101', 'xori': '001110',
                'lui': '001111', 'lb': '100000', 'lh': '100001', 'lw': '100011',
                'lbu': '100100', 'lhu': '100101'}


        Registers = {'$0' : '00000', '$at': '00001',
                     '$v0': '00010', '$v1': '00011',
                     '$a0': '00100', '$a1': '00101', '$a2': '00110', '$a3': '00111',
                     '$t0': '01000', '$t1': '01001', '$t2': '01010', '$t3': '01011',
                     '$t4': '01100', '$t5': '01101', '$t6': '01110', '$t7': '01111',
                     '$s0': '10000', '$s1': '10001', '$s2': '10010', '$s3': '10011',
                     '$s4': '10100', '$s5': '10101', '$s6': '10110', '$s7': '10111',
                     '$t8': '11000', '$t9': '11001', '$k0': '11010', '$k1': '11011',
                     '$gp': '11100', '$sp': '11101', '$fp': '11110', '$ra': '11111'}

        if inst[0] in Rdic:
                st = '000000'
                st += Registers[inst[2]]
                st += Registers[inst[3]]
                st += Registers[inst[1]]
                st += '00000'
                st += Rdic[inst[0]]
        elif inst[0] in Idic and flag == 0:
                st = Idic[inst[0]]
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
                st = Idic[inst[0]]
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
