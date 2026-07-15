# Australian Airline Punctuality and Reliability Visual Analytics



## Project Overview



This project develops an interactive multidimensional visual analytics workflow for the Australian Airline On-Time Performance dataset published by the Bureau of Infrastructure and Transport Research Economics (BITRE).



The analysis examines domestic airline punctuality and reliability from January 2010 to February 2024 across multiple analytical dimensions, including:



- time

- airports

- routes

- airlines

- flight activity

- departure on-time performance

- arrival on-time performance

- cancellations



R is used for data auditing, cleaning, feature engineering, validation, and reproducible findings analysis. Tableau is used to build interactive geographic, temporal, route, and airline visualisations.



The project was developed for COMP2026 Visual Analytics Assignment 2.



---



## Project Objectives



The analysis addresses the following questions:



1\. How are airport punctuality and flight activity distributed geographically?

2\. How has airport and network performance changed across years?

3\. How does airport performance vary across the 12 months of a selected complete year?

4\. How do routes compare in departure punctuality, arrival punctuality, flight volume, and cancellation reliability?

5\. How do airlines compare in punctuality and cancellation performance?

6\. What irregularities and multidimensional patterns become visible when operational measures are analysed jointly?



---



## Tools



### R



Used for:



- workbook auditing

- worksheet inspection

- duplicate detection

- data integration

- missing-value validation

- airline-name standardisation

- feature engineering

- analytical-layer creation

- weighted metric validation

- reproducible numerical findings



Main packages:



```r

readxl

dplyr

```



### Tableau



Used for:



- interactive geographic visualisation

- network time-series analysis

- airport heatmaps

- multidimensional route analysis

- airline comparison

- interactive parameters

- tooltips

- worksheet-level analytical filters



---



## Project Structure



```text

08\_airline\_service\_performance\_visual\_analytics/

│

├── data/

│   ├── raw/

│   │   └── Dataset Assignment 2.xlsx

│   │

│   └── processed/

│       ├── airline\_performance\_clean.csv

│       └── airline\_performance\_analysis.csv

│

├── scripts/

│   ├── 01\_data\_audit/

│   │   ├── 01\_data\_audit.Rmd

│   │   └── 01\_data\_audit.pdf

│   │

│   ├── 02\_data\_cleaning/

│   │   ├── 02\_data\_cleaning.Rmd

│   │   └── 02\_data\_cleaning.pdf

│   │

│   ├── 03\_feature\_engineering/

│   │   ├── 03\_feature\_engineering.Rmd

│   │   └── 03\_feature\_engineering.pdf

│   │

│   └── 04\_analysis\_findings/

│       ├── 04\_analysis\_findings.Rmd

│       └── 04\_analysis\_findings.pdf

│

├── tableau/

│   └── airline\_visual\_analytics.twb

│

├── figures/

│

├── report/

│

├── documents/

│

└── README.md

```



---



## Data Source



The project uses the BITRE Airline On-Time Performance dataset containing monthly Australian domestic aviation performance records.



Dataset coverage:



```text

January 2010 to February 2024

```



The original Excel workbook contained 12 worksheets.



A duplicate-key audit identified that all 4,197 observations in the standalone `2020` worksheet were already represented in the 2020 records of the `2020-23 OTP` worksheet.



The standalone `2020` worksheet was therefore excluded before integration to prevent double counting.



---



## Data Preparation Workflow



The R workflow is divided into four stages.



### 1. Data Audit



Location:



```text

scripts/01\_data\_audit/

```



The audit examines:



- worksheet names

- worksheet dimensions

- column structure

- date coverage

- record counts

- airport counts

- route counts

- airline labels

- potential duplicate sources



Key result:



```text

Standalone 2020 rows:          4,197

2020 rows in 2020-23 sheet:    4,197

Matching analytical keys:      4,197

```



The standalone 2020 worksheet was confirmed as duplicated data.



---



### 2. Data Cleaning and Integration



