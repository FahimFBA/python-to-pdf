# By: Md. Fahim Bin Amin
# Matplotlib Chart and FPDF Table in PDF example

from fpdf import fpdf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(211)
plt.title('Iris Dataset Averages by Planet Type')
plt.xlabel('Measurement Name')
plt.ylabel('Centimeters (cm)')

ticks = [4.0, 8.0, 12.0, 16.0]
a = [x - 1 for x in ticks]
b = [x + 1 for x in ticks]