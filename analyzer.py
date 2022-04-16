# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:23:28 2022

@author: maiaw
"""
import numpy as np
from importer import import_data
import matplotlib.pyplot as plt

def extract_temperature():
    i = 0
    num_samples = 400
    tempC = np.zeros(num_samples)
    result = import_data(num_samples)
        
    while(i < num_samples):
        tempC[i] = result['feeds'][i]['field1']
        i=i+1;
    
    plot_figure_tempC(tempC)
    
    return tempC
    
    
def extract_current():
    i = 0
    num_samples = 400
    corrA = np.zeros(num_samples)
    result = import_data(num_samples)
        
    while(i < num_samples):
        corrA[i] = result['feeds'][i]['field2']
        i=i+1;
    
    plot_figure_corrA(corrA)
    
    return corrA


def extract_rssi():
    i = 0
    num_samples = 400
    rssiDb = np.zeros(num_samples)
    result = import_data(num_samples)
        
    while(i < num_samples):
        rssiDb[i] = result['feeds'][i]['field3']
        i=i+1;
    
    plot_figure_rssiDb(rssiDb)
    return rssiDb


def plot_figure_tempC(tempC):
    plt.clf()
    plt.plot(tempC)
    plt.title('Gráfico de Temperatura')
    plt.xlabel('Amostra') #definindo nome do eixo X
    plt.ylabel('Temperatura [C]') #definindo nome do eixo Y
    plt.savefig('fig-temperature.png')
    
    
def plot_figure_corrA(corrA):
    plt.clf()
    plt.plot(corrA)
    plt.title('Gráfico de Corrente')
    plt.xlabel('Amostra') #definindo nome do eixo X
    plt.ylabel('Corrente [A]') #definindo nome do eixo Y
    plt.savefig('fig-current.png')
    
    
def plot_figure_rssiDb(rssiDb):
    plt.clf()
    plt.plot(rssiDb)
    plt.title('Gráfico de RSSI')
    plt.xlabel('Amostra') #definindo nome do eixo X
    plt.ylabel('RSSI [dB]') #definindo nome do eixo Y
    plt.savefig('fig-rssi.png')

extract_temperature()
extract_current()
extract_rssi()
