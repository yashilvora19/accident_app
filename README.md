
![banner.png](imgs/github_banner.png)
<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  </a>  
  &nbsp;&nbsp;&nbsp;  
    <a href="https://www.tensorflow.org/">
    <img src="https://img.shields.io/badge/TensorFlow-Latest-orange.svg" alt="TensorFlow Latest">
  </a> 
  &nbsp;&nbsp;&nbsp;
  
  <a href="https://scikit-learn.org/stable/install.html">
    <img src="https://img.shields.io/badge/scikit--learn-Latest-brightgreen.svg" alt="scikit-learn Latest">
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html">
    <img src="https://img.shields.io/badge/pandas-Latest-brightgreen.svg" alt="pandas Latest">
  </a>
  &nbsp;&nbsp;&nbsp;
    </p>
  <p align="center">
  <a href="https://numpy.org/install/">
    <img src="https://img.shields.io/badge/numpy-Latest-blue.svg" alt="numpy Latest">
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://seaborn.pydata.org/installing.html">
    <img src="https://img.shields.io/badge/seaborn-Latest-blueviolet.svg" alt="seaborn Latest">
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://matplotlib.org/users/installing.html">
    <img src="https://img.shields.io/badge/matplotlib-Latest-blueviolet.svg" alt="matplotlib Latest">
  </a>
</p>



# Members
Arnav Kamdar,
Ishika Agrawal,
Mishka Jethwani,
Yashil Vora

# Strategizing Safety : Predicting Road Accident Severity for Effective Prevention

## Table of Contents

