from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
	def __init__(self,root):
		self.root=root
		self.root.title("Student Management System")
		self.root.geometry("1350x700+0+0")

		title=Label(self.root,text="Student management system",bd=10,relief = GROOVE ,font=('Arial',40),bg="Blue",fg='White')
		title.pack(side=TOP,fill=X)

#varaible 
		self.Roll_No_var=StringVar()
		self.name_var=StringVar()
		self.email_var=StringVar()
		self.gender_var=StringVar()
		self.contact_var=StringVar()
		self.DOB_var=StringVar()
		self.search_by=StringVar()
		self.search_text=StringVar()

		Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg='Green')
		Manage_frame.place(x=20,y=100,width=450,height=580)
		
		m_title=Label(Manage_frame,text ="Manage Students",font=('Arial',20),bg='Green')
		m_title.grid(row=0,columnspan=2,pady=20)

		lbl_roll=Label(Manage_frame,text ="Roll no.",font=('Arial',20),bg='Green')
		lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

		txt_Roll=Entry(Manage_frame,textvariable = self.Roll_No_var,font=('Arial',15),bd=5,relief=GROOVE)
		txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


		lbl_name=Label(Manage_frame,text ="Name.",font=('Arial',20),bg='Green')
		lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

		txt_name=Entry(Manage_frame,textvariable = self.name_var,font=('Arial',15),bd=5,relief=GROOVE)
		txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")


		lbl_email=Label(Manage_frame,text ="Email",font=('Arial',20),bg='Green')
		lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

		txt_email=Entry(Manage_frame,textvariable = self.email_var,font=('Arial',15),bd=5,relief=GROOVE)
		txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")


		lbl_Gender=Label(Manage_frame,text ="Gender",font=('Arial',20),bg='Green')
		lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

		combo_gender=ttk.Combobox(Manage_frame,textvariable = self.gender_var,font=('Arial',15),state="readonly")
		combo_gender['values']=("male",'Female',"other")
		combo_gender.grid(row=4,column=1,padx=20,pady=10)

		lbl_contact=Label(Manage_frame,text ="Contact",font=('Arial',20),bg='Green')
		lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

		txt_contact=Entry(Manage_frame,textvariable = self.contact_var,font=('Arial',15),bd=5,relief=GROOVE)
		txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

		lbl_DOB=Label(Manage_frame,text ="DOB",font=('Arial',20),bg='Green')
		lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

		txt_DOB=Entry(Manage_frame,textvariable = self.DOB_var,font=('Arial',15),bd=5,relief=GROOVE)
		txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

		lbl_address=Label(Manage_frame,text ="Address",font=('Arial',20),bg='Green')
		lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

		self.txt_address=Text(Manage_frame,width=30,height=3)
		self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky='w')

		#button=

		btn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg='Green')
		btn_frame.place(x=15,y=500,width=420)

		addbtn=Button(btn_frame,text="add",width=10,command = self.add_students).grid(row=0,column=0,padx=10,pady=10)
		updatebtn=Button(btn_frame,text="update",width=10,command = self.update_data).grid(row=0,column=1,padx=10,pady=10)
		deletebtn=Button(btn_frame,text="delete",width=10,command = self.delete_data).grid(row=0,column=2,padx=10,pady=10)
		clearbtn=Button(btn_frame,text="clear",width=10,command = self.clear).grid(row=0,column=3,padx=10,pady=10)

		Detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='Green')
		Detail_frame.place(x=500,y=100,width=800,height=580)

		lbl_Search=Label(Detail_frame,text ="Search By",font=('Arial',20))
		lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

		combo_Search=ttk.Combobox(Detail_frame,textvariable=self.search_by,width=10,font=('Arial',15),state="readonly")
		combo_Search['values']=("roll_no",'Name',"Contact")
		combo_Search.grid(row=0,column=1,padx=20,pady=10)

		txt_Search=Entry(Detail_frame,textvariable=self.search_text,width=15, font=('Arial',10),bd=5,relief=GROOVE)
		txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

		Searchbtn=Button(Detail_frame,text="Search",width=10,pady = 5,command = self.search_data).grid(row=0,column=3,padx=10,pady=10)
		Showallbtn=Button(Detail_frame,text="Show All",width=10,pady = 5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


#table
		Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg='Green')
		Table_frame.place(x=10,y=70,width=760,height=500)

		scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
		self.Student_table=ttk.Treeview(Table_frame,column=("roll","Name",'Email',"Gender",'Contact','DOB','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)
		self.Student_table.heading("roll",text="roll no.")
		self.Student_table.heading("Name",text="Name")
		self.Student_table.heading("Email",text="Email")
		self.Student_table.heading("Gender",text="Gender")
		self.Student_table.heading("Contact",text="Contact")
		self.Student_table.heading("DOB",text="DOB")
		self.Student_table.heading("Address",text="Address")
		self.Student_table['show']='headings'
		self.Student_table.column('roll',width=50)
		self.Student_table.column('Name',width=120)
		self.Student_table.column('Email',width=150)
		self.Student_table.column('Gender',width=100)
		self.Student_table.column('Contact',width=100)
		self.Student_table.column('DOB',width=100)
		self.Student_table.column('Address',width=100)
		self.Student_table.pack(fill=BOTH,expand=1)
		self.Student_table.bind('<ButtonRelease-1>',self.get_cursor)
		self.fetch_data()

	def add_students(self):
		if self.Roll_No_var.get()=='' or self.name_var.get()=='':
			messagebox.showerror("Error", "All fields are reqired!")
		else:

			con=pymysql.connect(host='localhost',user='root',password='',database='stm')
			cur=con.cursor()
			cur.execute('insert into students values (%s,%s,%s,%s,%s,%s,%s)',(self.Roll_No_var.get(),
																		 self.name_var.get(),
																		 self.email_var.get(),	
																		 self.gender_var.get(),
																		 self.contact_var.get(),
																		 self.DOB_var.get(),
																		 self.txt_address.get('1.0',END)
																		 ))
			con.commit()
			self.fetch_data()
			self.clear()
			con.close()
			messagebox.showinfo("Success","Record is made")
	def fetch_data(self):
		con=pymysql.connect(host='localhost',user='root',password='',database='stm')
		cur=con.cursor()
		cur.execute('select * from students')
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
					self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()	
	def clear(self):
		self.Roll_No_var.set("")
		self.name_var.set("")
		self.email_var.set("")
		self.gender_var.set("")
		self.DOB_var.set("")
		self.contact_var.set("")
		self.txt_address.delete("1.0",END)

	def get_cursor(self,ev):
		cursor_row=self.Student_table.focus()
		contents=self.Student_table.item(cursor_row)
		row=contents["values"]
		self.Roll_No_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.gender_var.set(row[3])
		self.DOB_var.set(row[4])
		self.contact_var.set(row[5])
		self.txt_address.delete("1.0",END)
		self.txt_address.insert(END,row[6])


	def update_data(self):
		con=pymysql.connect(host='localhost',user='root',password='',database='stm')
		cur=con.cursor()
		cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,DOB=%s,address=%s where roll_no=%s", (
																								self.name_var.get(),
																								self.email_var.get(),	
																						   		self.gender_var.get(),
																								self.contact_var.get(),
																								self.DOB_var.get(),
																								self.txt_address.get('1.0',END),
																		 						self.Roll_No_var.get()
																								))
		con.commit()	
		self.fetch_data()
		self.clear()
		con.close()

	def delete_data(self):
		con=pymysql.connect(host='localhost',user='root',password='',database='stm')
		cur=con.cursor()
		cur.execute('delete from students where roll_no=%s', self.Roll_No_var.get())
		con.commit()
		con.close()
		self.fetch_data()
		self.clear()

	def search_data(self):
		con=pymysql.connect(host='localhost',user='root',password='',database='stm')
		cur=con.cursor()

		cur.execute("select * from students where " +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
					self.Student_table.insert('',END,values=row)
			con.commit()
		con.close()	

root = Tk()
ob = Student(root)
root.mainloop()
root=tk()