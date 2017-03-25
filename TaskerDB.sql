CREATE TABLE tasker (
taskID integer,
question char(200),
tweet char(200),
userAnswer char(200),
correctAnswer char(200)

);
COPY tasker FROM '/Users/Imauri/Documents/Tasker/Task Database - Self Driving Car Tweet Sentiment.csv' DELIMITER ','CSV HEADER

SELECT * 
FROM tasker;