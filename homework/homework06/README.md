# Homework 06 — Data Preprocessing

## Cleaning Strategy

The raw dataset is stored in `data/raw/starter_data.csv`.
Reusable preprocessing functions are implemented in
`src/cleaning.py`.

The notebook includes:

- Median imputation for missing numeric values
- Removal of observations with missing required fields
- Conversion of the date column to a datetime data type
- MinMax normalization of the numeric `value` feature
- Comparison of the original and processed datasets

The raw dataset contained no missing values. Therefore, the median
imputation and missing-row removal functions did not modify the
dataset.

The `date` column was converted from text to datetime because it
represents calendar dates.

The `value` column was normalized with MinMaxScaler, placing the
observed values on a scale from 0 to 1.

The cleaned dataset is saved to
`data/processed/starter_data_cleaned.csv`.

## Assumptions

Median imputation assumes that missing numeric observations are not
systematically biased. Dropping incomplete rows assumes that discarded
observations are not essential or systematically different from those
retained.  That is to say, that the missing observations are
Missing Completely At Random (MCAR).

MinMax scaling assumes that the observed minimum and maximum values
are reasonably representative. That is to say, that there are not even
higher or lower values that might be omitted on the basis of their being
extraordinarily high or low.  Which is to say, they are NOT
Missing Not At Random (MNAR).

No observations were discarded and no values were imputed in this
dataset because the raw data contained no missing values.

## Disclosure

I've used ChatGPT to walk me through this, as time is growing increasingly precious and it has been made clear that the concepts are what matter here.