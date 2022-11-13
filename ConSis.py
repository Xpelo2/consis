#ConSis V1
import wave

print("ConSis V1! (C) AlexSoft 2022-2023")
print(" ")
print("Enter AlPhonemes:")
phonemes = input("")
print("Enter output file:")
out = input()
print("Processing...")

procesneed = list(phonemes)
print(procesneed)
data = []
for x in procesneed:
    if x == " ":
        x = "space"
    print("LOGB:"+x)
    w = wave.open("alexset/"+x+'.wav', 'rb')
    print("LOG:"+x)
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(out, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()
print("Saved to "+out)