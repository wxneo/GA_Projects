# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Singapore Housing Data

### Problem Statement
We are a real estate start-up company in Singapore. HDB resale flat prices span a big range and seem to be influenced by different features of the flat. The general public may not be well-equipped with the information needed to aid their Real Estate decision making process. We have decided to develop a product where the general public can check the predicted HDB resale flat pricing, and answer common questions such as:
1. What are the available options given my current budget?
2. Which flat types and where can I afford as a buyer?
3. What price should I set when I sell my flat?
4. How to market my flat to increase its selling price?

Who are you: General public


### Datasets Used:
* [`train.csv`](../datasets/train.csv): A dataset with over 70 columns of different features relating to HDB flats, for resale transactions taking place from Mar 2012 to Apr 2021.
* [`pri_sch_popularity.csv`](../datasets/pri_sch_popularity.csv): [Primary School Popularity dataset](https://schlah.com/primary-schools) contains schools ranked based on Popularity in Primary 1 (P1) Registration.


### Data Dictionary
The data dictionary for the columns found in train.csv can be found at this [kaggle link](https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data).

Additionally we have added the following features:

| Feature | Type | Dataset | Description |
| :--- | :--- | :--- | :---|
| pop_ranking | int64 | pri_sch_popularity | Primary School ranking based on P1 registration popularity |
| pop_ranking_2cat | int | na | Primary School ranking split into 2 tiers - top 8 schools are Cat 1 and the reamaining are Cat 2 |
| postal_sector | object | na | First 2 characters of the 'postal' column is its [postal sector](https://www.mingproperty.sg/singapore-district-code/) | 
| housing_region | object | na | Housing regions of Core Central Region (CCR), Rest of Central Region (RCR), and Outside Central Region (OCR), [as defined by the Urban Redevelopment Authority](https://www.redbrick.sg/blog/singapore-districts-and-regions/), were assigned to each flat based on its postal sector. | 


### Key Takeaways
The following features were found to have the greatest impact on the model we have built:

* Town
* Storey Range
* Full Flat Type
* Pri Sch Name
* Floor Area SQM
* Lease Commencement Date
* MRT Nearest Distance
* Hawker Nearest Distance
* Mall Nearest Distance
* Pri Sch Nearest Distance


### Recommendations

* Recommendations for Buyers: 
	* Know your available options given your budget
	* Prioritize and personalize your wants
	* Quality home with comfortable price

* Recommendations for Sellers:
	* Appraise your property value based on market valuation
	* Pivot your selling strategies
	* Match your property’s unique selling points to the right buyers

