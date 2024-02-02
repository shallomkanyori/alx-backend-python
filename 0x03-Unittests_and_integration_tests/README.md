# Unit tests and Integration Test

## Tasks

### Task 0
File: [test_utils.py](test_utils.py)
Write the first unit test for `utils.access_nested_map`

Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.

Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.

Decorate the method with `@parameterized.expand` to test the function for following inputs:
```
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
```
For each of these inputs, test with `assertEqual` that the function returns the expected result.

The body of the test method should not be longer than 2 lines.

### Task 1
File: [test_utils.py](test_utils.py)
Implement `TestAccessNestedMap.test_access_nested_map_exception`. Use the `assertRaises` context manager to test that a `KeyError` is raised for the following inputs (use `@parameterized.expand`):
```
nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
```
Also make sure that the exception message is as expected.

### Task 2
File: [test_utils.py](test_utils.py)
Define the `TestGetJson(unittest.TestCase`) class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result.

Use `unittest.mock.patch` to patch `requests.get`. Make sure it returns a `Mock` object with a `json` method that returns `test_payload` which you parametrize alongside the `test_url` that you will pass to `get_json` with the following inputs:
```
test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
```

Test that the mocked `get` method was called exactly once (per input) with `test_url` as argument.
Test that the output of `get_json` is equal to `test_payload`.

### Task 3
File: [test_utils.py](test_utils.py)
Implement the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method.

Inside `test_memoize`, define following class
```
class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()
```

Use `unittest.mock.patch` to mock `a_method`. Test that when calling `a_property` twice, the correct result is returned but `a_method` is only called once using `assert_called_once`.

### Task 4
File: [test_client.py](test_client.py)
Declare the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method.
This method should test that `GithubOrgClient.org` returns the correct value.

Use `@patch` as a decorator to make sure `get_json` is called once with the expected argument but make sure it is not executed.
Use `@parameterized.expand` as a decorator to parametrize the test with a couple of `org` examples to pass to `GithubOrgClient`, in this order:
- `google`
- `abc`

Of course, no external HTTP calls should be made.
