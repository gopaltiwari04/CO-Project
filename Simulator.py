import sys

register = {'00000': 'zero', '00001': 'ra', '00010': 'sp', '00011': 'gp', '00100': 'tp', '00101': 't0', '00110': 't1', '00111': 't2',
             '01000': 's0', '01001': 's1', '01010': 'a0', '01011': 'a1', '01100': 'a2', '01101': 'a3', 
             '01110': 'a4', '01111': 'a5', '10000': 'a6', '10001': 'a7', '10010': 's2', '10011': 's3', '10100': 's4', 
             '10101': 's5', '10110': 's6', '10111': 's7', '11000': 's8', '11001': 's9', '11010': 's10', '11011': 's11', 
             '11100': 't3', '11101': 't4', '11110': 't5', '11111': 't6'
}

zero = '00000000000000000000000000000000'
ra = '00000000000000000000000000000000'
sp = '00000000000000000000000000000000'
gp = '00000000000000000000000000000000'
tp = '00000000000000000000000000000000'
t0 = '00000000000000000000000000000000'
t1 = '00000000000000000000000000000000'
t2 = '00000000000000000000000000000000'
s0 = '00000000000000000000000000000000'
s1 = '00000000000000000000000000000000'
a0 = '00000000000000000000000000000000'
a1 = '00000000000000000000000000000000'
a2 = '00000000000000000000000000000000'
a3 = '00000000000000000000000000000000' 
a4 = '00000000000000000000000000000000'
a5 = '00000000000000000000000000000000'
a6 = '00000000000000000000000000000000'
a7 = '00000000000000000000000000000000'
s2 = '00000000000000000000000000000000'
s3 = '00000000000000000000000000000000'
s4 = '00000000000000000000000000000000'
s5 = '00000000000000000000000000000000'
s6 = '00000000000000000000000000000000'
s7 = '00000000000000000000000000000000'
s8 = '00000000000000000000000000000000'
s9 = '00000000000000000000000000000000'
s10 = '00000000000000000000000000000000'
s11 = '00000000000000000000000000000000'
t3 = '00000000000000000000000000000000'
t4 = '00000000000000000000000000000000'
t5 = '00000000000000000000000000000000'
t6 = '00000000000000000000000000000000'
pc = 0

memory ={
        1:  '00000000000000000000000000000000',
        2:  '00000000000000000000000000000000',
        3:  '00000000000000000000000000000000',
        4:  '00000000000000000000000000000000',
        5:  '00000000000000000000000000000000',
        6:  '00000000000000000000000000000000', 
        7:  '00000000000000000000000000000000', 
        8:  '00000000000000000000000000000000',
        9:  '00000000000000000000000000000000', 
        10: '00000000000000000000000000000000', 
        11: '00000000000000000000000000000000', 
        12: '00000000000000000000000000000000',
        13: '00000000000000000000000000000000', 
        14: '00000000000000000000000000000000', 
        15: '00000000000000000000000000000000', 
        16: '00000000000000000000000000000000',
        17: '00000000000000000000000000000000', 
        18: '000000000000000000000000000000000', 
        19: '00000000000000000000000000000000', 
        20: '00000000000000000000000000000000',
        21: '00000000000000000000000000000000', 
        22: '00000000000000000000000000000000', 
        23: '00000000000000000000000000000000',  
        24: '00000000000000000000000000000000', 
        25: '00000000000000000000000000000000',
        26: '00000000000000000000000000000000', 
        27: '00000000000000000000000000000000', 
        28: '00000000000000000000000000000000', 
        29: '00000000000000000000000000000000',
        30: '00000000000000000000000000000000', 
        31: '00000000000000000000000000000000', 
        32: '00000000000000000000000000000000'
}

def btd(data, inp='unsigned'):
    if inp == 'signed':
        if data[0] == '1':
            result = -2 ** (len(data) - 1)
            for i in range(1, len(data)):
                result += int(data[i]) * (2 ** (len(data) - i - 1))
            return result
        elif data[0] == '0':
            result = 0
            for i in range(1, len(data)):
                result += int(data[i]) * (2 ** (len(data) - i - 1))
            return result
    else:
        result = 0
        for i in range(0, len(data)):
            result += int(data[i]) * (2 ** (len(data) - i - 1))
        return result

        
#def se(index, data, bits=32):
 #   if len(bin(data)[2:]) > bits:
  #      raise OverflowError
   # return index*(bits-len(bin(data)[2:])) + bin(data)[2:]
def se(data, bits=32):
    binary_data = bin(data & int("1"*bits, 2))[2:]  # Convert data to binary and truncate to specified number of bits
    if len(binary_data) > bits:
        raise OverflowError
    return ('1' * (bits - len(binary_data)) + binary_data).zfill(bits)  # Sign extend if necessary