Location:



```text

scripts/02\_data\_cleaning/

```



The remaining 11 worksheets were integrated.



Processing steps include:



- excluding the duplicated 2020 worksheet

- combining annual worksheets

- standardising column names

- trimming text fields

- converting monthly values to a consistent date type

- converting operational measures to numeric variables

- removing invalid non-data rows

- standardising airline labels

- validating duplicated analytical keys

- validating flight-count relationships

- inspecting missing OTP values



Integration result:



```text

Rows after worksheet integration:   80,977

Non-data rows removed:                    5

Final cleaned observations:          80,972

```



Airline labels were standardised from 14 raw labels to 12 consistent analytical labels.



Examples:



```text

virgin Australia   -> Virgin Australia

Regional Express   -> Rex Airlines

```



The dataset contained:



```text

91 missing departure OTP values

91 missing arrival OTP values

```



Validation confirmed that every missing OTP observation occurred where:



```text

Sectors\_Flown = 0

```



These percentages are mathematically undefined and were retained as missing values rather than replaced with zero.



Final validation identified:



```text

Duplicated analytical keys:          0

Scheduled-count inconsistencies:     0

Departure-count inconsistencies:     0

Arrival-count inconsistencies:       0

```



---



### 3. Feature Engineering and Analytical Layers



Location:



```text

scripts/03\_feature\_engineering/

```



Time variables were created:



```text

Year

Month\_Number

Month\_Name

```



An `Analysis\_Level` variable was created to separate different analytical grains.



The four analytical layers are:



` Analysis Level ` Records ` Purpose `

`---`---:`---`

` Network ` 170 ` Overall monthly network analysis `

` Airline ` 1,174 ` Airline comparison `

` Route ` 20,156 ` Route and airport analysis `

` Airline Route ` 59,472 ` Detailed airline-route analysis `



Total:



```text

80,972 observations

```



The final analytical dataset contains:



```text

80,972 rows

19 columns

15 years

170 monthly periods

4 analytical levels

```



Output:



```text

data/processed/airline\_performance\_analysis.csv

```



### Important Analytical Grain Rule



The processed dataset contains all four analytical levels in one file.



Every Tableau worksheet must explicitly filter `Analysis\_Level`.



Use:



```text

Network views      -> Analysis\_Level = Network

Airport views      -> Analysis\_Level = Route

Route views        -> Analysis\_Level = Route

Airline views      -> Analysis\_Level = Airline

```



Records from different analytical levels must not be summed together because this would produce duplicated aggregation.



---



### 4. Reproducible Findings Analysis



Location:



```text

scripts/04\_analysis\_findings/

```



This script reproduces the numerical findings reported in the analysis section.



It calculates:



- overall network performance

- annual network activity

- monthly cancellation peaks

- minimum monthly OTP

- airport activity concentration

- airport OTP rankings

- departure-arrival airport differences

- annual airport performance changes

- persistent airport performance patterns

- monthly 2023 airport patterns

- route benchmark groups

- route volume and cancellation performance

- route directional OTP gaps

- airline punctuality and cancellation performance



All numerical findings reported in the project report are derived from this script using the final analytical dataset.



This creates the following evidence chain:



```text

Raw BITRE workbook

&#x20;       ↓

Data audit

&#x20;       ↓

Data cleaning and validation

&#x20;       ↓

Feature engineering

&#x20;       ↓

Final analytical CSV

&#x20;       ↓

Reproducible R calculations

&#x20;       ↓

Report findings

```



---



## Performance Measures



Aggregated percentages use weighted calculations based on underlying flight counts.



### Weighted Departure OTP



```text

Total Departures On Time

---------------------------- × 100

Total Sectors Flown

```



### Weighted Arrival OTP



```text

Total Arrivals On Time

-------------------------- × 100

Total Sectors Flown

```



### Weighted Cancellation Rate



```text

Total Cancellations

--------------------------- × 100

Total Sectors Scheduled

```



