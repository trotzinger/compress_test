#!/bin/bash
# move one dir up! should be at same level as compress test, and of course the paths need to change
coverage run /home/trotzinger/compress_test/venv/bin/pytest --cov-report html --cov=/home/trotzinger/compress_test /home/trotzinger/compress_test/test_simple_compress.py;
lcov --capture --directory compress_test/ --output-file coverage.info;
genhtml coverage.info --output-directory HTMLout;
python -m http.server;
