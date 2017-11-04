# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:10:53 2017

@author: Fabian
"""

class ABBADiv1(object):
    def canObtain(self,initial,target):
        stringinitial = initial
        stringtarget = target
        #check if initial in target or reversed
        Stack = [stringinitial] 
        if (stringinitial in stringtarget) or (stringinitial[::-1] in stringtarget):
            while True:
            #append all possible moves
                for item in Stack[:]:  
                    Stack.remove(item)
                    Stack.append(self.addA(item))
                    Stack.append(self.addB(item))
                     
                newStack = []
                matches = 0
                for item in Stack[:]:
                    if item == stringtarget:
                        return "Possible"
                    
                    if ((item in stringtarget) or (item[::-1] in stringtarget)) and (len(item) <= len(stringtarget)):
                        newStack.append(item)
                        matches += 1
                        continue
                
                if matches != 0:    
                    Stack = newStack
                else:
                    break
        return "Impossible"    
        
    
        
    def addA(self,String):
        String += "A"
        return String
    
    def addB(self,String):
        String += "B"
        String = String[::-1]
        return String
    
if __name__ == "__main__":
    ABBA = ABBADiv1()
    print(ABBA.canObtain("AAABAAABB","BAABAAABAABAABBBAAAAAABBAABBBBBBBABB"))
    
    
    #BAAAAAABBAA
    #ABBAAAAAAB