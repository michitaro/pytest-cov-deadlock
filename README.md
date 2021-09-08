## Reproduction code for pytest-cov deadlock

When the option `--cov` is specified, `multiprocessing.Process.join` causes a deadlock occationally in a pytest session.

## Installation

```bash
mkdir .venv
pipenv --python $HOME/miniconda/envs/py39/bin/python
pipenv install
```

## Environment

Python 3.8 & 3.9 on Linux. On Mac, the problem does not occur.

```bash
$ ./.venv/bin/pip list
Package    Version
---------- -------
attrs      21.2.0
coverage   5.5
iniconfig  1.1.1
packaging  21.0
pip        21.0.1
pluggy     1.0.0
py         1.10.0
pyparsing  2.4.7
pytest     6.2.5
pytest-cov 2.12.1
setuptools 52.0.0
toml       0.10.2
wheel      0.36.2
```

```bash
$ ./.venv/bin/python --version
Python 3.9.6
```

```bash
$ ./.venv/bin/pytest --version
pytest 6.2.5
```

## Run the test

### Without `--cov`, the test passes.
```
$ pipenv run pytest
============================= test session starts =============================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /mnt/das02/michitaro/work/pytest-cov-bug
plugins: cov-2.12.1
collected 1 item

test_test.py .                                                          [100%]

============================== 1 passed in 1.40s ==============================
```

### With `--cov`, the test fails.

