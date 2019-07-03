from cmd_args import parse_cmd_args


def test_parse_cmd_args():
    result = parse_cmd_args(['hello'])
    assert result.IMAGE == 'hello'
    assert result.output is None
    assert result.annotate
    assert result.terms is None
    assert result.iterations is None


def test_parse_cmd_args_output():
    result = parse_cmd_args(['hello', '--output=file.jpg'])
    assert result.output == 'file.jpg'


def test_parse_cmd_args_annotate():
    result = parse_cmd_args(['hello', '--notext'])
    assert not result.annotate


def test_parse_cmd_args_terms():
    result = parse_cmd_args(['hello', '--terms=23'])
    assert result.terms == 23


def test_parse_cmd_args_iterations():
    result = parse_cmd_args(['hello', '--iterations=11'])
    assert result.iterations == 11
