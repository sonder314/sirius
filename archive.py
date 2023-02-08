def poland(s):
  stack = []
  product = 1
  for i in s:
    if i.isdigit():
      stack.append(int(i))
    else:
      product = calc(stack[-2], stack[-1], i)
      del stack[-1]
      del stack[-1]
      break
  for i in s:
    if i.isdigit():
      stack.append(int(i))
    else:
      product = calc(product, stack[-1], i)
      del stack[-1]


def calc(a, b, s):
  if s == '*':
    return a * b
  elif s == '+':
    return a + b
  return a - b

s = '8 9 + 1 7 - *'
s = ''.join(list(s.split(' ')))
print(poland(s))





#(a+b+c)*d = a b c + d*