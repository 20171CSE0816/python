from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tkinter as t
abot = ChatBot("vishal")

inf=open("out.txt",'r',encoding='utf-8')
of=open("a3.txt",'wb')
empty=''
r=inf.readline()
l=[]
convo=[]
while r!=empty:
    res = "".join(filter(lambda x: not x.isdigit(), r))
    a=res.replace('//, : pm - ', '').replace("//, : am -",' \n').replace('Vishal:','')
    of.write(a.encode('utf-8'))
    l.append(a.splitlines())
    r=inf.readline()
    
for i in l:
    convo.append(i[0])
    

trainer = ListTrainer(abot)

# now training the abot with the help of trainer

trainer.train(convo)

answer = abot.get_response("")
print(answer)
print("Talk to abot ")
while True:
  query = input()
  if query == 'exit':
        break
  answer = abot.get_response(query)
  print("abot : ", answer)
'''
main = t.Tk()

main.geometry("500x650")

main.title("My Chat abot")
img = t.PhotoImage(file="abot1.png")

photoL = t.Label(main, image=img)

photoL.pack(pady=5)


def ask_from_abot():
    query = textF.get()
    answer_from_abot = abot.get_response(query)
    msgs.insert(t.END, "you : " + query)
    print(type(answer_from_abot))
    msgs.insert(t.END, "abot : " + str(answer_from_abot))
    textF.delete(0, t.END)


frame = t.Frame(main)

sc = t.Scrollbar(frame)
msgs = t.Listbox(frame, width=80, height=20)

sc.pack(side=t.RIGHT, fill=t.Y)

msgs.pack(side=t.LEFT, fill=t.abotH, pady=10)

frame.pack()

# creating text field

textF = t.Entry(main, font=("Verdana", 20))
textF.pack(fill=t.X, pady=10)

btn = t.Button(main, text="Ask from abot", font=("Verdana", 20), command=ask_from_abot)
btn.pack()

main.mainloop()
'''