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
"""Archive commands for the unace program."""


def extract_ace(
    archive, compression, cmd, verbosity, interactive, outdir, password=None
):
    """Extract an ACE archive."""
    cmdlist = [cmd, "x"]
    if not outdir.endswith("/"):
        outdir += "/"
    if password:
        cmdlist.append("-p%s" % password)
    cmdlist.extend([archive, outdir])
    return cmdlist


def list_ace(archive, compression, cmd, verbosity, interactive, password=None):
    """List an ACE archive."""
    cmdlist = [cmd]
    if verbosity > 1:
        cmdlist.append("v")
    else:
        cmdlist.append("l")
    if password:
        cmdlist.append("-p%s" % password)
    cmdlist.append(archive)
    return cmdlist


def test_ace(archive, compression, cmd, verbosity, interactive, password=None):
    """Test an ACE archive."""
    cmdlist = [cmd, "t"]
    if password:
        cmdlist.append("-p%s" % password)
    cmdlist.append(archive)
    return cmdlist
