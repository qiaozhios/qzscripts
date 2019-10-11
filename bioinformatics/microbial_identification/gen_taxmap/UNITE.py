# -*- coding: utf-8 -*-
"""从从UNITE下载下来的FASTA文件中，提取序列ID与物种的对应关系"""

import click
from Bio import SeqIO


PREFIX = 'UNITE'


@click.command()
@click.option('--fasta', required=True, help='where to save fasta file')
@click.option('--taxmap', required=True, help='where to save taxmap file')
@click.argument('raw_fasta')
def main(fasta, taxmap, raw_fasta):
    with open(raw_fasta) as raw_fp, open(fasta, 'w') as fp, open(taxmap, 'w') as taxmap_fp:
        cnt = 0
        for r in SeqIO.parse(raw_fp, 'fasta'):
            cnt += 1
            raw_id = r.id
            new_id = '%s_%d' % (PREFIX, cnt)
            r.id = new_id
            r.name = ''
            r.description = ''
            tax = raw_id.split('|')[-1]
            fp.write(r.format('fasta'))
            taxmap_fp.write('%s\t%s\t%s\n' % (new_id, tax, raw_id))
    return 0


if __name__ == '__main__':
    main()
