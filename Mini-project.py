class CalUtils:
    def calAvgheight(self):
        self.names=[]
        self.height=[]
        self.totalStudentheight=float()
        self.totalStudentcount=float()

    def new(self):
        name=input('enter name: ')
        height=float(input('enter the height: '))
        totalcount=['Tom','Lee',name]
        totalheight=[1.22,1.45,height]
        avgheight=sum(totalheight)/len(totalcount)
        print(avgheight)
        f=open('ListOfStudentHeight.txt','a')
        f.write('\n'+str(name)+'\t'+str(height))
        f=open('ListOfStudentHeight.txt','r')
a=CalUtils()
while True:
    a.new()