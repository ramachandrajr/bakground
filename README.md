# bakground
A python script to run several background processes at once, and manage them well.

This script is in it's initial stages sorry for any inconvinience!

### Usage
1. To start the script:
```bash
$ python bakground.py
```

2. To run a command or run a process:
```bash
>> -c <bash command to run>
```

3. To show all process:
```bash
>> show
```

shows all the processes as a table
<table>
    |Index |Command    |State         |
    |------|-----------|--------------|
    |0     |\<cmd\>    |Running / done|
</table>


4. To kill a process:
```bash
>> -k <index number>


