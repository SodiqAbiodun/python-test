#!/usr/bin/env python3
"""
Python version of the time predictor for testing purposes.
This script replicates the functionality of src/predictor.ts
"""

import os
import sys
from typing import Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError('OPENAI_API_KEY is not defined in environment variables')

openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def predict_time(prompt: str) -> Dict:
    """
    Predict cleaning time based on a prompt.
    
    Args:
        prompt: The user's cleaning request prompt
        
    Returns:
        Dictionary containing:
        - estimatedDuration: float
        - bedrooms: int
        - bathrooms: int
        - confidence: float
        - rawResponse: str
    """
    try:
        # Create the completion request
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {
                    "role": "system",
                    "content": """You are a precise time estimation assistant for cleaning services. Your task is to extract number of bedrooms, bathrooms and size of square footage from prompt and estimate how long a given cleaning task will take in hours and minutes. 

Rules:
- If number of bedrooms or the number of bathrooms or the square footage size is not specified, then respond with a text that says "Your request is incomplete. Please provide the number of bedrooms, bathrooms, and the square footage to proceed"
- Final response should be with only the final duration in hours and minutes, no other text or information. Always give numerical values not string and for deep clean make the final value equal to the sum of estimated duration plus 2 hours.


Example responses:
- 2.0 for two hours
- 1.5 for one and a half hours
- 3.25 for three hours and 15 minutes"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response = completion.choices[0].message.content
        if response:
            response = response.strip()
        
        print(f'Model Response: {response}')
        print(f'Response type: {type(response)}')

        if response and 'specify the' in response:
            raise ValueError('Your request is incomplete. Please provide the number of bedrooms, bathrooms, and the square footage to proceed.')

        estimated_duration = response or 0
        bedrooms = int('3')  # Hardcoded for testing, matching TypeScript version
        bathrooms = int('3')  # Hardcoded for testing, matching TypeScript version

        try:
            estimated_duration = float(estimated_duration)
        except (ValueError, TypeError):
            raise ValueError('Invalid numeric values received from model')

        return {
            'estimatedDuration': float(estimated_duration),
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'confidence': 0.95,
            'rawResponse': response
        }
    
    except ValueError as e:
        # Re-throw validation errors
        if 'Invalid estimation' in str(e) or 'Please specify' in str(e):
            raise
        raise ValueError(f'Failed to generate prediction: {str(e)}')
    except Exception as e:
        error_msg = str(e)
        print(f'Error in prediction: {error_msg}')
        
        # Re-throw with more specific error messages
        if 'API key' in error_msg or 'authentication' in error_msg.lower():
            raise ValueError('OpenAI API key is invalid or missing')
        
        raise ValueError(f'Failed to generate prediction: {error_msg}')


def main():
    """Main function for command-line testing."""
    if len(sys.argv) < 2:
        print("Usage: python test_predictor.py <prompt>")
        print("\nExample:")
        print('  python test_predictor.py "Clean a 3 bedroom, 2 bathroom house with 1500 sq ft"')
        sys.exit(1)
    
    prompt = ' '.join(sys.argv[1:])
    
    try:
        result = predict_time(prompt)
        print("\n" + "="*50)
        print("PREDICTION RESULT:")
        print("="*50)
        print(f"Estimated Duration: {result['estimatedDuration']} hours")
        print(f"Bedrooms: {result['bedrooms']}")
        print(f"Bathrooms: {result['bathrooms']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Raw Response: {result['rawResponse']}")
        print("="*50)
    except Exception as e:
        print(f"\nERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

