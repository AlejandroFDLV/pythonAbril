class Worker:
    def __init__(self,id,fullName,address):
        #constructor, donde self sería como this.loquenecesite
        self.id=id
        self.fullName=fullName
        self.address=address
    def ShowDate(self):
        return f'Worker Data:\nId:{self.id}\nFull Name:{self.fullName}'
def main():
    #setear atributo como objWorker.id="Valor | cuando en def init self.id= ""
    objWorker = Worker('I-123','Carlos','Caracas')
    print(objWorker.ShowDate())
if __name__=='__main__':
    main()