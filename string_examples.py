s1 = "spam\n"
print(f"len(s1): {len(s1)}")
s2 = 'spam\n'
print(f"len(s2): {len(s2)}")
s3 = """spam\n"""
s4 = '''spam\n'''
print("Guido's the ex-BDFL of Python")
print('Guido\'s the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

query = """
select * 
from customers
where state = 'VA'
order by sales_monthly_avg
descending
"""
s5 = "spam\\n"  # escape \ with \
s6 = r"spam\n"  # no escape needed



