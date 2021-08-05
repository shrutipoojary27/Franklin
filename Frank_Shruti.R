#!/bin/Rscript

name<- 'Shruti_Poojary'
email<- "Poojaryshruti27@gmail.com"
username<- "@Shruti"
biostack<- "Data Analysis"
twitter<- "@Shruti"
output<- c(name,email,username,biostack,twitter)

cat(paste(output, collapse = ','))
sum(username != twitter)
