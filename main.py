import os
import random
import sys
import mido
import pygame
import pygame.midi
import time
import datetime
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(r'D:/optimisation/project')  # Add the directory containing pso.py to sys.path

from main_window_ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow

from GeneticAlgorithm import GeneticAlgorithm, chromosome
from Melody import Melody, octave, keys, scales, chord_progressions

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the UI class
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #==================================================
        #define objects
        #==================================================
        self.folder = str(datetime.datetime.now().timestamp())
        self.ga = GeneticAlgorithm()
        self.population = None
        #==================================================
        #perform actions
        #==================================================
        
        #==================================================
        #
        #==================================================
        self.ui.start_pushButton.clicked.connect(self.initialise_Problem)

        #==================================================
        #
        #==================================================
        self.ui.play_pushButton.clicked.connect(lambda: self.play_music(self.population[0]) if self.population else self.show_message("Population is not initialized."))
        # Connect the "Stop" buttons for individual 0
        self.ui.stop_pushButton.clicked.connect(lambda: self.stop_midi())




        #==================================================
        #
        #==================================================
        self.ui.play_pushButton_2.clicked.connect(lambda: self.play_music(self.population[1]) if self.population else self.show_message("Population is not initialized."))
       
        # Connect the "Stop" buttons for individual 1
        self.ui.stop_pushButton_2.clicked.connect(lambda: self.stop_midi())

        #==================================================
        #
        #==================================================
        self.ui.play_pushButton_3.clicked.connect(lambda: self.play_music(self.population[2]) if self.population else self.show_message("Population is not initialized."))
        # Connect the "Stop" buttons for individual 2
        self.ui.stop_pushButton_3.clicked.connect(lambda: self.stop_midi())


        self.ui.play_pushButton_4.clicked.connect(lambda: self.play_music(self.population[3]) if self.population else self.show_message("Population is not initialized."))
        # Connect the "Stop" buttons for individual 3
        self.ui.stop_pushButton_4.clicked.connect(lambda: self.stop_midi())
        
        #=================================================
        #
        #=================================================
        self.ui.evolve_pushButton.clicked.connect(self.evolve_population)




    def create_folder(self, folder_name):
        try:
            os.mkdir(folder_name)  # Create a directory with the given folder_name
            print(f"Folder '{folder_name}' created successfully.")
        except OSError:
            print(f"Creation of folder '{folder_name}' failed.")

            
    def initialise_Problem(self):
        print("initializing....")

        #==============================
        #create a folder to save sounds
        #==============================
        self.create_folder(self.folder)

        #==================================================
        #define initial parameters for melody
        #==================================================
        self.num_bars = int(self.ui.comboBox.currentText())
        self.num_notes = int(self.ui.comboBox_7.currentText())
        self.num_steps = (int(self.ui.comboBox_4.currentText()))-1
        self.scale = str(self.ui.comboBox_3.currentText())
        self.key = str(self.ui.comboBox_2.currentText())
        self.root = int(self.ui.comboBox_8.currentText())
        self.chord_progression = str(self.ui.comboBox_9.currentText())
        self.pauses = int(self.ui.comboBox_10.currentText())
        self.bpm = 120
        population_size = 4
        self.num_mutations = 2
        self.mutation_probability = 0.2
        self.generation_period = 0
        self.user_listning_period = [0.0,0.0,0.0,0.0]
        self.total_duration = None
        

        #==========================================
        #create a initial population of chromosomes
        #==========================================
        self.population = [self.ga.generate_chromosome(self.num_bars * self.num_notes * octave) for _ in range(population_size)]

        print()
        for v in self.population:
            print(v)
            print()
            print()
        pass
    
    def evaluate_fitness(self, chromosome: chromosome):


        rating_1 = self.ui.spinBox.value()/5
        rating_2 = self.ui.spinBox_2.value()/5
        rating_3 = self.ui.spinBox_3.value()/5 
        rating_4 = self.ui.spinBox_4.value()/5

        duration_1 = self.user_listning_period[0]
        
        duration_2 = self.user_listning_period[1]
        duration_3 = self.user_listning_period[2]
        duration_4 = self.user_listning_period[3]

        if chromosome == self.population[0]:        
            fitness_1 = duration_1 * rating_1
            return fitness_1
        
        elif chromosome == self.population[1]:
            fitness_2 = duration_2 * rating_2
            return fitness_2
        elif chromosome == self.population[2]:
            fitness_3 = duration_3 * rating_3
            return fitness_3
        elif chromosome == self.population[3]:
            fitness_4 = duration_4 * rating_4
            return fitness_4


        pass

    def evolve_population(self):

        self.generation_period +=1
        print()
        print("evolving generation ", self.generation_period)
        print()
        print()

        #===========================================================================================
        #evaluate the invididuals chromosome fitness
        #===========================================================================================
        population_fitness = [(chromatid, self.evaluate_fitness(chromatid)) for chromatid in self.population]

        #===========================================================================================
        #sort the invididuals based on their chromosome fitness
        #===========================================================================================
        sorted_population_fitness = sorted(population_fitness, key=lambda e: e[1], reverse=True)

        #===========================================================================================
        #evaluate the invididuals chromosome fitness
        #===========================================================================================
        self.population = [e[0] for e in sorted_population_fitness]

        #===========================================================================================
        #take best invididuals based chromosome fitness for next generation
        #===========================================================================================
        next_generation = self.population[0:2]

        for j in range(int(len(self.population) / 2) - 1):

            def fitness_lookup(genome):
                for e in population_fitness:
                    if e[0] == genome:
                        return e[1]
                return 0
            
            #===========================================================================================
            #follow generic GA
            #use elitim selection to choose parrents for next offsprings
            #use one point crossover
            #use uniform mutation to generate new offsprings
            #===========================================================================================
            parents = self.ga.elitism_selection(self.population, fitness_lookup)
            offspring_a, offspring_b = self.ga.one_point_crossover(parents[0], parents[1])
            offspring_a = self.ga.uniform_mutation(offspring_a, self.mutation_probability)
            offspring_b = self.ga.uniform_mutation(offspring_b, self.mutation_probability)

            #===========================================================================================
            #generate new populattion based on offsprings and best individuals
            #===========================================================================================
            next_generation += [offspring_a, offspring_b]

        self.population = next_generation

        #========================================
        #Shuffle to remove user predictability
        #========================================
        random.shuffle(self.population)

        

        
    
    

    def play_music(self, individual):
        print("individual :")
        print(individual)

        self.stop_music = False
        finish_time = None
        start_time = None

        index = self.population.index(individual)
        output_directory = "D:/optimisation/project/"  # melody directory path

        melody = Melody()
        chord_progression = chord_progressions[self.chord_progression]
        melody.set_melody(individual, self.num_bars, self.num_notes, self.num_steps, self.pauses, self.key, self.scale, self.root, chord_progression)

        output = os.path.join(output_directory, f"{self.folder}/melody_{index}_output.mid")
        print(output)

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(output), exist_ok=True)

        # Save the melody as a MIDI file
        melody.save_chromosome_to_midi(output, self.bpm)

        try:
            # Initialize pygame and its MIDI player
            pygame.init()
            pygame.midi.init()

            print("Using pygame")

            # Load the MIDI file for playback
            pygame.mixer.music.load(output)

            # Play the MIDI file
            pygame.mixer.music.play()

            start_time = time.time()

            # Wait for the music to finish (you can replace this with any other logic)

            while not self.stop_music:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                    # Handle other events if needed
                        pass
            print()

            
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            pygame.mixer.music.stop()
            finish_time = time.time()
            elapsed_time = finish_time - start_time
            duration = pygame.mixer.music.get_pos()

            print("duration Time: ", duration)
            print("Elapsed Time: ", elapsed_time)


            index = self.population.index(individual)

            elapsed_time=elapsed_time/1000
            print(self.user_listning_period)

            # Calculate the total duration
            if self.total_duration == None:
                midi_file = mido.MidiFile(output)
                duration = sum(msg.time for msg in midi_file.play())
                self.total_duration = duration / 1000.0
                print("duration seconds ", self.total_duration)
            
            weighted_duration = elapsed_time/self.total_duration
            self.user_listning_period[index]= weighted_duration

            # Clean up resources
            pygame.midi.quit()
            pygame.quit()

    def stop_midi(self):

        self.stop_music = True
        print
       





def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

