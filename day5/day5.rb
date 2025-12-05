class InventoryManager
  def initialize(fresh, available)
    @fresh = fresh
    @available = available
  end

  def available_fresh
    @available.select(&method(:is_fresh?))
  end

  def is_fresh?(ingredient)
    @fresh.any? { |f| f.include?(ingredient) }
  end
end

def parse_input(filename)
  content = File.read(filename)
  first_half, second_half = content.split("\n\n")

  fresh = first_half.split("\n").map do |range|
    from, to = range.split("-")
    (from.to_i..to.to_i)
  end
  available = second_half.split("\n").map(&:to_i)

  [fresh, available]
end

fresh, available = parse_input(ARGV[0])
manager = InventoryManager.new(fresh, available)

puts "Part 1: #{manager.available_fresh.size }"
