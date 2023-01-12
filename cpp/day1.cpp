#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>

int main()
{
  std::string input = "../input/day1.txt";
  std::string line;
  std::fstream file(input);

  int max = 0;
  int curr = 0;
  while (std::getline(file, line))
  {
    if (line.size() == 0)
    {
      max = std::max(max, curr);
      curr = 0;
    }
    else
    {
      curr += std::stoi(line);
    }
  }
  max = std::max(max, curr);

  std::cout << "Part 1: " << max
            << "\n";
  return max;
}