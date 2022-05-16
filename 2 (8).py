import os
print('Exist:', os.access('c:\\Users\\Akim', os.F_OK))
print('Readable:', os.access('c:\\Users\\Akim', os.R_OK))
print('Writable:', os.access('c:\\Users\\Akim', os.W_OK))
print('Executable:', os.access('c:\\Users\\Akim', os.X_OK))