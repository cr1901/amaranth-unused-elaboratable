# amaranth: UnusedElaboratable=no


from amaranth.sim import Simulator
from amaranth_template_fpga.foo import Foo


def test_foo():
    Simulator(Foo())  # Comment and add "pass" to quash warning.
