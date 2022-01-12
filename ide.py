from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess
file_path =''
def run():
    if file_path=='':
        save_prompt = Toplevel()
        text = Label(save_prompt, text = 'Please save your code')
        text.pack()
        return text
    command = f' python -m {file_path}'
    process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output,error = process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)
def set_file_path(path):
    global file_path
    file_path=path
def runc():
    code = editor.get('1.0',END)
    exec(code)
compiler = Tk()
compiler.title('PyLord')
menu_bar = Menu(compiler)

def save_As():
    try:
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files','*.py')])
        else:
            path = file_path
        #path = asksaveasfilename(filetypes=[('Python Files','*.py')])
        with open(path,'w') as file:
            code = editor.get('1.0',END)
            file.write(code)
            #editor.delete('1.0',END)
            #editor.insert(code)
            set_file_path(path)
    except Exception as e:
        print(e)

def op():
    try:
        path = askopenfilename(filetypes=[('Python Files','*.py')])
        with open(path,'r') as file:
            code = file.read()
            editor.delete('1.0',END)
            editor.insert('1.0',code)
            set_file_path(path)
    except Exception as e:
        print(e)

run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command = run)
menu_bar.add_cascade(label='Run',menu=run_bar)

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Open',command = op)
file_menu.add_command(label='Save',command =save_As )
file_menu.add_command(label='Save As',command = save_As)
file_menu.add_command(label='Exit',command = exit)
menu_bar.add_cascade(label='File',menu=file_menu)

editor = Text()
editor.pack()

code_output = Text(height=6)
code_output.pack()

compiler.config(menu=menu_bar)
compiler.mainloop()