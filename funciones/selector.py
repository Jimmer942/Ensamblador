#!/usr/bin/env python3

from funciones.typeR import r_type
from funciones.typeI import i_type

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

        if inst[0] in Rdic:
                st = r_type(inst, Rdic[inst[0]])
        if inst[0] in Idic:
                st = i_type(inst, Idic[inst[0]], flag)
        return st
