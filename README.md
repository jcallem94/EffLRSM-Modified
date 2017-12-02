<!-- To automatic generation of install.sh: All no code lines must start with #, <par>, * , or contain # -->
# Effective LRSM:
<par>WARNING! Clone with `--recursive` option in order to download the madgraph repo:</par>
```bash
# Uncomment to download repo:
# git clone --recursive git@github.com:jcallem94/EffLRSM-Modified.git
# cd EffLRSM-Modified
```

<!-- Or try directly here: -->

<!-- [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/restrepo/BSM-Submodules/SM?filepath=index.ipynb)-->



<!-- <par> The [instal.sh](./install.sh) script is generated automatically with the following commands in this file</par> -->

##  To run an example:

<par>copy the `UFO/EffLRSM_UFO` folder into  `madgraph/models` dir:</par>
```bash
cp -r UFO/EffLRSM_UFO/ madgraph/models/
```

<par>You must be now in the initial directory</par>


## Install madgraph tools
<par>Requires CERN-Root installation and setup </par>

```bash
./madgraph/bin/mg5_aMC << EOF
n
install pythia8
y
install Delphes
exit
EOF
```


## run model with madgraph

```bash
cd Run
../madgraph/bin/mg5_aMC bp.mdg
```

## Final remarks

* To run the model madgraph version 2.6.0  is requiered <!-- with pythia-pgs and Delphes installed. -->
