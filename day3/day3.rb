def max_joltage(battery)
  first = battery[0].to_i
  second = battery[1].to_i

  (1...battery.length - 1).each do |i|
    current = battery[i].to_i
    ahead = battery[i + 1].to_i

    if (current > first)
      first = current
      second = ahead
    elsif (ahead > second)
      second = ahead
    else
      # Do nothing, not an improvement
    end
  end

  "#{first}#{second}".to_i
end

joltages = []

File.foreach(ARGV[0]) do |line|
  joltages << max_joltage(line.strip)
end

puts joltages.sum
