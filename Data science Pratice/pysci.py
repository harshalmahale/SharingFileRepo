
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Let's create a class called TextAnalyzer to analyze text.
class TextAnalyzer(object):
    # The __init__ method initializes the class with a 'text' parameter.
    # We will store the provided 'text' as an instance variable.
    def __init__(self, text):
        formatted_text = text.replace('.','').replace(',','').replace('!','').replace('?','')
        formatted_text = formatted_text.lower()
        self.fmttext = formatted_text
    
    def freqAll(self):
        wordlist = self.fmttext.split(' ')
        freqMap = {}
        for word in set(wordlist):
            freqMap[word] = wordlist.count(word)
        return freqMap
    

    def wordof(self,word):
        freqdict = self.freqAll()
        
        if word in freqdict:
            return freqdict[word]
        else:
            return 0        
        
        
analyzed = TextAnalyzer(givenstring)
print("formatted Text: ",analyzed.fmttext)

freqMap = analyzed.freqAll()
print(freqMap)

word = "dolor"
frequency = analyzed.wordof(word)
print("The specific word is ", word ,"appears",frequency,"times")