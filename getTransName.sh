#!/bin/bash

#提取prelnc.gtf对应的转录本
gffread prelnc.gtf -g ../00ref/genome.fa -w prelnc_trans.fa && \

#CPC2鉴定
mkdir cpc2 && \
python3 ~/software/cpc2/bin/CPC2.py -i prelnc_trans.fa -o cpc2/out && \
awk '{if ($8=="noncoding") print $1 "\t" $8}' cpc2/out.txt >>cpc.noncoding.txt && \

#CNCI支持python2
mkdir cnci && \
python ~/software/CNCI-master/CNCI.py  -f prelnc_trans.fa  -o cnci/output -m pl -p 20 && \
awk '{if ($2=="noncoding") print $1 "\t" $2}' cnci/output/CNCI.index >>cnci.noncoding.txt && \

#取交集的trans_name
sort cnci.noncoding.txt  cpc.noncoding.txt|uniq -d| cut -f 1 >>noncoding.txt && \

#删除中间文件
rm cpc2 cnci prelnc_trans.fa cpc.noncoding.txt cnci.noncoding.txt -r
