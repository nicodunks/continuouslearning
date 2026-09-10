#!/usr/bin/env python3
"""Stream the full graph and extract an explicitly defined navigation seed circuit."""
from collections import Counter
import csv
import json
from pathlib import Path
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.feather as feather

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data/raw'
OUT = ROOT / 'data/derived'
# Explicit selection, not a claim that these are the whole navigation system.
EXACT = {'EPG','EPGt','PEG','PEN_a(PEN1)','PEN_b(PEN2)','Delta7','EL','PFL1','PFL2','PFL3','PFGs'}
PREFIXES = ('ER','PFN','PFR','FC','hDelta')

def write_csv(name, fields, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    annotations = feather.read_table(RAW / 'body-annotations-male-cns-v1.0-minconf-0.5.feather').to_pylist()
    by_id = {n['bodyId']: n for n in annotations}
    assert len(by_id) == len(annotations), 'Duplicate annotation IDs'
    selected = {i:n for i,n in by_id.items() if n['type'] and (n['type'] in EXACT or n['type'].startswith(PREFIXES))}
    ids = pa.array(sorted(selected), type=pa.int64())
    fields = ['bodyId','type','instance','class','superclass','somaSide','rootSide','status','hemibrainType','flywireType']
    write_csv('navigation_neurons.csv', fields, ({k:n[k] for k in fields} for n in selected.values()))
    counts = Counter(n['type'] for n in selected.values())
    write_csv('type_counts.csv', ['type','neurons'], ({'type':t,'neurons':n} for t,n in sorted(counts.items())))
    totals = Counter(); pairs = Counter(); dn_pairs = Counter(); type_pairs = Counter()
    path = RAW / 'connectome-weights-male-cns-v1.0-minconf-0.5.feather'
    with pa.memory_map(str(path), 'r') as source:
        reader = pa.ipc.open_file(source)
        schema = reader.schema
        print('Graph schema:', schema, flush=True)
        assert {'body_pre','body_post','weight'} <= set(schema.names)
        with (OUT / 'navigation_edges.csv').open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['body_pre','body_post','weight','type_pre','type_post']); writer.writeheader()
            for idx in range(reader.num_record_batches):
                batch = pa.Table.from_batches([reader.get_batch(idx)])
                totals['graph_rows'] += len(batch)
                totals['graph_weight_sum'] += pc.sum(batch['weight']).as_py()
                is_pre = pc.is_in(batch['body_pre'], value_set=ids)
                outgoing = batch.filter(is_pre).select(['body_pre','body_post','weight'])
                for e in outgoing.to_pylist():
                    a,b,w = e['body_pre'],e['body_post'],e['weight']
                    assert w > 0
                    if b in selected:
                        ta,tb = selected[a]['type'],selected[b]['type']
                        writer.writerow(dict(e,type_pre=ta,type_post=tb))
                        totals['seed_edge_rows'] += 1; totals['seed_weight_sum'] += w
                        pairs[ta,tb] += w; type_pairs[ta,tb] += 1
                    dest = by_id.get(b,{})
                    if selected[a]['type'] in ('PFL2','PFL3') and dest.get('superclass') == 'descending_neuron':
                        dn_pairs[selected[a]['type'],dest.get('type') or '(untyped)',b] += w
    write_csv('type_connectivity.csv', ['type_pre','type_post','weight','edge_rows'], ({'type_pre':a,'type_post':b,'weight':w,'edge_rows':type_pairs[a,b]} for (a,b),w in sorted(pairs.items(),key=lambda x:-x[1])))
    write_csv('pfl_descending_partners.csv', ['type_pre','type_post','body_post','weight'], ({'type_pre':a,'type_post':b,'body_post':i,'weight':w} for (a,b,i),w in sorted(dn_pairs.items(),key=lambda x:-x[1])))
    summary = dict(dataset='male-cns:v1.0', annotation_rows=len(annotations), cx_annotation_rows=sum(n['class']=='CX' for n in annotations), seed_neurons=len(selected), seed_types=len(counts), selection={'exact':sorted(EXACT),'prefixes':list(PREFIXES)}, **totals)
    (OUT / 'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))

if __name__ == '__main__': main()
