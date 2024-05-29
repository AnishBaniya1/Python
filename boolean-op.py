onList=True
inStock=True
onSale = False 
rotten = False 
# and 
print(onList and inStock)
print(onList and inStock and onSale)
#or
print(onList or onSale)
print(onList or onSale or rotten)
#not
print(not rotten)
#combining
print(((onList or onSale)and inStock) and not rotten)

print(onList or inStock and onSale)
print(onSale and inStock or onList)