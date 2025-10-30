from pyswmm import Simulation
import glob
import os
import re
import shutil
from joblib import Parallel, delayed
import time

tempo_inicial = time.time()

list_of_files = glob.glob('*.inp') # files .inp to be readed
# print(list_of_files)

def run_swmm_parallel(file_name):
    with Simulation(file_name, outputfile= str(file_name) + '.out' , reportfile= str(file_name) + '.rpt') as sim:
        for step in sim:
            pass
    return file_name

resultado = Parallel(n_jobs=4)(delayed(run_swmm_parallel)(file_name) for file_name in list_of_files)

# print(resultado)
print(f"Demorou: {time.time() - tempo_inicial}")
f = open('output.txt', 'w')
print(f"Demorou: {time.time() - tempo_inicial}", file = f)
print(resultado, file=f)