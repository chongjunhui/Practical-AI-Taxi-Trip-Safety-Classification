import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import tensorflow
import joblib

root = tk.Tk()
root.title('Portable Driving Classifier')
# root.iconbitmap('class.ico')
root.resizable(0, 0)
root.rowconfigure(14,weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=4)
# canvas = tk.Canvas(root, height=600, width=1000, bg='grey')
# canvas.grid(row=12, column=0)
# frame = tk.Frame(root, bg='white')
# # frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
left_side = tk.Frame(root)
middle_side = tk.Frame(root)
left_side.grid(row=0, column=0)
middle_side.grid(row=0, column=1)


global para_arr
global test_arr

def Close():
    root.destroy()

def deleteparams():
    inputtxt1.delete('1.0', tk.END)
    inputtxt2.delete('1.0', tk.END)
    inputtxt4.delete('1.0', tk.END)
    inputtxt5.delete('1.0', tk.END)
    inputtxt6.delete('1.0', tk.END)
    inputtxt7.delete('1.0', tk.END)
    inputtxt8.delete('1.0', tk.END)
    inputtxt9.delete('1.0', tk.END)
    inputtxt10.delete('1.0', tk.END)
    inputtxt11.delete('1.0', tk.END)



def saveparams():
    para_arr = []
    inp1 = inputtxt1.get(1.0, "end-1c")
    inp2 = inputtxt2.get(1.0, "end-1c")
    inp4 = inputtxt4.get(1.0, "end-1c")
    inp5 = inputtxt5.get(1.0, "end-1c")
    inp6 = inputtxt6.get(1.0, "end-1c")
    inp7 = inputtxt7.get(1.0, "end-1c")
    inp8 = inputtxt8.get(1.0, "end-1c")
    inp9 = inputtxt9.get(1.0, "end-1c")
    inp10 = inputtxt10.get(1.0, "end-1c")
    inp11 = inputtxt11.get(1.0, "end-1c")
    para_arr.append(inp1)
    para_arr.append(inp2)
    para_arr.append(inp4)
    para_arr.append(inp5)
    para_arr.append(inp6)
    para_arr.append(inp7)
    para_arr.append(inp8)
    para_arr.append(inp9)
    para_arr.append(inp10)
    para_arr.append(inp11)

    try:
        finalinp = f' These are your inputs:\nAccuracy: {inp1}\nBearing: {inp2}\nAcceleration X: {inp4}\nAcceleration Y: {inp5}\nAcceleration Z: {inp6}\nGyro X: {inp7}\nGyro Y: {inp8}\nGyro Z: {inp9}\nSpeed: {inp10}\nSecond: {inp11}'
        for ind,i in enumerate(para_arr):
            para_arr[ind]=float(i)
        test_arr = np.array(para_arr)
        
        # load the model from disk
        loaded_model = joblib.load('finalized_model.sav')
        y_pred = loaded_model.predict(np.reshape(test_arr,(1, -1)))
        if y_pred:
            finalinp += f'\n\nDangerous Trip'
        else:
            finalinp += f'\n\nSafe Trip'
        outputlbl.config(text = finalinp)
    except ValueError:
        finalinp = f'Parameters are invalid'
        outputlbl.config(text = finalinp)



# Create Accuracy Input text box
lbl1 = tk.Label(left_side, text = "Input your accuracy")
lbl1.grid(row=0, column=0, padx=10, pady=10)
inputtxt1 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt1.grid(row = 0, column= 1, padx=10, pady=10)


# Create Bearing Input text box
lbl2 = tk.Label(left_side, text = "Input your bearing")
lbl2.grid(row=1, column=0, padx=10, pady=10)
inputtxt2 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt2.grid(row = 1, column=1, padx=10, pady=10)


# Create acceleration_x Input text box
lbl4 = tk.Label(left_side, text = "Input your acceleration x")
lbl4.grid(row=3, column=0, padx=10, pady=10)
inputtxt4 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt4.grid(row=3, column=1, padx=10, pady=10)

# # Create acceleration_y Input text box
lbl5 = tk.Label(left_side, text = "Input your acceleration y")
lbl5.grid(row=4, column=0, padx=10, pady=10)
inputtxt5 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt5.grid(row=4, column=1, padx=10, pady=10)

# # Create acceleration_z Input text box
lbl6 = tk.Label(left_side, text = "Input your acceleration z")
lbl6.grid(row=5, column=0, padx=10, pady=10)
inputtxt6 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt6.grid(row=5, column=1, padx=10, pady=10)

# # Create  gyro_x Input text box
lbl7 = tk.Label(left_side, text = "Input your gyro x")
lbl7.grid(row=6, column=0, padx=10, pady=10)
inputtxt7 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt7.grid(row=6, column=1, padx=10, pady=10)

# # Create  gyro_y Input text box
lbl8 = tk.Label(left_side, text = "Input your gyro y")
lbl8.grid(row=7, column=0, padx=10, pady=10)
inputtxt8 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt8.grid(row=7, column=1, padx=10, pady=10)

# Create  gyro_z Input text box
lbl9 = tk.Label(left_side, text = "Input your gyro z")
lbl9.grid(row=8, column=0, padx=10, pady=10)
inputtxt9 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt9.grid(row=8, column=1, padx=10, pady=10)

# Create  speed Input text box
lbl10 = tk.Label(left_side, text = "What is the speed? ")
lbl10.grid(row=9, column=0, padx=10, pady=10)
inputtxt10 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt10.grid(row=9, column=1, padx=10, pady=10)

# Create  second Input text box
lbl11 = tk.Label(left_side, text = "How long is the trip?")
lbl11.grid(row=10, column=0, padx=10, pady=10)
inputtxt11 = tk.Text(left_side, height = 1,  width = 20) # TextBox Creation
inputtxt11.grid(row=10, column=1, padx=10, pady=10)

# save params
savebutton = tk.Button(left_side, text = "Predict", command = saveparams)# Button Creation
savebutton.grid(row = 11, column = 1, pady=10)

# save params
deletebutton = tk.Button(left_side, text = "Delete", command = deleteparams)# Button Creation
deletebutton.grid(row = 11, column = 0, pady=10)


# show params
outputlbl = tk.Label(middle_side, text = "")
outputlbl.grid(row=0, column=0,sticky='NSEW', padx=10)

# Create Exit button
exit_button = tk.Button(root, text="Exit", command=Close)
exit_button.grid(row=22, column=0)


root.mainloop()