Simple averages of published percentage fields are not used for aggregated analysis because observations have different flight volumes.



Using weighted calculations prevents low-volume observations from having the same analytical influence as high-volume operations.



---



## Tableau Calculated Fields



### Weighted Departure OTP



```tableau

IF SUM(\[Sectors\_Flown]) = 0 THEN

&#x20;   NULL

ELSE

&#x20;   SUM(\[Departures\_On\_Time]) / SUM(\[Sectors\_Flown])

END

```



### Weighted Arrival OTP



```tableau

IF SUM(\[Sectors\_Flown]) = 0 THEN

&#x20;   NULL

ELSE

&#x20;   SUM(\[Arrivals\_On\_Time]) / SUM(\[Sectors\_Flown])

END

```



### Weighted Cancellation Rate



```tableau

IF SUM(\[Sectors\_Scheduled]) = 0 THEN

&#x20;   NULL

ELSE

&#x20;   SUM(\[Cancellations]) / SUM(\[Sectors\_Scheduled])

END

```



The Tableau calculated fields are formatted as percentages.



The calculations must not be multiplied by 100 in Tableau because percentage formatting handles the display conversion.



---



## Interactive Airport Perspective



A Tableau parameter named:



```text

Airport Perspective

```



contains:



```text

Departure

Arrival

```



The parameter controls both the airport dimension and OTP measure.



### Selected Airport



```tableau

IF \[Airport Perspective] = "Departure" THEN

&#x20;   \[Departing\_Port]

ELSE

&#x20;   \[Arriving\_Port]

END

```



### Selected Airport OTP



```tableau

IF \[Airport Perspective] = "Departure" THEN

&#x20;   \[Weighted Departure OTP]

ELSE

&#x20;   \[Weighted Arrival OTP]

END

```



This allows the geographic and airport heatmap views to switch dynamically between departure and arrival perspectives.



---



## Tableau Visualisations



The Tableau workbook contains seven analytical worksheets.



### 01 — Network OTP Trend



```text

01\_Network\_OTP\_Trend

```



Purpose:



- examine long-term network punctuality

- compare weighted departure and arrival OTP

- identify temporal irregularities



Dimensions and measures:



```text

X-axis: Month

Y-axis: Weighted OTP

Lines: Departure OTP and Arrival OTP

Analysis Level: Network

```



---



### 02 — Network Cancellation Trend



```text

02\_Network\_Cancellation\_Trend

```



Purpose:



- examine network cancellation reliability

- identify cancellation spikes and unusual periods



Dimensions and measures:



```text

X-axis: Month

Y-axis: Weighted Cancellation Rate

Analysis Level: Network

```



Cancellation is displayed separately from OTP because its scale and extreme spikes would reduce the readability of punctuality measures in a combined chart.



---



### 03 — Geographic Airport Performance



```text

03\_Geographic\_Airport\_Performance

```



Purpose:



- analyse geographic airport performance

- compare operational scale and punctuality

- switch between departure and arrival perspectives



Visual encoding:



```text

Position  -> Airport geography

Size      -> Sectors Flown

Colour    -> Weighted OTP

Parameter -> Airport Perspective

```



Three airport locations required manual coordinate matching:



```text

Mildura

Ayers Rock

Hamilton Island

```



---



### 04 — Airport Performance by Year



```text

04\_Airport\_Year\_Heatmap

```



Purpose:



- compare airport performance across years

- identify persistent and network-wide temporal patterns



Visual encoding:



```text

Rows    -> Airport

Columns -> Year

Colour  -> Weighted OTP

```



The view covers:



```text

2010-2023

```



The partial 2024 data were excluded from annual comparison because the dataset contains only January and February 2024.



The colour scale is fixed from:



```text

50% to 100%

```



---



### 05 — Airport Monthly Performance in 2023



```text

05\_Airport\_Month\_Heatmap\_2023

```



Purpose:



- analyse airport performance through all 12 months of a complete year

