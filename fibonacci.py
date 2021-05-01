fibonacci = [1, 1]

for i in range(100) :
  fibonacci.append(fibonacci[i]+fibonacci[i+1])
  if max(fibonacci) == 55 :
    break

print(fibonacci)
