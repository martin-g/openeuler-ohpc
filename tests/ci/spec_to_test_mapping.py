#!/usr/bin/env python3
#
# This script tries to create a mapping between spec files
# and which tests to enable in the test suite.
# This script will return three shell arrays (TESTS, ADMIN_TESTS and PKGS).

import os
import sys

# This dictionary defines the mapping
# 'path/to/file.spec': [
#     'test-option',
#     'admin-test-option',
#     'required packages for test',
# ]
test_map = {
    'components/rms/slurm/SPECS/slurm.spec': [
        'munge',
        '',
        'magpie-ohpc pdsh-mod-slurm-ohpc pdsh-ohpc'
    ],
    'components/dev-tools/hwloc/SPECS/hwloc.spec': [
        'hwloc',
        '',
        '',
    ],
    'components/rms/magpie/SPECS/magpie.spec': [
        'munge',
        '',
        'pdsh-mod-slurm-ohpc pdsh-ohpc'
    ],
    'components/admin/pdsh/SPECS/pdsh.spec': [
        'munge',
        '',
        'magpie-ohpc'
    ],
    'components/dev-tools/easybuild/SPECS/easybuild.spec': [
        'easybuild',
        '',
        'gcc-c++',
    ],
    'components/io-libs/adios2/SPECS/adios2.spec': [
        'adios2',
        '',
        'openmpi4-gnu12-ohpc \
            mpich-gnu12-ohpc \
            python3-numpy-gnu12-ohpc \
            python3-mpi4py-gnu12-mpich-ohpc \
            python3-mpi4py-gnu12-openmpi4-ohpc'
    ],
    'components/io-libs/hdf5/SPECS/hdf5.spec': [
        'hdf5',
        '',
        'zlib-devel automake-ohpc libtool-ohpc autoconf-ohpc'
    ],
    'components/parallel-libs/ptscotch/SPECS/ptscotch.spec': [
        'ptscotch',
        '',
        'zlib-devel'
    ],
    'components/serial-libs/scotch/SPECS/scotch.spec': [
        'scotch',
        '',
        'zlib-devel'
    ],
    'components/parallel-libs/fftw/SPECS/fftw.spec': [
        'fftw',
        '',
        ''
    ],
    'components/parallel-libs/hypre/SPECS/hypre.spec': [
        'hypre',
        '',
        ''
    ],
    'components/parallel-libs/mfem/SPECS/mfem.spec': [
        'mfem',
        '',
        ''
    ],
    'components/parallel-libs/mumps/SPECS/mumps.spec': [
        'mumps',
        '',
        ''
    ],
    'components/parallel-libs/opencoarrays/SPECS/opencoarrays.spec': [
        'opencoarrays',
        '',
        ''
    ],
    'components/parallel-libs/petsc/SPECS/petsc.spec': [
        'petsc',
        '',
        ''
    ],
    'components/io-libs/phdf5/SPECS/hdf5.spec': [
        'phdf5',
        '',
        'zlib-devel automake-ohpc libtool-ohpc autoconf-ohpc'
    ],
    'components/io-libs/pnetcdf/SPECS/pnetcdf.spec': [
        'pnetcdf',
        '',
        ''
    ],
    'components/parallel-libs/scalapack/SPECS/scalapack.spec': [
        'scalapack',
        '',
        ''
    ],
    'components/parallel-libs/slepc/SPECS/slepc.spec': [
        'slepc',
        '',
        ''
    ],
    'components/serial-libs/superlu/SPECS/superlu.spec': [
        'superlu',
        '',
        ''
    ],
    'components/parallel-libs/superlu_dist/SPECS/superlu_dist.spec': [
        'superlu_dist',
        '',
        'scalapack-gnu12-openmpi4-ohpc scalapack-gnu12-mpich-ohpc'
    ],
    'components/parallel-libs/trilinos/SPECS/trilinos.spec': [
        'trilinos',
        '',
        ''
    ],
    'components/perf-tools/extrae/SPECS/extrae.spec': [
        'extrae',
        '',
        'lmod-defaults-gnu12-openmpi4-ohpc'
    ],
    'components/perf-tools/geopm/SPECS/geopm.spec': [
        'geopm',
        '',
        ''
    ],
    'components/perf-tools/likwid/SPECS/likwid.spec': [
        'likwid',
        '',
        ''
    ],
    'components/perf-tools/papi/SPECS/papi.spec': [
        'papi',
        '',
        ''
    ],
    'components/perf-tools/scalasca/SPECS/scalasca.spec': [
        'scalasca',
        '',
        'lmod-defaults-gnu12-openmpi4-ohpc'
    ],
    'components/perf-tools/tau/SPECS/tau.spec': [
        'tau',
        '',
        ''
    ],
    'components/mpi-families/openmpi/SPECS/openmpi.spec': [
        'slurm',
        '',
        ''
    ],
    'components/mpi-families/mpich/SPECS/mpich.spec': [
        'slurm',
        '',
        ''
    ],
    'components/dev-tools/spack/SPECS/spack.spec': [
        '',
        'spack',
        ''
    ],
    'components/admin/conman/SPECS/conman.spec': [
        '',
        'oob',
        ''
    ],
    'components/dev-tools/autoconf/SPECS/autoconf.spec': [
        'autotools',
        '',
        'automake-ohpc libtool-ohpc'
    ],
    'components/dev-tools/cmake/SPECS/cmake.spec': [
        'cmake',
        '',
        ''
    ],
    'components/parallel-libs/boost/SPECS/boost.spec': [
        'boost',
        '',
        ''
    ],
    'components/serial-libs/openblas/SPECS/openblas.spec': [
        'openblas',
        '',
        ''
    ],
    'components/serial-libs/R/SPECS/R.spec': [
        'R',
        '',
        ''
    ],
    'components/perf-tools/dimemas/SPECS/dimemas.spec': [
        'dimemas',
        '',
        'lmod-defaults-gnu12-openmpi4-ohpc'
    ],
    'components/runtimes/charliecloud/SPECS/charliecloud.spec': [
        'charliecloud',
        '',
        'singularity-ce'
     ],
    'components/io-libs/netcdf-fortran/SPECS/netcdf-fortran.spec': [
        'netcdf',
        '',
        'netcdf-cxx-gnu12-openmpi4-ohpc netcdf-cxx-gnu12-mpich-ohpc'
    ],
    'components/io-libs/netcdf-cxx/SPECS/netcdf-cxx.spec': [
        'netcdf',
        '',
        'netcdf-fortran-gnu12-openmpi4-ohpc netcdf-fortran-gnu12-mpich-ohpc'
    ],
    'components/perf-tools/imb/SPECS/imb.spec': [
        'imb',
        '',
        ''
    ],
    'components/dev-tools/mpi4py/SPECS/python-mpi4py.spec': [
        'mpi4py',
        '',
        ''
    ],
}