- identify monthly variation and potential seasonal structure



The year 2023 was selected because it is the most recent complete calendar year in the dataset.



Visual encoding:



```text

Rows    -> Airport

Columns -> Month

Colour  -> Weighted OTP

```



Months are sorted chronologically using `Month\_Number`.



---



### 06 — Route Performance Scatter Plot



```text

06\_Route\_Performance\_Scatter

```



Purpose:



- examine multidimensional route performance

- compare departure and arrival punctuality

- analyse flight volume and cancellation reliability

- identify unusual route observations



Visual encoding:



```text

X-position -> Weighted Departure OTP

Y-position -> Weighted Arrival OTP

Size       -> Sectors Flown

Colour     -> Weighted Cancellation Rate

Detail     -> Route

```



Each mark simultaneously represents:



```text

Route identity

Departure punctuality

Arrival punctuality

Flight volume

Cancellation reliability

```



---



### 07 — Airline Performance Comparison



```text

07\_Airline\_Performance\_Comparison

```



Purpose:



- directly compare airline punctuality

- compare weighted departure and arrival OTP



Visual encoding:



```text

Rows   -> Airline

Bars   -> Departure OTP and Arrival OTP

Colour -> Measure Names

```



Interactive tooltips retain:



```text

Cancellation Rate

Sectors Flown

```



A grouped horizontal bar chart was selected instead of a scatter plot because the small number of airline categories produced a sparse scatter view with limited comparative value.



---



## Key Findings



Selected reproducible findings include:



### Network Performance



```text

Weighted Departure OTP:      81.0%

Weighted Arrival OTP:        79.9%

Overall Cancellation Rate:    2.62%

```



Major cancellation peaks:



```text

April 2020:   33.6%

July 2021:    31.8%

```



Lowest monthly network punctuality:



```text

July 2022

Departure OTP: 54.0%

Arrival OTP:   55.0%

```



---



### Airport Performance



Sydney, Melbourne, and Brisbane together accounted for:



```text

56.6% of departure flight activity

```



Selected airport results:



```text

Highest Departure OTP: Port Lincoln   89.4%

Highest Arrival OTP:   Newman         89.0%



Lowest Departure OTP:  Sunshine Coast 69.3%

Lowest Arrival OTP:    Port Macquarie 74.4%

```



---



### Airport Performance Across Years



Between 2021 and 2022:



```text

Airports compared:               36

Airports with lower Arrival OTP: 36

```



Between 2022 and 2023:



```text

Airports compared:                36

Airports with higher Arrival OTP: 29

```



Persistent patterns:



```text

Port Lincoln:

Arrival OTP >= 85% in 12 of 14 complete years



Port Macquarie:

Arrival OTP < 80% in 13 of 14 complete years

```



---



### Monthly Performance in 2023



Network Arrival OTP:



```text

January:   76.7%

July:      68.2%

November:  64.1%

December:  63.6%

```



Airports below 70% Arrival OTP:



```text

January:    3

July:      18

November:  26

December:  21

```



The 2023 view identifies monthly variation and widespread late-year weakness.



However, one complete year is insufficient to establish a recurring seasonal cycle across multiple years.



---



### Route Performance



2023 network benchmarks:



```text

Departure OTP: 71.0%

Arrival OTP:   70.6%

```



Route classification:



```text

Above both benchmarks: 45 routes

Below both benchmarks: 60 routes

Mixed performance:     21 routes

```



Highest-volume route:



```text

Melbourne-Sydney

Sectors Flown:       24,222

Departure OTP:        72.5%

Arrival OTP:          67.6%

Cancellation Rate:     8.95%

```



Largest directional OTP differences include:



```text

Darwin-Adelaide:  +12.5 percentage points

Adelaide-Darwin:  -12.3 percentage points

```



---



### Airline Performance



Selected 2023 results:



