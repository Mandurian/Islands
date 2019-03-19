# -*- coding: utf-8 -*-
from random import randint

"""
Created on Mon Jan 28 19:48:39 2019

@author: Nikodem Staszek
"""
class Liczba_wysp:
    
    def __init__(self,rzad,kolumna,macierz):
        self.rzad = rzad
        self.kolumna = kolumna
        self.macierz = macierz
         
    def czy_do_dfs(self,a,b,odwiedzony):
        return( b>=0 and b<self.kolumna  and a>=0 and a<self.rzad and not odwiedzony[a][b] and self.macierz[a][b]==1)
        
    def DFS(self, a,b,odwiedzony):
        numer_kol = [-1,-1,-1, 0,0,0, 1,1,1]
        numer_rzad =[-1, 0, 1,-1,0,1,-1,0,1]
        
        odwiedzony[a][b] = True;
        
        for c in range(len(numer_kol)):
            if(self.czy_do_dfs(a+numer_rzad[c],b+numer_kol[c],odwiedzony)):
                self.DFS(a+numer_rzad[c],b+numer_kol[c],odwiedzony)
            
    def licznik_wysp(self):
        licznik = 0
        
        
        odwiedzony = [[False for b in range(self.kolumna)]for a in range(self.rzad)] 
        #odwiedzony=[] 
       # for a in range(self.rzad):
       #    temp=[]
       #     for b in range(self.kolumna):
       #         temp.append(False)
       #     odwiedzony.append(temp)
       #     temp.clear()
       #     print(odwiedzony) 
            
        for a in range(self.rzad):
            for b in range(self.kolumna):
                if odwiedzony[a][b] ==  False and self.macierz[a][b] == 1:
                    self.DFS(a,b,odwiedzony)
                    licznik = licznik + 1
        return licznik
    def wypisz_macierz(self):
        
        for i in range(self.rzad):
            for j in range(self.kolumna):
                print(self.macierz[i][j],end=' ')
            print()    
 
r, k = int(input("rzedy: ")), int(input("kolumny: "))

map = [[1 if randint(1,4)>3 else 0 for a in range(r)]for b in range(k)]
wyspy = Liczba_wysp(len(map),len(map[0]),map)
b = wyspy.licznik_wysp()

wyspy.wypisz_macierz()
print ("liczba wysp to: "+str(b))
