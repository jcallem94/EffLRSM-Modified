<!-- To automatic generation of install.sh: All no code lines must start with #, <par>, * , or contain # -->
<par>WARNING! Clone with `--recursive` option in order to download the Toolbox submodles:</par>
```bash
git clone --recursive git@github.com:restrepo/BSM-Submodules.git
```

Or try directly here:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/restrepo/BSM-Submodules/SM?filepath=index.ipynb)

# README in EffLRSM:
<par> The [instal.sh](./install.sh) script is generated automatically with the following commands in this file</par>
##  To run an example:

<par>copy the SimplifiedDMSSSFDM folder into  `SimplifiedDM-SSSFDM-Toolbox/madgraph/models` dir:</par>
```bash
cp -r SimplifiedDMSSSFDM/ SimplifiedDM-SSSFDM-Toolbox/madgraph/models/
```

<par>You must be now in the initial directory</par>


## Install madgraph tools
<par>Requires CERN-Root installation and setup </par>

```bash
./SimplifiedDM-SSSFDM-Toolbox/madgraph/bin/mg5_aMC << EOF
n
install pythia8
install Delphes
exit
EOF
```

## run model with madgraph

```bash
cd Run
../SimplifiedDM-SSSFDM-Toolbox/madgraph/bin/mg5_aMC FFjll_3.mdg
```

## Test

* Check root file:
```bash
if [ ! -f "FFjll_3/Events/run_01/tag_1_delphes_events.root" ];then echo ERROR: run failed;exit;fi
```
* Compare header of event file
```bash
gunzip FFjll_3/Events/run_01/events.lhe
grep -B10000 "</header>" FFjll_3/Events/run_01/events.lhe > /tmp/header.lhe
diff header.lhe /tmp/header.lhe
# an empty output is expected for this diff command
gzip FFjll_3/Events/run_01/events.lhe
```

## Final remarks

* To run the model madgraph version 2_3_3  is requiered with pythia-pgs and Delphes installed.





