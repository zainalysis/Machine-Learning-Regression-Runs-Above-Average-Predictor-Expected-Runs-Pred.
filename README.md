# Runs Above Average Predictor: Expected Runs

### Developed by Zain Ul Hassan (@zainalysis)

## Overview

The **Runs Above Average Predictor** is a machine learning application designed to predict expected runs in T20 cricket matches. By analyzing ball-by-ball data, this tool helps in assessing player performance and strategizing for future matches.

## Features

- **Real-time Predictions**: Get expected runs for a given ball based on current match conditions.
- **Interactive User Interface**: Built with Streamlit for a smooth user experience.
- **Comprehensive Analysis**: Analyze batting performance using advanced metrics.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- Required Python libraries listed in `requirements.txt`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/zainalysis/Runs-Above-Average-Predictor-Expected-Runs-Pred.git
cd Runs-Above-Average-Predictor-Expected-Runs-Pred
pip install -r requirements.txt
streamlit run app.py
**Input Variables**
The model predicts expected runs based on the following input variables:

_inns_rr: Innings run rate
inns_wkts: Number of wickets lost in the innings
inns_balls_rem: Balls remaining in the innings
nth_ball: Current ball number in the innings (calculated as 120 - inns_balls_rem)_

**Output**
The application provides a predicted total of expected runs as a floating-point value based on the input parameters.

**Model Details**
The model is built using Keras and saved in the Joblib format. Ensure that the required model file is available in the specified path when deploying the app.

**Contributions**
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or fixes.

**License**
This project is licensed under the MIT License.

**Acknowledgments**
Thanks to the open-source community specially Mr. Himanish Ganjoo for their valuable contributions and support.

**Link To The Application**
https://runs-above-average-predictor-expected-runs-byzainalysis.streamlit.app/
