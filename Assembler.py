register_encoding={                            # register encoding dictionary
    "zero":"00000",
    "ra":"00001",
    "sp":"00010",
    "gp":"00011",
    "tp":"00100",
    "t0":"00101",
    "t1":"00110",
    "t2":"00111",
    "s0":"01000",
    "fp":"01000",
    "s1":"01001",
    "a0":"01010",
    "a1":"01011",
    "a2":"01100",
    "a3":"01101",
    "a4":"01110",
    "a5":"01111",
    "a6":"10000",
    "a7":"10001",
    "s2":"10010",
    "s3":"10011",
    "s4":"10100",
    "s5":"10101",
    "s6":"10110",
    "s7":"10111",
    "s8":"11000",
    "s9":"11001",
    "s10":"11010",
    "s11":"11011",
    "t3":"11100",
    "t4":"11101",
    "t5":"11110",
    "t6":"11111"
}
r_type_dictionary={                                      # R-type instructions encoding dictionary
    "opcode":"0110011",
    "add":["000","0000000"],                             # function-3 and function 7 mapping
    "sub":["000","0100000"],
    "sll":["001","0000000"],
    "slt":["010","0000000"],
    "sltu":["011","0000000"],
    "xor":["100","0000000"],
    "srl":["101","0000000"],
    "or":["110","0000000"],
    "and":["111","0000000"],
}
i_type_dictionary={                             # I-type instructions encoding dictionary
    "lw":["0000011","010"],                     # opcode and function 3 mapping
    "addi":["0010011","000"],
    "sltiu":["0010011","011"],
    "jalr":["1100111","000"],
}
s_type_dictionary = {                            # S-type instructions encoding dictionary
    "sw":["0100011","010"],                    # opcode and function 3 mapping
}
b_type_dictionary={                            # B-type instructions encoding dictionary
    "beq":["1100011","000"],                   # opcode and function 3 mapping
    "bne":["1100011","001"],
    "blt":["1100011","100"],
    "bge":["1100011","101"],
    "bltu":["1100011","110"],
    "bgeu":["1100011","111"],
}
u_type_dictionary={                         # U-type instructions encoding dictionary
    "lui":"0110111",                         # opcode mapping
    "auipc":"0010111",
}
j_type_dictionary={                        # J-type instructions encoding dictionary
    "jal":"1101111",                        # opcode mapping
}
label_dictionary={}                         # label dictionary for storing labels and their line numbers
def int_to_bin(num,bits):                    # function for integer to binary conversion with n no of bits
    bin_of_num=""
    bin_2_complement=""
    if(num<0):
        bin_of_num=str(bin(int(num))[3:])
        if(bin_of_num[0]=="1"):
            bin_of_num="0"+bin_of_num
        
        
        for i in range(len(bin_of_num)):
            if(bin_of_num[i]=="0"):
                bin_2_complement=bin_2_complement+"1"
            
            else:
                bin_2_complement=bin_2_complement+"0"
        
        for i in range(len(bin_2_complement)-1,-(len(bin_2_complement)+1),-1):
            if(bin_2_complement[i]=="0"):
                bin_2_complement=bin_2_complement[:i]+"1"+bin_2_complement[i+1:]
                break
            else:
                bin_2_complement=bin_2_complement[:i]+"0"+bin_2_complement[i+1:]
        
        bin_of_num=bin_2_complement
        for i in range(bits-len(bin_of_num)):
            bin_of_num="1"+bin_of_num
        
        
    
    if(num>=0):
        bin_of_num=str(bin(int(num))[2:])
        for i in range(bits-len(bin_of_num)):
            bin_of_num="0"+bin_of_num
    return bin_of_num
f=open("./input.txt","r")                       # file handling for taking assembly code as input from file
assembly_lines=f.readlines()
for i in range(len(assembly_lines)):
    assembly_lines[i]=assembly_lines[i].rstrip("\n")
f.close()



f=open("./output.txt","w")            # file handling for taking machine code as output in a file
count=0
instruction_type={}                        # extracting instruction_type from assembly lines into dictionary woth key as line number
for i in range(len(assembly_lines)):
    # extractang instruction type
    if ":" in assembly_lines[i]:
        label_dictionary[assembly_lines[i].split(":")[0]]=i
        instruction_type[i+1]=assembly_lines[i].split(":")[1].lstrip().split(" ")[0]
    else:
        instruction_type[i+1]=assembly_lines[i].lstrip().split(" ")[0]


