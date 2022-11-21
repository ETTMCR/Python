def num2ease(the_num):
    """
    A function which convert a number into is digit ease type , e.g. 1234567890 --> 1_234_567_890.
    It returns str type, which can be converted into integer by int
    """
    #numun=(str(number)).split()
    #print (numun)
    list1=[]
    list2=[]
    list1[:0] = str(the_num)
    list1[::-1]=str(the_num) # reversed order
    for x in range(0,len(list1)):
        if x%3 ==0 :
            list2.append('_')
            list2.append(list1[x])
        else :
            list2.append(list1[x])
    if list2[0]=='_' :
        (list2.pop(0))
    list2=list2[::-1]
    num_converted = ''.join(list2)
    return num_converted

number = 12300456789   # --> 12_300_456_789
print (num2ease((number)))
