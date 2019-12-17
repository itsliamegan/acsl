require "prime"

class Number
  def initialize(value)
    @value = value
  end

  def transform(position)
    transform_left(position) + transform_position_digit + transform_right(position)
  end

  def transform_position_digit
    prime_factors.count.to_s
  end

  def transform_left(position)
    left_digits = digits[0..-position - 1]

    left_digits
      .map { |d| d + digits[-position] }
      .join
  end

  def transform_right(position)
    return "" if position == 1

    right_digits = digits[-position + 1..]

    right_digits
      .map { |d| (d - digits[-position]).abs }
      .join
  end

  def digits
    @value.to_s.split("").map(&:to_i)
  end

  def prime_factors
    factors.filter { |n| Prime.prime?(n) }
  end

  def factors
    (1..@value).filter { |n| @value % n == 0 }
  end
end
