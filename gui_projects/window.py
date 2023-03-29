from tkinter import *
  
top = Tk()
Lb = Listbox(top)

Lb.insert(1, 'American Airlines')
Lb.insert(2, 'Delta Airlines')
Lb.insert(3, 'Allegiant Air')
Lb.insert(4, 'Envoy Air (American Eagle)')
Lb.insert(5, 'Spirit Airlines')
Lb.insert(6, 'Southwest Airlines')
Lb.insert(7, 'CitiJet')
Lb.insert(8, 'All Airlines')
Lb.pack()
top.mainloop()