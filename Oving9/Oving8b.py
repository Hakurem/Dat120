#1b & c) 

#lag klasse for flervalgs

    
class Flervalg:
    def __init__(self, question,answers,correct):
        self.question = question
        self.answers = answers
        self.correct = correct
        
        
    def __str__(self):
      output = f"{self.question}\n"
      for i,v in enumerate(self.answers):
          output += f"\n{i+1}. {v}"
      return output
     
        
    def checkans(self,ans):
        return ans == self.correct 
        
        
    def ask(self):
        print(self)
        while True:
            try:
                ans = int(input("Write the number of the correct choice: "))
                if ans >= 1 and ans <= len(self.answers):
                    break
                else:
                    print('Your option is not valid')
            except ValueError: 
                print('Your answer is not valid')
        
        print("\n")
        return self.checkans(ans)
       

class MultipleChoice:
    def __init__(self):
        self.Questions = list()
        self.Correct = 0
        self.Antall = 7
        
        self.Questions.append( Flervalg("What is an operating system?"
                                  ,["interface between the hardware and application programs","collection of programs that manages hardware resources","system service provider to the application programs","all of the mentioned"]
                                  ,4)
                              )
        self.Questions.append(
                           Flervalg("What is the main function of the command interpreter?"
                                 ,["to provide the interface between the API and application program","to handle the files in the operating system","to get and execute the next user-specified command","none of the mentioned"]
                                 ,3)
                           )
        
        self.Questions.append(
                           Flervalg("Which of the following is billionth of a second?"
                                 ,["Microsecond","NanoSecond","Terbyte","Gigabyte"]
                                 ,2)
                           )
        
        self.Questions.append(
                           Flervalg("In Operating Systems, which of the following is/are CPU scheduling algorithms?"
                                 ,["Priority","Round Robin","Shortest Job First","All of the mentsioned"]
                                 ,4)
                           )
        self.Questions.append(
                           Flervalg("To access the services of the operating system, the interface is provided by the ___________"
                                  ,["Library","System calls","Assembly instructions","API"]
                                 ,2)
                           )
        
        self.Questions.append(
                           Flervalg("What does TLB stand for in computer science?"
                                  ,["Tractor-Loader-Backhoe","Text Library","Toolbar","Translation Lookaside Buffer"]
                                 ,4)
                           )
       
        self.Questions.append(
                           Flervalg("CPU scheduling is the basis of ___________"
                                 ,["multiprogramming operating systems","larger memory sized systems","multiprocessor systems","none of the mentioned"]
                                 ,1)
                           )
        
        
    def start(self):
        for v in self.Questions:
            self.Correct += v.ask()
        
        print(f"Your score was {self.Correct}/{self.Antall}")
        
        if self.Correct <= 1: 
            print('Bad')
        elif self.Correct <= 3:
            print("Below average")
        elif self.Correct <= 5:
            print("Average")
        elif self.Correct <= 7:
            print("Very good")
        
        
        return
                
def StartQuestions():
    Test = MultipleChoice()
    Test.start()

StartQuestions()