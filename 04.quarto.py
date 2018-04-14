import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

somma = 0
counter = 0
media = 0.0

class MyWindow(Gtk.Window):



    def __init__(self):
        Gtk.Window.__init__(self, title="media dei voti")
        
        # creiamo un contenitore per i bottoni etc...
        self.contenitore = Gtk.Box(spacing=6)
        self.add(self.contenitore)
        
        # demo per un campo di testo 
        self.voti = Gtk.Entry()

	#bottone per inserimento dati
        self.bottone_dati = Gtk.Button(label = "Inserisci")
        self.bottone_dati.connect("clicked",self.on_bottone_dati_clicked)	
	
                
        #bottone 
        self.bottone = Gtk.Button(label="Calcola Media")
        self.bottone.connect("clicked", self.on_button_clicked)
       
	# demo per una label di testo
        self.media = Gtk.Label("Media =      ")
        
        # aggiungiamo tutto al contenitore
        self.contenitore.add(self.voti)
        self.contenitore.add(self.bottone_dati)
        self.contenitore.add(self.bottone)
        self.contenitore.add(self.media)


    def on_bottone_dati_clicked(self, widget):  
        # Inserisce i dati
        global counter
        global somma
        counter = counter + 1  
        value = int(self.voti.get_text())
        somma = somma + value
        self.voti.set_text("")

    def on_button_clicked(self, widget):
        global counter
        global somma
        global media
        M = somma / counter
        self.media.set_text("Media =   " + str(M) +" ")
        
        


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
