#Frequency of every unique character in word
def freq(my_word:str) -> dict:
    myfreq = {}
    for e in my_word:
        if e in myfreq:
            myfreq[e] += 1
        else:
            myfreq[e] = 1
    return(myfreq)
print(freq("david"))
print(freq("catherine"))
print(freq("watermelon"))
