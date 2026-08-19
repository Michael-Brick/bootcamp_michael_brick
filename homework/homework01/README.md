# Equity Return and Treasury Yield Correlations
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement<1–2 paragraphs: what problem & why it matters>
In which economic sectors do the prices of equities demonstrate the most sensitivity to changes in treasury yields and interest rates?  Are there other factors or contexts that might affect that relative sensitivity?  This is important for the sake of establishing and understanding correlations between different shares’ price behavior, and therefore for the sake of identifying diversification benefits and performing effective portfolio management.  It is an interesting lens through which to gain understanding of the internal dynamics of particular industries and businesses, as it essentially reveals anticipated and perceived investment horizons and cash conversion cycles.
## Stakeholder & User
The ultimate stakeholders and proprietors would likely be fund managers and their investing clients, but would likely be used by back-office analysts and traders.  Because standard industry practice is to measure correlations and betas using a month as the most relevant unit of time, the correlations and betas would likely need to be updated in Bayesian fashion on a monthly basis in time for major strategic moves and asset allocation decisions to be reassessed.  
## Useful Answer & Decision
The useful answer will be mostly predictive but also causal, since understanding causality aids in prediction insofar as it helps establish the sequence.  If one phenomenon causes another phenomenon, it usually closely precedes that phenomenon quite closely.  If two phenomena are simply correlated with each other insofar as they tend to happen at the same time, that makes for less actionable predictions.  The product should present a kind of regression model and some form of variance or confidence interval establishing each industry’s price sensitivity with respect to yields and interest rates.  This confidence interval can take the form of the MAE and RMSE the model has historically returned.  
## Assumptions & Constraints
•	Daily price behavior of share price and yield behavior is quite easy to obtain going back as long as stocks have been listed on a given exchange. 
•	Data is updated and becomes available at least every 24 hours.  
•	More difficult to incorporate this model into an intraday trading strategy.  
•	Should not be any proprietary or legal concerns in using such publicly available information.  
•	A specific vendor may need to be identified. 
## Known Unknowns / Risks
•	Interest rate sensitivity may change over time.
•	Industries may not be so easy to define (blue around the edges).
•	Must make sure a sufficiently representative sample of companies is drawn for each industry, which are of dramatically different sizes.
•	May need to perform repeated bootstrapping analysis to confirm correlations remain similar within smaller sections of selected populations.
## Lifecycle Mapping
Goal → Stage → Deliverable- <Goal A> → Problem Framing & Scoping (Stage 01) → <Deliverable X>- ...
## Repo Plan
data/, src/, notebooks/, docs/ ; cadence for updates
