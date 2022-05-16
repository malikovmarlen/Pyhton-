import os 
file = 'A.txt'
location = "c:\\Users\\Akim\\Documents\\PP2\\PP2_2022_Spring"
path = os.path.join(location, file) 
os.remove(path) 