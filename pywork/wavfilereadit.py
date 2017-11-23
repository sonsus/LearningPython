import numpy as np
from scipy.io import wavfile

np.set_printoptions(threshold=np.nan)
rate, raw = wavfile.read("./f001.wav")
with open("raw_test.txt", "w") as rawf:
    rawf.write(str(raw))

rate1, mono=wavfile.read("/home/seonils/Documents/muhan_records/mono256.wav")
with open("mono_test.txt", "w") as monof:
    monof.write(str(mono))
print("done")

