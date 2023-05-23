import numpy as np

seq_st = '0 1 2 3 -4 -11'


def str_int_list(seq_str):
    seq_i = []
    seq_str_list = list(seq_str.split(" "))
    for k in seq_str_list:
        seq_i.append(int(k))
    return seq_i

seq_it = str_int_list(seq_st)
print(seq_it)

x_direction = models.CharField(default='1 -1', max_length=50)
y_direction = models.CharField(default='1 -1', max_length=50)

x_fct_choices = (
    ('choice', 'Zufall'),
    ('ger', 'Gerade'),
    ('abs', 'Betrag'),
    ('sin', 'Sinus'),
    ('cos', 'Cosinus'),
    ('sinc', 'Sinus cardinalis'),

)
x_fct = models.CharField(default='choice', max_length=50, choices=x_fct_choices)

y_fct_choices = (
    ('choice', 'Zufall'),
    ('ger', 'Gerade'),
    ('abs', 'Betrag'),
    ('par2', 'Parabel 2. Grades'),
    ('sin', 'Sinus'),
    ('cos', 'Cosinus'),
    ('sinc', 'Sinus cardinalis'),

)
y_fct = models.CharField(default='choice', max_length=50, choices=y_fct_choices)