- [**Introduction**](#introduction)

- [**Try The Model On Our Webapp**](#try-the-model-on-our-webapp)

- [**Methods**](#methods)
    - [Data Exploration](#data-exploration)
    - [Preprocessing Steps](#preprocessing-steps)
    - [Model 1: Logistic Regression](#model-1-logistic-regression)
    - [Model 2: Neural Networks](#model-2-neural-networks)
    - [Model 3: Support Vector Machines](#model-3-svms)

- [**Results**](#results)
    - [Data Exploration](#data-exploration-results)
    - [Preprocessing Steps](#preprocessing-results)
    - [Model 1: Logistic Regression](#model-1-logistic-regression-results)
    - [Model 2: Neural Networks](#model-2-neural-network-results)
    - [Model 3: Support Vector Machines](#model-3-svms-results)

- [**Discussion**](#discussion)
    - [Data Exploration](#data-exploration-discussion)
    - [Preprocessing Steps](#preprocessing-discussion)
    - [Model 1: Logistic Regression](#model-1-logistic-regression-discussion)
    - [Model 2: Neural Networks](#model-2-neural-network-discussion)
    - [Model 3: Support Vector Machines](#model-3-svms-discussion)

- [**Conclusion**](#conclusion-and-future-steps)

## Introduction

One of the leading causes of non natural death is road accidents. There may be several contributing factors that lead to vehicle casualties, including traffic, weather, road conditions etc. We wanted to predict the severity of road accidents ranging from Slight, Serious, to Fatal using supervised models such as Logistic Regression, SVMs, Neural Nets, Decision Trees etc. Attributes that may be used to predict the data include the road conditions, the weather conditions, vehicle types, or what kind of area they’re in. 

Our data is mainly focused on locations in the UK, so while it may not necessarily apply similarly in the US, we could still use this model to run on US datasets and see the results. It is a dataset with 14 columns and over 600k observations, with columns including severity of accident, the date, number of casualties, longitude,  latitude, road surface conditions, road types, urban/ rural areas, weather conditions, and vehicle types.

Ethical concerns consist ----- if our stakeholders were vehicle companies, would they have reduced sales if, say, trucks were more likely to lead to severe accidents? However, by figuring out what would predict the severity of road accidents, we can also prevent harm by noting the features that largely impact the severity. 

## Try The Model On Our Webapp

We built a webapp to demonstrate our work and let you play around with our model. You can find our journey and test our model in more detail [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)!

TODO

## Methods

### Data Exploration 
#### Visualization Steps

We made use of the pairplot and heatmap with correlation matrix in order to get an overall sense of the distribution of data. Through this we were also able to get correlations between different features and became one with the data.

All of this collectively gave us a better idea of what the data looks like which in turn gives us a better idea of which models to use in the next step of this project.

We then plotted different types of graphs to compare and visulaise diffrent aspects of our data. By plotting various graphs, we aimed to gain a deeper understanding of our data and compare different attributes effectively. The different graphs we plotted were

1. Accidents by Light Conditions
2. Accidents over Time
3. Number of Vehicles V/S Number of Casualities

### Preprocessing Steps
Our work done can be found in the notebook `Data_Cleaning_and_EDA_Final.ipynb`. Here is the link to this [notebook](https://github.com/yashilvora19/accident_severity_prediction/blob/main/Data_Cleaning_and_EDA_Final.ipynb).

We already began preprocessing the data by one hot encoding most of the categorical data (`Road_Surface_Conditions`, `Road_Type`, `Urban_or_Rural_Area`, `Vehicle_Type`), and for `Light_Conditions`, we chose to make it ordinal and encode it from 0 for Dark, and 3 for Daylight. We selected MultiBinarizer to do multiple one-hot encoding for each row for the `Weather Conditions` as there were multiple categories that were satistified. Then we chose to normalize the `Latitude` and `Longitude` to make it a more contained value. We left the `Number_of_Casualties` and `Number_of_Vehicles` as is, as the values were just integers and seemed to have no large outliers.

### Model 1: Logistic Regression

Our work done can be found in the notebook `Milestone_3.ipynb`. Here is the link to this [notebook](https://github.com/yashilvora19/accident_severity_prediction/blob/main/Milestone%203.ipynb).

#### Logistic Regression
In our project, we our trying to classify accidents into the following categories:
1. Mild
2. Severe
3. Fatal

Since this is a classification task, we chose logistic regression as our machine learning model.

Our model analyses the given data (42 columns) and outputs 0 is the accident is classified as 'slight', 1 if it is 'serious', and 2 if it is 'fatal'. We use multiclass logistic regression since there are more than 2 labels. 


### Model 2: Neural Networks

Our work done can be found in the notebook `Milestone_4.ipynb`. Here is the link to this [jupyter notebook](https://github.com/yashilvora19/accident_severity_prediction/blob/main/Milestone_4.ipynb).

For this milestone, we have decided to run a Neural Network on our data. The aim is to get a model that works at a better accuracy than 85%, i.e. it should not predict only 'Mild' accidents (this was a drawback of our last model) and should try to classify the accidents as Severe and Fatal as well. 

#### Neural Network: 
In the Neural Network we created, we used the following specifications and parameters:
- 4 layers: Upon some tuning of the number of layers, we found that 4 layers was the sweet spot between efficiency and output. We also did not want to overfit our training data, so we decided to keep the number of layers relatively low. 
- Sigmoid activation functions in hidden layers: We tuned our hyperparameters to find that this worked best as an activation function in our three hidden layers. A sigmoid activation function is simple enough for efficient runtime, and works well with classification problems. Our hidden layers have 64, 32, and 16 units respectively, to allow the data to scale down for our final output layer
- Softmax activation function in output layer: Since our output is a multinomial classification, we found that softmax was the best activation function to match the results we wanted. We used three units in our output layer, since our model is supposed to classify into three classes: 'Mild', 'Severe', and 'Fatal'.
- Adam optimizer: We used Adam over SGD as our optimizer because it is better suited for large datasets, and converges faster without any tradeoff accuracy-wise.
- Sparse categorical crossentropy loss: We used  "Sparse Categorical Crossentropy" as our loss function because it allows for the data to not be one-hot encoded (which aligns with our preprocessed data) and optimizes for minimized loss across all three classes. We found from past work that using optimization functions such as mse would not work as efficiently with multiple classes. 

### Model 3: SVMs

TODO: Work for SVM's here...

## Results

### Data Exploration Results
Through the heatmap and pair-plot we had decided to plot we got we were able to see trends and patterns through a few more visualizations of light intensities VS number of accidents, number of casualties VS number of vehicles, and how the number of accidents varied over the past 4 years. 

The pair-plot we had plotted is given below. Through this pairplot, we can see the clear relation between latitude and longitude since it maps out the shape of UK.
We can also see a correlation between year and number of casulties, since the number of casualties decreases per year. There also seems to be correlations between the latitude and longitude and the number of casualties/accidents. 
![pairplot](imgs/pairplot.png)

Next, we plotted a heatmap, we can see that the highest correlations is with Number of Casualties, at 0.088 . 
![heatmap](imgs/heatmap.png)

Other graphs that we plotted are given below: 

1. Accidents by Light Conditions
We can seee that the maximum number of accidents happen in the daylight.
![img1](imgs/img1.png)

3. Accidents over Time
Number of accidents seem to be similar in all the years for similar timings during the year.
![img2](imgs/img2.png)

4. Number of Vehicles V/S Number of Casualities
Through this, we can see that greater the number of vehicles we have, more the casualties. This is another useful inference which gives us an indication about how the data is correlated.
![img3](imgs/img3.png)

### Preprocessing Results

#### Categorical Features
Categorical features which were one-hot encoded to convert them into numerical representations include, Road_Surface_ConditionsRoad_Type, Urban_or_Rural_Area, and Vehicle_Type. This conversion was necessary to incorporate these features into machine learning models effectively.

Light_Conditions, while also a categorical feature, was treated as ordinal and encoded from 0 to 3 to preserve the inherent order in its categories.

To handle the Weather Conditions feature, which could have multiple categories per row, we utilized the MultiBinarizer technique. This allowed us to represent each weather condition as a binary feature, facilitating its inclusion in the analysis.

#### Numerical Features

The Latitude and Longitude features were normalized to ensure that their magnitudes did not unduly influence the machine learning algorithms. Normalization was performed by subtracting the mean and dividing by the standard deviation of each feature.
Before normalization, summary statistics such as mean and standard deviation were calculated for these features to provide insights into their distributions and the extent of scaling required.

#### Feature Retention

The features Number_of_Casualties and Number_of_Vehicles were left unchanged during preprocessing. This decision was made based on their inherent numerical nature and relevance to the study objective. These features were considered essential for predicting accident severity and were thus retained without transformation.

### Model 1: Logistic Regression Results
Further evaluations on the performance of the model have been done within the file labelled `Milestone 3.ipynb`.
The accuracy of our Logistic Regression model, came out to be 85.19%, 85.14% and 85.26% for our Training, Testing and Validation. Other parameters such as recall, precision and support can be seen below in the classification reports.
![accuracy](imgs/accuracy.png)

We also plotted the frequency of our actual and predicted values.
![freq1](imgs/freq1.png)
![freq2](imgs/freq2.png)


We can see this issue through the graph of the distribution of the data as well- the actual values have majority accidents classified as mild while the predicted values have all of them classified as that.
![graph.png](imgs/graph.png)

Since all 3 accuracies are close to each other (around 85%), and at the same the mean squared error is also close (around 0.18), we can say that there is no major underfitting or overfitting that can be observed.

### Model 2: Neural Network Results

The accuracy of our Neural Network model, came out to be 85.3%, 85.05% and 85.1% for our Training, Testing and Validation. Other parameters such as recall, precision and support can be seen below in the classification reports.

Classification report and confusion matrix for the 'Mild' severity class.

![class1](imgs/nn_cm_1.png)

Classification report and confusion matrix for the 'Severe' severity class.

![class1](imgs/nn_cm_2.png)

Classification report and confusion matrix for the 'Fatal' severity class.

![class1](imgs/nn_cm_3.png)

Following are the results we found, plotted as graphs: 
![loss_acc](imgs/nn_loss_acc.png)

Additionally, in our previous work we found that a Logistic Regression fails to classify values into all three classes. We wanted to check if this was the issue here as well, so we plotted out our frequencies for actual and predicted values for each class as shown:

![class1freqs](imgs/nn_bar1.png)

![class2freqs](imgs/nn_bar2.png)

![class3freqs](imgs/nn_bar3.png)

All 3 accuracies appear to be close to each other (around 85%). However, looking at the graph for validation accuracy, we see that it is gradually decreasing across epochs. This shows signs of minor overfitting, but since the overall accuracy drops by a very low percentage, it can be neglected.

### Model 3: SVMs Results
TODO


## Discussion

### Data Exploration Discussion 
For this we decided to start with a heat map and a pair plot to get a basic understanding of how the data is. After generating the pairplot we found that there is a  clear relation between latitude and longitude. Further, we can also see a correlation between year and number of casulties, since the number of casualties decreases per year. There also seems to be correlations between the latitude and longitude and the number of casualties/accidents. This could indicate that some regions in UK have more accidents and more work needs to be done there. This includes lack of traffic signals, poor road safety, or just rash drivers breaking speed limits. 

Next, by generating a heatmap we came to the concusion that  there is an extremely low correlation between Accident Severity and all other columns. As seen earlier,  the highest correlations is with Number of Casualties, at 0.088. However, it should be noted that this doesn't mean that there isn't a connection between our input and output. 

After plotting the basic graphs we wanted to explore the data more so we decided to plot some more graphs and found three to have very intresting insights. 
1. Accidents by Light Conditions
Intuitively, we would have thought that a lot of accidents happen during the darkness. However, through this barplot, this is false. The maximum number of accidents happen in the daylight as we have seen earlier. A possible reason for this could be that drivers are more reckless and speed more during when there is daylight, but are more careful in the dark.

2.. Accidents over Time
We saw that there is not much variance in the accidents that happen through the years. While, there are some timings during the year that have had more accidents these seem to be repeating. A possible reason of this could be more people going out dueing vacations, increase in activity during festivals etc. However, there is no change in the number of accidents over the years this shows that no significant improvements have been made recently to make it safer and prevent accidents making this project even more important.

3. Number of Vehicles V/S Number of Casualities
Like we would have expected, more the number of behicals are involved in an accident, more the peeple are at danger ultimately resulting in more casualities.

### Preprocessing Discussion

#### Categorical Features

Encoding categorical features is crucial for machine learning models as they typically require numerical inputs. One-hot encoding allows for the representation of categorical variables without imposing an arbitrary order, while ordinal encoding preserves the order inherent in certain features like Light_Conditions.
The use of MultiBinarizer for Weather Conditions was justified due to the presence of multiple categories per row. This approach enabled us to capture the variability in weather conditions without introducing excessive dimensionality into the dataset.

#### Numerical Features

Scaling numerical features is essential to prevent features with large magnitudes from dominating those with smaller magnitudes during model training. Normalization, as applied to Latitude and Longitude, ensures that all features contribute equally to the learning process, thereby improving model performance.
Normalization of Latitude and Longitude is particularly beneficial in geospatial analyses, as it allows for more meaningful comparisons between geographical locations.

#### Feature Retention

Retaining Number_of_Casualties and Number_of_Vehicles without transformation was deemed appropriate due to their direct relevance to the study objective. These features provide crucial information about the severity and complexity of accidents, making them indispensable for predictive modeling.

### Model 1: Logistic Regression Discussion
We performed Standardzation on our model before we moved forward with actual model implementation. We chose to use standardization as our preprocessing technique due to the following reasons:
1. Our data didn't follow a normal distribution, hence standardizing it was imperative in order to get accurate results.
2. Maining the relationship between datapoints is also important, and since standardization doesn't distort our data distribution, it works well for preprocessing.
3. Standardization also takes into account outliers, which will again make our model better.

We chose logistic regression because of the following reasons:
1. Simplicity: It's easy to implement, and is also one of the first models we learnt in class. 
2. Efficiency: It is known to be a very popular classification model for categorical data, which is what we are focusing on. It is also very fast.
3. Accuracy: It also provides a probability for each outcome, which makes it easier to understand how confident the model is in its predictions.

Conclusion: 
While this would look like the model is performing well on a surface level, if we take a look at the classification reports and the confusion matrix plotted, we can clearly see that there are definitely issues with this model! The recall scores for classes 1 and 2 (or 'Severe' and 'Fatal') accidents are 0. This means that we are rarely predicting those values and 'Mild' accidents are being predicted the most. It is also worth noting that in our dataset, majority of the accidents our mild and this could result in a bias in the data. Due to this bias, it is reasonable to assume that our logistic regression model is biased too and there can be a lot of improvements that can be made here.

### Model 2: Neural Network Discussion

We decided to use a Neural Network as it seemed the logical next step from a regression model, and it can work with classification problems pretty well. Our model analyses the given data (42 columns) and outputs 0 is the accident is classified as 'slight', 1 if it is 'serious', and 2 if it is 'fatal'. We use multiclass classification since there are more than 2 labels. 

Following are some advantages of a Neural Network over the previous models we have considered:
- Neural Networks are able to capture more complicated relationships between non-linear data.
- Having different nodes and activation functions allows us a greater insight into the relationships between variables.
- Neural Networks additionally give us the chance to tune our hyperparameters, allowing us to optimize manually for the greatest efficiency across both training and testing data.

Conclusion: 
While the model appears to perform only marginally better than the logistic regression model previously created, if we take a look at the classification reports and the confusion matrix plotted, we see some clear advantages. The precision scores for classes 1 and 2 (or 'Severe' and 'Fatal') accidents are 0.31 and 0.13 respectively, as opposed to the 0s we saw in logistic regression. This means that we are actually obtaining predictions for those values, which is a clear improvement over the last model. However, there are still large issues. Though the model predicts values from classes 'Severe' and 'Fatal', it does not do so nearly as accurately as it should, as shown in the graphs above. The bias in our data, though countered slightly by the complexity of our model, is still highly relevant. Additionally, there are still improvements to be made vis a vis accuracy - we will work towards improving this in our next model. 

### Model 3: SVMs Discussion
TODO

## Conclusion and Future Steps

TODO:

This is where you do a mind dump on your opinions and possible future directions. Basically what you wish you could have done differently. Here you close with final thoughts

We now look to compare our results from this model to those of even more classification models, such as Decision Trees and SVMs. Some issues that we might encounter when doing this would be to adapt these models to multinomial classification, which is something that we have not worked with yet. We are eager for the challenge, and aspire to get a better understanding of a range of classification models. Ideally, this would improve the accuracy beyond what we have had in the past two models. This would further help us determine which one works the best for our data. 

## Collaboration
