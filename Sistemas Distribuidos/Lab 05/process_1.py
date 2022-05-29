
import sys
from ProcessOne import ProcessOne


process = ProcessOne(sys.argv[1], sys.argv[2])
process.send_message()
process.wait_callback()