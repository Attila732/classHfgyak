from FileReader import DolgozoFile

class MiskolcFile:
    def __init__(self):
        self.workerList=[]
    def read(self):
        dolg=DolgozoFile()
        self.workerList=dolg.readFile()
        print(type(self.workerList))
          
    def writeMiskolc(self):
        file=open("miskolc.txt","w",encoding="utf-8")
        for worker in self.workerList:
            if (worker.city=="Miskolc"):
                # vesszo=file.write(",")
                file.write(worker.name)
                file.write(",")
                file.write(worker.city)
                file.write(",")
                file.write(worker.address)
                file.write(",")
                file.write(worker.salary)
                file.write(",")
                file.write(worker.bonus)
                file.write(",")
                file.write(worker.born)
                file.write(",")
                file.write(worker.hire)
                # file.write("\n")
        file.close()    


misFile=MiskolcFile()
misFile.read()  
misFile.writeMiskolc() 
      
