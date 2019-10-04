#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    validate_matrix_mul(m_a, m_b)
    mult_matrix = []
    for row in m_a:
        num_colum_m_b = 0
        list_columns = []
        while num_colum_m_b < len(m_b[0]):
            mult_item = 0
            for index_row_m_a in range(len(row)):
                m_a_value = row[index_row_m_a]
                m_b_value = m_b[index_row_m_a][num_colum_m_b]
                validate_type_values_matrix(m_a_value, m_b_value)
                mult_item += (m_a_value * m_b_value)
            list_columns.append(mult_item)
            num_colum_m_b += 1
        mult_matrix.append(list_columns)
    return mult_matrix


def validate_matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a[0], list):
        raise TypeError('m_a must be a list of lists')
    if not isinstance(m_b[0], list):
        raise TypeError('m_b must be a list of lists')
    for row_m_a in m_a:
        for row_m_b in m_b:
            if len(row_m_a) != len(row_m_b):
                validate_size_each_matrix(m_a, m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


def validate_size_each_matrix(m_a, m_b):
    len_row_ma_a = len(m_a[0])
    len_row_ma_b = len(m_b[0])
    for row in m_a:
        if len(row) != len_row_ma_a:
            raise TypeError('each row of m_a must be of the same size')
    for row in m_b:
        if len(row) != len_row_ma_b:
            raise TypeError('each row of m_b must be of the same size')


def validate_type_values_matrix(m_a_value, m_b_value):
    if not isinstance(m_a_value, (int, float)):
        raise TypeError('m_a should contain only integers or floats')
    if not isinstance(m_b_value, (int, float)):
        raise TypeError('m_b should contain only integers or floats')
