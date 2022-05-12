# Example  python findCodeANdExon.py gffcompare.annotated.gtf output.gtf

import sys

# 输入gffcompare得到的gtf，输出最终exon>2 classCode=u,x,i的gtf
annot_gtf = sys.argv[1]
out_gtf = sys.argv[2]

# list_transname存放classCode=u,x,i的transcriptID，list_exon在list_transname基础上筛选到exon>2的transcript
list_transname = []
list_exon = []

# 输入文件:主要用来提取符合要求的transcriptID
with open(annot_gtf) as annot:
    for line in annot.readlines():
        a,b,gtftype,d,e,f,g,h,attr = line.split('\t')
        # 判断gtftype:transcript or exon，二选一
        # transcript用来确定classCode
        # exon用来确定exonNum
        if gtftype == 'transcript':
            # 判断classCode，进行存储
            if 'class_code "x"' in attr or 'class_code "u"' in attr or 'class_code "i"' in attr:
                transname = attr.split(';')[0].split('"')[1]
                list_transname.append(transname)
            else:
                continue
        else:
            trName = attr.split(';')[0].split('"')[1]
            exName = attr.split(';')[2]
            # PART1 : trName in list_transname判断这个exon对应的transcriptID的classCode是否为u,x,i
            # PART2 : 只要存在exon_number "2"，对应的transcriptID一定有多个exon，进行存储
            if trName in list_transname and exName == ' exon_number "2"':
                list_exon.append(trName)
            else:continue
annot.close()

# 输出文件:包含transcript和exon两个type
with open(out_gtf,'w') as gtf:
    with open(annot_gtf) as annote:
        for line in annote.readlines():
            a,s,d,f,g,h,j,k,note=line.split('\t')
            trName=note.split(';')[0].split('"')[1]
            # 如果这行的trName在list_exon中，就写入最终文件
            if trName in list_exon:
                gtf.write(line)
            else:
                continue
    annote.close()
gtf.close()
