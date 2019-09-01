from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform


_io = [
    ("clk25", 0, Pins("Y13"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("AB19"), IOStandard("LVCMOS33"),
            Misc("SLEW=FAST")),
        Subsignal("rx", Pins("AA21"), IOStandard("LVCMOS33"),
            Misc("SLEW=FAST"))),

    ("spiflash", 0,
        Subsignal("cs_n", Pins("T5")),
        Subsignal("clk", Pins("Y21")),
        Subsignal("mosi", Pins("AB20")),
        Subsignal("miso", Pins("AA20"), Misc("PULLUP")),
        Subsignal("wp", Pins("AA18")),
        IOStandard("LVCMOS33"), Misc("SLEW=FAST")),

    ("ddram_clock_a", 0,
        Subsignal("p", Pins("H20")),
        Subsignal("n", Pins("J19")),
        IOStandard("SSTL18_II")),
    ("ddram_a", 0,
        Subsignal("a", Pins("F21 F22 E22 G20 F20 K20 K19 E20 C20 C22 G19 F19 D22")),
        Subsignal("ba", Pins("J17 K17 H18")),
        Subsignal("cke", Pins("D21")),
        Subsignal("ras_n", Pins("H21")),
        Subsignal("cas_n", Pins("H22")),
        Subsignal("we_n", Pins("H19")),
        Subsignal(
            "dq", Pins("N20 N22 M21 M22 J20 J22 K21 K22 P21 P22 R20 R22 U20 U22 V21 V22")
        ),
        Subsignal("dqs", Pins("L20 T21"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("L22 T22"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dm", Pins("L19 M20")),
        Subsignal("odt", Pins("G22")),
        IOStandard("SSTL18_II")),

    ("ddram_clock_b", 0,
        Subsignal("p", Pins("H4")),
        Subsignal("n", Pins("H3")),
        IOStandard("SSTL18_II")),
    ("ddram_b", 0,
        Subsignal("a", Pins("H2 H1 H5 K6 F3 K3 J4 H6 E3 E1 G4 C1 D1")),
        Subsignal("ba", Pins("G3 G1 F1")),
        Subsignal("cke", Pins("D2")),
        Subsignal("ras_n", Pins("K5")),
        Subsignal("cas_n", Pins("K4")),
        Subsignal("we_n", Pins("F2")),
        Subsignal(
            "dq", Pins("N3 N1 M2 M1 J3 J1 K2 K1 P2 P1 R3 R1 U3 U1 V2 V1")
        ),
        Subsignal("dqs", Pins("L3 T2"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("L1 T1"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dm", Pins("L4 M3")),
        Subsignal("odt", Pins("J6")),
        IOStandard("SSTL18_II")),

    ("pano_button", 0, Pins("H12"), IOStandard("LVCMOS33")),

    ("led_red", 0, Pins("E12"), IOStandard("LVCMOS33"), Drive(8)),
    ("led_blue", 0, Pins("H13"), IOStandard("LVCMOS33"), Drive(8)),
    ("led_green", 0, Pins("F13"), IOStandard("LVCMOS33"), Drive(8)),

    ("eth_clocks", 0,
        Subsignal("gtx", Pins("AA12")),
        Subsignal("tx", Pins("Y11")),
        Subsignal("rx", Pins("AB11")),
        IOStandard("LVCMOS33")),
    ("eth", 0,
        Subsignal("rst_n", Pins("R11")),
        Subsignal("mdio", Pins("AA2")),
        Subsignal("mdc", Pins("AB6")),
        Subsignal("dv", Pins("Y7")),
        Subsignal("rx_er", Pins("Y8")),
        Subsignal("rx_data", Pins("Y3 Y4 R9 R7 V9 R8 U9 Y9")),
        Subsignal("tx_en", Pins("AA8")),
        Subsignal("tx_er", Pins("AB8")), # NC
        Subsignal("tx_data", Pins("AB2 AB3 AB4 AB7 AB9 AB10 T7 Y10")),
        Subsignal("col", Pins("V7")),
        Subsignal("crs", Pins("W4")),
        IOStandard("LVCMOS33")),

    ("i2c", 0,
        Subsignal("scl", Pins("E8")),
        Subsignal("sda", Pins("D9")),
        IOStandard("LVCMOS33")),

    ("dvi", 0,
        Subsignal("d", Pins("D17 A14 A15 A16 A17 A18 D14 B14 B16 B18 E16 D15")),
        Subsignal("de", Pins("F14")),
        Subsignal("clk", Pins("E14")),
        Subsignal("clk_n", Pins("F15")),
        Subsignal("vsync", Pins("C16")),
        Subsignal("hsync", Pins("F12")),
        Subsignal("scl", Pins("C14")),
        Subsignal("sda", Pins("C17")),
        Subsignal("int", Pins("D13")),
        Subsignal("reset_n", Pins("C15")),
        IOStandard("LVCMOS33")),

    ("hdmi", 0,
        Subsignal("d", Pins("T18 U16 V17 V19 V18 W17 Y17 Y15 Y18 Y19 AB21 T17")),
        Subsignal("de", Pins("AB16")),
        Subsignal("clk", Pins("T15")),
        Subsignal("vsync", Pins("T16")),
        Subsignal("hsync", Pins("AB15")),
        Subsignal("scl", Pins("AA21")),
        Subsignal("sda", Pins("AB19")),
        Subsignal("int", Pins("AB18")),
        Subsignal("reset_n", Pins("W18")),
        IOStandard("LVCMOS33")),
]


class Platform(XilinxPlatform):
    default_clk_name = "clk25"
    default_clk_period = 40

    def __init__(self, rev="C"):
        if rev == "B":
            XilinxPlatform.__init__(self, "xc6slx150-fgg484-3", _io)
        elif rev == "C":
            XilinxPlatform.__init__(self, "xc6slx100-fgg484-3", _io)
        else:
            raise NotImplementedError
        self.add_platform_command("CONFIG VCCAUX=\"2.5\";\n")

    def create_programmer(self):
        raise NotImplementedError
