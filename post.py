import numpy
from swmm.toolkit.shared_enum import NodeAttribute
from pyswmm import Output
from datetime import datetime
import matplotlib.pyplot as plt
import sys
from numpy import average, matrix
import numpy as np
import glob

#from macpath import join
lista = []


# EndAcrylic
#list_of_files = glob.glob('./files/*.out') # files .out to be readed

list_of_files = glob.glob('*.out') # files .out to be readed  - by ruti

# print(list_of_files)

for file_name in list_of_files:
    print(file_name)
    with Output(file_name) as out:
        ts = out.node_series('EndAcrylic', NodeAttribute.INVERT_DEPTH)
        tl = out.node_series('SP_L', NodeAttribute.INVERT_DEPTH)
        tu = out.node_series('SP_U', NodeAttribute.INVERT_DEPTH)
        tJ = out.node_series('T_J', NodeAttribute.INVERT_DEPTH)
        size = 601
        time = matrix([float(0.0)]*size)
        HD = matrix([float(0.0)]*size)
        HDl = matrix([float(0.0)]*size)
        HDu = matrix([float(0.0)]*size)
        HDJ = matrix([float(0.0)]*size)
        
        i=1
        for index in ts:
           # print(index, ts[index])
            D = ts[index]
            Dl = tl[index]
            Du = tu[index]
            DJ = tJ[index]
            HD[0,i] = D 
            HDl[0,i] = Dl 
            HDu[0,i] = Du 
            HDJ[0,i] = DJ 
            
            i = i + 1  
            print(i)          
    #___   
    HD = np.transpose(HD)
    HDl = np.transpose(HDl)
    HDu = np.transpose(HDu)
    HDJ = np.transpose(HDJ)
    mediaHD= sum(HD[590:])/11
    mediaHDl= sum(HDl[590:])/11
    mediaHDu= sum(HDu[590:])/11
    mediaHDJ= sum(HDJ[590:])/11
    lista2= [mediaHDu,mediaHDl,mediaHD,mediaHDJ]  
    print (lista2)  
    #with open('arquivo2.txt','a') as arquivo:
    #    arquivo.write(str(lista) +'\n')
    #    lista_guardar = lista.append(arquivo)
       # print(lista_guardar)
    # 
    with open('arquivo3.txt','a') as arquivo3:
        #out_arr = numpy.hstack((mediaHDu, mediaHDl, mediaHD))  #write, upstream, lateral and downstream
        #arquivo3.write(str(out_arr) + '\n')
        arquivo3.write(str(file_name)+ "   "+str(mediaHDu)+"  "+str(mediaHDl)+"  "+str(mediaHD)+"  "+str(mediaHDJ) +'\n')

    np.savetxt(str(file_name) + '.txt',HDu,fmt='%.5f')
    np.savetxt(str(file_name) + '.txt',HDl,fmt='%.5f')
    np.savetxt(str(file_name) + '.txt',HD,fmt='%.5f')
    np.savetxt(str(file_name) + '.txt',HDJ,fmt='%.5f')
    time = np.linspace(0,10,601) 
    plt.plot(time,HDJ,color='red', label='EndAcrylic')
    plt.xlabel(r"$Time(min)$")
    plt.ylabel(r"$Depth(m)$")
    plt.grid(color='k', linestyle=(0, (5, 10)) , linewidth=0.2)
    plt.legend(frameon=False,loc='upper left', ncol=1,fontsize=9)
    plt.savefig(str(file_name) + ".pdf")
    # plt.show()
    plt.close(True)

    #print(lista_guardar)