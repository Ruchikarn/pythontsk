sample = 'sample@yahoo.com'
parts = sample.split('@')

print(parts)

inner_parts = parts[-1].split('.')

print(inner_parts[0].title())

# Join Example

animals = ['Dog', 'Cat', 'Rat', 'Lion']

str_animals = ' '.join(animals)

print(type(str_animals))
print(str_animals)
