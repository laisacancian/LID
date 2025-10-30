import numpy
import glob
import shutil
import os
from random import seed
from random import random
import numpy as np
from numpy import average, matrix


# Read base file to change parameters
with open("junction_inp_0.inp",'r') as f:
    get_all=f.readlines()

dk = 0.1 # intervalo de valores do coef. de perda local
cont = 0 # contador de arquivos
nk = 2 # numero de valores do coef. de perda local em cada direcao

for i in range(nk):
    ############################################## OBS: colocar 20 para os resultados finais
    kUp = i*dk
    for j in range(nk):
        kLat = j*dk
        for k in range(nk):
            kDw = k*dk
            cont = cont + 1
            print(cont, kLat,kDw,kUp)
            shutil.copy("junction_inp_0.inp", os.path.join(f"junction_inp_{cont}.inp"))
            shutil.copy("junction_ini_0.ini", os.path.join(f"junction_ini_{cont}.ini"))
            file_name = f"junction_inp_{cont}.inp"
            print(file_name)
            with open('K_value.txt','a') as res:
                out_arr = numpy.hstack((kUp,kLat,kDw)) 
                res.write(str(file_name)+ "   "+str(out_arr) + '\n')

            with open(file_name,'w') as f:
                for iw,line in enumerate(get_all,1):         ## STARTS THE NUMBERING FROM 1 (by default it begins with 0)    
                    if iw == 96:                              ## OVERWRITES line:96
                        f.writelines("L_PC             0          " + str("{:.1f}".format(kLat)) + "        0          NO         0         \n")
                    elif iw == 97:                              ## OVERWRITES line:97
                        f.writelines("U_PC             0          " + str("{:.1f}".format(kUp)) + "        0          NO         0         \n")
                    elif iw == 98:                              ## OVERWRITES line:98
                        f.writelines("D_PC             " + str("{:.1f}".format(kDw)) + "        0          0          NO         0         \n")
                    else:
                        f.writelines(line)

            

