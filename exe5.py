#exercício filtando dados com uma list comprehension
orders = [
    ('order_039', 'open', 'cab_14'),
    ('order_034', 'open', 'cab_79'),
    ('order_032', 'open', 'cab_104'),
    ('order_026', 'closed', 'cab_79'),
    ('order_021', 'open', 'cab_45'),
    ('ordedr_018', 'closed', 'cab_26'),
    ('order_008', 'closed', 'cab_112')
]

# Usando List Comprehension para gerar a lista de táxis indisponíveis
unavailable_list = [x[2] for x in orders if x[1] == 'open']
print(unavailable_list)
