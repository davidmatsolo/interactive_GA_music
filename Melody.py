import secrets
from typing import List
import os
import fluidsynth
from pydub import AudioSegment

import pygame
import pygame.midi 
from GeneticAlgorithm import chromosome
from midiutil import MIDIFile
from pyo import *
import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
import random
import click
from datetime import datetime

#=========================================================================
#define melody components
#=========================================================================
scales: List[str] = ["major", "minorM", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian"]
keys = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A#", "Bb"]
octave= 7
chord_progressions = {
    "C": ["Cmaj7", "Cmaj7", "Fmaj7", "Gdom7"],
    "C#": ['C#maj7', 'D#m7', 'E#m7', 'F#maj7', 'G#7', 'A#m7', 'B#m7b5'],
    "Db": ['Dbmaj7', 'Ebm7', 'Fm7', 'Gbmaj7', 'Ab7', 'Bbm7', 'Cm7b5'],
    "D": ['Dmaj7', 'Em7', 'F#m7', 'Gmaj7', 'A7', 'Bm7', 'C#m7b5'],
    "D#": ['D#maj7', 'Fm7', 'Gm7', 'G#maj7', 'A#7', 'Cm7', 'Dm7b5'],
    "Eb": ['Ebmaj7', 'Fm7', 'Gm7', 'Abmaj7', 'Bb7', 'Cm7', 'Dm7b5'],
    "E": ['Emaj7', 'F#m7', 'G#m7', 'A#maj7', 'B7', 'C#m7', 'D#m7b5'],
    "F": ['Fmaj7', 'Gm7', 'Am7', 'Bbmaj7', 'C7', 'Dm7', 'Em7b5'],
    "F#": ['F#maj7', 'G#m7', 'A#m7', 'Cmaj7', 'D#7', 'Fm7', 'Gm7b5'],
    "Gb": ['Gbmaj7', 'Abm7', 'Bbm7', 'Cbmaj7', 'Db7', 'Ebm7', 'Fm7b5'],
    "G": ['Gmaj7', 'Am7', 'Bm7', 'Cmaj7', 'D7', 'Em7', 'F#m7b5'],
    "G#": ['G#maj7', 'A#m7', 'Cm7', 'Dmaj7', 'E#7', 'Fm7', 'Gm7b5'],
    "Ab": ['Abmaj7', 'Bbm7', 'Cm7', 'Dbmaj7', 'Eb7', 'Fm7', 'Gm7b5'],
    "A": ['Amaj7', 'Bm7', 'C#m7', 'Dmaj7', 'E7', 'F#m7', 'G#m7b5'],
    "A#": ['A#maj7', 'Cm7', 'Dm7', 'D#maj7', 'F7', 'Gm7', 'Am7b5'],
    "Bb": ['Bbmaj7', 'Cm7', 'Dm7', 'Ebmaj7', 'F7', 'Gm7', 'Am7b5'],
}



#=========================================================================
#define melody class
#=========================================================================
class Melody:
    def __init__(self):
        self.notes = []
        self.beat = []
        self.velocity = []

    def set_melody(self, chromosome: chromosome, num_bars: int, num_notes: int, num_steps: int,
                   pauses: int, key: str, scale: str, root: int, chord_progression: List[str]):
        
        def bits_notes_to_int_notes(bits: List[int]) -> int:
            return sum(bit * 2 ** index for index, bit in enumerate(bits))

        notes = [chromosome[i * octave:i * octave + octave] for i in range(num_bars * num_notes)]
        note_length = 4 / float(num_notes)
        

        scl = EventScale(root=key, scale=scale, first=root)

        chord_index = 0  # Index to keep track of the current chord in the progression

        for note in notes:
            integer = bits_notes_to_int_notes(note)
        
            print("note ", note, "is ", integer)

            if not pauses:
                integer = integer % 2 ** (octave - 1)

            if integer >= 2 ** (octave - 1):
                self.notes.append(0)
                velocity = random.randint(80, 100)
                self.velocity.append(velocity)
                self.beat.append(note_length)
            else:
                if len(self.notes) > 0 and self.notes[-1] == integer:
                    self.beat[-1] += note_length
                else:
                    self.notes.append(integer)
                    velocity = random.randint(80, 100)
                    self.velocity.append(velocity)
                    self.beat.append(note_length)

            # Add chord progression logic
            if chord_index < len(chord_progression):
                chord_name = chord_progression[chord_index]
                # change chords every bar or based on a certain pattern.
                if len(self.beat) % num_notes == 0:
                    # Update the scale based on the current chord
                    scl = EventScale(root=chord_name, scale=scale)
                    chord_index += 1
        #print("notes", notes)
        steps = []
        for step in range(num_steps):
            steps.append([scl[(note + step * 2) % len(scl)] for note in self.notes])

        self.notes = steps


    
    def save_chromosome_to_midi(self, filename: str, bpm: int):
        """
        Generate individuals based on the given size.
        :param filename: Output MIDI file name
        :param bpm: Beats per minute
        """
        
        
        if len(self.notes[0]) != len(self.beat) or len(self.notes[0]) != len(self.velocity):
            raise ValueError

        mf = MIDIFile(1)

        track = 0
        channel = 0

        time = 0.0
        mf.addTrackName(track, time, "Sample Track")
        mf.addTempo(track, time, bpm)

        for i, vel in enumerate(self.velocity):
            if vel > 0:
                for step in self.notes:
                    mf.addNote(track, channel, step[i], time, self.beat[i], vel)

            time += self.beat[i]

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            mf.writeFile(f)



