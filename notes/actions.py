import notes.note as model

class Actions:
    
    def create(self, user):

        title = input("Introduce the title:")
        body = input("introduce the content:")
        
        note = model.Note(user[0], title, body)
        save = note.save()

        if save[0] >= 1:
            print(f"Perfect {user[1]}, note created and saved succesfully!!")
        else:
            print("Something went wrong, note couldn't be save")
    
    def show(self, user):
        print(f"These are your notes {user[1]}:\n")

        note = model.Note(user[0]) 
        ls_notes = note.ls()
        
        for note in ls_notes:
            print("********************************")
            print(f"TITLE:{note[2]}\n")
            print(f"{note[3]}\n")
            
        input() 

    def delete(self, user):
        print(f"\nOK let's delete, what is the title of the note? ")

        title = input()

        if title == "":
            print("Couldn't delete the note")
            return

        note = model.Note(user[0], title)
        erased = note.d()

        if erased[0] >= 1:
            print(f'Note {title} has been deleted!!')
        else:
            print("Couldn't delete the note")