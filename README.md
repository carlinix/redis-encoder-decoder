# RedisEncoderDecoder Utility Module

A utility module for encoding and decoding dictionaries with JSON values for use with Redis.

## Overview

The `RedisEncoderDecoder` module provides a convenient way to encode and decode dictionaries with JSON values. This is particularly useful when working with Redis, where values are often stored as strings. By using JSON serialization, complex data types such as dictionaries and lists can be easily stored and retrieved from Redis.

## Features

- **Encode dictionaries to JSON strings**: Convert dictionary values to JSON formatted strings for easy storage in Redis.
- **Decode JSON strings to original data types**: Convert JSON formatted strings back to their original data types.
- **Error Handling**: Gracefully handle non-serializable values and invalid JSON strings with proper logging.

## Installation

To install the module, use Poetry:

```bash
poetry add redis-encoder-decoder
```

## Usage

### Encoding a Dictionary

```python
from redis_encoder_decoder import RedisEncoderDecoder

dictionary = {'key1': {'nested_key': 42}, 'key2': 'value', 'key3': [1, 2, 3]}
encoded_dict = RedisEncoderDecoder.encoder(dictionary)
print(encoded_dict)
# Output: {'key1': '{"nested_key": 42}', 'key2': 'value', 'key3': '[1, 2, 3]'}
```

### Decoding a Dictionary

```python
from redis_encoder_decoder import RedisEncoderDecoder

encoded_dict = {'key1': '{"nested_key": 42}', 'key2': 'value', 'key3': '[1, 2, 3]'}
decoded_dict = RedisEncoderDecoder.decoder(encoded_dict)
print(decoded_dict)
# Output: {'key1': {'nested_key': 42}, 'key2': 'value', 'key3': [1, 2, 3]}
```

## Benefits

### JSON Serialization for Redis

Redis is a powerful in-memory data structure store commonly used as a database, cache, and message broker. However, it stores all values as strings, which can be limiting when dealing with complex data types. The `RedisEncoderDecoder` module addresses this limitation by serializing Python dictionaries and other complex data types into JSON strings, making it easy to store and retrieve these types from Redis.

### Error Handling

The module includes robust error handling to manage cases where values are not JSON serializable or JSON strings are invalid. It logs warnings and retains original values, ensuring that data integrity is maintained even when issues arise.

## Contributing

We welcome contributions to improve the `RedisEncoderDecoder` module! Here are some ways you can contribute:

1. **Report Bugs**: If you encounter any issues, please report them using the GitHub issue tracker.

2. **Submit Pull Requests**: If you have an improvement or a fix, submit a pull request. Please ensure your code follows the existing coding style and passes all tests.

3. **Write Tests**: Help us improve the module's robustness by writing tests. Make sure your tests cover edge cases and different scenarios.

4. **Improve Documentation**: If you find any part of the documentation unclear or incomplete, feel free to suggest changes or add more details.

### Steps to Contribute

1. **Fork the Repository**: Create a fork of the repository on GitHub.

2. **Clone Your Fork**: Clone your fork to your local machine.

    ```bash
    git clone https://github.com/yourusername/redis-encoder-decoder.git
    cd redis-encoder-decoder
    ```

3. **Create a Branch**: Create a new branch for your feature or bugfix.

    ```bash
    git checkout -b feature-name
    ```

4. **Install Dependencies**: Use Poetry to install the project dependencies.

    ```bash
    poetry install
    ```

5. **Make Changes**: Implement your changes.

6. **Run Tests**: Ensure all tests pass.

    ```bash
    poetry run pytest --cov=redis_encoder_decoder tests/
    ```

7. **Commit and Push**: Commit your changes and push them to your fork.

    ```bash
    git add .
    git commit -m "Description of your changes"
    git push origin feature-name
    ```

8. **Submit a Pull Request**: Go to the original repository and submit a pull request.

We appreciate your contributions and are excited to see what you will improve!

## License

This project is licensed under the LGPL v2.1 License - see the [LICENSE](LICENSE) file for details.
