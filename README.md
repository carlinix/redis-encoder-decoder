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
