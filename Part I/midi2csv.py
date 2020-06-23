import py_midicsv as pm
import csv

# Load the MIDI file and parse it into CSV format
csv_string = pm.midi_to_csv("Liz_et3.mid")

for list in csv_string:
    print (list) #this works so now I can return the midi information 
