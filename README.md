Deployment url: <https://j-k-covid19-data-api.herokuapp.com/> 

Pair Programming

Process:

We first divided the work into requirements 1 and 2, and requirements 3 and 4 due to their respective dependencies/coupling on each other. Kevin worked 1-2 and Juan worked on 3-4, and as expected we were challenged/stuck at some parts of the development. 

Part 1 (Kevin):

The most challenging thing I got stuck on was how to design/structure the data representation in our database; how does the data that users send in through csv files look like in our server/database. At this moment I asked Juan to pair with me and I explained the challenge and my thought process, which was that the time series format had way too many columns and with SQLAlchemy I did not know of a way to add that many columns in our Model. We discussed possible solutions and decided to just add one column in our model that represents a date, and each date from a time series file would be a new entry on the TimeSeries model with the corresponding Province/State, Country/Region, etc. There was not much coding involved but in this case Juan was the navigator as he analyzed the challenge from an outside perspective and I was the driver since I was responsible for coding the solution. 

Part 2 (Juan):

A challenge I faced was getting the routing correct and working with html templates while writing the code for the query part. I paired with Kevin at this time to get started with my code since he had finished most of the adding files part which required routing and using html templates. I explained to him that I wanted a button to lead to a different page but was not sure how to transfer information through pages and how templates worked. I became the driver and Kevin was the navigator, he explained to me how he did routing and used templates. With his help, I figured out how to get a button to route to another page and how to add what I wanted to that page with templates.

Reflection (Kevin):

I believe the process went generally well, both times that we paired up to try and solve a challenge, we were productive and got a better understanding of the assignment or we just came up with a solution. I liked having a peer to bounce ideas off of and learn from, this aspect of our process was quite valuable. However, setting up a time to pair up was quite difficult, our availability to work was drastically different and if one of us was stuck on something, that person would have to wait until the other was available in order to then pair up. 

Reflection (Juan):

Overall, I enjoyed pair programming. On both occasions, Kevin and I solved the problem at hand relatively quickly with each other's help. I found it easier to focus on my work while Kevin was the navigator and he helped me a lot with his knowledge. I disliked it at first, it was hard getting used to being the driver while the navigator told me what to do but eventually we both got the hang of it. We also were not available at the same times for multiple days which made it harder to set up pair programming.

Testing Coverage

- Screenshot provided on our repo's Issues tab.

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
