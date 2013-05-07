if __FILE__ == $0
  puts (1..999).to_a.select{ |x| x % 3 == 0 or x % 5 == 0 }.reduce(:+)
end