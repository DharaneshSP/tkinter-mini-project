import customtkinter as ct
#import tkinter as t




ct.set_appearance_mode("black")
ct.set_default_color_theme("dark-blue")




root = ct.CTk()

root.title("GPA ")
#t.pack()
root.geometry("500x500")

_english_theory = ct.StringVar()
_maths=ct.StringVar()
_physics_theory=ct.StringVar()
_chemistry_theory=ct.StringVar()
_python_theory=ct.StringVar()
_aptitude=ct.StringVar()

_physics_chem_lab=ct.StringVar()
_python_lab=ct.StringVar()
_english_lab=ct.StringVar()

def calculate():
	points={"O":10 , "A+":9 , "A":8 , "B+":7 ,"B":6 ,"o":10 , "a+":9 , "a":8 , "b+":7 , "b":6 ,"C":5, "c":5 }
	
	english_theory =_english_theory.get() 
	maths=_maths.get()
	physics_theory=_physics_theory.get()
	chemistry_theory=_chemistry_theory.get()
	python_theory=_python_theory.get()
	aptitude=_aptitude.get()

	physics_chem_lab=_physics_chem_lab.get()
	python_lab=_python_lab.get()
	english_lab=_english_lab.get()





	#Credits 
	#theory
	english_credit=3
	maths_credit=4
	python_credit=3
	physics_credit=3
	chemistry_credit=3
	aptitude_credit=3

#practical
	python_lab_credit=2
	physics_chem_lab_credit=2
	english_lab_credit=1

#Gradescores of Each

	score_english_theory=points[english_theory]*english_credit
	score_matrices=points[maths]*maths_credit
	score_physics_theory=points[physics_theory]*physics_credit
	score_python_theory=points[python_theory]*python_credit
	score_chemistry_theory=points[chemistry_theory]*chemistry_credit

	score_aptitude=points[aptitude]*aptitude_credit

	score_python_lab=points[python_lab]*python_lab_credit
	score_phy_chem_lab=points[physics_chem_lab]*physics_chem_lab_credit
	score_english_lab=points[english_lab]*english_lab_credit

	totalscore=score_english_theory+score_matrices+score_physics_theory+score_python_theory+score_chemistry_theory+score_aptitude+score_python_lab+score_phy_chem_lab+score_english_lab

	totalcredits=english_credit+maths_credit+python_credit+physics_credit+chemistry_credit+aptitude_credit+python_lab_credit+physics_chem_lab_credit+english_lab_credit
	GPA=totalscore/totalcredits
	GPA=f'{GPA:.2f}'
	display = ct.CTkLabel(root , text =GPA , fg_color="black" , corner_radius=10 , width=30)
	display.place(relx=0.5 , rely=0.90 , anchor="center")
	
    
	
    


  
	
	
#print(totalcredits)
#print("\n\n\tGPA Score =  ","%.4f"%GPA)



'''
_english_theory = t.StringVar()
_maths=t.StringVar()
_physics_theory=t.StringVar()
_chemistry_theory=t.StringVar()
_python_theory=t.StringVar()
_aptitude=t.StringVar()

_physics_chem_lab=t.StringVar()
_python_lab=t.StringVar()
_english_lab=t.StringVar()



'''




options=['O','A+',"A",'B',"B+","C","D"]

_english_theory=ct.CTkComboBox(root,values=options)


_maths=ct.CTkComboBox(root,values=options)
_physics_theory=ct.CTkComboBox(root,values=options)
_chemistry_theory=ct.CTkComboBox(root,values=options)
_python_theory=ct.CTkComboBox(root,values=options)
_aptitude=ct.CTkComboBox(root,values=options)


_physics_chem_lab=ct.CTkComboBox(root,values=options)
_python_lab=ct.CTkComboBox(root,values=options)
#_english_lab.set("Select Grade")
_english_lab=ct.CTkComboBox(root,values=options)

submit=ct.CTkButton(root, text="Submit" , command = calculate)


'''
def click(event) :
	eng.delete(0,t.END)
	

eng.insert(0, "")
eng.bind("<Button-1>",click)
'''


#print(dir(t))


theorylabel= ct.CTkLabel(root,text="THEORY" , fg_color="#536E8A" , corner_radius=5 , font=("monospace" , 10))

praclabel= ct.CTkLabel(root,text="PRACTICAL" , fg_color="#536E8A" , corner_radius=5 , font=("monospace" , 10) )



englabel= ct.CTkLabel(root,text="English")
matlabel= ct.CTkLabel(root,text="Maths")
chelabel= ct.CTkLabel(root,text="Chemistry")
aptlabel= ct.CTkLabel(root,text="Aptitude")
pylabel= ct.CTkLabel(root,text="Python")
phylabel= ct.CTkLabel(root,text="Physics")
 

phyllabel= ct.CTkLabel(root,text="Phy & chem")
engllabel= ct.CTkLabel(root,text="English")
pyllabel= ct.CTkLabel(root,text="Python")



praclabel.place(relx=0.5,rely=0.53,anchor="center") 
theorylabel.place(relx=0.5, rely=0.045  , anchor="center")

englabel.place(relx=0.3 , rely=0.15 , anchor='center')
matlabel.place(relx=0.3 , rely=0.2 , anchor='center')
phylabel.place(relx=0.3 , rely=0.25 , anchor='center')
chelabel.place(relx=0.3 , rely=0.3, anchor='center')
pylabel.place(relx=0.3 , rely=0.35 , anchor='center')
aptlabel.place(relx=0.3 , rely=0.4 , anchor='center')

phyllabel.place(relx=0.3,rely=0.6 ,anchor="center")

pyllabel.place(relx=0.3,rely=0.65 ,anchor="center")

engllabel.place(relx=0.3,rely=0.7 ,anchor="center")



_english_theory.place(relx=0.72 , rely=0.15 , anchor="center")
_maths.place(relx=0.72 , rely=0.2 , anchor="center")
_physics_theory.place(relx=0.72 , rely=0.25 , anchor="center")
_chemistry_theory.place(relx=0.72 , rely=0.3 , anchor="center")
_python_theory.place(relx=0.72 , rely=0.35 , anchor="center")
_aptitude.place(relx=0.72 , rely=0.4 , anchor="center")

_physics_chem_lab.place(relx=0.72 , rely=0.60 , anchor="center")
_python_lab.place(relx=0.72 , rely=0.65 , anchor="center")
_english_lab.place(relx=0.72 , rely=0.70 , anchor="center")



#eng.pack()

# mat.pack()
# phy.pack()
# che.pack()
# pyt.pack()
# apt.pack()
# chel.pack()
# pyl.pack()
# engl.pack()





submit.place(relx=0.5,rely=0.8,anchor="center")


root.mainloop()