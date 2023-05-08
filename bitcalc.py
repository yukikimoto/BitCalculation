def binary_addition(a, b): #足し算
    carry = "0"
    result = []
    
    if len(a) != len(b):
        if len(a) > len(b):
            while len(a) != len(b):
                b.insert(0, "0")
        else:
            while len(a) != len(b):
                a.insert(0, "0")
            

    for i in reversed(range(len(a))):
        if a[i] == "1" and b[i] == "1" and carry == "1":
            result.insert(0, "1")
            carry = "1"
        elif a[i] == "0" and b[i] == "0" and carry == "0":
            result.insert(0, "0")
            carry = "0"
        elif (a[i] == "1" and b[i] == "1" and carry == "0") or (a[i] == "1" and b[i] == "0" and carry == "1") or (a[i] == "0" and b[i] == "1" and carry == "1"):
            result.insert(0, "0")
            carry = "1"
        else:
            result.insert(0, "1")
            carry = "0"
            
    if carry == "1":
        result.insert(0, "1")
    return result


def binary_subtraction(a, b): #引き算
    x = "0001"
    binary_x = list(x)
    if len(a) != len(b):
        if len(a) > len(b):
            while len(a) != len(b):
                b.insert(0, "0")
        else:
            while len(a) != len(b):
                a.insert(0, "0")
                
    for i in range(len(b)):
        if b[i] == "0":
            b[i] = "1"
        else:
            b[i] = "0"
            
            
    complement_result = binary_addition(binary_x, b)
    
    s = binary_addition(a, complement_result)
    result = s[1:]
    return result




def binary_multiplication(a, b): #掛け算
    b_1 = list("0000")
    b_2 = list("0000")
    b_3 = list("0000")
    b_4 = list("0000")
    
    if b[3] == "1":
        b_1 = a.copy()

    if b[2] == "1":
        b_2 = a.copy()
        b_2.append("0")

        
        
    if b[1] == "1":
        b_3 = a.copy()
        for i in range(2):
            b_3.append("0")
        print(b_3)
            
    if b[0] == "1":
        b_4 = a.copy()
        for i in range(3):
            b_4.append("0")


    result_1 = binary_addition(b_1, b_2)
    result_2 = binary_addition(result_1 ,b_3)
    print(result_2)
    
    result = binary_addition(result_2 ,b_4)
    return result


def binary_calculation(binary_string1, binary_string2, binary_calc): #計算方法を判別
    binary_list1 = list(binary_string1)
    binary_list2 = list(binary_string2)
    
    if binary_calc == "add" or "subt" or "mult" or "div":
        if binary_calc == "add":
            binary_result = "".join(binary_addition(binary_list1, binary_list2))

        elif binary_calc == "subt":
            binary_result = "".join(binary_subtraction(binary_list1, binary_list2))

        elif binary_calc == "mult":
            binary_result = "".join(binary_multiplication(binary_list1, binary_list2))

        else:
            binary_result = binary_addition(binary_list1, binary_list2)

    else:
        binary_result = "演算方法が間違っています。"
    
    return binary_result


binary_string1 = input("一つ目の数値を入力してください : ")
binary_string2 = input("二つ目の数値を入力してください : ")
binary_calc = input("演算方法を入力してください : ")
binary_result = binary_calculation(binary_string1, binary_string2, binary_calc)
print("結果:", binary_result)
