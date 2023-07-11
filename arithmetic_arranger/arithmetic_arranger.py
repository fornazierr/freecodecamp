import re

def real_len(length: int) -> int:
  if length == 1:
    return 3
  elif length == 2:
    return 4
  elif length == 3:
    return 5
  elif length >= 4:
    return 6
  
  

def arithmetic_arranger(problems, awnsers):
  #max 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."

  linha1 = list()
  linha2 = list()
  ops = list()
  linha4 = list()
  tamanho = list()

  for i in problems:
    val1 = i.split(" ")[0]
    op = i.split(" ")[1]
    val2 = i.split(" ")[2]

    if len(val1) >= 5 or len(val2) >= 5:
      return "Error: Numbers cannot be more than four digits."

    if op != "+" and op != "-":
      return "Error: Operator must be '+' or '-'."

    if re.search("[a-zA-Z]", val1) or re.search("[a-zA-Z]", val2):
      return "Error: Numbers must only contain digits."
    
    res = 0
    if op == "+":
      res = str(int(val1) + int(val2))
    elif op == "-":
      res = str(int(val1) - int(val2))
    
    linha1.append(val1)
    linha2.append(val2)
    ops.append(op)
    linha4.append(res)
    if (len(val1) >= len(val2)):
      tamanho.append(real_len(len(val1)))
    else:
      tamanho.append(real_len(len(val2)))

  l1 = ""
  l2 = ""
  l3 = ""
  l4 = ""
  for i in range(0, len(linha1)):
    #montar a linha
    sz = tamanho[i]
    l1 = l1 + f"{linha1[i]:>{sz}}{'':>4}"
    l2 = l2 + f"{ops[i]:<1}{linha2[i]:>{sz-1}}{'':>4}"
    l3 = l3 + f"{'-'*sz}{'':>4}"
    l4 = l4 + f"{linha4[i]:>{sz}}{'':>4}"
  
  return f"{l1}\n{l2}\n{l3}\n{l4}"