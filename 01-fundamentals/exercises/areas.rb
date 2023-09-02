def square_area(x, y)
  x * y
end

def triangle_area(x, y)
  (x * y) / 2
end

def circle_area(r)
  3.14 * (r**2)
end

def shape
  print("What shape would you like to calculate?\n>")
  gets.chomp.downcase
end

def area
  case shape
  when "square"
    print("What's the lenght of the first side?\n>")
    x = gets.chomp.to_i
    print("What's the lenght of the second side?\n>")
    y = gets.chomp.to_i
    area = square_area(x, y)
  when "triangle"
    print("What's the base of the triangle?\n>")
    x = gets.chomp.to_i
    print("What's the height of the triangle?\n>")
    y = gets.chomp.to_i
    area = triangle_area(x, y)
  when "circle"
    print("What's the radius of the circle?\n>")
    r = gets.chomp.to_i
    area = circle_area(r)
  else
    puts("#{shape.capitalize} is not a valid shape")
    return 1
  end

  puts("The area of the #{shape} is #{area}")
end

area
