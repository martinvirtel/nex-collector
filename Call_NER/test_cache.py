from joblib import Memory
import os


cachedir = "./temp"
if not os.path.exists(cachedir) :
   os.mkdir(cachedir)


memory = Memory(cachedir=cachedir, verbose=0)

@memory.cache
def f(x) :
   print("Jetzt laufe ich wirklich! ",x)

#@memory.cache
def g(x) :
    return open("./tmpfile","w")



print("Erster Durchlauf:")
for x in range(0,100):
   f(x)
   g(x)



print("Zweiter Durchlauf:")
for x in range(0,100):
   f(x)