from cmd_args import parse_cmd_args


def test_parse_cmd_args():
    result = parse_cmd_args(['hello', 'world'])
    assert result.IMAGE == 'hello'
    assert result.DESTINATION == 'world'
    assert result.annotate == False
