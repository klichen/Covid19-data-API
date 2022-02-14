Deployment url: <https://j-k-covid19-data-api.herokuapp.com/> 

Documentation 

Adding and Updating:

<https://documenter.getpostman.com/view/18079075/UVC6iSCT>

How To Use Query Page:

- type of place text box: 

options are: "ProvinceState" or "Country Region"

- place(s) text box:

list the places you want in the format "Abc,Def" with no spaces and a comma in between place

- date(s) text box {time series only}:

the date is in the format: m/d/yy

for a range of dates, the starting date goes first and end date goes second: "m/d/yy,m/d/yy"

if only looking at one day specifically, both the starting date and end date should be the same. ex: "1/1/20,1/1/20"

- data {daily reports only}:

options are: "Confirmed", "Deaths", "Recovered", "Active"

if submitting multiple, the format should be "Confirmed,Deaths,Recovered" with no spaces and a comma in between each option

- output type:

type in "CSV"; json was not implemented





--Pair programmed with Juan Ayala
