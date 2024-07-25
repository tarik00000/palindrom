# Napiši program koji unosi string, a zatim provjerava da li je palindrom, tj. da li se čita isto sa obje strane. 
string = input("Unesi string: ")
if string == string[::-1]:
    print("String je palindrom.")
else:
    print("String nije palindrom.")
