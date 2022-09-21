# Trash-Segmentation
This project aims to mitigate the classification of trash objects by developing a model that automatically detects different types of waste products into predefined classes. The solution begins with implementing **Faster R-CNN model** to estimate the boundary of each category of object present within an image using a confidence score (IOU Metric). This further extends to implement **Mask R-CNN** for image segmentation to detect the type of waste.



# Motivation

- According to the studies published by the "Recycling rate of municipal solid waste in the United States 1960-2018. Published by Ian Tiseo, Mar 30, 2022
", only 30% of recyclable materials actually get recycled.
- Automated system needed to improve efficiency and create a sustainable process to manage waste.
- Instance segmentation is challenging as it requires the correct detection of all objects in an image while also precisely segmenting each instance.


# Architecture Diagram

# Dataset
- The data was scraped from Google Images using the [Simple Image Downloader](https://libraries.io/pypi/simple-image-download) library.
- The images are broadly classified into 6 classes such as Metal, Glass, Paper, Organic, E-Waste and Medical.
- We have: 856 examples, 685 are training and 171 testing. (80-20 split).

# Approach

# Usage

# Contribution

# Credits

