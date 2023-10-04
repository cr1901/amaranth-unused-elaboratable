# amaranth: UnusedElaboratable=no

import pytest

from amaranth.sim import Simulator


class SimulatorFixture:
    def __init__(self, req, cfg):
        self.mod = req.node.get_closest_marker("module").args[0]
        self.name = req.node.name
        self.sim = Simulator(self.mod)


@pytest.fixture
def sim_mod(request, pytestconfig):
    simfix = SimulatorFixture(request, pytestconfig)
    return (simfix, simfix.mod)
