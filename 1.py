def anagrams(str1, liststr):
    newlist= []
    slovo = sorted(str1)
    for s in liststr:
        if slovo == sorted(s):
            newlist.append(s)
    return newlist

print(anagrams("sosi", ["sosiska", "sos", "isos", "ssoi"]))
print(anagrams ("sos", ["sosiska", "kiska"])) 