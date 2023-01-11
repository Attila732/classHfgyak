from dolgozok import Dolgozo
class reading:
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
        print(self.workerList)     
            
    def countSzeged(self):
        counter=0
        for worker in self.workerList:
            if(worker.city=="Szeged"):
                counter+=1
        print("Szegedi dolgozók: ",counter)     
    def maxSalary(self):
        name=""
        max=0
        for salar in self.workerList:
           
           
           if int(salar.salary)>max:
                max=int(salar.salary)
                name=salar.name
        print(max,name)    
           
            
           


kiir=reading()   
kiir.readFile()
kiir.countSzeged()
kiir.maxSalary()
   