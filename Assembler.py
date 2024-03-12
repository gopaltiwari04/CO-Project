opcodes = {
  "add": "0110011",
  "sub": "0110011",
  "sll": "0110011",
  "slt": "0110011",
  "sltu": "0110011",
  "xor": "0110011",
  "srl": "0110011",
  "or": "0110011",
  "and": "0110011",
  "lw": "0000011",
  "addi": "0010011",
  "sltiu": "0010011",
  "jalr": "1100111",
  "sw": "0100011",
  "beq": "1100011",
  "bne": "1100011",
  "blt": "1100011",
  "bge": "1100011",
  "bltu": "1100011",
  "bgeu": "1100011",
  "lui": "0110111",
  "auipc": "0010111",
  "jal": "1101111",
}

resistor = {
  "zero": "00000",
  "ra": "00001",
  "sp": "00010",
  "gp": "00011",
  "tp": "00100",
  "t0": "00101",
  "t1": "00110",
  "t2": "00111",
  "s0": "01000",
  "fp": "01000",
  "s1": "01001",
  "a0": "01010",
  "a1": "01011",
  "a2": "01100",
  "a3": "01101",
  "a4": "01110",
  "a5": "01111",
  "a6": "10000",
  "a7": "10001",
  "s2": "10010",
  "s3": "10011",
  "s4": "10100",
  "s5": "10101",
  "s6": "10110",
  "s7": "10111",
  "s8": "11000",
  "s9": "11001",
  "s10": "11010",
  "s11": "11011",
  "t3": "11100",
  "t4": "11101",
  "t5": "11110",
  "t6": "11111"
}

func7={
    "add": "0000000",
    "sub": "0100000",
    "sll": "0000000",
    "slt": "0000000",
    "sltu": "0000000",
    "xor": "0000000",
    "srl": "0000000",
    "or": "0000000",
    "and": "0000000",
}

func3={
    "add": "000",
  "sub": "000",
  "sll": "001",
  "slt": "010",
  "sltu": "011",
  "xor": "100",
  "srl": "101",
  "or": "110",
  "and": "111",
  "lw": "010",
  "addi": "000",
  "sltiu": "011",
  "jalr": "000",
  "sw": "010",
  "beq": "000",
  "bne": "001",
  "blt": "100",
  "bge": "101",
  "bltu": "110",
  "bgeu": "111",
}

def encode_r_type(a,b,c,d):
    if b not in resistor or c not in resistor or d not in resistor:
        raise ValueError("Invalid")
    x = resistor[b]
    y = resistor[c]
    z = resistor[d]
    m = opcodes[a]
    l = func3[a]
    i = func7[a]
    k = f"{i}{z}{y}{l}{x}{m}"
    return k

def encode_i_type(op,x,s,imm):
    if x not in resistor or s not in resistor:
        raise ValueError("Invalid")
    a5 = resistor[s]
    f3 = func3[op]
    ra = resistor[x]
    opp = opcodes[op]
    imm = int(imm) 
    if imm<0:
        imm = 2**12 + imm
    imm = format(int(imm),'012b')
    x = f"{imm}{a5}{f3}{ra}{opp}"
    return x

def encode_s_type(a,b,c,d):
    if b not in resistor or d not in resistor:
        raise ValueError("Invalid")
    imm = format(int(c),'012b')
    imm_11_5 = imm[:7]
    imm_4_0 = imm[7:]
    x = resistor[b]
    y = resistor[d]
    opp = opcodes[a]
    x = f"{imm_11_5}{x}{y}{imm_4_0}{opp}"
    return x

def encode_b_type(instruction, rs1, rs2, imm):
    if rs1 not in resistor or rs2 not in resistor:
        raise ValueError("Invalid")
    imm= int(imm)
    imm= format(imm, '012b')
    imm_12= imm[0]
    imm_10_5= imm[1:7]
    imm_4_1= imm[7:12]
    imm_11= imm_12
    imm_11_5= imm_10_5
    imm_4_1= imm_4_1
    x= resistor[rs1]
    y= resistor[rs2]
    opp = opcodes[instruction]
    x = f"{imm_12}{imm_10_5}{y}{x}{imm_4_1}{imm_11_5}{opp}"
    return x

