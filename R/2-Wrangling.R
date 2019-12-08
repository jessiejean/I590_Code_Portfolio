#Wrangle data by making it 'tidy' using 'tidyverse' - dplyr package
#1 Each observation is in a row
#2 Each variable is in a column
#3Each value has its own cell

#Install Library
install.packages("tidyverse")  
library(tidyverse)

#Basic functions for data manipulation:
filter() to select cases based on their values.
  filter(flights, month == 1, day == 1) -- selects all flights on Jan 1st

arrange() to reorder the cases.
  arrange(flights, year, month, day) -- reorders values in ascending order, additional columns listed used to break ties
  arrange(flights, desc(arr_delay)) -- order by desending value

select() and rename() to select variables based on their names.
  select(flights, d, e, f) -- select columns by name
  select(flights, d:f) -- select columns between d and f (inclusive)
  select(flights, -d:f) -- select all columns except those from d to f (inclusive)
  rename(flights, d=flightnumber) -- renames column d to flightnumber

mutate() and transmute() to add new variables that are functions of existing variables.
  mutate(flights, newvar = d - f, newvarperhr = newvar/60) -- adds new column newvar, can reference created variable within new var  
  transmute(flights, newvar = d - f, newvarperhr = newvar/60) -- only keeps newly created variables

summarise() to condense multiple values to a single value.
  summarise(flights, mean = mean(f, na.rm = TRUE) -- one row created for mean of column
  
sample_n() and sample_frac() to take random samples.
  sample_n(flights, 10) -- selects 10 random rows 
  sample_frac(flights, 0.01) -- selects random rows as a percentage of the whole population  
            
            
source: https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html
