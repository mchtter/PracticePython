class Questions:
    def __init__(self, questionText, questionAnswer, choiceList):
        self.questionText = questionText
        self.questionAnswer = questionAnswer
        self.choiceList = choiceList

    def answerCheck(self, answer):
        return self.questionAnswer == answer


class Quiz:
    def __init__(self, questionText):
        self.questionText = questionText
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questionText[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.questionText}')

        for q in question.choiceList:
            print("-" + q)

        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.answerCheck(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questionText) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Score: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questionText)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz OVER!")
        else:
            print(
                f"Question {questionNumber} of {totalQuestion}".center(100, '*'))


q01 = Questions('Where is the capital of Turkey?',              'Ankara',       [
                'Izmir',        'Istanbul',   'Ankara',        'Diyarbakır', 'Erzurum'])
q02 = Questions('Where is the capital of United States?',       'Washington DC', [
                'Washington DC', 'New York',   'Seattle',       'Miami',      'Los Angeles'])
q03 = Questions('Where is the capital of United Kingdom?',      'London',       [
                'Oxford',       'Manchester', 'London',        'Cambridge',  'Liverpool'])
q04 = Questions('Where is the capital of Germany?',             'Berlin',       [
                'Munih',        'Berlin',     'Frankfurt',     'Hamburg',    'Köln'])
q05 = Questions('Where is the capital of Belgium?',             'Brussels',     [
                'Hasselt',      'Brugge',     'Anvers',        'Brussels',   'Halle'])
q06 = Questions('Where is the capital of Brazil?',              'Brasilia',     [
                'Brasilia',     'Salvador',   'Rio de Janeiro', 'São Paulo',  'Santo Andrê'])
q07 = Questions('Where is the capital of Egypt?',               'Cairo',        [
                'Ismailiye',    'Luksor',     'Asuan',         'Dimyat',     'Cairo'])
q08 = Questions('Where is the capital of Iraq?',                'Baghdad',      [
                'Erbil',        'Musul',      'Kerkuk',        'Baghdad',    'Basra'])
q09 = Questions('Where is the capital of Israel?',              'Tel Aviv',     [
                'Netanya',      'Tel Aviv',   'Hayfa',         'Tiberya',    'Akka'])
q10 = Questions('Where is the capital of Mexico?',              'Mexico City',  [
                'Mexico City',  'Guadalajara', 'Cancùn',        'Monterrey',  'Tijuana'])
q11 = Questions('Where is the capital of Netherlands?',         'Amsterdam',    [
                'Lahey',        'Rotterdam',  'Amsterdam',     'Utrecht',    'Maastricht'])
q12 = Questions('Where is the capital of Russia?',              'Moscow',       [
                'Petersburg',   'Soçi',       'Vladivostok',   'Moscow',     'Volgograd'])
q13 = Questions('Where is the capital of Uzbekistan?',          'Tashkent',     [
                'Buhara',       'Tashkent',   'Semekand',      'Tirmiz',     'Namangan'])
q14 = Questions('Where is the capital of Sweden?',              'Stockholm',    [
                'Visby',        'Göteborg',   'Malmö',         'Helsingborg', 'Stockholm'])
q15 = Questions('Where is the capital of Turkmenistan?',        'Ashgabat',     [
                'Daşoğuz',      'Türkmenabat', 'Ashgabat',      'Balkanabat', 'Atamurat'])
q16 = Questions('Where is the capital of Ukraine?',             'Kiev',         [
                'Lviv',         'Odessa',     'Harkov',        'Kiev',       'Çernivtsi'])
q17 = Questions('Where is the capital of United Arab Emirates?', 'Abu Dhabi',    [
                'Dubai',        'Sharjah',    'Abu Dhabi',     'Qaiwain',    'Fujairah'])
q18 = Questions('Where is the capital of Philippines?',         'Manila',       [
                'Manila',       'Quezon City', 'Makati',        'Cebu City',  'Baguio'])
q19 = Questions('Where is the capital of Pakistan?',            'Islamabad',    [
                'Lahor',        'Islamabad',  'Peşaver',       'Multan',     'Ketta'])
q20 = Questions('Where is the capital of Lebanon?',             'Beirut',       [
                'Trablusşam',   'Sayda',      'Beirut',        'Sur',        'Tyre'])
questionText = [q01, q02, q03, q04, q05, q06, q07, q08, q09,
                q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]


quiz = Quiz(questionText)
test = quiz.getQuestion()
index = quiz.questionIndex

quiz.loadQuestion()
