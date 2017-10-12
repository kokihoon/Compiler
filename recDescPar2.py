
token = ''
token_list = ''
count = 0


def error():
    print("error")
    exit()

def blank():
    global token
    global count
    global token_list    
    token = token_list[count]
    count += 1

def term():
    global token
    global count
    global token_list

    temp = factor()
    while(token == ' ' or token=='\t'):
        blank()
    
    while(token =='*'):
        match('*')
        temp = int(temp) * int(factor())
    return temp

def factor():
    global token
    global count
    global token_list
    temp = ''
    while(token == ' ' or token=='\t'):
        blank()

    if(token=='('):
        match('(')
        temp = exp1()
        match(')')
    elif(token.isdigit()):
        count -= 1
        while(token_list[count]=='0' or token_list[count]=='1' or token_list[count]=='2' or token_list[count]=='3' or token_list[count]=='4' or token_list[count]=='5' or token_list[count]=='6' or token_list[count]=='7' or token_list[count]=='8' or token_list[count]=='9'):
            temp += token_list[count]
            count += 1
        token = token_list[count]
        count += 1
    else:
        error()
    return temp

def match(expectedToken):
    global token
    global count
    global token_list
    if(token == expectedToken):
        token = token_list[count]
        count +=1
    else:
        error()

def exp1():
    global token
    global count
    global token_list
    temp = term()

    while(token == ' ' or token == '\t'):
        blank()
    
    while(token=='+' or token=='-'):
        if(token == '+'):
            match('+')
            temp = int(temp) + int(term())

        elif(token=='-'):
             match('-')
             temp = int(temp) - int(term())
    return temp
    
def main():
    global token
    global count
    global token_list    
    result = ''
    token_list = input()
    token_list+='\n'
    token = token_list[count]
    count += 1
    result = exp1()
    if(token =='\n'):
        print("Result = ", result)
    else:
        error()

if __name__ == '__main__':
    main()