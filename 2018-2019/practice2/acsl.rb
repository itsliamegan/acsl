class TestString
  def initialize(input)
    transformed_input = transform_input_to_regex_form(input)
    @regex = Regexp.new(transformed_input, Regexp::IGNORECASE)
  end

  def match?(test)
    !!(@regex =~ test)
  end

  def transform_input_to_regex_form(input)
    input.gsub('*', '.*').gsub('?', '.')
  end
end

words = gets.chomp.split ', '

(1..5).each do
  input = gets.chomp
  test_string = TestString.new(input)
  matching_words = words.select { |word| test_string.match? word }
  puts matching_words.join ', '
end
