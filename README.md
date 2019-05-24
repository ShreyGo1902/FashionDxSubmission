# FashionDxSubmission

1. renaming.py 

Renames all images depending on the class to which they belong. For example all Stripes images are renamed to stripes.(img num).jpg
This is done so labelling becomes easier

2. FabricClassificationFinal.ipynb

Labels the images
Splits then into training and validation (770 images for training and 75 for validation). train_data.npy is numpy array of training images with their respective labels
CNN model is saved after training
I put some images in a seperate folder and predicted their type using the trained model. prediction.png is the plot of some of the images corresponding to their labels

3. app.py

Web app using flask
User can upload image from UI for prediction
Clear cache from browser otherwise earlier image is displayed or use a different port every time. 
app_index.png and display.png are screenshots of the webapp
templates folder contains the html files
sample_upload_images folder contains test samples
app.py calls a function CNNmodel.py for prediction

4. model_performance.ipynb

Precision, recall, f1score, confusion_matrix and accuracy is calculated in this notebook 