```text

QantasLink

Departure OTP: 76.4%

Arrival OTP:   76.3%



Rex Airlines

Departure OTP:     76.3%

Cancellation Rate:  1.85%



Bonza

Departure OTP:     62.6%

Arrival OTP:       64.2%

Cancellation Rate: 12.7%

Sectors Flown:      1,094

```



The results demonstrate that punctuality should be interpreted together with cancellation reliability and operational scale rather than through OTP rankings alone.



---



## Reproducibility



Run the R Markdown files in the following order:



```text

01\_data\_audit

&#x20;     ↓

02\_data\_cleaning

&#x20;     ↓

03\_feature\_engineering

&#x20;     ↓

04\_analysis\_findings

```



Expected final analytical dataset:



```text

data/processed/airline\_performance\_analysis.csv

```



Then open the Tableau workbook:



```text

tableau/airline\_visual\_analytics.twb

```



The Tableau workbook should use:



```text

data/processed/airline\_performance\_analysis.csv

```



as its analytical data source.



For submission or transfer to another computer, a Tableau packaged workbook (`.twbx`) is recommended so that the local data source is included with the workbook.



---



## Analytical Limitations



The dataset does not contain several variables that could explain the operational causes of observed performance changes, including:



- weather

- airport congestion

- staffing

- aircraft availability

- passenger volume

- delay duration

- disruption causes



The dataset is aggregated monthly and therefore cannot represent flight-level or day-level variation.



The 2024 data cover only January and February and should not be interpreted as a complete annual period.



The 2023 monthly analysis identifies within-year variation but does not independently establish recurring seasonality across multiple years.



The analysis is therefore descriptive rather than causal.



---



## Potential Extensions



Future analysis could incorporate:



- clustering of airports or routes with similar operational profiles

- principal component analysis for dimensionality reduction

- automated anomaly detection

- Isolation Forest

- multi-year seasonal time-series analysis

- weather and congestion data

- passenger-volume data

- flight-level delay data

- database-backed or pre-aggregated visual querying for larger datasets



These methods could complement interactive visual analysis by systematically identifying unusual observations and reducing dimensional complexity.



---



## Author



**Phạm Minh Khôi**  

Student ID: **22145599**



COMP2026 — Visual Analytics  

Assignment 2 — Multidimensional Data Visualisation



---



## References



Bureau of Infrastructure and Transport Research Economics. (n.d.). *Airline on-time performance—Monthly reports and time series data*. Retrieved July 15, 2026, from https://www.bitre.gov.au/resource/aviation/airline-time-performance-monthly-reports-and-time-series-data



Heer, J., \& Shneiderman, B. (2012). Interactive dynamics for visual analysis. *Communications of the ACM, 55*(4), 45–54. https://doi.org/10.1145/2133806.2133821



Liu, F. T., Ting, K. M., \& Zhou, Z.-H. (2008). Isolation forest. In *2008 Eighth IEEE International Conference on Data Mining* (pp. 413–422). IEEE. https://doi.org/10.1109/ICDM.2008.17



Liu, Z., Jiang, B., \& Heer, J. (2013). imMens: Real-time visual querying of big data. *Computer Graphics Forum, 32*(3pt4), 421–430. https://doi.org/10.1111/cgf.12129



Oliveira, A. V. M., Oliveira, B. F., \& Vassallo, M. D. (2023). Airport service quality perception and flight delays: Examining the influence of psychosituational latent traits of respondents in passenger satisfaction surveys. *Research in Transportation Economics, 102*, 101371. https://doi.org/10.1016/j.retrec.2023.101371



Pearson, K. (1901). LIII. On lines and planes of closest fit to systems of points in space. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, 2*(11), 559–572. https://doi.org/10.1080/14786440109462720



Shneiderman, B. (1996). The eyes have it: A task by data type taxonomy for information visualizations. In *Proceedings of the 1996 IEEE Symposium on Visual Languages* (pp. 336–343). IEEE. https://doi.org/10.1109/VL.1996.545307

