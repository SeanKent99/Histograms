from ROOT import *
from tqdm import tqdm

f1 = TFile.Open("/raid/raid8/ferrico/Useful_Code_HZZ/CMSSW_10_2_15/src/Full_RunII/madgraph/DYJetsToLL_M-50_Full_RunII_madgraph_m2e_2016.root")

t1 = f1.Get("passedEvents")

h1 = TH2F("2dHisto", "etaVSrelativepT", 50, -3, 3, 50, 0, 1)

for i in tqdm(range (t1.GetEntries())):
    t1.GetEntry(i)
    ptSig1 = t1.pterr1/t1.pT1
    ptSig2 = t1.pterr2/t1.pT2
    h1.Fill(t1.eta1, ptSig1)
    h1.Fill(t1.eta2, ptSig2)

c1 = TCanvas()
h1.Draw('COLZ')
c1.Update()
c1.SaveAs("plot1.pdf",'RECREATE')
#c1.Print("plot1.pdf","PDF")
