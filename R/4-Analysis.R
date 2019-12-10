#Create scatterplot of 2 variables and draw fitted line

plot(y ~ x, data = dataset, col = "choosecolor", pch = 20,
     main = "Title for Chart")
fittedline = lm(y ~ x, data = dataset)
abline(fittedline, col = "choosecolor", lwd = 3)


#Create QQ plot to draw correlation between sample and normal distribution
qqnorm(dataset$variable, pch = 1, frame = FALSE)
qqline(dataset$variable, col = "choosecolor", lwd = 2)




Source: https://rpubs.com/williamsurles/294096 
