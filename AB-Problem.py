# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:01:53 2017

@author: Fabian
"""
#N characters = 3
#K pairs = 2
#ABB
class AB():
    def createString(self,N,K):
        #first initiallize String
        String = ["A" for i in range(N)]
        #String = ["B","A","B","B","B","A","B"]
        Pairs = self.getPairs(String)


        while Pairs != K:
            Pairs = self.getPairs(String)
            if Pairs < K:
                String = String[1:] + ["B"]
            elif Pairs > K:
                String = String[1:] + ["A"]

            if String[:len(String)//2] == ["B" for i in range(len(String)//2)]:
                return "";
            
        return String

    def getPairs(self,String):
        Pairs = 0
        for i,mainIndex in enumerate(String):
            if mainIndex == "A":
                for subIndex in String[i+1:]:
                    if subIndex == "B":
                        Pairs += 1
            else:
                continue
        return Pairs
                    
        
if __name__ == "__main__":
    AB = AB()
    print(AB.createString(10,40))