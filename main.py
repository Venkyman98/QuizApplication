class quiz:

    def __init__(self):
        
        print()
        print('Welcome to UPSC Lite!')
        self.question_input = []
        self.topic = []
        self.difficulty = []
        self.options = []
        self.answer = {}
        self.question_no = 1
        self.total_score = 0
        self.role()


    def question(self):
        flag = True
        while flag == True:
            question = input('Enter your question:\n')
            self.question_input.append(question)
            tp = input('Enter Section:\n')
            self.topic.append(tp)
            df = input('Enter Difficulty:\n')
            self.difficulty.append(df)
            a = []
            print('Enter the Options:\n')
            for i in range(4):
                a.append(input('Option '+str((i+1))+': '))
            self.options.append(a)
            

            self.answer[self.question_no]=int(input('Enter the correct option: \n'))
            self.question_no += 1
            

            new = input('Press Y to add more question or N to stop:\n')
            if new == 'N' or new == 'n':
                flag = False
                print()
                self.admin_menu()
            else:
                pass



    def display(self):
        print('Here are the total number of questions:',len(self.question_input))
        print()
        for i in range(len(self.question_input)):
            print('Question: '+self.question_input[i])
            for j in range(len(self.options[i])):
                print(str(j+1)+')'+str(self.options[i][j]))
            print()
        self.role()

    def admin(self):
        name = input('Enter Name:\n')
        ID = input('Enter passID:\n')
        print()
        print('Hello! Welcome Mr',name)
        print()
        self.admin_menu()
        
    def admin_menu(self):
        print('1.Add questions\n2.Display questions\n3.Exit')
        n=int(input())
        if n==1:
            self.question()
        elif n==2:
            self.display()
        elif n==3:
            self.role()
        else:
            print('Enter valid choice')
            self.admin_menu()

    def student(self):
        name = input('Enter Name:\n')
        id = int(input('Enter Id:\n'))
        print('Hello',name)
        print('Your Quiz is ready!')
        print()
        self.student_menu()

    def student_menu(self):
        print('1.View Sections\n2.Give Test\n3.Exit')
        f=int(input())
        if f==1:
            self.view_sections()
        elif f==2:
            self.give_test()
        elif f==3:
            self.role()
        else:
            print('Enter valid choice')
            self.student_menu()



    def view_sections(self):
        x=set(self.topic)
        print('Sections:\n',x)
        print()
        self.student_menu()

    def give_test(self):
        print()
        print('Welcome to your quiz!')
        print('The marking system for the following quiz is pretty simple.')
        print('For easy questions - 10 marks\nFor medium questions - 20 marks\nFor hard questions - 30 marks')
        print('All the best!')
        print()
        score = 0

        for i in range(len(self.question_input)):
            print('Section:'+self.topic[i])
            print('Level of Difficulty:',self.difficulty[i])
            print()
            print(self.question_input[i])
            for j in range(len(self.options[i])):
                print('Option '+str(j+1)+')'+str(self.options[i][j]))
            
            print()
            std_choice = int(input('Enter option number:'))
            print()

            if std_choice == self.answer[i+1]:
                
                if self.difficulty[i] == 'easy':
                    score += 10
                elif self.difficulty[i] == 'medium':
                    score += 20
                elif self.difficulty[i] == 'hard':
                    score += 30
                    # self.total_score += score
            self.total_score = 0
            for h in self.difficulty:
                if h == 'easy':
                    self.total_score += 10
                elif h == 'medium':
                    self.total_score += 20
                elif h == 'hard':
                    self.total_score += 30


        print('You scored',str(score),'out of',self.total_score)
        print('Have a nice day! :)')
    
    def role(self):
        print('\nChoose your role: \n1.Admin \n2.Student')
        choice = int(input())
        if choice == 1:
            self.admin()
        elif choice == 2:
            self.student()

a = quiz()