import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting Counter Test")

    # Set initial values
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    
    # Create a 10us clock
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset the counter
    dut._log.info("Reset")
    dut.rst_n.value = 0  # Active low reset
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1  # Stop reset

    dut._log.info("Checking counter behavior")
    
    # Wait for 3 clock cycles
    await ClockCycles(dut.clk, 3)
    
    # Since we waited 3 cycles, the counter should be exactly at 3
    assert dut.uo_out.value == 3
    
    dut._log.info("Test passed successfully!")
