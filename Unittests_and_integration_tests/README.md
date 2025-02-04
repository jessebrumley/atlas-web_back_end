# Unittests and Integration Tests

## Master

## Description
Unit testing ensures that a specific function returns expected results for different inputs. A unit test should cover both standard inputs and edge cases, testing only the logic inside the function. Calls to other functions should be mocked, especially if they involve network or database access.

Integration tests evaluate a code path end-to-end, verifying the interactions between components. Only low-level functions making external calls (e.g., HTTP requests, file I/O, database I/O) are typically mocked.

### Running Tests
Execute tests using:
```sh
python -m unittest path/to/test_file.py
```

## Resources
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — Mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/51126828)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives
By the end of this project, you should be able to:
- Explain the difference between unit and integration tests.
- Apply common testing patterns such as mocking, parameterization, and fixtures.

## Requirements
- All files should be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.9**.
- Files must follow **pycodestyle** (version 2.5).
- All files should be executable.
- All modules, classes, and functions must include documentation.
- Functions and coroutines must be type-annotated.

## Required Files
- `utils.py`
- `client.py`
- `fixtures.py`

## Tasks
### 0. Parameterize a Unit Test
Write unit tests for `utils.access_nested_map` using `@parameterized.expand` with various input cases. Use `assertEqual` to verify outputs.

**File:** `test_utils.py`

### 1. Test Exception Handling
Test `utils.access_nested_map` for `KeyError` exceptions using `assertRaises` and parameterized inputs.

**File:** `test_utils.py`

### 2. Mock HTTP Calls
Mock `requests.get` using `unittest.mock.patch` to test `utils.get_json` without making real HTTP requests.

**File:** `test_utils.py`

### 3. Memoization Test
Test `utils.memoize` to ensure method calls are cached. Use `assert_called_once` to verify memoization behavior.

**File:** `test_utils.py`

### 4. Mocking with Decorators
Test `client.GithubOrgClient.org` by patching `get_json`. Use parameterized organization names.

**File:** `test_client.py`

### 5. Mocking a Property
Patch `GithubOrgClient.org` to test `_public_repos_url` behavior with controlled payloads.

**File:** `test_client.py`

### 6. More Patching
Test `GithubOrgClient.public_repos` by mocking `_public_repos_url` and `get_json` using decorators and context managers.

**File:** `test_client.py`

### 7. Parameterize License Checks
Parameterize `GithubOrgClient.has_license` to validate repo license checks.

**File:** `test_client.py`

### 8. Integration Test: Fixtures
Use `@parameterized_class` to set up fixtures for `GithubOrgClient.public_repos`. Mock `requests.get` for integration testing.

**File:** `test_client.py`

### Author
[Jesse Brumley](https://github.com/jessebrumley)