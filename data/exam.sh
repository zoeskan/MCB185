# Live Assessment

   1 CC tax_group:diatoms
 178 CC tax_group:fungi
 286 CC tax_group:insects
 103 CC tax_group:nematodes
 805 CC tax_group:plants
  94 CC tax_group:urochordates
 879 CC tax_group:vertebrates

11663 +
14811 -

## Commands
937  cd Code/MCB185/data
938  zless jaspar2024_core.transfac.gz| grep "tax_group" | sort | uniq -c > exam.sh  940  nano exam.sh
939  zless A.thaliana.gff.gz | cut -f7 | sort | uniq -c >> exam.sh
