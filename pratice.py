pri = {"(": 3,")" : 3,"*":2,"/":2,"+":1,"-" :1}

n= list(input())
result = []
stack = []

for i in range(len(n)) :
    if n[i].isalnum() :
        print("피연사자가 들어왔음으로 result에 n[i](=%s)을 추가합니다"%n[i]) 
        result.append(n[i])
        print("값 추가후 result : ",end = " ")
        print(result)
        print("-------------------------------")


    elif len(stack) == 0 :
        print("stack이 비어 있음으로 stack 에 n[i](=%s)을 추가 합니다"%n[i])
        stack.append(n[i])
        print("값 추가후 stack : ",end = " ")
        print(stack)
        print("-------------------------------")

    
    elif n[i] == "(" : 
        print(" ( 이 들어왔음으로 그대로 stack 에 n[i](=%s)을 추가 합니다"%n[i])
        stack.append(n[i])
        print("값 추가후 stack : ",end = " ")
        print(stack)
        print("-------------------------------")

    elif stack and stack[-1] == "(" : 
        print("stack의 top 부분이 ( 임으로 tack 에 n[i](=%s)을 추가 합니다"%n[i])
        stack.append(n[i])
        print("값 추가후 stack : ",end = " ")
        print(stack)
        print("-------------------------------")

    elif stack and n[i] == ")" : 
        print("스택이 비어있지 않고 )이 들어왔음으로 top이( 될떄까지 pop합니다")
        while stack and stack[-1] != "(":
            n=stack.pop()
            print("현재 stack에서 pop한 값 : %s"%n)
            print("현재 stack 상태 : ",end = '')
            print(stack)
            print("-------------------------------")
            print("pop한 값을 result에 넣습니다")
            result.append(n)
            print("값 추가후 result : ",end = " ")
            print(result)
            print("-------------------------------")

        print("stack의 top부분이 ( 임으로 그부분을 pop해줍니다")    
        stack.pop()
        print("현재 stack 상태 : ",end = '')
        print(stack)
        print("-------------------------------")

    elif stack and n[i] in pri : 
        while stack and (pri[stack[-1]] >= pri[n[i]] ) :
            print("현재 들어온 값(=%s)의 우선순위가 stack의 top보다 작습니다"%n[i])
            print("현재 들어온 값을 stack 에 넣어줍니다")
            print("값(=%s) 추가후  stack 상태 : "%n[i],end = '')
            print(stack)
            stack.append(n[i])
            n = stack.pop()
            stack.append(n[i])
            print("현재 pop한 값 = %s"%n)
            print ("현재 stack 상태 : ")
            print(stack)
            print("-------------------------------")
            print("pop(=%s)한값을 result에 넣습니다"%n)
            result.append(n)
            print("값 추가후 result : ",end = " ")
            print(result)
            print("-------------------------------")
            
           
        print("현재 들어온 값(=%s)이 우선순위가 stack의 top 보다 큽니다 "%n[i])
        print("stack 의 값(=%s)을 추가합니다"%n[i])
        stack.append(n[i])    
        print("값(=%s) 추가후  stack 상태 : "%n[i],end = '')
        print(stack)
        print("-------------------------------")

while stack : 
    print("stack에 남아있는 모든 요소를 출력합니다")
    n = stack.pop()
    print("현재 pop한 값 = %s"%n)
    print("pop(=%s)한값을 result에 넣습니다"%n)
    result.append(n)
    print("값 추가후 result : ",end = " ")
    print(result)
    print("-------------------------------")
    


print("".join(list(map(str,result))))
