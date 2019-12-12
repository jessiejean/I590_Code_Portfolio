#Bar chart: main for title, color selection, x and y labels
Numbers<-table(mtcars$cyl,mtcars$gear)
barplot(Numbers,main='Automobile cylinder number grouped by number of gears', 
        col=c('red','orange', 'steelblue'),legend=rownames(Numbers),xlab='Number of Gears',
        ylab='count')

# histogram of frequency of ozone values in 'airquality' dataset
hist(airquality$Temp,col='steelblue',main='Maximum Daily Temperature',
     xlab='Temperature (degrees Fahrenheit)')


# Plot Ozone and Temperature measurements for only the month of September 
with(subset(airquality,Month==9),plot(Wind,Ozone,col='steelblue',pch=20,cex=1.5)) 
title('Wind and Temperature in NYC in September of 1973')

#Boxplot for both categorical and continuous variable data
mtcars<-transform(mtcars,cyl=factor(cyl)) # convert 'cyl' column from class 'numeric' to class 'factor'
class(mtcars$cyl) # 'cyl' is now a categorical variable 
boxplot(mpg~cyl,mtcars,xlab='Number of Cylinders',ylab='miles per gallon',
        main='miles per gallon for varied cylinders in automobiles',cex.main=1.2)

#Correlogram shows amount of correlation between datasets
data("mtcars")
corr_matrix <- cor(mtcars)
corrplot(corr_matrix)

# with numbers and lower
corrplot(corr_matrix,
         method = 'number',
         type = "lower")




#Source: https://www.kdnuggets.com/2018/06/7-simple-data-visualizations-should-know-r.html
