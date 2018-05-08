# Testing-python
Model Python test codes for Advitiy

Testing is performed using `unittest` library of python. Please install it beforehand if it's not already installed.
(https://docs.python.org/2/library/unittest.html#module-unittest)
Data files for testcases are in directory test-data. The data file for each test is of type `.json`. The data has to be added in the `list` format. 
In order to run test for multiple data values, `ddt` module is used. It can be installed by
<pre><code>pip install ddt
</code></pre>
The documentation and some useful examples for use of `ddt`. Especially check
(http://ddt.readthedocs.io/en/latest/index.html)
(https://stackoverflow.com/questions/21990561/unittest-run-the-same-test-for-a-list-of-inputs-and-outputs)

testcode can be simply run using `python test_frames.py`
