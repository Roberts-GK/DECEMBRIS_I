Lietotaja_skaitlis = int(input("Ievadiet skaitli:")) 
summa=0 
for skaitlis in range(1, Lietotaja_skaitlis + 1): 
    summa += skaitlis 
    
print(f"Summa no 1 līdz {Lietotaja_skaitlis} ir: {summa}")
