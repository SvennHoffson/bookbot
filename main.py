def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    from stats import word_count
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    from stats import list
    print(list)
    print("============= END ===============")
main()