part_2={}                                   # extracting part 2 of each assembly line into dictionary with key as line number
for i in range(len(assembly_lines)):
    # extracting part 2
    if ":" in assembly_lines[i]:
        part_2[i+1]=assembly_lines[i].split(":")[1].lstrip().split(" ")[1]
    else:
        part_2[i+1]=assembly_lines[i].lstrip().split(" ")[1]


registers_or_immediate={}                    # extracting registers/immediadate from part 2 into dictionary with key as line number
for i in range(len(part_2)):
    # extracting registers/immediadate
    registers_or_immediate[i+1]=part_2[i+1].split(",")

for i in range(len(assembly_lines)):                      # traversing through assembly lines
    # for each assembly checking which insgtruction type is it
    if instruction_type[i+1] in r_type_dictionary.keys():
        if registers_or_immediate[i+1][2] not in register_encoding.keys() or registers_or_immediate[i+1][1] not in register_encoding.keys() or registers_or_immediate[i+1][0] not in register_encoding.keys():
            output_line=(f'ERROR: not valid register')
            if(count!=len(assembly_lines)-1):
                f.write(output_line+"\n")
                count=count+1
            else:
                f.write(output_line)
            continue

        output_line=r_type_dictionary[instruction_type[i+1]][1]+register_encoding[registers_or_immediate[i+1][2]]+register_encoding[registers_or_immediate[i+1][1]]+ r_type_dictionary[instruction_type[i+1]][0]+ register_encoding[registers_or_immediate[i+1][0]]+r_type_dictionary["opcode"]
        if(count!=len(assembly_lines)-1):
            f.write(output_line+"\n")
            count=count+1
        else:
            f.write(output_line)

    elif instruction_type[i+1] in i_type_dictionary.keys() and ("(" not in part_2[i+1]):
        immediate_value=int(registers_or_immediate[i+1][2])
        immediate_binary=int_to_bin(immediate_value,12)
        if registers_or_immediate[i+1][1] not in register_encoding.keys() or registers_or_immediate[i+1][0] not in register_encoding.keys():
            output_line=(f'ERROR: not valid register')
            if(count!=len(assembly_lines)-1):
                f.write(output_line+"\n")
                count=count+1
            else:
                f.write(output_line)
            continue
        output_line=immediate_binary+register_encoding[registers_or_immediate[i+1][1]]+i_type_dictionary[instruction_type[i+1]][1]  + register_encoding[registers_or_immediate[i+1][0]]  + i_type_dictionary[instruction_type[i+1]][0]
        if(count!=len(assembly_lines)-1):
            f.write(output_line+"\n")
            count=count+1
        else:
            f.write(output_line)

    elif instruction_type[i+1] in i_type_dictionary.keys() and ("(" in part_2[i+1]):
        immediate_value=int(registers_or_immediate[i+1][1].split("(")[0])
        immediate_binary=int_to_bin(immediate_value,12)
        return_addrress_register=registers_or_immediate[i+1][0]
        source_address_register=registers_or_immediate[i+1][1].split("(")[1].rstrip(")")
        if return_addrress_register not in register_encoding.keys() or source_address_register not in register_encoding.keys():
            output_line=(f'ERROR: not valid register')
            if(count!=len(assembly_lines)-1):
                f.write(output_line+"\n")
                count=count+1
            else:
                f.write(output_line)
            continue
        output_line=immediate_binary+register_encoding[source_address_register]+i_type_dictionary[instruction_type[i+1]][1]+register_encoding[return_addrress_register]+i_type_dictionary[instruction_type[i+1]][0]
        if(count!=len(assembly_lines)-1):
            f.write(output_line+"\n")
            count=count+1
        else:
            f.write(output_line)
    elif instruction_type[i+1] in s_type_dictionary.keys():
        data_register=registers_or_immediate[i+1][0]
        source_address_register=registers_or_immediate[i+1][1].split("(")[1].rstrip(")")
        immediate_offset=int(registers_or_immediate[i+1][1].split("(")[0])
        binary_immediate_offset=int_to_bin(immediate_offset,12)

        if data_register not in register_encoding.keys() or source_address_register not in register_encoding.keys():
            output_line=(f'ERROR: not valid register')
            if(count!=len(assembly_lines)-1):
                f.write(output_line+"\n")
                count=count+1
            else:
                f.write(output_line)
            continue
        output_line=binary_immediate_offset[0:7]+register_encoding[data_register]+register_encoding[source_address_register]+s_type_dictionary[instruction_type[i+1]][1]+binary_immediate_offset[7:12]+s_type_dictionary[instruction_type[i+1]][0]
        if count!=len(assembly_lines)-1:
            f.write(output_line+"\n")
            count=count+1
        else:
            f.write(output_line)
    elif instruction_type[i+1] in b_type_dictionary.keys():
        if registers_or_immediate[i+1][2] not in label_dictionary.keys():
            label_immidiate=int(registers_or_immediate[i+1][2])
            label_immidiate_bin=int_to_bin(label_immidiate,13)
            if registers_or_immediate[i+1][0] not in register_encoding.keys() or registers_or_immediate[i+1][1] not in register_encoding.keys():
                output_line=(f'ERROR: not valid register')
                if count!=len(assembly_lines)-1 :
                    f.write(output_line+"\n")
                    count=count+1
                else:
                    f.write(output_line)
                continue
            output_line=label_immidiate_bin[0]+label_immidiate_bin[2:8]+register_encoding[registers_or_immediate[i+1][1]]+register_encoding[registers_or_immediate[i+1][0]]+b_type_dictionary[instruction_type[i+1]][1]+label_immidiate_bin[8:12]+label_immidiate_bin[1]+b_type_dictionary[instruction_type[i+1]][0]
            if count!=len(assembly_lines)-1:
                f.write(output_line+"\n")
                count=count+1
            else:
                f.write(output_line)
        elif registers_or_immediate[i+1][2] in label_dictionary.keys():
            label_lineno=label_dictionary[registers_or_immediate[i+1][2]]
            label_immidiate=int_to_bin((i-label_lineno)*4,13)
            if registers_or_immediate[i+1][0] not in register_encoding.keys() or registers_or_immediate[i+1][1] not in register_encoding.keys():
                output_line=(f'ERROR: not valid register')
                if count!=len(assembly_lines)-1:
                    f.write(output_line+"\n")
                    count=count+1
                else:
                    f.write(output_line)
                continue
            output_line=label_immidiate[0]+label_immidiate[2:8]+register_encoding[registers_or_immediate[i+1][1]]+register_encoding[registers_or_immediate[i+1][0]]+b_type_dictionary[instruction_type[i+1]][1]+label_immidiate[8:12]+label_immidiate[1]+b_type_dictionary[instruction_type[i+1]][0]
            if count!=len(assembly_lines)-1:
                f.write(output_line+"\n")
                count=count+ 1
            else:
                f.write(output_line)
    elif instruction_type[i+1] in u_type_dictionary.keys():
        immediate_value=int(registers_or_immediate[i+1][1])
        immediate_binary=int_to_bin(immediate_value,32)
        if registers_or_immediate[i+1][0] not in register_encoding.keys():
            output_line=(f'ERROR: not valid register')
            if count!=len(assembly_lines)-1:
                f.write(output_line+"\n")
                count=count+1
            else:
                f.write(output_line)
            continue
        
        output_line=immediate_binary[0:20]+register_encoding[registers_or_immediate[i+1][0]]+ u_type_dictionary[instruction_type[i+1]]
        if count!=len(assembly_lines)-1:
            f.write(output_line+"\n")
            count=count+1
        else:
            f.write(output_line)
        
    elif instruction_type[i+1] in j_type_dictionary.keys():
        label_immidiate=int(registers_or_immediate[i+1][1])
        label_immidiate_bin =int_to_bin(label_immidiate,21)
        if registers_or_immediate[i+1][0] not in register_encoding.keys():
            output_line=(f'ERROR: not valid register')
            if count!=len(assembly_lines)-1:
                f.write(output_line+"\n")
                count=count+ 1
            else:
                f.write(output_line)
            continue
        
        output_line=label_immidiate_bin[0]+label_immidiate_bin[10:20] +label_immidiate_bin[9]+label_immidiate_bin[1:9]+register_encoding[registers_or_immediate[i+1][0]]+j_type_dictionary[instruction_type[i+1]]
        if count!=len(assembly_lines)-1:
            f.write(output_line+"\n")
            count=count+ 1
        else:
            f.write(output_line)


    else:
        # for wrong instructions types
        output_line=(f'ERROR: {instruction_type[i+1]} is not a valid instruction at line {i+1}')
        if count!=len(assembly_lines)-1:
            f.write(output_line+"\n")
            count=count+ 1
        else:
            f.write(output_line)

f.close()
