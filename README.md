# Python Test - Time Predictor

A Python testing project for a cleaning service time predictor that uses OpenAI's GPT-4o-mini model to estimate cleaning duration based on property details (bedrooms, bathrooms, square footage).

## Prerequisites

- Python 3.7 or higher
- OpenAI API key
- pip (Python package installer)

## Project Structure

```
python-test/
├── test_predictor.py      # Main predictor implementation
├── test_examples.py       # Test cases and examples
├── requirements_test.txt  # Python dependencies
├── .env                   # Environment variables (not in git)
└── README.md             # This file
```

## Setup Instructions

### 1. Create a Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

Once your virtual environment is activated, install the required packages:

```bash
pip install -r requirements_test.txt
```

This will install:
- `openai>=1.0.0` - OpenAI API client
- `python-dotenv>=1.0.0` - Environment variable management

### 3. Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
# Create .env file
touch .env  # On Windows: type nul > .env
```

Add your OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

**Note:** The `.env` file is already in `.gitignore` to prevent committing sensitive information.

## Running Tests

### Run All Test Cases

To run all example test cases:

```bash
python test_examples.py
```

This will execute multiple test scenarios including:
- Valid requests with all details
- Deep clean requests
- Missing information scenarios

### Run Individual Predictions

To test the predictor with a custom prompt:

```bash
python test_predictor.py "Clean a 3 bedroom, 2 bathroom house with 1500 sq ft"
```

### Example Output

```
==================================================
PREDICTION RESULT:
==================================================
Estimated Duration: 2.5 hours
Bedrooms: 3
Bathrooms: 3
Confidence: 0.95
Raw Response: 2.5
==================================================
```

## Test Cases

The `test_examples.py` script includes the following test scenarios:

1. **Valid request with all details** - Complete property information
2. **Deep clean request** - Deep cleaning with all details (adds 2 hours)
3. **Missing bedrooms** - Tests error handling
4. **Missing bathrooms** - Tests error handling
5. **Missing square footage** - Tests error handling

## How It Works

The predictor:
1. Takes a cleaning request prompt as input
2. Uses OpenAI's GPT-4o-mini model to extract property details
3. Estimates cleaning duration based on bedrooms, bathrooms, and square footage
4. Returns structured data with estimated duration, property details, and confidence score

## Troubleshooting

### API Key Issues

If you encounter authentication errors:
- Verify your `OPENAI_API_KEY` is correctly set in the `.env` file
- Ensure there are no extra spaces or quotes around the API key
- Check that your OpenAI API key is valid and has sufficient credits

### Import Errors

If you get import errors:
- Make sure your virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements_test.txt`
- Check that you're using Python 3.7 or higher: `python --version`

### Missing Information Errors

The predictor requires:
- Number of bedrooms
- Number of bathrooms
- Square footage

If any of these are missing, the predictor will raise a `ValueError` asking for complete information.

## License

This is a test project for development and testing purposes.

