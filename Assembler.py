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

registers = {
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

def assemble(input_file):
    binary_output = []
    labels = {}
    line_number = 0
    pc = 0
    for line in input_file:
        line_number += 1
        if line.strip() == "" or line.strip().startswith("#"):
            continue
        if ":" in line:
            label, _ = line.split(":")
            labels[label.strip()] = pc
            continue
        instruction_parts = line.strip().split()
        opcode = opcodes.get(instruction_parts[0])
        if opcode:
            if instruction_parts[0] in ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]:
                rd = registers.get(instruction_parts[1])
                rs1 = registers.get(instruction_parts[2])
                rs2 = registers.get(instruction_parts[3])
                machine_code = f"{opcode}{rs2}{rs1}000{rd}0110011"
                binary_output.append(machine_code)
            elif instruction_parts[0] in ["lw", "sw"]:
                offset, reg, base = instruction_parts[2].split("(")
                offset = int(offset)
                reg = registers.get(reg)
                base = registers.get(base[:-1])
                machine_code = f"{offset:012b}{reg}{opcode}{base}"
                binary_output.append(machine_code)
            elif instruction_parts[0] in ["addi", "sltiu", "jalr"]:
                imm = int(instruction_parts[2])
                rd = registers.get(instruction_parts[1])
                rs1 = registers.get(instruction_parts[3])
                machine_code = f"{imm:012b}{rs1}{opcode}{rd}"
                binary_output.append(machine_code)
            elif instruction_parts[0] in ["beq", "bne"]:
                imm = labels.get(instruction_parts[3]) - pc
                if imm < 0:
                    imm += 1 << 12
                machine_code = f"{imm:012b}{registers.get(instruction_parts[1])}{registers.get(instruction_parts[2])}{opcode}"
                binary_output.append(machine_code)
            elif instruction_parts[0] == "jal":
                imm = labels.get(instruction_parts[1]) - pc
                if imm < 0:
                    imm += 1 << 12
                machine_code = f"{imm:020b}{opcode}"
                binary_output.append(machine_code)
            else:
                return None, f"Error: Unknown instruction at line {line_number}"
            pc += 1
        else:
            return None, f"Error: Unknown opcode at line {line_number}"
    if "zero" not in registers.values():
        return None, "Error: Register 'zero' (x0) not found in register table"
    binary_output.append("00000000000000000000000000000000")  # Virtual Halt instruction
    return binary_output, None

def main():
    with open("C:\Users\tewar\OneDrive\Desktop\CO Project", "r") as f:
        binary_output, error = assemble(f)
    if error:
        print(error)
    else:
        with open("output.txt", "w") as f:
            for binary in binary_output:
                f.write(binary + "\n")
