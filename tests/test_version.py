import re

def test_version(script_runner):
    ret = script_runner.run('pdf-toc', '--version')
    assert ret.success
    assert re.match(r'^pdf-toc \d+\.\d+\.\d+', ret.stdout)
    assert ret.stderr == ''
