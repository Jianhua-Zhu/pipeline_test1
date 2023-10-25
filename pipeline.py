import sys,os
from argparse import ArgumentParser

def resolveConfig(sample_info):
  dict_info = {}
  dict_new = {}
  with open(sample_info,"r") as f:
    patient_list = []
    for i in f.readlines()[1:]:
      line = i.strip()
      ll = line.split("\t")
      patient = ll[0]
      type_s = ll[1]
      path = ll[3]
      if patient not in patient_list:
        patient_list.append(patient)
      key = patient+"_"+type_s
      dict_info.setdefault(key,[]).append(path)
  return patient_list,dict_info

#patient,dict_info = resolveConfig("sample.info")

if __name__ == '__main__':
  parser = ArgumentParser(description="WES pipeline test 2023.10.24")
  parser.add_argument("-i","--input",action="store",dest="input file",
                     help="input patient and sample information",required=True)
  parser.add_argument("-o","--outpath",action="store",dest="output path",
                     help="output path",required=True)
  args = parser.parse_args()
  patient, dict_info = resolveConfig(args.input)
  for p in patient:
    path = args.outpath+"/"+p
    os.mkdirs(path)
