# Import from comma delimited text file where first row contains variable names
# assign the variable id to row names
mydata <- read.table("c:/mydata.csv", header=TRUE,
   sep=",", row.names="id")

# Import from excel where first row contains variable names
install.packages("readxl")
# Loading
library("readxl")
# Import xls files
my_data <- read_excel("my_file.xls")
# Import xlsx files
my_data <- read_excel("my_file.xlsx")
# Import worksheet by its name
my_data <- read_excel("my_file.xlsx", sheet = "data")
# Import worksheet by its index
my_data <- read_excel("my_file.xlsx", sheet = 2)
