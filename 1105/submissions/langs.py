def find_unique_speakers(french_speakers, spanish_speakers, english_speakers):
    # Split the strings into sets of names
    french = set(french_speakers.split(', '))
    spanish = set(spanish_speakers.split(', '))
    english = set(english_speakers.split(', '))

    # Find students who speak only one language
    only_one_language = (french - spanish - english) | (spanish - french - english) | (english - french - spanish)

    # Sort and return the names
    return sorted(only_one_language)

def main():
    # Sample input
    french_speakers = input()
    spanish_speakers = input()
    english_speakers = input()

    # Find and print the students who speak only one language
    unique_speakers = find_unique_speakers(french_speakers, spanish_speakers, english_speakers)
    if len(unique_speakers) == 0:
        print("No one speaks only one language.")
    else:
        for name in unique_speakers:
                print(name)


if __name__ == "__main__":
    main()

