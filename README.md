# compress_test

REQUIRES:

    #c coverage requires:
    sudo apt install lcov
    #python requires:
    pip3 install pytest
    pip3 install pytest-cov
    
    
To build shared library (.so) with ability to see c coverage:


     cc -fprofile-arcs -ftest-coverage -fPIC -shared -lgcov -o simple_compress.so simple_compress.c

To run tests and generate HTML coverage including for C code:
    
    move the script "compress_test_and_report.sh" up one dir, then rename the paths to match your filesystem, then run.
    
If the script is not working, the following are the steps:
        
    from 1 dir up from compress_test:
    $> coverage run --source=compress_test /home/trotzinger/compress_test/venv/bin/pytest --cov-report html --cov=compress_test compress_test/test_simple_compress.py
    $> lcov --capture --directory compress_test/ --output-file coverage.info
    $> genhtml coverage.info --output-directory HTMLout
    $> python -m http.server #(navigate to HTMLout to view C coverage)
    