def dtb(data, mode='unsigned', bits=32):
    if mode == 'signed':
        if data < 0:
            # Handle negative signed numbers
            abs_data_binary = bin(abs(data))[2:].zfill(bits)  # Get binary representation of absolute value
            ones_complement = ''.join('1' if bit == '0' else '0' for bit in abs_data_binary)  # One's complement
            twos_complement = int(ones_complement, 2) + 1  # Two's complement
            return sign_extend('1', twos_complement, bits)  # Perform sign extension
        else:
            # Handle positive signed numbers
            return sign_extend('0', data, bits)  # Perform sign extension
    elif mode == 'unsigned':
        if data < 0:
            raise OverflowError
        else:
            return sign_extend('0', data, bits)  # Perform sign extension

class solution:
    def xsth(self, val):
        opcode = val[-7:]
        funct3 = val[17:20]

        if opcode == '0110011':
            if funct3 == '000':
                if val[:7] == '0100000':
                    self.sub(val)
                else:
                    self.add(val)
            elif funct3 == '001':
                self.sll(val)
            elif funct3 == '010':
                self.slt(val)
            elif funct3 == '011':
                self.sltu(val)
            elif funct3 == '100':
                self.xor(val)
            elif funct3 == '101':
                self.srl(val)
            elif funct3 == '110':
                self.OR(val)
            elif funct3 == '111':
                self.AND(val)
        elif opcode == '0000011' and funct3 == '010':
            self.lw(val)
        elif opcode == '0010011':
            if funct3 == '000':
                self.addi(val)
            elif funct3 == '011':
                self.sltiu(val)
        elif opcode == '1100111' and funct3 == '000':
            self.jalr(val)
        elif opcode == '0100011' and val[16:19] == '010':
            self.sw(val)

        '''if val[-7:] == '0110011' and val[:7] == '0100000' and val[17:20] == '000':
            self.sub(val)
        elif val[-7:] == '0110011' and val[17:20] == '000':
            self.add(val)
        elif val[-7:] == '0110011' and val[17:20] == '001':
            self.sll(val)
        elif val[-7:] == '0110011' and val[17:20] == '010':
            self.slt(val)
        elif val[-7:] == '0110011' and val[17:20] == '011':
            self.sltu(val)
        elif val[-7:] == '0110011' and val[17:20] == '100':
            self.xor(val)
        elif val[-7:] == '0110011' and val[17:20] == '101':
            self.srl(val)
        elif val[-7:] == '0110011' and val[17:20] == '110':
            self.OR(val)
        elif val[-7:] == '0110011' and val[17:20] == '111':
            self.AND(val)
        elif val[-7:] == '0000011' and val[17:20] == '010':
            self.lw(val)
        elif val[-7:] == '0010011' and val[17:20] == '000':
            self.addi(val)
        elif val[-7:] == '0010011' and val[17:20] == '011':
            self.sltiu(val)
        elif val[-7:] == '1100111' and val[17:20] == '000':
            self.jalr(val)
        elif val[-7:] == '0100011' and val[16:19] == '010':
            self.sw(val)'''
        
    
    
    #def add(self, val):
     #   globals()['pc'] += 4
      #  globals()[register[val[20:25]]] = dtb(btd(globals()[register[val[12:17]]], 'signed') + btd(globals()[register[val[7:12]]], 'signed'), 'signed')
       # output_f.write(str(globals()['pc'])+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    def add(self, val):
        global pc, output_f
    
        pc += 4
        rs1 = register[val[12:17]]
        rs2 = register[val[7:12]]
        rd = register[val[20:25]]

        result = btd(globals()[rs1], 'signed') + btd(globals()[rs2], 'signed')
        globals()[rd] = dtb(result, 'signed')
    
        output_f.write(
            f"{pc} {zero} {ra} {sp} {gp} {tp} {t0} {t1} {t2} {s0} {s1} "
            f"{a0} {a1} {a2} {a3} {a4} {a5} {a6} {a7} {s2} {s3} {s4} "
            f"{s5} {s6} {s7} {s8} {s9} {s10} {s11} {t3} {t4} {t5} {t6}\n"
        )
    
    '''def sub(self, val):
        globals()['pc'] += 4
        globals()[register[val[20:25]]] = dtb(btd(globals()[register[val[12:17]]], 'signed') - btd(globals()[register[val[7:12]]], 'signed'), 'signed')
        output_f.write(str(globals()['pc'])+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
      '''
    def sub(self, val):
        global pc, output_f
        pc += 4
        register_val = register[val[20:25]]
        register_val_1 = register[val[12:17]]
        register_val_2 = register[val[7:12]]
        result = btd(register_val_1, 'signed') - btd(register_val_2, 'signed')
        globals()[register_val] = dtb(result, 'signed')
        output_f.write(' '.join(map(str, [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6])) + '\n')

    def sll(self, val):
        global pc, output_f
        pc += 4
        register_val = register[val[20:25]]
        register_val_1 = register[val[12:17]]
        register_val_2 = register[val[7:12]]
        result = btd(globals()[register_val_1], 'signed') << btd(globals()[register_val_2])
        globals()[register_val] = dtb(result, 'signed')
        output_f.write(' '.join(map(str, [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6])) + '\n')

    def slt(self, val):
        global pc, output_f
        pc += 4
        if btd(globals()[register[val[12:17]]], 'signed') < btd(globals()[register[val[7:12]]], 'signed'):
            globals()[register[val[20:25]]] = dtb(1, 'signed')
        else:
            globals()[register[val[20:25]]] = dtb(0, 'signed')
        output_f.write(' '.join(map(str, [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6])) + '\n')
        
    def sltu(self, val):
        global pc, output_f
        pc += 4
        src1 = btd(globals()[register[val[12:17]]])
        src2 = btd(globals()[register[val[7:12]]])
        dest_reg = register[val[20:25]]
    
        if src1 < src2:
            globals()[dest_reg] = dtb(1, 'signed')
        else:
            globals()[dest_reg] = dtb(0, 'signed')
    
        output_f.write(' '.join(map(str, [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6])) + '\n')
    
    def xor(self, val):
        global pc, output_f

        pc += 4
        src1 = btd(globals()[register[val[12:17]]], 'signed')
        src2 = btd(globals()[register[val[7:12]]], 'signed')
        dest_reg = register[val[20:25]]

        result = src1 ^ src2
        globals()[dest_reg] = dtb(result, 'signed')

        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')
        
    def srl(self, val):
        global pc, output_f
    
        pc += 4
        src1 = btd(globals()[register[val[12:17]]], 'signed')
        src2 = btd(globals()[register[val[7:12]]], 'signed')
        dest_reg = register[val[20:25]]
    
        result = src1 >> src2
        globals()[dest_reg] = dtb(result, 'signed')

        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')

    def OR(self, val):
        global pc, output_f
    
        pc += 4
        src1 = btd(globals()[register[val[12:17]]], 'signed')
        src2 = btd(globals()[register[val[7:12]]], 'signed')
        dest_reg = register[val[20:25]]
    
        result = src1 | src2
        globals()[dest_reg] = dtb(result, 'signed')

        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')

    def AND(self, val):
        global pc, output_f
    
        pc += 4
        src1 = btd(globals()[register[val[12:17]]], 'signed')
        src2 = btd(globals()[register[val[7:12]]], 'signed')
        dest_reg = register[val[20:25]]
    
        result = src1 & src2
        globals()[dest_reg] = dtb(result, 'signed')

        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')

    def lw(self, val):
        global pc, output_f

        dest_reg = register[val[20:25]]
        offset = btd(val[:12], 'signed')
        base_addr = btd(globals()[register[val[12:17]]], 'signed')
    
        globals()[dest_reg] = memory[base_addr + offset]

        pc += 4
        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')

    def addi(self, val):
        global pc, output_f

        dest_reg = register[val[20:25]]
        src1 = btd(globals()[register[val[12:17]]], 'signed')
        imm = btd(val[:12], 'signed')

        globals()[dest_reg] = dtb(src1 + imm, 'signed')

        pc += 4
        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')

    def sltiu(self, val):
        global pc, output_f

        dest_reg = register[val[20:25]]
        src1 = btd(globals()[register[val[12:17]]])
        imm = btd(val[:12])

        if src1 < imm:
            globals()[dest_reg] = dtb(1, 'signed')
        else:
            globals()[dest_reg] = dtb(0, 'signed')

        pc += 4
        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')

    def jalr(self, val):
        global pc, output_f

        dest_reg = register[val[20:25]]
        return_addr = pc + 4
        jump_addr = (btd(globals()[register[val[12:17]]], 'signed') + btd(val[:12], 'signed')) & ~1

        globals()[dest_reg] = dtb(return_addr, 'signed')
        pc = jump_addr

        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')

    def sw(self, val):
        global pc, output_f

        src_reg = register[val[7:12]]
        offset = btd(val[:7] + val[20:25], 'signed')
        base_addr = btd(globals()[register[val[12:17]]], 'signed')

        memory[base_addr + offset] = globals()[src_reg]

        pc += 4
        output_values = [pc, zero, ra, sp, gp, tp, t0, t1, t2, s0, s1, a0, a1, a2, a3, a4, a5, a6, a7, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, t3, t4, t5, t6]
        output_f.write(' '.join(map(str, output_values)) + '\n')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    input_file = sys.argv[-2]
    output_file = sys.argv[-1]
    
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            isp = line.strip()
            solution_inst = solution()
            solution_inst.xsth(isp)
            # Write the final state of registers and memory to the output file
            output_f.write(f"{pc} {zero} {ra} {sp} {gp} {tp} {t0} {t1} {t2} {s0} {s1} {a0} {a1} {a2} {a3} {a4} {a5} {a6} {a7} {s2} {s3} {s4} {s5} {s6} {s7} {s8} {s9} {s10} {s11} {t3} {t4} {t5} {t6}\n")