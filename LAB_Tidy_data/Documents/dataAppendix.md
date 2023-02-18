# Data appendix
All files from /AnalysisData are described here.

# AnalysisData/norm.csv
data with added normalised values by average litres of pure alcochol drunk per capita. all 0 values of data is deleted
* country - country
* beer - average amount of beer cans drunk per capita.
* spirit - average amount of measures of liquors drunk per capita
* wine - average amount of glasses of wine drunk per capita
* pure_alcohol - average amount of litres of pure alcochol drunk per capita
* wine_norm - average amount of glasses of wine drunk per capita divided by verage amount of litres of pure alcochol drunk per capita.
* beer_norm - average amount of beer cans drunk per capita divided by verage amount of litres of pure alcochol drunk per capita.
* spirit_norm - average amount of measures of liquors drunk per capita divided by verage amount of litres of pure alcochol drunk per capita.

# AnalysisData/PCA.csv
casted data of  Beer_servings, Wine_servings, Spirit_servings on principal component axes
* first_component - dataset casted on first component vector
* second_component - dataset casted on second component vector
* third_component - dataset casted on third component vector
first, second and third vector are defined in AnalysisData/eigen_vectors_values.csv by index

# AnalysisData/eigen_vectors_values.csv
each value is a different vector
* beer - length on beer axis
* spirit - length on spirit axis
* wine - length on wine axis
* eigen value - eigenvalue associated with a given eigenvector

