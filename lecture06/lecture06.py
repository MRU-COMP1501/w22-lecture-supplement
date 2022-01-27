# slide 10
PI = 3.14159
SPEED_OF_LIGHT = 2e8
print(f'PI to 3 decimals: {PI:.3f}')
print(f'PI with g format: {PI:g}')
print(f'Speed of light with g format: {SPEED_OF_LIGHT:g}')
print(f'Speed of light with f format: {SPEED_OF_LIGHT:f}')
print(f'Speed of light with f format, thousand separator, '
       f'no decimals: {SPEED_OF_LIGHT:,.0f}')

# slide 11
percent_remaining = 96.66666666
print('UMR has', int(percent_remaining), '% fuel remaining')
print(f'UMR has {int(percent_remaining)}% fuel remaining')

# slide 13
print()
print(f'{"Left":<20}')
print(f'{"Centre":^20}')
print(f'{"Right":>20}')
print(f'{"Longer Right":>20}')
print(f'{percent_remaining:>20.1f}')
print()

# slide 16
print('-' * 20)
print(f'{"Left":<20}')
print(f'{"Centre":^20}')
print(f'{"Right":>20}')
print('*' * 10 + '$' * 10)
print('-' * 20)
