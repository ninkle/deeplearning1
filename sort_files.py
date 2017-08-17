import os
import shutil
import pandas as pd

########################## DOGSCATS ##########################

# files = os.listdir("train")
# begin with directory train containing unsorted cat/dog jpgs
# move cat/dog jpgs into respective directories
'''for f in files:
	if (f.startswith("cat.")):
		shutil.move("train/"+f, "train/cat/"+f)
	elif (f.startswith("dog.")):
		shutil.move("train/"+f, "train/dog/"+f)'''

# splits training and validation sets 80/20
'''files = os.listdir("train/dog")
dog_val = int(len(files) * 0.2)

for f in files[:dog_val]:
	shutil.move("train/dog/"+f, "val/dog/"+f'''

########################## CIFAR ##########################

# takes a folder "train" of images (number.png) and sorts into separate folders based on corresponding
# entry in trainLabels.csv
'''files = os.listdir("data/CIFAR/train")
df = pd.read_csv("data/CIFAR/trainLabels.csv")

for i in range(len(files)):
    f = str(i+1)
    shutil.move("data/CIFAR/train/"+(f+".png"), "data/CIFAR/"+df["label"][i]+"/"+(f+".png"))'''
    
# splits training and validation sets 80/20 
path = "data/CIFAR/train/"
for i in os.listdir(path):
    if not i.startswith("."):  # ignores hidden files
        val_size = int(len(os.listdir(path+i))*0.2) # get size of validation data
        if not os.path.exists("data/CIFAR/val/"+i):
            os.mkdir("data/CIFAR/val/"+i)  # initialize validation directory
        files = os.listdir(path+i)
        for f in files[:val_size]:
            shutil.move(path+i+"/"+f, "data/CIFAR/val/"+i+"/"+f)



    

