class InventoryManager
  def initialize(fresh, available)
    @fresh = deduplicate(fresh)
    @available = available
  end

  def available_fresh
    @available.select(&method(:is_fresh?))
  end

  def fresh_count
    @fresh.map(&:size).reduce(&:+)
  end

  def is_fresh?(ingredient)
    @fresh.any? { |f| f.include?(ingredient) }
  end

  private

  def deduplicate(fresh)
    result = [fresh[0]]

    fresh[1..].each do |range|
      previous = result[-1]

      if previous.cover?(range)
        next
      elsif previous.overlap?(range)
        result.pop
        result << (previous.first..range.last)
      else
        result << range
      end
    end

    result
  end
end

def parse_input(filename)
  content = File.read(filename)
  first_half, second_half = content.split("\n\n")

  fresh = first_half.split("\n").map { |range|
    from, to = range.split("-")
    (from.to_i..to.to_i)
  }.sort_by(&:first)
  available = second_half.split("\n").map(&:to_i)

  [fresh, available]
end

fresh, available = parse_input(ARGV[0])
manager = InventoryManager.new(fresh, available)

puts "Part 1: #{manager.available_fresh.size }"
puts "Part 2: #{manager.fresh_count}"
