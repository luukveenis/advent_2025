def is_accessible?(layout, x, y)
  width = layout[0].length
  height = layout.length
  paper_count = 0

  ([0, x - 1].max..[width - 1, x + 1].min).each do |i|
    ([0, y - 1].max..[height - 1, y + 1].min).each do |j|
      if ((i != x || j != y) && layout[i][j] == "@")
        paper_count += 1
      end
    end
  end

  paper_count < 4
end

def accessible_rolls(layout)
  accessible = []

  (0...layout.length).each do |i|
    (0...layout[i].length).each do |j|
      if layout[i][j] == "."
        next
      else
        accessible << [i, j] if is_accessible?(layout, i, j)
      end
    end
  end

  accessible
end

layout = File.readlines(ARGV[0]).map do |line|
  line.strip.chars
end

puts accessible_rolls(layout).size
