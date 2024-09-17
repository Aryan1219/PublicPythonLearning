def armstrong(num: str)-> str:
    act_num = int(num)
    num = [*num]
    

    num2 = 0
    for i in num:
        num2 += int(i)**3
    if num2  == act_num:
        return 'It is armstrong'
    else:
        return 'Not armstrong'
    
print(armstrong('153'))

