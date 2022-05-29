#!/bin/bash
#
python3 process_1.py 10000001 15000 >> output1.txt &
python3 process_1.py 10000002 15000 >> output2.txt &
python3 process_1.py 10000003 15000 >> output3.txt &
python3 process_1.py 10000004 15000 >> output4.txt &
python3 process_1.py 10000005 15000 >> output5.txt