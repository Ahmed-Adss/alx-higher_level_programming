c=[]
def flatten(T):
    global c
    for i in range(len(T)):
        #if element is annything other than list
        if(isinstance(T[i],list)==False):
            c.append(T[i])
        #call flatten recursively till you don't get a list
        else :
            flatten(T[i])
#driver code
flatten([1,2,[3,4,5],'j',[7,[8,9]]])
print(c)
