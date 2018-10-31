# FileFifo
Persistent threadsafe buffer in python3.

Interthread communication persistent across executions and reboots

# demo
~~~~
$python3 filefifo.py
~~~~

# details
1. Contructor: FileFifo("file.txt")
1. Methods: append() appendleft() popleft()
1. doesn't work in multiprocessing (would require os level mutexes)

