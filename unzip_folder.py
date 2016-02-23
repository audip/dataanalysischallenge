import os
import zipfile
import operator

dictionary_namecount = {}
progress = 0

with zipfile.ZipFile('namesbystate.zip') as namesbystate:
    for filename in namesbystate.namelist():
        if not os.path.isdir(filename) and filename != 'StateReadMe.pdf':
            # if m.endswith('.mp3'):
            # read the file
            with namesbystate.open(filename) as f:
                for line in f:
                    #process by line
                    str = line.split(',')
                    baby_name = str[3]
                    # print baby_name, filename
                    progress = progress + 1
                    # print progress
                    # dictionary_namecount[baby_name] = 1
                    if baby_name not in dictionary_namecount:
                        dictionary_namecount[baby_name] = 1
                    else:
                        dictionary_namecount[baby_name] += 1

# print dictionary_namecount
# print max(dictionary_namecount.iteritems(), key=operator.itemgetter(1))[0]

def keywithmaxval(d):
    # Fastest key value sorter approach
    # Key: Baby's name, Value: Count of name occurence
    name_count=list(d.values())
    dict_key=list(d.keys())
    return dict_key[name_count.index(max(name_count))]

highest_key = keywithmaxval(dictionary_namecount)
print highest_key
