#http://xkcd.com/710/ or you could leave the job to you computer and go out with your friends :P
number = int(raw_input())
stack = []
while number!=1:
    if number%2==0: number = number//2
    else:   number = 3*number+1
    stack.append(number)
print(len(stack))