skip_ci_specs = []
skip_ci_specs_env = os.getenv('SKIP_CI_SPECS')
if skip_ci_specs_env:
    skip_ci_specs = skip_ci_specs_env.rstrip().split('\n')
for spec in skip_ci_specs:
    if spec in test_map:
        test_map.pop(spec)

if len(sys.argv) <= 1:
    print('TESTS=() ADMIN_TESTS=() PKGS=()')
    sys.exit(0)

tests = ''
admin_tests = ''
pkgs = ''

specs_to_test = sys.argv[1:]

test_all_specs_env = os.getenv('SIMPLE_CI_TEST_ALL')
if test_all_specs_env:
    specs_to_test = test_map.keys()

for i in specs_to_test:
    if i in test_map.keys():
        if len(tests) > 0:
            tests += ' '
        if len(admin_tests) > 0:
            admin_tests += ' '
        if len(pkgs) > 0:
            pkgs += ' '

        if len(test_map[i][0]) > 0:
            tests += f'--enable-{test_map[i][0]}'
        if len(test_map[i][1]) > 0:
            admin_tests += f'--enable-{test_map[i][1]}'
        pkgs += test_map[i][2]

if test_all_specs_env:
    pkgs = 'EasyBuild-ohpc R-gnu12-ohpc adios2-gnu12-openmpi4-ohpc \
        autoconf-ohpc automake-ohpc boost-gnu12-openmpi4-ohpc \
        charliecloud-ohpc cmake-ohpc conman-ohpc dimemas-gnu12-openmpi4-ohpc \
        extrae-gnu12-openmpi4-ohpc fftw-gnu12-openmpi4-ohpc genders-ohpc \
        gsl-gnu12-ohpc hdf5-gnu12-ohpc hpc-workspace-ohpc \
        hypre-gnu12-openmpi4-ohpc imb-gnu12-openmpi4-ohpc libtool-ohpc \
        lmod-defaults-gnu12-openmpi4-ohpc losf-ohpc magpie-ohpc \
        metis-gnu12-ohpc mfem-gnu12-openmpi4-ohpc mrsh-ohpc \
        mumps-gnu12-openmpi4-ohpc netcdf-cxx-gnu12-openmpi4-ohpc \
        netcdf-fortran-gnu12-openmpi4-ohpc netcdf-gnu12-openmpi4-ohpc \
        omb-gnu12-openmpi4-ohpc openblas-gnu12-ohpc \
        opencoarrays-gnu12-openmpi4-ohpc papi-ohpc paraver-ohpc \
        pdsh-mod-genders-ohpc pdsh-mod-slurm-ohpc pdsh-mod-slurm-ohpc \
        pdsh-ohpc pdtoolkit-gnu12-ohpc petsc-gnu12-openmpi4-ohpc \
        phdf5-gnu12-openmpi4-ohpc plasma-gnu12-ohpc pmix-ohpc \
        pnetcdf-gnu12-openmpi4-ohpc ptscotch-gnu12-openmpi4-ohpc \
        python3-Cython-ohpc python3-mpi4py-gnu12-openmpi4-ohpc \
        python3-numpy-gnu12-ohpc scalapack-gnu12-openmpi4-ohpc \
        scalasca-gnu12-openmpi4-ohpc scorep-gnu12-openmpi4-ohpc \
        scotch-gnu12-ohpc sionlib-gnu12-openmpi4-ohpc \
        slepc-gnu12-openmpi4-ohpc slurm-contribs-ohpc slurm-devel-ohpc \
        slurm-libpmi-ohpc slurm-openlava-ohpc slurm-pam_slurm-ohpc \
        slurm-perlapi-ohpc slurm-slurmdbd-ohpc slurm-sview-ohpc \
        slurm-torque-ohpc superlu-gnu12-ohpc superlu_dist-gnu12-openmpi4-ohpc \
        tau-gnu12-openmpi4-ohpc trilinos-gnu12-openmpi4-ohpc ucx-cma-ohpc \
        ucx-rdmacm-ohpc valgrind-ohpc warewulf-cluster-ohpc \
        warewulf-common-ohpc warewulf-ipmi-ohpc warewulf-provision-ohpc \
        warewulf-vnfs-ohpc'

print(
    'TESTS=(%s) ADMIN_TESTS=(%s) PKGS=(%s)' % (
        tests,
        admin_tests,
        pkgs,
    )
)
