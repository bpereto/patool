# -*- coding: utf-8 -*-
# Copyright (C) 2010-2015 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Archive commands for the lrzip program."""
import os
from .. import util


def extract_lrzip(archive, compression, cmd, verbosity, interactive, outdir):
    """Extract a LRZIP archive."""
    cmdlist = [cmd, "-d"]
    if verbosity > 1:
        cmdlist.append("-v")
    outfile = util.get_single_outfile(outdir, archive)
    cmdlist.extend(["-o", outfile, os.path.abspath(archive)])
    return cmdlist


def test_lrzip(archive, compression, cmd, verbosity, interactive):
    """Test a LRZIP archive."""
    cmdlist = [cmd, "-t"]
    if verbosity > 1:
        cmdlist.append("-v")
    cmdlist.append(archive)
    return cmdlist


def create_lrzip(archive, compression, cmd, verbosity, interactive, filenames):
    """Create a LRZIP archive."""
    cmdlist = [cmd, "-o", archive]
    if verbosity > 1:
        cmdlist.append("-v")
    cmdlist.extend(filenames)
    return cmdlist
