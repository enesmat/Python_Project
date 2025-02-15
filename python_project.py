#Python_Project - To-Do-List

import os #Interagieren mit dem OS-Betriebssystem - Verwaltung von Dateien und Verzeichnissen

#Aufgaben hinzufügen
def add_task(): #Funktion zum hinzufügen
    task = input("Bitte Ihre Aufgabe eintragen: ") #Benutzeraufforderung
    with open("todo_list.txt", "a") as file: #Öffnen der Datei im Anhängemodus - Datei wird automatisch erstellt. With schließt die Datei nach dem Block automatisch.
        file.write(task + "\n") #Hinzufügen einer neuen Aufgabe in die txt-Datei. \n steht für ein Zeilenumbruch nach jeder Aufgabe.
    print("Aufgabe hinzugefügt") #Bestätigung

#Aufgaben anzeigen
def show_tasks(): #Funktion zum anzeigen
    try: #Versuch zum Öffnen der txt-Datei
        with open("todo_list.txt", "r") as file: #Öffnen der Datei im Lesemodus
            tasks = file.readlines() #Alle Zeilen werden gelesen und als Liste in der Variable tasks gespeichert.
            if not tasks: #Prüfung, ob die Datei Aufgaben enthält.
                print("Keine Aufgaben hinzugefügt.") #False-Ausgabe, wenn die Datei leer ist.
    except FileNotFoundError: #Fehlerbehandlung zum try-Vorgang - falls der Versuch die txt-Datei zu Öffnen schief geht, wird die entsprechende Fehlermeldung ausgegeben.
        print("Die Datei todo_list.txt existiert nicht.")

#Aufgaben als erledigt markieren
def mark_task_done(): #Funktion zum markieren
    show_tasks() #Diese Funktion ist dafür verwantworlich, die Aufgaben aus der txt-Datei anzuzeigen. Erst dann kann der Benutzer die Aufgaben markieren.
    try:
        task_number = int(input("Bitte geben Sie die Nummer der Aufgabe ein, die Sie als erledigt markieren möchten. ")) #Benutzeraufforderung
        with open ("todo_list.txt", "r") as file: #öffnen der Datei im Lesemodus
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks): #Sicherstellung, dass task_number mind. 1 ist. Prüfung ob die eingegebene Nummer gültig ist - Zahl muss zwischen 1 und der Anzahl der Aufgaben liegen (nicht größer)
            tasks[task_number - 1] = "X " + tasks[task_number - 1] #Falls eingegebene Nr. gültig ist, dann wird an den Anfang der Aufgabe in X gesetzt. -1 wird verwendet, weil index = 0 ist, aber die Aufgaben bei 1 beginnen.
            with open ("todo_list.txt", "w") as file: #Speichern der Änderung in die Datei im Schreibmodus.
                file.writelines(tasks)
            print("Aufgabe als erledigt markiert.") #Bestätigung der Markierung
        else:
            print("Aufgabennummer nicht vorhanden") #Fehlerbehandlung
    except ValueError:
        print("Bitte eine gültige Nummer eingeben.") #Fehlerbehandlung

#Aufgaben löschen
def delete_task(): #Funktion zum löschen
    show_tasks() #Anzeigen der Aufgaben
    try:
        task_number = int(input("Bitte geben Sie die Nummer der erledigten Aufgabe ein, die Sie löschen möchten. ")) #Benutzereingabe
        with open ("todo_list.txt", "r") as file: #Die txt-Datei wird im Lesemodus geöffnet
            tasks = file.readlines() #Zeilen werden gelesen und gespeichert
        if 1 <= task_number <= len(tasks) and tasks[task_number - 1].startswith("X "): #Prüfung ob die eingegebene Nr. gültig ist UND ob die Aufgabe als erledigt markiert wurde (mit X anfängt)
            del tasks[task_number - 1] #Wenn die Bedingung in der oberen Zeile erfüllt ist, wird die Aufgabe gelöscht. -1, weil index = 0
            with open ("todo_list.txt", "w") as file: #Öffnen der Datei im Schreibmodus
                file.writelines(tasks) #Die Änderungen werden gespeichert
            print("Aufgabe wurde gelöscht.") #Bestätigung
        else:
            print("Ungültige Aufgabennummer oder die Aufgabe ist nicht als erledigt markiert.") #Fehlerbehandlung
    except ValueError:
        print("Bitte eine gültige Nummer eingeben.") #Fehlerbehandlung

#Menü
def main(): #Hauptmenü
    while True: #Unendliche Schleife (läuft bis das Programm mit der Eingabe 5 beendet wird)
        print("Menü:")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Aufgabe löschen")
        print("5. Beenden")

        choice = input("Bitte wählen Sie eine Option (1-5): ")
        #Der Benutzer wird aufgefordert eine der Auswahlmöglichkeiten zu wählen. Die Eingabe wird in der Variable choice gespeichert.

        #Die Benutzereingabe wird überprüft und führt eine der fünf Optionen aus:
        if choice == "1": #Eingabe der Zahl 1 öffnet die add_task() Funktion.
            add_task()
        elif choice == "2": #Eingabe der Zahl 2 öffnet die show_task() Funktion.
            show_tasks()
        elif choice == "3": #Eingabe der Zahl 3 öffnet die mark_task_task() Funktion.
            mark_task_done()
        elif choice == "4": #Eingabe der Zahl 4 öffnet die delete_task() Funktion.
            delete_task()
        elif choice == "5": ##Eingabe der Zahl 5 beendet das Programm mit der break-Anweisung und die while-True-Schleife wird verlassen.
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 5") #Fehlerbehandlung bei ungültiger Eingabe

#Ausführung des Skripts
if __name__ == "__main__":
    main()    




