import timeit

import ascii
Sample = "COME away come away, death And in sad cypres let me be laid Fly away fly away, breath I am slain by a fair cruel maid My shroud of white stuck all with yew O prepare it My part of death no one so true Did share it Not a flower not a flower sweet On my black coffin let there be strown Not a friend, not a friend greet My poor corse, where my bones shall be thrown A thousand thousand sighs to save Lay me O where Sad true lover never find my grave To weep there"
class hModulo:
    def __init__(self):
        self.M = 499
        self.HashT =[[]]*(self.M+1)
    def mKey(self, string):
        key = ""
        for char in string:
            key += str(ord(char))
        return int(key)
    def modHash(self, key):
        return key % self.M
    def modinsert(self, key, value):
        hValue = self.modHash(key)
        if self.HashT[hValue] == []:
            self.HashT[hValue] = [value]
            return
        else:
            for i in range(len(self.HashT[hValue])):
                if self.HashT[hValue][i]['key'] == key:
                    self.HashT[hValue][i]['position'].append(value['position'][0])
                    return
            self.HashT[hValue].append(value)
    def ModSearch(self, key):
        hValue = self.modHash(key)
        if self.HashT[hValue] != []:
            for i in self.HashT[hValue]:
                if i["key"] == key:
                    return i["position"]
                return
        else:
            return
class hMulti:
    def __init__(self):
        self.M = 499
        self.G = .314159
        self.HashTable = [None]*self.M
    def mKey(self, string):
        key = ""
        for char in string:
            key += str(ord(char))
        return int(key)
    def Hash(self, key):
        a = float(key) * self.G
        b = a % 1
        c = int(b*self.M)
        return c
    def multiinsert(self, key, value):
        hValue = self.Hash(key)
        if self.HashTable[hValue] == None:
            self.HashTable[hValue] = value
        else:
            for i in range(hValue+1, len(self.HashTable)):
                if self.HashTable[i] == None:
                    self.HashTable[i] = value
                    return
                elif self.HashTable[i]["key"] == key:
                    self.HashTable[i]["position"].append(value["position"][0])
                    return
    def MultiSearch(self, key):
        hValue = self.Hash(key)
        if self.HashTable[hValue] == None:
            return
        elif self.HashTable[hValue]["key"] == key:
            return self.HashTable[hValue]["position"]
        else:
            for i in range(hValue+1, len(self.HashTable)):
                if self.HashTable[i] == None:
                    return
                if self.HashTable[i]["key"] == key:
                    return self.HashTable[i]["position"]
hello = hModulo()
hello2 = hMulti()
string = ""
def Modulo():
    string = ""
    for i in range(len(Sample)):
        if Sample[i] != " ":
            string += Sample[i]
        else:
            value = {"key": hello.mKey(string), "position": [i - len(string)], "word": string}
            hello.modinsert(value["key"], value)
            string = ""
        if i == len(Sample)-1:
            value = {"key": hello.mKey(string), "position": [i - len(string)], "word": string}
            hello.modinsert(value["key"], value)
    print(hello.ModSearch(hello.mKey("flower")))
    print(hello.HashT)
def Multiplication():
    string = ""
    for i in range(len(Sample)):
        if Sample[i] != " ":
            string += Sample[i]
        else:
            value = {"key": hello.mKey(string), "position": [i - len(string)], "word": string}
            hello2.multiinsert(value["key"], value)
            string = ""
        if i == len(Sample)-1:
            value = {"key": hello.mKey(string), "position": [i - len(string)], "word": string}
            hello2.multiinsert(value["key"], value)
    print(hello2.MultiSearch(hello.mKey("flower")))
    print(hello2.HashTable)
print(timeit.timeit(Multiplication, number=1))
print(timeit.timeit(Modulo, number=1))
