import pytest
from redis_encdec.redis_encoder_decoder import RedisEncoderDecoder


def test_encoder():
    input_dict = {"a": [1, 2, 3], "b": {"c": "d"}}
    expected_output = {'a': '[1, 2, 3]', 'b': '{"c": "d"}'}
    assert RedisEncoderDecoder.encoder(input_dict) == expected_output


def test_decoder():
    input_dict = {'a': '[1, 2, 3]', 'b': '{"c": "d"}'}
    expected_output = {"a": [1, 2, 3], "b": {"c": "d"}}
    assert RedisEncoderDecoder.decoder(input_dict) == expected_output
