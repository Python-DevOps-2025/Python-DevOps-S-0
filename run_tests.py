"""
Test runner for all tasks
Run all tests and provide a summary
"""

import unittest
import sys
import os

# Add src and tests directories to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests'))

def run_all_tests():
    """Run all test suites and return results."""
    
    # Discover and run all test files
    loader = unittest.TestLoader()
    tests_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests')
    suite = loader.discover(tests_dir, pattern='test_*.py')
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%" if result.testsRun > 0 else "N/A")
    
    if result.failures:
        print(f"\nFAILURES ({len(result.failures)}):")
        for test, traceback in result.failures:
            print(f"- {test}")
    
    if result.errors:
        print(f"\nERRORS ({len(result.errors)}):")
        for test, traceback in result.errors:
            print(f"- {test}")
    
    return result.wasSuccessful()


def run_individual_task_tests():
    """Run tests for each task individually."""
    tasks = [
        ("Task 1: List Statistics", "tests.test_task1"),
        ("Task 2: Filter Transform", "tests.test_task2"), 
        ("Task 3: Word Frequency", "tests.test_task3"),
        ("Task 4: Email Validator", "tests.test_task4"),
        ("Task 5: Number Parser", "tests.test_task5"),
        ("Task 6: Parentheses Checker", "tests.test_task6")
    ]
    
    print("Running individual task tests...")
    print("="*60)
    
    for task_name, test_module in tasks:
        print(f"\n{task_name}")
        print("-" * len(task_name))
        
        try:
            # Import and run specific test module
            suite = unittest.TestLoader().loadTestsFromName(test_module)
            runner = unittest.TextTestRunner(verbosity=1, stream=sys.stdout)
            result = runner.run(suite)
            
            status = "✓ PASSED" if result.wasSuccessful() else "✗ FAILED"
            print(f"Status: {status}")
            
        except Exception as e:
            print(f"Error running {test_module}: {e}")


if __name__ == "__main__":
    print("Python DevOps S-0 - Test Runner")
    print("="*60)
    
    if len(sys.argv) > 1 and sys.argv[1] == "individual":
        run_individual_task_tests()
    else:
        success = run_all_tests()
        sys.exit(0 if success else 1)