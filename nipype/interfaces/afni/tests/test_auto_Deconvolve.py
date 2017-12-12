# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import Deconvolve


def test_Deconvolve_inputs():
    input_map = dict(STATmask=dict(argstr='-STATmask %s',
    ),
    TR_1D=dict(argstr='-TR_1D %f',
    ),
    allzero_OK=dict(argstr='-allzero_OK',
    ),
    args=dict(argstr='%s',
    ),
    automask=dict(argstr='-automask',
    ),
    cbucket=dict(argstr='-cbucket %s',
    ),
    censor=dict(argstr='-censor %s',
    ),
    dmbase=dict(argstr='-dmbase',
    ),
    dname=dict(argstr='-D%s=%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    force_TR=dict(argstr='-force_TR %f',
    position=0,
    ),
    fout=dict(argstr='-fout',
    ),
    global_times=dict(argstr='-global_times',
    xor=['local_times'],
    ),
    glt_label=dict(argstr='-glt_label %d %s...',
    position=-1,
    requires=['gltsym'],
    ),
    gltsym=dict(argstr="-gltsym 'SYM: %s'...",
    position=-2,
    ),
    goforit=dict(argstr='-GOFORIT %i',
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_files=dict(argstr='-input %s',
    copyfile=False,
    position=1,
    sep=' ',
    ),
    input1D=dict(argstr='-input1D %s',
    ),
    jobs=dict(argstr='-jobs %d',
    ),
    legendre=dict(argstr='-legendre',
    ),
    local_times=dict(argstr='-local_times',
    xor=['global_times'],
    ),
    mask=dict(argstr='-mask %s',
    ),
    noblock=dict(argstr='-noblock',
    ),
    nocond=dict(argstr='-nocond',
    ),
    nodmbase=dict(argstr='-nodmbase',
    ),
    nolegendre=dict(argstr='-nolegendre',
    ),
    nosvd=dict(argstr='-nosvd',
    ),
    num_glt=dict(argstr='-num_glt %d',
    position=-3,
    ),
    num_stimts=dict(argstr='-num_stimts %d',
    position=-6,
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    ortvec=dict(argstr='-ortvec %s %s',
    ),
    out_file=dict(argstr='-bucket %s',
    ),
    outputtype=dict(),
    polort=dict(argstr='-polort %d',
    ),
    rmsmin=dict(argstr='-rmsmin %f',
    ),
    rout=dict(argstr='-rout',
    ),
    sat=dict(argstr='-sat',
    xor=['trans'],
    ),
    singvals=dict(argstr='-singvals',
    ),
    stim_label=dict(argstr='-stim_label %d %s...',
    position=-4,
    requires=['stim_times'],
    ),
    stim_times=dict(argstr="-stim_times %d %s '%s'...",
    position=-5,
    ),
    stim_times_subtract=dict(argstr='-stim_times_subtract %f',
    ),
    svd=dict(argstr='-svd',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    tout=dict(argstr='-tout',
    ),
    trans=dict(argstr='-trans',
    xor=['sat'],
    ),
    vout=dict(argstr='-vout',
    ),
    x1D=dict(argstr='-x1D %s',
    ),
    x1D_stop=dict(argstr='-x1D_stop',
    ),
    )
    inputs = Deconvolve.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Deconvolve_outputs():
    output_map = dict(cbucket=dict(),
    out_file=dict(),
    reml_script=dict(),
    x1D=dict(),
    )
    outputs = Deconvolve.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
