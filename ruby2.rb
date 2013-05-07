if __FILE__ == $0
  total = 0
    f1 = 1
    f2 = 2
    while f2 < 4000000
      total += f2
      f1 = 2*f2+f1
      f2 = 2*f1-f2
    end
    puts total
end