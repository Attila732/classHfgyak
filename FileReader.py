from dolgozok import Dolgozo
class DolgozoFile:
    def __init__(self):
        self.workerList=[]
    def readFile(self): 
        print("Megszámlálás...")   
        
        file=open("dolgozok100.txt" , "r" , encoding="utf-8")
        row=file.readline()
        while(row):
            row=file.readline()
            if(len(row)!=0):
                rowSp=row.split(":")
                dolg=Dolgozo()
                dolg.name=rowSp[0]
                dolg.city=rowSp[1]
                dolg.address=rowSp[2]
                dolg.salary=rowSp[3]
                dolg.bonus=rowSp[4]
                dolg.born=rowSp[5]
                dolg.hire=rowSp[6]

                self.workerList.append(dolg)
        return self.workerList   
        