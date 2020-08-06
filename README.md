# topNanoAOD-datasets

Lists of datasets produced in topNanoAOD campaigns

Please make a pull request to add your samples to the relevant list.

The format is e.g.:
```
'2016':
    ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8:
        dbs: /ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/palencia-TopNanoAODv6-1-1_2016-88146d75cb10601530484643de5f7795/USER
        parents:
        - /ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM
        responsible: Enrique
        site: T2_CH_CERN
        comment: 
```

Processed extensions whose files are published under the same DBS entry do not need a separate entry: just put the main sample and the extensions in the `parents` list.
