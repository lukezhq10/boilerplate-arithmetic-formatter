# if len(problems) > 5 return 'Error: Too many problems.'
def check_problem_count(problems):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  else:
    return None


def check_operator(string):
  if '/' in string or '*' in string:
    return "Error: Operator must be '+' or '-'." ''
  else:
    return None


def check_operands(string):
  operands = string.split()
  for operand in operands:
    if not operand.isdigit() and not (operand == '+' or operand == '-'):
      return 'Error: Numbers must only contain digits.'
    elif len(operand) > 4:
      return 'Error: Numbers cannot be more than four digits.'
  return None


def arithmetic_arranger(problems, sum=False):
  # problems is an array of math q's in strings
  # arranged_problems should be the arranged vers of the strings
  # if second arg = True, return the sum. If not called/default = False, return no sum

  # check problem count
  problem_count_error = check_problem_count(problems)
  if problem_count_error:
    return problem_count_error

  #initialize the lines
  top_line = ""
  bottom_line = ""
  dash_line = ""
  result_line = ""
  
  # for loop to go through each problem in the array
  for problem in problems:
    # check operators
    operator_error = check_operator(problem)
    if operator_error:
      return operator_error
    # check operands
    operand_error = check_operands(problem)
    if operand_error:
      return operand_error
    
    # split problem into operands and operators
    operand1, operator, operand2 = problem.split()

    #calculate length of longest operand
    length = max(len(operand1), len(operand2))

    #build formatted lines
    # 4 spaces at the end of each line to make space between problems
    top_line += operand1.rjust(length + 2) + "    "
    print(top_line)
    bottom_line += operator + " " + operand2.rjust(length) + "    "
    print(bottom_line)
    dash_line += "-" * (length + 2) + "    "
    print(dash_line)

    # calculate sum if requested
    if sum:
      if operator == '+':
        result = str(int(operand1) + int(operand2))
      else:
        result = str(int(operand1) - int(operand2))
      result_line += result.rjust(length + 2) + "    "

  # arrange the lines and remove any extra white spaces
  arranged_problems = top_line.rstrip() + "\n" + bottom_line.rstrip() + "\n" + dash_line.rstrip()

  # show sum if sum = true
  if sum and result_line:
    arranged_problems += "\n" + result_line.rstrip()
    
  return arranged_problems