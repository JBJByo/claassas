class gugudanClass:
    def setInput(self):
        startDan = int(input("시작 단"))
        endDan = int(input("마지막 단"))
        self.hiddenstartDan = startDan
        self.hiddenendDan = endDan

    def loginProcess(self):
        password = input("비밀번호")
        if(password == "1234"):
            self.hiddenAllow = True
        else:
            self.hiddemAllow = False

    def setJungsuk(self):
        outputStyle = input("정석대로 출력하려면 1을 입력")
        self.hiddenOutputStyle = outputStyle


    def gugudanOutput(self):
        if int(self.hiddenOutputStyle) == 1:
            for dan in range(self.hiddenstartDan, self.hiddenendDan+1):
                for i in range(1,10):
                    print(f"{i}*{dan}={dan*i}")     

        else:
            for dan in range(self.hiddenstartDan, self.hiddenendDan+1):
                for i in range(1,10):
                      print(f"{i}*{dan}={dan*i}")     

    def gugudanIntrodue(self):
        print("구구단이다.")

gugudanClass = gugudanClass()
gugudanClass.gugudanIntrodue()
gugudanClass.setInput()
gugudanClass.setJungsuk()
gugudanClass.gugudanOutput()
