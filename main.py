# ini projek arithmetic formatter
# description:
# input : arithmatic_arranger(["3801 - 2", "123 + 49"])
# output:
""" 

  3801      123
-    2    +  49
------    -----

"""

def isP_OR_M(opr):
    return opr in "+-"

def length_check(string):
    return len(string)<5

def is_digit(string):
    return string.isdigit()

def arr_join(arr):
    res = []
    for item in arr:
        res+=item
    
    return res

def error_checker(arr):
    res_list=[]
    res_list.append(len(arr)<6)
    res_list.append(
        all(
            map(
                isP_OR_M,
                [problem.split(" ")[1] for problem in arr]
            )
        )
    )
    res_list.append(
        all(
            map(
                length_check,
                arr_join([problem.split(" ")[::2] for problem in arr])
            )
        )
    )
    res_list.append(
        all(
            map(
                is_digit,
                arr_join([problem.split(" ")[::2] for problem in arr])
            )
        )
    )

    return res_list

def splitter(string):
    return string.split(" ")

def prettier(arr,show_answer=False):
    if show_answer:
        return "\n".join(arr)
    return "\n".join(arr[:-1])

def get_max(num1,num2,res_num):
    if len(num1)==len(num2):
            if len(num1)==len(res_num):
                theMax=max(len(num1),len(num2),len(str(res_num)))+2
            else:
                if len(res_num)>max(len(num1),len(num2)):
                    theMax=max(len(num1),len(num2),len(str(res_num)))+1
                else:
                    theMax=max(len(num1),len(num2),len(str(res_num)))+2
    else:
        if len(res_num)>max(len(num2),len(num1)):
            theMax=max(len(num1),len(num2),len(str(res_num)))+1
        else:
            theMax=max(len(num1),len(num2),len(str(res_num)))+2

    return theMax

def arithmetic_arranger(problems,show_answers=False):
    errors=error_checker(problems)
    if not errors[0]: return "Error: Too many problems."
    if not errors[1]: return "Error: Operator must be '+' or '-'."
    if not errors[2]: return "Error: Numbers cannot be more than four digits."
    if not errors[3]: return "Error: Numbers must only contain digits."

    data=list(map(splitter,problems))

    data=[tuple(
        (data[i][j] for i in range(len(data)))
    ) for j in range(3)]

    results = list(map(eval,problems))
    results = list(map(str, results))

    max_list=[]
    for i in range(len(data[0])):
        theMax=get_max(data[0][i],data[2][i],results[i])
        
        max_list.append(theMax)

    lines = ["","","",""]
    for i in range(len(data[0])):
        lines[0]+=" "*(max_list[i]-len(data[0][i]))+data[0][i]+" "*4

        lines[1]+=data[1][i]+" "*(max_list[i]-1-len(data[2][i]))+data[2][i]+" "*4
        
        lines[2]+="-"*max_list[i]+" "*4

        lines[3]+=" "*(max_list[i]-len(results[i]))+results[i]+" "*4
    
    res=[]
    for item in lines:
        res.append(item[:-4])

    return prettier(res, show_answers)


# print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))


print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))

"""
  11      3801      1      123         1\n
+  4    - 2999    + 2    +  49    - 9380\n
----    ------    ---    -----    ------

  11     3801      1      123         1',
+  4    -2999    + 2    +  49    - 9380',
----    -----    ---    -----    ------',

  11      3801      1      123         1',
+  4    - 2999    + 2    +  49    - 9380',
----    ------    ---    -----    ------',


"""


# print("123".isdigit())