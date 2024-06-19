def calculate_points(word):
    points = {'a': 2.0, 'e': 1.0, 'i': 3.0, 'o': 0.5, 'u': 0.5}
    score = 0
    for char in word:
        if char in points:
            score += points[char]
    return score

def main():
    input_word = input()
    print(calculate_points(input_word))

if __name__ == "__main__":
    main()  