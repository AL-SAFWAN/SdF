
class User:
    
    def __init__(self, email,name, password) -> None:
        self.email = email;
        self.name = name
        self.password= password
        
def f1():
    print("hello")
def f2():
    print("world")

questions= ['option 1', 'option 2', 'option 3']
anwsers=[f1,f2, lambda :print("this is from lambda")]

def createQuestions(qestions: list) -> str:
    newQuestions = ""
    for i,q in enumerate(qestions):
        newQuestions += f"{i+1}) " + q + " \n"
    return newQuestions
    

def Menu(questions: list, anwsers:list) -> None:
    print(questions, anwsers)
    #  make a question list
    q = createQuestions(questions)
    isError = True 
    
    while isError:
      try:
          a = int(input(q))  
          isError = False
      except:
          print("enter a number")
          continue
      if 0<= a <= len(anwsers):
        anwsers[a-1]()
      else:
        print (f"Valid Option: 1-{len(anwsers)}")
        isError= True
    
def userAuthentication():
    # save the user name and password
        
    Menu(["Login", "Create an account"],[lambda :Menu(questions,anwsers),f1] ) 


userAuthentication()
#Menu(questions, anwsers)1

    stdscr.nodelay(True)
    x,y,z = 0,0,0
    
    while True:
        z+=1 
        try:
            key = stdscr.getkey()   
        except:
            key = None
        if key == "KEY_LEFT":
            x-=1
            pass
        elif key == "KEY_RIGHT":
            x +=1
        elif key == "KEY_DOWN":
            y+= 1
        elif key == "KEY_UP":
            y-=1
        stdscr.clear() 
        stdscr.addstr(0,z//600,'hello world')
        stdscr.addstr(y,x,"0")
        stdscr.refresh()
            
            
            
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_YELLOW)
    h,w = stdscr.getmaxyx()
    text = "Hello World"
    x = w//2 - len(text)//2
    y = h//2
    
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y,x,text)
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    
    stdscr.get_wch() 