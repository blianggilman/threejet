import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("SlimmedNtuplizer")
process.load("FWCore.MessageService.MessageLogger_cfi")

options = VarParsing.VarParsing('analysis')
options.outputFile = 'slimmed_ntuple_testing.root'
options.inputFiles = 'file:./testfile.root'
options.maxEvents = -1
options.register('reportEvery',
                 1000000, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Number of events to process before reporting progress.")
options.parseArguments()

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(options.reportEvery)

process.source = cms.Source(
                            "PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles)
                            )

process.load('threejet.SlimmedNtuplizer.slimmedntuplizer_cfi')

process.slimmedntuplizer.output_file_name = cms.string(options.outputFile)

#### Redefine JEC variables here

process.options = cms.untracked.PSet(SkipEvent = cms.untracked.vstring('ProductNotFound'))
process.p = cms.Path(process.slimmedntuplizer)


