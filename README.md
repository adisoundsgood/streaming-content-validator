# Streaming Content Validator

[![Python CI](https://github.com/adisoundsgood/streaming-content-validator/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/adisoundsgood/streaming-content-validator/actions/workflows/python-app.yml)

## Overview

My objective was to create a simple test automation framework that validates a list of content from a mock streaming service (or API) to ensure data consistency and accuracy. This simulates a real-world scenario of testing backend APIs and services in a streaming platform.

## Features Implemented

1. Mock API for Streaming Content:
- Use Flask or Django to build a basic API that serves streaming content data (e.g., show names, genres, episode counts, etc.).
- You could use a small dataset representing various content categories like sports, entertainment, and news to align with Disney+ and ESPN+.
Automated Testing:

2. Use PyTest or unittest to automate testing for:
- Correct data structure validation (e.g., all fields like title, genre, and episodes are present).
- Data accuracy checks (e.g., ensuring the number of episodes is an integer).
- API response times.
  
3. Test Coverage Reporting:
- Implement test coverage reporting using pytest-cov or a similar tool to track code coverage.
  
4. Continuous Integration (Optional):
- Set up a basic CI pipeline using GitHub Actions to run your tests on every code push.

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
