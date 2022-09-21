from simple_image_download import simple_image_download as simp 
response = simp.simple_image_download

# Add all the related keywords by which the images has to be searched
lst=['mask waste', 'hospital waste', 'surgical waste', 'surgical gloves waste', 'syringe waste']

# Mention the number of images to be downloaded for each category 
# Top N images from the search results would be downloaded
for rep in lst:
    response().download(rep, 150)