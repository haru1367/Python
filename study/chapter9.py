class SoccerPlayer(object):
    def __init__(self,name,position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self,back_number):
        self.back_number = back_number
    def __str__(self):
        return f'Hello, My name is {self.name}, I play in {self.position}, my back_number is {self.back_number}'
messi = SoccerPlayer('Messi','CF',10)
print(messi)
messi.change_back_number(30)
print(messi)

names =['이강인','손흥민','정우영']
positions=['CM','ST','LF']
numbers=[18,7,9]

players = [[name,position,number] for name, position, number in zip(names,positions,numbers)]

player_objects = [SoccerPlayer(name,position,number) for name,position,number in zip(names,positions,numbers)]
for i in range(0,len(names)):
    print(player_objects[i])


class Note:
    def __init__(self,contents=None):
        self.contents = contents
    
    def write_contents(self,contents):
        self.contents = contents
    
    def remove_all(self):
        self.contents=''

    def __str__(self):
        return self.contents

class Notebook:
    def __init__(self,title):
        self.title = title
        self.page_number = 1
        self.notes={}
    
    def add_note(self,note,page=0):
        if self.page_number<300:
            if page==0:
                self.notes[self.page_number] = note
                self.page_number+=1
            elif self.page_number>0 and self.page_number<300:
                self.notes={page:note}
                self.page_number+=1
            else:
                print('페이지가 모두 채워졌다.')
    def remove_note(self,page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print('해당 페이지는 존재하지 않는다.')
    def get_number_of_pages(self):
        return len(self.notes.keys())
            
