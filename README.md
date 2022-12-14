#  Project 2: Ames Housing Data and Kaggle Challenge

 - [Problem Statement](#Problem-Statement)
 - [Background](#Background)
 - [Executive Summary](#Executive-Summary)
 - [Data Sources](#Data-Sources)
 - [Conclusions & Recommendations](#Conclusions-&-Recommendations)


### Problem Statement
1. Part 1: Creating a regression model based on the Ames Housing Dataset. Our goal is to generate linear regression model using the training dataset and this model predict the price of a house at sale. The best model will be used to generate a prediction set to be uploaded to Kaggle to compare our score with other competitor.([*source*](https://www.kaggle.com/competitions/dsi-us-11-project-2-regression-challenge))
2. Part 2: Using the model, solve a data science problem in a business. We as a team of real estate consultants providing advice to property developers/ clients for asset appreciation.Our aim is to dentify features with a strong positive correlation to the sale price of a home and generate business insights to maximize the ROI.We will focus the analysis on the selected  neighbourhood(s) as well as the choosen features that can fetch the better sale price.


---
### Background
Ames is a city in the state of Iowa, USA. It is best known as the home of Iowa State University, with leading agriculture, design, engineering, and veterinary medicine colleges. It is the ninth largest city, with a population of about 67,000 people.
Ames is also known as a college city, where the students makes up about half of its population. This also means that property rental is a huge market in this city.
![Iowan is known as state of University](Iowa.png)

---
### Executive Summary
**INTRODUCTION**

To generate a reliable model on the tarining set of Ames property sales price, the dataset are imported and pre-processed before testing on multiple model. Each columns of the dataset represent different features that contributing to the changes of property sales price in AMES. The dataset examines the house sold between 2006-2010 and consist of 79 features and 1 output variable, the Sale Price. 
Besides that,in order to calculate the investment ROI, our team have taken the estimated average cost to build the rooms from the website([*HomeGuide*](https://homeguide.com/costs/)). 

**METHODOLOGY**

A **data science workflow** was implemented to conduct this analysis. Firstly, the **problem statement** was defined???Generate a robust property sales price prediction model and provide business insight to investor/home buider to maximize their ROI. 
Next, **data cleaning** was conducted to ensure that all datatypes were accurate and any other errors were fixed.Using all data, an **exploratory data analysis** was conducted to explore relation between the features and target variable. From here, the features that are not linear with sale price will be dropped as they have violate the assumption of linear regression. The outliers are also eliminated in this stage to reduce our model's noise. 
**Preprocessing & Feature Engineering**. The following steps are taken in order to get the optimized prediction in Linear Regression model: 
- logarithm of target variable to reduce skewness
- train test split on training data
- multicollinearity detection (VIF)
- reduce data skewness (Box Cox)
- Standard Scaler for numerical features
- One Hot Encoder for categorical features


Once all data was processed, **Model Tuning** can be carried out using GridSearchCV and Pipelines. The model and hyperparamter that generate the best mean_squared_error score can be drawn from this section.Lastly, the model have to pass certain criteria in **Model Evaluation** step. The model must be well generalised (train-test MSE different <5%), has normally distibuted standard error and good linear relation between actual and predicted output.
 

**SIGNIFICANT FINDINGS**

The result shows that the top features that have confidence level of 95% which linearly associated with Ames's property sales price are the numerical features, starting from the area of the property to quality and then the property age. Besides that, for categorical feature, the neighbourhood features seems to be having relatively higher coefficient than the other categorical data. Hence, our team decided to dig more into this features in our business decision direction in part 2 of this project.

### Data Sources
The sources of the datasets used in this project: 

* [`train.csv`](./datasets/train.csv): Training dataset for property sale price in AMES
* [`test.csv`](./datasets/test.csv): Testing dataset to generate prediction and submit to Kaggle Competition


### Conclusions-&-Recommendations
The final linear regression model is:
- Ridge (Alpha=40)
- Generalisation : 0.0284% MSE different between test and train dataset
- Kaggle Score: 19,456

The three neighbourhoods that studied in this project are: OldTown, CollegeCreek and Somerst. They are choosen due to their low MSE diff with training dataset and sufficient number of data available (>100 rows). 
 
This map shows the location of the neighbourhoods and the Iowa Univeristy which is the landmark in AMES. It can be seen that CollegeCreek and Somerst are relatively closer to the university area compare to Old Town.
![Map showing the location of the neighbourhood in AMES city](neighborhood.png)

The features that selected in this project are Bedroom, Full Bathroom and Half Bathroom. The result is finalized as below:

| Neighbourhood | Recommended Features | ROI   | 
| ------------- |:-------------:       | -----:|
| Sommerset     | Bedroom              | 35%   |
| College Creek | Full bathroom        | 200%  |
| Old Town      | Full bathroom        | 107%  |

We recommend developers who want to build property in the three neighbourhoods, to optimize their investments by increasing the number of different feature type by referring to the analytical result.
The examples of interpretion from the result are:
1. There is an increased demand for properties with multiple bedrooms in Somerst, this could be due to to the higher proportion of students. However a word of caution to investors would be not to invest in bathrooms as this feature is not profitable.
2. The number of bedrooms has higher limitations in gains compared to the other features given a limited lot area.
3. Increasing bedrooms has larger impact on the absolute value of property due to its possiblity of adding more rooms than bathrooms.

**Limitation**

- Multicollinearity still persists despite actions taken to reduce it.
- Cost in calculating ROI is a rough estimation, might be different depend on location and season.
- Insufficient data to analyse other neighbourhoods.



