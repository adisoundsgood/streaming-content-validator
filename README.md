# Streaming Content Validator

[![Python CI](https://github.com/adisoundsgood/streaming-content-validator/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/adisoundsgood/streaming-content-validator/actions/workflows/python-app.yml)

## Overview

My objective was to create a simple test automation framework that validates a list of content from a mock streaming service to ensure data consistency and accuracy. This simulates a real-world scenario of testing backend APIs and services in a streaming platform.

## Features Implemented

### 1. Mock API for Streaming Content ([app.py]((https://github.com/adisoundsgood/streaming-content-validator/blob/main/app.py))):
- Used Flask to build a basic API that serves streaming content data (show names, genres, episode counts).
- Used a small dataset representing various content categories such as sports and entertainment.

### 2. Use PyTest to automate testing for ([tests/test_api.py](https://github.com/adisoundsgood/streaming-content-validator/blob/main/tests/test_api.py)):
- Correct data structure validation (all fields (title, genre, and episodes) are present).
- Data accuracy checks (e.g., ensuring the number of episodes is an integer).
- API response times.
  
### 3. Test Coverage Reporting ([python-app.yml](https://github.com/adisoundsgood/streaming-content-validator/blob/main/.github/workflows/python-app.yml)):
- Implemented test coverage reporting using pytest-cov track code coverage.
- As per Github actions workflow, coverage reports are uploaded per code push/build.
  
### 4. Continuous Integration ([python-app.yml](https://github.com/adisoundsgood/streaming-content-validator/blob/main/.github/workflows/python-app.yml)):
- Set up a basic CI pipeline using GitHub Actions to run tests on every code push.

## Tools and Tech Stack:
- Python
- Flask (for API)
- PyTest (for automation)
- GitHub Actions (for CI)

## Getting Started

### Prerequisites

- Python 3.x
- `pip` for installing Python packages

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
