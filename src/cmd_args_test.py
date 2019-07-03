from cmd_args import parse_cmd_args


def test_parse_cmd_args():
    result = parse_cmd_args(['hello'])
    assert result.IMAGE == 'hello'
    assert result.output is None
    assert not result.annotate
    assert result.terms is None


def test_parse_cmd_args_output():
    result = parse_cmd_args(['hello', '--output=file.jpg'])
    assert result.output == 'file.jpg'


def test_parse_cmd_args_annotate():
    result = parse_cmd_args(['hello', '--annotate'])
    assert result.annotate


def test_parse_cmd_args_terms():
    result = parse_cmd_args(['hello', '--terms=23'])
    assert result.terms == 23
