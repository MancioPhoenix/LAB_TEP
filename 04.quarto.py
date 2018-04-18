import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="media dei voti")
        
        # creiamo un contenitore per i bottoni etc...
        self.contenitore = Gtk.Box(spacing=6)
        self.add(self.contenitore)
        
        # demo per un campo di testo 
        self.voti = Gtk.Entry()
                
        #bottone 
        self.bottone = Gtk.Button(label="Calcola Media")
        self.bottone.connect("clicked", self.on_button_clicked)
        
		# demo per una label di testo
        self.media = Gtk.Label("media =      ")
        
        # aggiungiamo tutto al contenitore
        self.contenitore.add(self.voti)
        self.contenitore.add(self.bottone)
        self.contenitore.add(self.media)

    def on_button_clicked(self, widget):
        # calcola la media ......
        # e modifica la label di testo self.media di conseguenza ...
        
        self.media.set_text(self.voti.get_text())
		# TODO : calcolare la media estraendo dalla stringa i valori ...

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
