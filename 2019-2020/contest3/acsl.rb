EXPRESSIONS_TO_COORDS = {
  # Ruleset 1

  "B" => [[0, 0], [1, 0], [2, 0], [3, 0],
          [0, 1], [1, 1], [2, 1], [3, 1]],

  "D" => [[0, 1], [1, 1], [2, 1], [3, 1],
          [0, 2], [1, 2], [2, 2], [3, 2]],

  "~B" => [[0, 2], [1, 2], [2, 2], [3, 2],
           [0, 3], [1, 3], [2, 3], [3, 3]],

  "A" => [[0, 0], [0, 1], [0, 2], [0, 3],
          [1, 0], [1, 1], [1, 2], [1, 3]],

  "C" => [[1, 0], [1, 1], [1, 2], [1, 3],
          [2, 0], [2, 1], [2, 2], [2, 3]],

  "~A" => [[2, 0], [2, 1], [2, 2], [2, 3],
           [3, 0], [3, 1], [3, 2], [3, 3]],

  "~D" => [[0, 0], [1, 0], [2, 0], [3, 0],
           [0, 3], [1, 3], [2, 3], [3, 3]],

  "~C" => [[0, 0], [0, 1], [0, 2], [0, 3],
           [3, 0], [3, 1], [3, 2], [3, 3]],

  # Ruleset 2

  "B~D" => [[0, 0], [1, 0], [2, 0], [3, 0]],
  "BD" => [[0, 1], [1, 1], [2, 1], [3, 1]],
  "~BD" => [[0, 2], [1, 2], [2, 2], [3, 2]],
  "~B~D" => [[0, 3], [1, 3], [2, 3], [3, 3]],

  "A~C" => [[0, 0], [0, 1], [0, 2], [0, 3]],
  "AC" => [[1, 0], [1, 1], [1, 2], [1, 3]],
  "~AC" => [[2, 0], [2, 1], [2, 2], [2, 3]],
  "~A~C" => [[3, 0], [3, 1], [3, 2], [3, 3]],

  "AB" => [[0, 0], [1, 0],
           [0, 1], [1, 1]],

  "BC" => [[1, 0], [2, 0],
           [1, 1], [2, 1]],

  "~AB" => [[2, 0], [3, 0],
            [2, 1], [3, 1]],

  "AD" => [[0, 1], [1, 1],
           [0, 2], [1, 2]],

  "CD" => [[1, 1], [2, 1],
           [1, 2], [2, 2]],

  "~AD" => [[2, 1], [3, 1],
            [2, 2], [3, 2]],

  "A~B" => [[0, 2], [1, 2],
            [0, 3], [1, 3]],

  "~BC" => [[1, 2], [2, 2],
            [1, 3], [2, 3]],

  "~A~B" => [[2, 2], [3, 2],
            [2, 3], [3, 3]],

  # Ruleset 3

  "A~D" => [[0, 0], [1, 0],
            [0, 3], [1, 3]],

  "C~D" => [[1, 0], [2, 0],
            [1, 3], [2, 3]],

  "~A~D" => [[2, 0], [3, 0],
             [2, 3], [3, 3]],

  "B~C" => [[0, 0], [3, 0],
            [0, 1], [3, 1]],

  "~CD" => [[0, 1], [3, 1],
            [0, 2], [3, 2]],

  "~B~C" => [[0, 2], [3, 2],
             [0, 3], [3, 3]],

  # Ruleset 4

  "~C~D" => [[0, 0], [3, 0],
             [0, 3], [3, 3]],

  # Ruleset 5

  "AB~D" => [[0, 0], [1, 0]],
  "BC~D" => [[1, 0], [2, 0]],
  "~AB~D" => [[2, 0], [3, 0]],
  "ABD" => [[0, 1], [1, 1]],
  "BCD" => [[1, 1], [2, 1]],
  "~ABD" => [[2, 1], [3, 1]],
  "A~BD" => [[0, 2], [1, 2]],
  "~BCD" => [[1, 2], [2, 2]],
  "~A~BD" => [[2, 2], [3, 2]],
  "A~B~D" => [[0, 3], [1, 3]],
  "~BC~D" => [[1, 3], [2, 3]],
  "~A~B~D" => [[2, 3], [3, 3]],

  "AB~C" => [[0, 0], [0, 1]],
  "ABC" => [[1, 0], [1, 1]],
  "~ABC" => [[2, 0], [2, 1]],
  "~AB~C" => [[3, 0], [3, 1]],
  "A~CD" => [[0, 1], [0, 2]],
  "ACD" => [[1, 1], [1, 2]],
  "~ACD" => [[2, 1], [2, 2]],
  "~A~CD" => [[3, 1], [3, 2]],
  "A~B~C" => [[0, 2], [0, 3]],
  "A~BC" => [[1, 2], [1, 3]],
  "~A~BC" => [[2, 2], [2, 3]],
  "~A~B~C" => [[3, 2], [3, 3]],

  # Ruleset 6

  "B~C~D" => [[0, 0], [3, 0]],
  "B~CD" => [[0, 1], [3, 1]],
  "~B~CD" => [[0, 2], [3, 2]],
  "~B~C~D" => [[0, 3], [3, 3]],

  "A~C~D" => [[0, 0], [0, 3]],
  "AC~D" => [[1, 0], [1, 3]],
  "~AC~D" => [[2, 0], [2, 3]],
  "~A~C~D" => [[3, 0], [3, 3]],

  # Ruleset 7

  "AB~C~D" => [[0, 0]],
  "ABC~D" => [[1, 0]],
  "~ABC~D" => [[2, 0]],
  "~AB~C~D" => [[3, 0]],

  "AB~CD" => [[0, 1]],
  "ABCD" => [[1, 1]],
  "~ABCD" => [[2, 1]],
  "~AB~CD" => [[3, 1]],

  "A~B~CD" => [[0, 2]],
  "A~BCD" => [[1, 2]],
  "~A~BCD" => [[2, 2]],
  "~A~B~CD" => [[3, 2]],

  "A~B~C~D" => [[0, 3]],
  "A~BC~D" => [[1, 3]],
  "~A~BC~D" => [[2, 3]],
  "~A~B~C~D" => [[3, 3]],
}

