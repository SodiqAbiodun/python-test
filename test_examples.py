#!/usr/bin/env python3
"""
Example test cases for the predictor script.
Run this to test various scenarios.
"""

from test_predictor import predict_time
import json

def test_case(name: str, prompt: str):
    """Run a single test case and print results."""
    print(f"\n{'='*60}")
    print(f"TEST: {name}")
    print(f"Prompt: {prompt}")
    print('='*60)
    
    try:
        result = predict_time(prompt)
        print(f"✓ SUCCESS")
        print(f"  Estimated Duration: {result['estimatedDuration']} hours")
        print(f"  Bedrooms: {result['bedrooms']}")
        print(f"  Bathrooms: {result['bathrooms']}")
        print(f"  Confidence: {result['confidence']}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {str(e)}")
        return False

def main():
    """Run all test cases."""
    print("Running predictor test cases...\n")
    
    test_cases = [
        ("Valid request with all details", 
         "Clean a 3 bedroom, 2 bathroom house with 1500 sq ft"),
        
        ("Deep clean request", 
         "Deep clean a 4 bedroom, 3 bathroom house with 2000 sq ft"),
        
        ("Missing bedrooms", 
         "Clean a 2 bathroom house with 1200 sq ft"),
        
        ("Missing bathrooms", 
         "Clean a 3 bedroom house with 1500 sq ft"),
        
        ("Missing square footage", 
         "Clean a 3 bedroom, 2 bathroom house"),
    ]
    
    results = []
    for name, prompt in test_cases:
        success = test_case(name, prompt)
        results.append((name, success))
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print('='*60)
    passed = sum(1 for _, success in results if success)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    for name, success in results:
        status = "✓" if success else "✗"
        print(f"  {status} {name}")

if __name__ == '__main__':
    main()

