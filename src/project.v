`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    reg [3:0] count;
    assign uo_out = {4'b0000, count};

    always @(posedge clk) begin
        if (!rst_n)
            count <= 4'b0000;
        else
            count <= count + 1;
    end

endmodule
