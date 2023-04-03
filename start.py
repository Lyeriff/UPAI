from collections import defaultdict
from opcodes import OPCODES
from time import sleep
class Stack:
    stack = []
    pointer = 0
    def push(self, v):
        self.stack.append(v)
        self.pointer += 1
        return 1
        
    def pop(self):
        self.pointer -= 1  
        return self.stack.pop()
    
    def __str__(self) -> str:
        return f"{self.stack}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __bool__(self):
        return True if self.stack else False
    
class Memory():
    memory = defaultdict(int)
    def __init__(self) -> None:
        self.memory["%STACK%"] = Stack()

    def direct_addressing(self, string):
        return self.memory[str(string)]
    
    def indirect_addressing(self, string):
        return self.memory[str(self.memory[string])]
    
    def immediate_addressing(self, string):
        return int(string[1:])
    
    def under_addressing(self, string):
        return memory[string[1:-1]+":"]

    adressing_chart = {"[": indirect_addressing, "(": under_addressing, '#': immediate_addressing}

    def __getitem__(self, string):
        string = string.lstrip()
        
        if string[0]=='[':
            return self.indirect_addressing(string[1:-1])
        elif string[0]=='#':
            return self.immediate_addressing(string)
        elif string[0]=="(":
            return self.under_addressing(string)
        return self.memory[string]

    def __setitem__(self, key, value):
        self.memory[key] = value

    def __str__(self) -> str:
        s = "MEMORY--> \n" + "\n".join([f"{i} : {self.memory[i]}" for i in self.memory])
        return s
    
    def __repr__(self) -> str:
        return self.__str__()
    
    
class Instruction:
    opcode = None
    operands = []
    def __init__(self,string) -> None:
        
        if not string or string == '\n':
            self.opcode = "EMPTY"
            self.operands = ["-"]
            return
        S = string.split(maxsplit=1)
        self.opcode = S.pop(0) if S else "EMPTY"
        self.operands = S[0].split(",", maxsplit=1) if len(S) else [""]
    
    def __str__(self) -> str:
        temp_s = " ".join(i for i in self.operands)
        return f"{self.opcode} {temp_s}"
    
    def __repr__(self) -> str:
        return self.__str__()


def parse_instructions(IN_string:str) -> list:
    FUNC_SET = {}
    FN_list = IN_string.split('_end')
    for func in FN_list:
        split_list = func.split('\n')
        # split_list = [i for i in split_list if i != '']
        # print(split_list)
        if not split_list: continue
        FUNC_SET[split_list[1]] = [Instruction(i) for i in split_list[2:]]
    return FUNC_SET

def parse_instructions2(memory, IN_string):
    INS_List = []
    
    for i, instr in enumerate(IN_string.split('\n')):
        if instr and instr[0] == "_":
            memory[instr] = i+1
            INS_List.append(Instruction(""))
        else:
            INS_List.append(Instruction(instr))
    
    return INS_List

def run_instructions(memory, INS:list):
    
    ptr = 0 
    ptr = memory['_main:']
    memory["%PC%"] = ptr
    while ptr < len(INS):
        ptr = memory["%PC%"]

        inst = INS[ptr]
        opr1 = inst.operands[0]
        opr2 = inst.operands[1] if len(inst.operands) >1 else ""
        
        ret_hold = OPCODES[inst.opcode](memory, opr1, opr2)
        
        
        if ret_hold is None:
            ptr += 1
        else:
            ptr = ret_hold
        
        memory["%PC%"] = ptr
    
    return 0

def read_close(path = 'code.upai'):
    upai_file = open(path, "r")
    data = upai_file.read()
    upai_file.close()
    return data



memory = Memory()

ins_set = read_close('codes/code3.upai')
INS_LIST = parse_instructions2(memory, ins_set)
run_instructions(memory, INS_LIST)


# print(bin(-66)[3::])