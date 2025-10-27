from decimal import Decimal

# ---- Operation in decimal form
dec = 0.1 + 0.1 + 0.1 - 0.3   # give incorrect value
print(dec)

dec_Correct = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(dec_Correct)
print(dec_Correct)