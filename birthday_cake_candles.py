sel_numbers = [4, 3, 4, 4, 2, 4, 1]
sel_numbers.sort(reverse=True)
blow_candles = []
candle_count = 0
blow_candles.append(sel_numbers[0])
for x in sel_numbers:
    if x > blow_candles[0]:
        blow_candles.insert(0, x)

for x in sel_numbers:
    if x == blow_candles[0]:
        candle_count = candle_count + 1

print(candle_count)
