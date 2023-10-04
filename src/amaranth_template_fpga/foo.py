from amaranth import Elaboratable, Module, Signal


class Foo(Elaboratable):
    def elaborate(self, platform):
        m = Module()

        foo = Signal()
        m.d.sync += foo.eq(foo)

        return m
