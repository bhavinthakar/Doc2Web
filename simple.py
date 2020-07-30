import m5
from m5.objects import *

# Create a system
system = System()
print(system)

# Setup a clock domain
system.clk_domain=SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain=VoltageDomain()

# Setup memory mode
system.mem_mode='timing'
system.mem_ranges= [AddrRange('512MB')]

# Create a CPU
system.cpu= TimingSimpleCPU()

# Create a memory bus
system.membus = SystemXBar()

# Connect CPU to membus
system.cpu.icache_port=system.membus.slave
system.cpu.dcache_port=system.membus.slave 

# Create Interrupt Controller
system.cpu.createInterruptController()

system.system_port=system.membus.slave

# create a memory controller
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range=system.mem_ranges[0]
system.mem_ctrl.port=system.membus.master

# create a process
process =Process() 
process.cmd=['tests/test-progs/hello/bin/riscv/linux/hello']
system.cpu.workload= process 
system.cpu.createThreads()

root=Root(full_system=False, system=system)
m5.instantiate()

print("Beginning Simulation...")
exit_event=m5.simulate()

print("Exiting @ tick {} because {}".format(m5.curTick(),exit_event.getCause()))