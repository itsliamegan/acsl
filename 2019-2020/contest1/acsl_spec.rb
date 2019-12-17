require "./acsl"

describe Number do
  describe "#digits" do
    it "gets all the digits of the number" do
      number = Number.new(1234)
      
      expect(number.digits).to match_array [1, 2, 3, 4]
    end
  end

  describe "#factors" do
    it "gets all of the factors of the number" do
      number = Number.new(12)

      expect(number.factors).to match_array [1, 2, 3, 4, 6, 12]
    end
  end

  describe "#prime_factors" do
    it "gets all of the prime factors of the number" do
      number = Number.new(12)

      expect(number.prime_factors).to match_array [2, 3]
    end
  end

  describe "#transform_position_digit" do
    it "gets the count of prime factors of the number" do
      number = Number.new(102438)

      expect(number.transform_position_digit).to eq "4"
    end
  end

  describe "#transform_left" do
    it "adds the number at the position to all the digits left of that number" do
      number = Number.new(123456789)

      expect(number.transform_left(5)).to eq "6789"
    end
  end

  describe "#transform_right" do
    it "subtracts and absolute values all the digits to the right of the number at the position" do
      number = Number.new(987654321)

      expect(number.transform_right(5)).to eq "1234"
    end
  end
  
  describe "#transform" do
    it "passess all the examples" do
      first = Number.new(102438)
      second = Number.new(4329)
      third = Number.new(6710)
      fourth = Number.new(16807)
      fifth = Number.new(60098065452)

      expect(first.transform(3)).to eq "546414"
      expect(second.transform(1)).to eq "1312113"
      expect(third.transform(2)).to eq "7841"
      expect(fourth.transform(1)).to eq "8131571"
    end 
  end
end