def hex_to_bin(hex)
  hex.hex.to_s(2).rjust(4, "0")
end

def hex_to_rows(hex)
  rows = []

  rows[0] = hex_to_bin(hex[0]).split("")
  rows[1] = hex_to_bin(hex[1]).split("")
  rows[2] = hex_to_bin(hex[2]).split("")
  rows[3] = hex_to_bin(hex[3]).split("")

  rows
end

def rows_to_enabled_coords(rows)
  enabled_coords = []

  rows.each.with_index do |row, y|
    row.each.with_index do |item, x|
      if item == "1"
        enabled_coords << [x, y]
      end
    end
  end

  enabled_coords
end

def enabled_coords_have_other_coords(enabled_coords, potential_coords)
  potential_coords.each do |potential_coord|
    unless enabled_coords.include?(potential_coord)
      return false
    end
  end

  true
end

def remove_coords(from, to_remove)
  to_remove.each do |coord|
    from.delete(coord)
  end
end

def extract_expressions(enabled_coords)
  expressions = []

  EXPRESSIONS_TO_COORDS.each do |expression, potential_coords|
    if enabled_coords_have_other_coords(enabled_coords, potential_coords)
      remove_coords(enabled_coords, potential_coords)
      expressions << expression
    end
  end

  expressions
end

5.times do
  hex = gets
  rows = hex_to_rows(hex)
  enabled_coords = rows_to_enabled_coords(rows)
  expressions = extract_expressions(enabled_coords)

  puts expressions.join("+")
end
