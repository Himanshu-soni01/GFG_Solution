def maxInstance(s):
    dict_1 = {'a':0,'b':0,'n':0}
    dict_2 = {'l':0,'o':0}
        
    if len(s)<7:
        return 0
        
    for i in s:
        if i in dict_1:
            dict_1[i] += 1 
        elif i in dict_2:
            dict_2[i] += 1
        
    m_1=min(dict_1.values())
    m_2=min(dict_2.values())
        
    if m_2//2 == m_1:
        return m_1
    else:
        return min(m_2//2,m_1)

s="loonbalxballpoon"
print(maxInstance(s))