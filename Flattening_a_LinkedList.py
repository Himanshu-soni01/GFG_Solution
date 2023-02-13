def flatten(root):
    #Your code here
    count=1
    b=root
    hold=root.next
    while hold:
        while b.bottom:
            b=b.bottom
            count+=1
        b.bottom = hold
        hold=hold.next
        
    while b.bottom:
        b=b.bottom
        count+=1
    
    for i in range(count):
        b=root
        for i in range(count-1):
            if b.data>b.bottom.data:
                b.data,b.bottom.data = b.bottom.data,b.data
            b=b.bottom

    return root
