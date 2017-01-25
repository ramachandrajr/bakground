import subprocess, time, math, re, shlex, signal, os, signal

procs = []



# ==========
# OBJECTS AND CONSTRUCTORS
# ==========

# Process Object constructor.
class Proc:
    proc_id = 0
    proc_cmd = ""
    proc_time_stamp = time.time()
    proc_object = ""
    proc_state = "running"
    def __init__(self, cmd, proc_obj):
        self.proc_object = proc_obj
        self.proc_id = proc_obj.pid
        self.proc_cmd = cmd
        
    def save(self):
        """This function Inserts all the above data into an array."""
        procs.append(self)
    
    def poll(self):
        if ((self.proc_state == "running") & (self.proc_object.poll() != None)):
            self.proc_state = "done"
            return "done"
        else:
            pass
     
     

# ==========     
# FUNCTIONS
# ==========    
     
# Show all processes.        
def view_procs():
    """Shows all the processes that are running."""
    remove_dead()
    print "%10s %40s %10s" % ( "Index", "Command", "State" )
    for i in range(len(procs)):
        print "%10d %40s %10s" % ( i, procs[i].proc_cmd, procs[i].proc_state )

# Remove dead processes.
def remove_dead():
    """Removes any finished processes."""
    for proc in procs:
        if (proc.poll() == "done"):
            pass
            # del procs[proc]
 


# Kill a specific process.        
def kill_proc(i):
    """Kills the process at this certain index."""
    if (len(procs) > 0):
        procs[i].proc_object.terminate()
        procs[i].proc_object.kill()
        # os.kill(procs[i].proc_id, 0)

# Get Output of a Process.
def get_op(i):
    """Gets the output of a process."""
    if (len(procs) > 0):
        print procs[i].proc_object.stdout.read()


# ==========
# START BACKGROUND PROCESS
# ==========

# Incase we want to start a background process.
def start(cmd):
    """Starts a subprocess by using subprocess.Popen and returns the created object."""

    # subprocess.Popen(args, bufsize=0, executable=None,
    # stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False,
    # shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None,
    # creationflags=0);
    
    cmd = shlex.split(cmd)
    sp = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    sp._internal_poll(_deadstate='dead') 
    # Create a new Subprocess and Proc object.
    proc_0 = Proc(cmd, sp)
    # Saves data to the procs array.
    proc_0.save()


    

    
# ==========
# REAL SCRIPT STARTS HERE
# ==========

# Deal with inputs.
while True:
    inp = raw_input(">> ")
    if (inp == "exit"):
        break
    elif ("-c" in inp):
        m = re.search("^-c (.+?)$", inp)
        print "Starting a new process %s" % m.group(1)
        start(m.group(1))
    elif (inp == "show"):
        view_procs()
    elif ("-k" in inp):
        m = re.search("^-k (\d+)$", inp)
        print "Killing process %d" % procs[int(m.group(1))].proc_id
        kill_proc(int(m.group(1)))
    elif ("-o" in inp):
        m = re.search("^-o (\d+)$", inp)
        print "Output of process %d" % procs[int(m.group(1))].proc_id
        get_op(int(m.group(1)))
    else:
        pass
