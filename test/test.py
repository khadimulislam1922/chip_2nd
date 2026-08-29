import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles, FallingEdge

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting Counter Test")

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Reset")
    dut.rst_n.value = 0  
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1  

    dut._log.info("Checking counter behavior")
    
    await ClockCycles(dut.clk, 3)
    await FallingEdge(dut.clk) # লজিক গেট সেটেল হওয়ার জন্য অপেক্ষা
    
    assert int(dut.uo_out.value) == 3
    
    dut._log.info("Test passed successfully!")
