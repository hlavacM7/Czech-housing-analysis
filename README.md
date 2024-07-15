# Czech Housing Analysis

This is an end-to-end project where I have implemented a Flask application that predicts house prices in the Czech Republic based on four features.

## Results
- **Performance Metrics**: My main metric was the R² score, which ended up being quite good given the available data.
- Here's a quick snapshot of the results:

![Results Image](https://github.com/hlavacM7/Czech-housing-analysis/blob/main/Result.JPG)

## Description of the Pipeline
Here's how the magic happens:

1. **Data Collection**: Data was scraped using Beautiful Soup from [reality.idnes.cz](https://reality.idnes.cz/).
2. **Data Cleaning**: The dataset was quite messy, so I removed rows containing 0 values and outliers that were significantly influencing the results.
3. **Modeling**: I used Lazy Predict, which evaluates various regression models and suggests the best one to use.
4. **Evaluation**: The model was evaluated using the R² score.
5. **Deployment**: The model was deployed using Flask.

## Tools Used
Here's a list of the main tools and libraries I used in this project:

- **Python**: The main programming language.
- **Pandas**: For data manipulation and analysis.
- **Beautiful Soup**: For web scraping.
- **Matplotlib**: For data visualization.
- **Scikit-learn**: For machine learning algorithms.
- **Flask**: For the web app.
