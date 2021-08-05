#!/bin/Rscript

name<- 'Shruti_Poojary'
email<- "Poojaryshruti27@gmail.com"
username<- "@Shruti"
biostack<- "Data Analysis"
twitter<- "@Shruti"
d<- sum(username != twitter)
output<- c(name,email,username,biostack,twitter, d)

cat(paste(output, collapse = ','))

