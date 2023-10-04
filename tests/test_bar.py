# amaranth: UnusedElaboratable=no

import pytest

from amaranth_template_fpga.bar import Bar


@pytest.mark.module(Bar())
@pytest.mark.xfail(run=False)  # Comment to quash UnusedElaboratable warning.
def test_bar(sim_mod):
    pass
