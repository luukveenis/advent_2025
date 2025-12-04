def max_joltage(battery, count)
  result = []
  next_start = 0

  (0...count).each do |i|
    max = 0

    (next_start..battery.length - count + i).each do |j|
      if (battery[j].to_i > max)
        max = battery[j].to_i
        next_start = j + 1
      end
    end

    result << max
  end

  result.join.to_i
end

part1_result = []

File.foreach(ARGV[0]) do |line|
  part1_result << max_joltage(line.strip, 2)
end

puts part1_result.sum
