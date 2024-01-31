import random
import os
import re
import string

class Vertex:
    def __init__(self,value):
        self.value = value
        self.adjacent = {}
        self.neighbour = []
        self.neighbour_weights = []
    def add_edge(self,vertex,weight=0):
        self.adjacent[vertex] = weight
    def increment_edge(self,vertex,weight=0):
        self.adjacent[vertex] = self.adjacent.get(vertex,0)+1
    def probability_map(self):
        for (vertex,weight) in self.adjacent.items():
            self.neighbour.append(vertex)
            self.neighbour_weights.append(weight)
    def next_word(self):
        return random.choices(self.neighbour,weights = self.neighbour_weights)
    
class Graph:
    def __init__(self):
        self.vertices = {}
    def get_vertex_values(self):
        return set(self.verticess.keys())
    def add_vertex(self,value):
        self.vertices[value] = Vertex(value)
    def get_vertex(self,value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]
    def get_next_word(self,currentValue):
        return self.vertices[currentValue.value].next_word()
    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.probability_map()

def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8") 
        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        # text = re.sub(r'\[(.+)\]', ' ', text)
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = words[:1000]
    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)
        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)
        prev_word = word_vertex
    g.generate_probability_mappings()
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        #print(_)
        composition.append(word.value)
        next_word_vertex = g.get_next_word(word)
        word = next_word_vertex[0] if next_word_vertex else None
    return composition
def main():
    #words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    # for song in os.listdir('songs/{}'.format(artist)):
        # if song == '.DS_Store':
        #     continue
        # words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song))),"
    words = ["hi","how","are","you","hi","hello","nice","to","meet","you"]
    g = make_graph(words)
    composition = compose(g, words,len(words))
    print(' '.join(composition))


if __name__ == '__main__':
    main()
          