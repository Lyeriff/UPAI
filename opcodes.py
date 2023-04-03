def addr(memory, reg1:str, reg2:str) ->None:
    if reg2.isnumeric():
        memory[reg1] += int(reg2)
    else:
        memory[reg1] += memory[reg2]

def multr(memory, reg1:str, reg2:str) ->None:
    if reg2.isnumeric():
        memory[reg1] *= int(reg2)
    else:
        memory[reg1] *= memory[reg2]

def xorr(memory, reg1:str, reg2:str) ->None:
    # print("\ndat :", memory[reg1], memory[reg2])
    # print("\nxor :", memory[reg1]^memory[reg2])
    memory[reg1] ^= memory[reg2]


def andr(memory, reg1:str, reg2:str) ->None:
    memory[reg1] &= memory[reg2]

def orr(memory, reg1:str, reg2:str) ->None:
    memory[reg1] |= memory[reg2]


def shr(memory, reg1:str, reg2:str) ->None:
    memory[reg1] >>= memory[reg2]


def shl(memory, reg1:str, reg2:str) ->None:
    memory[reg1] <<= memory[reg2]


def mov(memory, reg1:str, reg2:str):
    if reg2.isnumeric():
        memory[reg1] = int(reg2)
    else:
        memory[reg1] = memory[reg2]

def movs(memory, reg1:str, reg2:str):
    memory[reg1] = reg2
    

def subr(memory, reg1:str, reg2:str) ->None:
    if reg2.isnumeric():
        memory[reg1] -= int(reg2)
    else:
        memory[reg1] -= memory[reg2]

def inc(memory, reg1:str, reg2="") ->None:
    memory[reg1] += 1

def dec(memory, reg1:str, reg2="") ->None:
    memory[reg1] -= 1

def rprint(memory, reg1:str, reg2="") ->None:
    if memory[reg1]=="%endl%": print()
    else: print(memory[reg1], end=" ")

def print_ascii(memory, reg1:str, reg2="") -> int | None:
    print(ord(memory[reg1]), end="")
    return None

def empty_ins(memory, reg1:str, reg2="") -> None:
    return None

def jumpif(memory, reg1:str, reg2="") -> int | None:
    if memory[reg1]:
        if reg2[0] not in["(", "[", "#"]:
            return int(reg2)
        else:
            return memory[reg2]
    return None

def jumpinv(memory, reg1:str, reg2="") -> int | None:
    if memory[reg1]:
        if reg2[0] not in ["(", "[", "#"]:
            return int(reg2)
        else:
            return memory[reg2]
    return None
def jumpE(memory, reg1:str, reg2="") -> int:
    if memory["%CMP%"]:
        return memory[reg2]
    return None



def comp_store(memory, reg1:str, reg2="") -> int | None:
    # print(memory[reg1], memory[reg2])
    if memory[reg1] == memory[reg2]:
        memory["%CMP%"] = 1
    else:
        memory["%CMP%"] = 0

def arr(memory, reg1:str="", reg2="") -> None:
    index = int(reg1)
    for i in reg2.split(","):
        memory[str(index)] = int(i)
        index += 1



def call(memory, reg1:str, reg2="") -> None:
    if reg1.isnumeric():
        memory["%STACK%"].push(memory["%PC%"]+1)
        return int(reg1)
    else:
        
        memory["%STACK%"].push(memory["%PC%"]+1)
        return int(memory[reg1+":"])
        
    
def ret(memory, reg1:str="", reg2="") -> None:
    if memory["%STACK%"]:
        return memory["%STACK%"].pop()
    return memory["%PC%"] + 1

def desp_mem(memory, reg1:str="", reg2="") -> None:
    print(memory)

def end(memory, reg1:str="", reg2="") -> None:
    exit()
    

OPCODES = {"ADD": addr, 
           "SUB": subr, 
           "MUL": multr,
           "MOV": mov, 
           "XOR": xorr,
           "OR": orr,
           "AND": andr, 
           "SHR": shr,
           "SHL": shl,
           "MOVS": movs,
           "RPRINT": rprint, 
           "INC": inc, 
           "DEC": dec, 
           "JUMP": jumpif,
           "JUMPE": jumpE,
           "JUMPINV": jumpinv,
           "RASCPRINT": print_ascii, 
           "EMPTY": empty_ins,
           "CMP": comp_store,
           "CALL" : call,
           "RET" : ret,
           "ARR": arr,
           "SMEM": desp_mem,
           "END": end}



