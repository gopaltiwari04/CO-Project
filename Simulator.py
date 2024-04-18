#Making DICTIONARY and assigning values to registers and memory
register = {'00000': 'zero', '00001': 'ra', '00010': 'sp', '00011': 'gp', '00100': 'tp', '00101': 't0', '00110': 't1', '00111': 't2',
             '01000': 's0', '01001': 's1', '01010': 'a0', '01011': 'a1', '01100': 'a2', '01101': 'a3', 
             '01110': 'a4', '01111': 'a5', '10000': 'a6', '10001': 'a7', '10010': 's2', '10011': 's3', '10100': 's4', 
             '10101': 's5', '10110': 's6', '10111': 's7', '11000': 's8', '11001': 's9', '11010': 's10', '11011': 's11', 
             '11100': 't3', '11101': 't4', '11110': 't5', '11111': 't6'
}
#initializing all registers to 0
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
#initializing all memory locations to 0
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
#Conversion
def bin_to_dec(num, type='unsigned'):
    if type == 'signed':
        if num[0] == '1':
            s = 0
            s = s + (-2)(len(num)-1)
            for i in range(1, len(num)):
                s = s + int(num[i])(2*(len(num)-i-1))
            return s
        if num[0] == '0':
            s = 0
            for i in range(1, len(num)):
                s = s + int(num[i])(2*(len(num)-i-1))
            return s
    else:
        s = 0
        for i in range(0, len(num)):
            s = s + int(num[i])(2*(len(num)-i-1))
            return s

#Sign Extending
def sgn_extend(digit, num, size=32):
    if len(bin(num)[2:]) > size:
        raise OverflowError('Error: Illegal immediate overflow')
    return digit*(size-len(bin(num)[2:])) + bin(num)[2:]

#Conversion
def dec_to_bin(num, type='unsigned', size=32):
    global output
    if type == 'signed':
        if num < 0:
            number = '0' + bin(abs(num))[2:]
            new = ''
            for i in number:
                if i == '0':
                    new = new + '1'
                else:
                    new = new + '0'
            onescomplement = int(new, 2)
            twoscomplement = onescomplement + 1
            return sgn_extend('1', twoscomplement, size)
        if num >= 0:
            twoscomplement = num
            return sgn_extend('0', twoscomplement, size)
    if type == 'unsigned':
        if num < 0:
            raise OverflowError('Error: Illegal immediate overflow')
        nums = num
        return sgn_extend('0', nums, size)

#Class for simulator
class simulator:
    def execution(self, val):
        if val[-7:] == '0110011' and val[:7] == '0100000' and val[17:20] == '000':
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
            self.sw(val)
    
    #function for add instructions 
    def add(self, val):
        globals()['pc'] += 4
        globals()[register[val[20:25]]] = dec_to_bin(bin_to_dec(globals()[register[val[12:17]]], 'signed') + bin_to_dec(globals()[register[val[7:12]]], 'signed'), 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for sub instructions
    def sub(self, val):
        globals()['pc'] += 4
        globals()[register[val[20:25]]] = dec_to_bin(bin_to_dec(globals()[register[val[12:17]]], 'signed') - bin_to_dec(globals()[register[val[7:12]]], 'signed'), 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for sll instructions
    def sll(self, val):
        globals()['pc'] += 4
        globals()[register[val[20:25]]] = dec_to_bin(bin_to_dec(globals()[register[val[12:17]]], 'signed') << bin_to_dec(globals()[register[val[7:12]]]), 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for slt instructions
    def slt(self, val):
        globals()['pc'] += 4
        if bin_to_dec(globals()[register[val[12:17]]], 'signed') < bin_to_dec(globals()[register[val[7:12]]], 'signed'):
            globals()[register[val[20:25]]] = dec_to_bin(1, 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for sltu instructions
    def sltu(self, val):
        globals()['pc'] += 4
        if bin_to_dec(globals()[register[val[12:17]]]) < bin_to_dec(globals()[register[val[7:12]]]):
            globals()[register[val[20:25]]] = dec_to_bin(1, 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for xor instructions
    def xor(self, val):
        globals()['pc'] += 4
        globals()[register[val[20:25]]] = dec_to_bin(bin_to_dec(globals()[register[val[12:17]]], 'signed') ^ bin_to_dec(globals()[register[val[7:12]]], 'signed'), 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for srl instructions
    def srl(self, val):
        globals()['pc'] += 4
        globals()[register[val[20:25]]] = dec_to_bin(bin_to_dec(globals()[register[val[12:17]]], 'signed') >> bin_to_dec(globals()[register[val[7:12]]]), 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for OR instructions
    def OR(self, val):
        globals()['pc'] += 4
        globals()[register[val[20:25]]] = dec_to_bin(bin_to_dec(globals()[register[val[12:17]]], 'signed') | bin_to_dec(globals()[register[val[7:12]]], 'signed'), 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for AND instructions
    def AND(self, val):
        globals()['pc'] += 4
        globals()[register[val[20:25]]] = dec_to_bin(bin_to_dec(globals()[register[val[12:17]]], 'signed') & bin_to_dec(globals()[register[val[7:12]]], 'signed'), 'signed')
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for lw instructions 
    def lw(self, val):
        globals()[register[val[20:25]]] = memory[bin_to_dec(globals()[register[val[12:17]]], 'signed') + bin_to_dec(val[:12], 'signed') - 65536]
        globals()['pc'] += 4
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for addi instructions
    def addi(self, val):
        globals()[register[val[20:25]]] = dec_to_bin(bin_to_dec(globals()[register[val[12:17]]], 'signed') + bin_to_dec(val[:12], 'signed'), 'signed')
        globals()['pc'] += 4
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for sltiu instructions
    def sltiu(self, val):
        if bin_to_dec(globals()[register[val[12:17]]]) < bin_to_dec(val[:12]):
            globals()[register[val[20:25]]] = dec_to_bin(1, 'signed')
        globals()['pc'] += 4
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for jalr instructions
    def jalr(self, val):
        globals()[register[val[20:25]]] = dec_to_bin(globals()['pc'] + 4, 'signed')
        globals()['pc'] = (bin_to_dec(globals()[register[val[12:17]]], 'signed') + bin_to_dec(val[:12], 'signed')) & ~1
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])
    
    #function for sw instructions
    def sw(self, val):
        globals()[register[val[7:12]]] = memory[bin_to_dec(val[:7]+val[20:25], 'signed')+bin_to_dec(globals()[register[val[12:17]]], 'signed')-65536]
        globals()['pc'] += 4
        output.write(globals()['pc']+' '+globals()['zero']+' '+globals()['ra']+' '+globals()['sp']+' '+globals()['gp']+' '+globals()['tp']+' '+globals()['t0']+' '+globals()['t1']+' '+globals()['t2']+' '+globals()['s0']+' '+globals()['s1']+' '+globals()['a0']+' '+globals()['a1']+' '+globals()['a2']+' '+globals()['a3']+' '+globals()['a4']+' '+globals()['a5']+' '+globals()['a6']+' '+globals()['a7']+' '+globals()['s2']+' '+globals()['s3']+' '+globals()['s4']+' '+globals()['s5']+' '+globals()['s6']+' '+globals()['s7']+' '+globals()['s8']+' '+globals()['s9']+' '+globals()['s10']+' '+globals()['s11']+' '+globals()['t3']+' '+globals()['t4']+' '+globals()['t5']+' '+globals()['t6'])