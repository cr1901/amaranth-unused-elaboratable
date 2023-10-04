from amaranth import Elaboratable, Module, Signal

from .foo import Foo


class Bar(Elaboratable):
    def __init__(self):
        self.foo = Foo()

    def elaborate(self, platform):
        m = Module()
        m.submodules.foo = self.foo

        bar = Signal()
        m.d.sync += bar.eq(bar)

        return m
