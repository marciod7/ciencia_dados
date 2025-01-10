import pandas as pd

# Corrigindo os nomes de 'ordedr_018' para 'order_018'
orders = [
    ('order_039', 'open', 'cab_14'),
    ('order_034', 'open', 'cab_79'),
    ('order_032', 'open', 'cab_104'),
    ('order_026', 'closed', 'cab_79'),
    ('order_021', 'open', 'cab_45'),
    ('order_018', 'closed', 'cab_26'),  # Corrigido
    ('order_008', 'closed', 'cab_112')
]
df_orders = pd.DataFrame(orders, columns=['order', 'status', 'cab'])
df_orders_open = df_orders[df_orders['status'] == 'open']
unavailable_list = df_orders_open['cab'].values.tolist()
print(unavailable_list)

from geopy.distance import distance
pick_up = 46.083822, 38.967845
cab_26 = 46.073852, 38.991890
cab_112 = 46.078228, 39.003949
cab_104 = 46.071226, 39.004947
cab_14 = 46.004859, 38.095825
cab_79 = 46.088621, 39.033929
cab_45 = 46.141225, 39.124934
cabs = {'cab_26': cab_26, 'cab_112': cab_112, 'cab_14': cab_14,
        'cab_104': cab_104, 'cab_79': cab_79, 'cab_45': cab_45}
dist_list = []

for cab_name, cab_loc in cabs.items():
    if cab_name not in unavailable_list:
        dist = distance(pick_up, cab_loc).m
        dist_list.append((cab_name, round(dist)))

print(dist_list)
print(min(dist_list, key=lambda x: x[1]))

# Corrigindo o nome de 'ca_26' para 'cab_26'
cabs_list = [
    ('cab_14', 1),
    ('cab_79', 0),
    ('cab_104', 0),
    ('cab_45', 1),
    ('cab_26', 0),  # Corrigido
    ('cab_112', 1)
]
df_cabs = pd.DataFrame(cabs_list, columns=['cab', 'seat'])
df_dist = pd.DataFrame(dist_list, columns=['cab', 'dist'])

df = pd.merge(df_cabs, df_dist, on='cab', how='inner')
print(df)  # Para ver o DataFrame final

result_list = list(df.itertuples(index=False, name=None))
result_list = [x for x in result_list if x[1] == 1]
print(min(result_list, key=lambda x: x[2]))