# def encode_u_type(a,b,c):
#     if b not in resistor:
#         raise ValueError("Invalid")
#     imm = int(c)
#     if imm<0:
#         imm=2**32+imm
#     imm = format(imm,'32b')
#     x = resistor[b]
#     opp = opcodes[a]
#     x = f"{imm[:20]}{x}{opp}"
#     return x
def encode_u_type(op,a,imm):
    if a not in resistor:
        raise ValueError("Invalid")
    q = int(imm)
    if q<0:
        q = 2**32 + q
    imm_20 = format((q >> 12) & 0xFFFFF, '020b')
    imm_12 = format((q >> 12) & 0xFFFFF, '020b')
    x =  resistor[a]
    y = opcodes[op]
    o = f"{imm_20}{x}{y}"
    return o
def encode_j_type(op,a,imm):
    if a not in resistor:
        raise ValueError("Invalid")
    q = int(imm)
    if q<-1048578 or q>=1048576:
        raise ValueError("address out of range")
    imm_20 = format((q >> 20) & 0b1, '01b')
    imm_10_1 = format((q >> 1) & 0x3FF, '010b')
    imm_11 = format((q >> 11) & 0b1, '01b')
    imm_19_12 = format((q >> 12) & 0xFF, '08b')

    x =  resistor[a]
    y = opcodes[op]
    o = f"{imm_20}{imm_10_1}{imm_11}{imm_19_12}{x}{y}"
    return o

def encode_z_type(op,x,k,s):
    if x not in resistor or s not in resistor:
        raise ValueError("Invalid")
    a5 = resistor[s]
    f3 = func3[op]
    ra = resistor[x]
    opp = opcodes[op]
    k = int(k)
    if k<0:
        k = 2**12 + k
    k = format(int(k),'012b')
    x = f"{k}{a5}{f3}{ra}{opp}"
    return x


def encode_instruction(instruction):
    if instruction[0] in ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]:
        return encode_r_type(instruction[0], instruction[1], instruction[2], instruction[3])
    elif instruction[0] in ["addi", "sltiu", "jalr", "beq", "bne", "blt", "bge", "bltu", "bgeu"]:
        return encode_i_type(instruction[0], instruction[1], instruction[2], instruction[3])
    
    elif instruction[0] in ["lw","sw"]:
        return encode_z_type(instruction[0], instruction[1], instruction[2], instruction[3])
    elif instruction[0] in ["lui", "auipc"]:
        return encode_u_type(instruction[0], instruction[1], instruction[2])
    
    elif instruction[0] in ["jal"]:
        return encode_j_type(instruction[0], instruction[1], instruction[2])
    elif instruction[0] in ["slli", "srli", "srai"]:
        return encode_i_type(instruction[0], instruction[1], instruction[2], instruction[3])
    elif instruction[0] in ["sb", "sh", "sw"]:
        return encode_s_type(instruction[0], instruction[1], instruction[2], instruction[3])
    elif instruction[0] in ["beq", "bne", "blt", "bge", "bltu", "bgeu"]:
        return encode_b_type(instruction[0], instruction[1], instruction[2], instruction[3])
   
    else:
        raise ValueError("Invalid instruction")


def gg(f):
    labels = {}
    line_number = 0
    l=[]
    for line in f:
        line = line.replace('(', ' ')
        
        line = line.replace(')', '')
        
        instruction_list = line.replace(',', ' ').split()
        
        print(instruction_list)
        l.append(encode_instruction(instruction_list))
        if line[-1] == ":":
            labels[line[:-1]] = line_number
        else:
            line_number += 1
    return l



def main():
    with open("/Users/adityayadav/Desktop/test1.txt", "r") as f:
        binary_output = gg(f)
    
    with open("/Users/adityayadav/Desktop/abc.txt", "w") as f:
        for binary in binary_output:
            f.write(binary + "\n")
main()
