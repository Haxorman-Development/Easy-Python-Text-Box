padding = 5

def printTextBox(arr):
  result = '╔'
  result += '═' * (lengthOfLongestItem(arr)+(padding*2))
  result += '╗'
  for line in arr:
    result += '\n'
    result += '║'
    result += ' ' * padding
    result += line + (' ' * padding)
    if not len(line) == lengthOfLongestItem(arr):
      result += ' ' * getLengthDifference(line, max(arr, key=len))
    result += '║'
  result += '\n'
  result += '╚'
  result += '═' * (lengthOfLongestItem(arr)+(padding*2))
  result += '╝'
  print(result)

def lengthOfLongestItem(arr):
  return len(max(arr, key=len))

def getLengthDifference(str1, str2):
  if len(str1) > len(str2):
    return len(str1) - len(str2)
  else:
    return len(str2) - len(str1)

printTextBox([
  'hello world',
  'omg wow'
])
