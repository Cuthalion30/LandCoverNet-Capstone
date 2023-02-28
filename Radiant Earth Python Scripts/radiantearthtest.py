from radiant_mlhub import Dataset

ds = Dataset.fetch('ref_landcovernet_au_v1')
for c in ds.collections:
    print(c.id)
