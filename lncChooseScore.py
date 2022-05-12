# Example  python3 lncChooseScore.py noncoding.txt prelnc.gtf lnc.gtf

import sys

# 输入CPC2和CNCI取交集后的trans_name，以及findCodeANdExon.py得到的prelnc.gtf，输出lnc.gtf
lncTransName = sys.argv[1]
in_gtf = sys.argv[2]
out_gtf = sys.argv[3]

# list_transname存放取交集后的trans_name
list_transname = []


with open(lncTransName) as transname:
    for item in transname.readlines():
        list_transname.append(item.replace('\n', ''))
transname.close()


# findCodeANdExon.py得到的gtf
with open(out_gtf, 'w') as o_gtf:
    with open(in_gtf) as i_gtf:
        for line in i_gtf.readlines():
            a, b, c, d, e, f, g, h, attr = line.split('\t')
            trName = attr.split(';')[0].split('"')[1]
            # 如果这行的trName在list_exon中，就写入最终文件
            if trName in list_transname:
                o_gtf.write(line)
            else:
                continue
    i_gtf.close()
o_gtf.close()
