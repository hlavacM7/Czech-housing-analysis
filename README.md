# Czech housing analysis

This is an end to end project in which i have implemented flask application, that is able to predict house prices in the Czech republic based on 4 features.

## Results
- **Performance Metrics**: My main metric was R2 score, which ended up being quite good, given the data that was available
- Here's a quick snapshot of the results:

![Results Image]((https://github.com/hlavacM7/Czech-housing-analysis/blob/main/Result.JPG))

## Description of the Pipeline
Here's how the magic happens:

1. **Data Collection**: Data was scraped using Beautiful Soup from https://reality.idnes.cz/
2. **Data Cleaning**: The dataset was quite messy, so I had to remove rows that contained 0 values and i also had to remove the outliers because they were influencing the result a lot
3. **Modeling**: I have used Lazy predict which goes through all the possible regression models and shows me which one to select
4. **Evaluation**: R2 score
5. **Deployment**: 

## Tools Used
Here's a list of the main tools and libraries I used in this project:

- **Python**: The main programming language.
- **Pandas**: For data manipulation and analysis.
- **BeautifoulSoup**: For web scraping.
- **Matplotlib**: For data visualization.
- **Scikit-learn**: For machine learning algorithms.
- **Flask**: For the web app.
