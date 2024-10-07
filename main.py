import pickle
import pygame
import io
from game_object import Player
def save_empty_dict_to_pickle(filename):
    empty_dict = {}
    with open(filename, 'wb') as file:
        pickle.dump(empty_dict, file)





# Example usage:
filename = r"datastore.pickle"
save_empty_dict_to_pickle(filename)
#print(type(b"hello"))