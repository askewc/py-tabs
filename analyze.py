from essentia.standard import *
import matplotlib.pyplot as plt
filename = 'input/wav/city-of-stars'
wavFilename = filename + '.wav'
pngFilename = filename + '.png'
# we start by instantiating the audio loader:
loader = essentia.standard.MonoLoader(filename=wavFilename)

# and then we actually perform the loading:
audio = loader()

# pylab contains the plot() function, as well as figure, etc... (same names as Matlab)

plt.rcParams['figure.figsize'] = (15, 6) # set plot sizes to something larger than default

plt.plot(audio[1*44100:2*44100])
plt.title("This is how the 2nd second of this audio looks like:")
plt.savefig(pngFilename)
