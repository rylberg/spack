##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-paramhelpers
#
# You can edit this file again by typing:
#
#     spack edit r-paramhelpers
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class RParamhelpers(RPackage):
    """Functions for parameter descriptions and operations in black-box
     optimization, tuning and machine learning. Parameters can be described
     (type, constraints, defaults, etc.), combined to parameter sets and can
     in general be programmed on. A useful OptPath object (archive) to log
     function evaluations is also provided."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/berndbischl/ParamHelpers"
    url      = "https://cran.r-project.org/src/contrib/ParamHelpers_1.10.tar.gz"

    version('1.10', '36e9060488ebd484d62cd991a4693332')

    depends_on('r-bbmisc', type=('build', 'run'))
    depends_on('r-checkmate', type=('build', 'run'))
