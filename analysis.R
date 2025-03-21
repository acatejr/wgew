library(reader)
library(lubridate)
library(dplyr)
library(ggplot2)

# Read the data from csv
data = read.csv("./data/summary_precip_data.csv")

# Transform the date column from string to date and group by gage and month
data$Date = mdy(data$Date)

# Group by Gage id, month and compute total depth, mean and median for
# the event by month.
aggregate_data = data %>% mutate(year=year(Date), month=month(Date), day=day(Date)) %>%
  group_by(Gage, month) %>%
  summarise(
    total_depth=sum(Depth),
    mean=mean(Depth),
    median=median(Depth),
    q1=quantile(Depth, 0.25),
    q3=quantile(Depth, 0.75)
  )

is_iqr_outler = function(depth, gage, month, k=1.5) {
  df = filter(aggregate_data, Gage=={{gage}} & month=={{month}})
  iqr = df$q3 - df$q1
  lower_bound = df$q1 - k * iqr
  upper_bound = df$q3 + k * iqr
  return(depth < lower_bound | depth > upper_bound)
}

df = data %>%
  select(Gage, Date, Depth) %>%
  mutate(month=month(Date)) %>%
  mutate(iqr_outler=is_iqr_outler(Depth, Gage, month))

outliers = df %>% filter(iqr_outler==TRUE) %>%
  group_by(Gage) %>%
  summarise(
    outlier_count=n()
  )

ggplot(outliers, aes(x=Gage, y=outlier_count)) +
 geom_bar(stat = "identity", width=1) + 
  geom_text(hjust=0, vjust=0)

# ggplot(outliers, aes(x=as.factor(Gage) y=outlier_count)) +
#   geom_bar(color="blue", fill=rgb(0.1,0.4,0.5,0.7) )