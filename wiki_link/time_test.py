from wiki_link_import import wiki_query
import time

mark1=time.time()
for x in range(1100,1300):
    print(wiki_query(x))
mark2=time.time()
print("DONE!")
print("Duration: ",mark2-mark1)
