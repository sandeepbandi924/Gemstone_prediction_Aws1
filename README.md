# Gemstone Prediction using AWS

## Overview
This project focuses on predicting the type of gemstone based on given features using machine learning. The model is deployed on AWS to provide predictions via a cloud-based API.

## Features
- Data Preprocessing and Feature Engineering
- Machine Learning Model Training
- Model Deployment on AWS
- API Integration for Predictions

## Tech Stack
- **Programming Language:** Python
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **Model Deployment:** AWS Lambda, AWS API Gateway
- **Web Framework:** FastAPI
- **Version Control:** GitHub

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/sandeepbandi924/Gemstone_prediction_Aws1.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Gemstone_prediction_Aws1
   ```
3. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Train the model:
   ```sh
   python train.py
   ```
2. Run the FastAPI server:
   ```sh
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```
3. Access the API:
   - Open `http://localhost:8000/docs` to test the API endpoints.

## AWS Deployment
1. Package the model and dependencies for AWS Lambda.
2. Deploy the Lambda function using AWS SAM or the AWS Console.
3. Configure API Gateway to expose the endpoint.

## API Endpoints
- `POST /predict` - Takes gemstone features as input and returns the predicted type.

## Contributing
Feel free to fork this repository, submit issues, or make pull requests to improve the project.

## License
This project is licensed under the MIT License.

## Author
[Sandeep Bandi](https://github.com/sandeepbandi924)