```
$ pipenv run pytest --cov
============================= test session starts =============================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /mnt/das02/michitaro/work/pytest-cov-bug
plugins: cov-2.12.1
collected 1 item

test_test.py F                                                          [100%]

================================== FAILURES ===================================
__________________________________ test_main __________________________________

    def test_main():
        for i in range(200):
            run_thread()
            if len(errors) > 0:
>               raise RuntimeError(f'join timeout occured in trial {i}')
E               RuntimeError: join timeout occured in trial 11

test_test.py:33: RuntimeError

----------- coverage: platform linux, python 3.9.6-final-0 -----------
Name                                                                         Stmts   Miss  Cover
------------------------------------------------------------------------------------------------
.venv/lib/python3.9/site-packages/_pytest/_argcomplete.py                       37     36     3%
.venv/lib/python3.9/site-packages/_pytest/_code/code.py                        699    489    30%
.venv/lib/python3.9/site-packages/_pytest/_code/source.py                      142     91    36%
.venv/lib/python3.9/site-packages/_pytest/_io/terminalwriter.py                113     65    42%
.venv/lib/python3.9/site-packages/_pytest/_io/wcwidth.py                        25     16    36%
.venv/lib/python3.9/site-packages/_pytest/assertion/__init__.py                 84     73    13%
.venv/lib/python3.9/site-packages/_pytest/assertion/rewrite.py                 626    504    19%
.venv/lib/python3.9/site-packages/_pytest/cacheprovider.py                     314    266    15%
.venv/lib/python3.9/site-packages/_pytest/capture.py                           560    481    14%
.venv/lib/python3.9/site-packages/_pytest/compat.py                            162    129    20%
.venv/lib/python3.9/site-packages/_pytest/config/__init__.py                   806    692    14%
.venv/lib/python3.9/site-packages/_pytest/config/argparsing.py                 253    208    18%
.venv/lib/python3.9/site-packages/_pytest/debugging.py                         228    219     4%
.venv/lib/python3.9/site-packages/_pytest/deprecated.py                         16     15     6%
.venv/lib/python3.9/site-packages/_pytest/doctest.py                           351    341     3%
.venv/lib/python3.9/site-packages/_pytest/faulthandler.py                       64     46    28%
.venv/lib/python3.9/site-packages/_pytest/fixtures.py                          833    709    15%
.venv/lib/python3.9/site-packages/_pytest/helpconfig.py                        133    123     8%
.venv/lib/python3.9/site-packages/_pytest/junitxml.py                          373    371     1%
.venv/lib/python3.9/site-packages/_pytest/logging.py                           402    294    27%
.venv/lib/python3.9/site-packages/_pytest/main.py                              461    287    38%
.venv/lib/python3.9/site-packages/_pytest/mark/__init__.py                     141    126    11%
.venv/lib/python3.9/site-packages/_pytest/mark/structures.py                   244    227     7%
.venv/lib/python3.9/site-packages/_pytest/monkeypatch.py                       171    158     8%
.venv/lib/python3.9/site-packages/_pytest/nodes.py                             271    173    36%
.venv/lib/python3.9/site-packages/_pytest/nose.py                               22     11    50%
.venv/lib/python3.9/site-packages/_pytest/pastebin.py                           70     69     1%
.venv/lib/python3.9/site-packages/_pytest/pathlib.py                           338    279    17%
.venv/lib/python3.9/site-packages/_pytest/python.py                            851    677    20%
.venv/lib/python3.9/site-packages/_pytest/reports.py                           279    244    13%
.venv/lib/python3.9/site-packages/_pytest/runner.py                            299    161    46%
.venv/lib/python3.9/site-packages/_pytest/setuponly.py                          56     54     4%
.venv/lib/python3.9/site-packages/_pytest/setupplan.py                          24     22     8%
.venv/lib/python3.9/site-packages/_pytest/skipping.py                          178    146    18%
.venv/lib/python3.9/site-packages/_pytest/stepwise.py                           68     67     1%
.venv/lib/python3.9/site-packages/_pytest/store.py                              34     27    21%
.venv/lib/python3.9/site-packages/_pytest/terminal.py                          897    682    24%
.venv/lib/python3.9/site-packages/_pytest/threadexception.py                    44     29    34%
.venv/lib/python3.9/site-packages/_pytest/tmpdir.py                            117    102    13%
.venv/lib/python3.9/site-packages/_pytest/unittest.py                          243    234     4%
.venv/lib/python3.9/site-packages/_pytest/unraisableexception.py                44     29    34%
.venv/lib/python3.9/site-packages/_pytest/warnings.py                           63     44    30%
.venv/lib/python3.9/site-packages/_virtualenv.py                                81     80     1%
.venv/lib/python3.9/site-packages/pluggy/_callers.py                            40     10    75%
.venv/lib/python3.9/site-packages/pluggy/_hooks.py                             156     92    41%
.venv/lib/python3.9/site-packages/pluggy/_manager.py                           190    148    22%
.venv/lib/python3.9/site-packages/pluggy/_result.py                             30     22    27%
.venv/lib/python3.9/site-packages/pluggy/_tracing.py                            41     31    24%
.venv/lib/python3.9/site-packages/py/_builtin.py                               112     78    30%
.venv/lib/python3.9/site-packages/py/_code/__init__.py                           0      0   100%
.venv/lib/python3.9/site-packages/py/_code/code.py                             531    408    23%
.venv/lib/python3.9/site-packages/py/_error.py                                  52     47    10%
.venv/lib/python3.9/site-packages/py/_path/common.py                           277    211    24%
.venv/lib/python3.9/site-packages/py/_path/local.py                            694    616    11%
.venv/lib/python3.9/site-packages/py/_vendored_packages/apipkg/__init__.py     152    129    15%
.venv/lib/python3.9/site-packages/pytest/collect.py                             21     19    10%
.venv/lib/python3.9/site-packages/pytest_cov/compat.py                          21     17    19%
.venv/lib/python3.9/site-packages/pytest_cov/embed.py                           80     73     9%
.venv/lib/python3.9/site-packages/pytest_cov/engine.py                         238    217     9%
.venv/lib/python3.9/site-packages/pytest_cov/plugin.py                         209    191     9%
test_test.py                                                                    23      0   100%
------------------------------------------------------------------------------------------------
TOTAL                                                                        14084  11405    19%

=========================== short test summary info ===========================
FAILED test_test.py::test_main - RuntimeError: join timeout occured in trial 11
============================== 1 failed in 3.58s ==============================
^CError in atexit._run_exitfuncs:
Traceback (most recent call last):
  File "/home/michitaro/anaconda3/envs/py39/lib/python3.9/multiprocessing/popen_fork.py", line 27, in poll
    pid, sts = os.waitpid(self.pid, flag)
KeyboardInterrupt
```
